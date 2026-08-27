---
title: "An Error Instead of 500: Teaching the Service to Explain What Went Wrong"
project: diploma_supplement_service
pair: diploma-diagnostika-oshibok
platform: VK
type: Engineering update
date: 2026-08-27
source_from: 7a0bd5cfe524785615b9b73cd6a045be3f47012e
source_rev: 121f4c15cc732a9a6376ee2cd3a1c5264d6f44dc
lang: en
authors:
  - Nikita Konkin
summary: "An update about diagnostics: errors propagated across service boundaries, a record of every request, logs that survive a container restart, and the first automated test runner."
translation_of: 2026-08-27-diagnostika-oshibok.md
links:
  demo: "https://xn----etb9agicel.xn--p1ai/"
  repo: "https://github.com/nikita-konkin/diploma_supplement_service"
tags: [programming, java, python, docker, logging, testing]
---

Earlier breakdowns covered the service from two angles: the architecture of its three modules, and the pipeline that carries data from Excel to XML. Both described it working. This update is about the opposite case — what happens when processing fails, and how the person on the other side of the screen finds out.

## What was wrong

The service has three parts: a Java gateway, `java-api`, and two Python engines — `python-engine` for pivot tables and `python-xml-engine` for XML generation. The gateway takes a file from the browser and hands it to whichever engine is needed.

The problem lived on the boundary between them. An engine could return a meaningful error — that the uploaded workbook has no sheet of the expected shape, say — but the gateway inspected the response like this:

```java
if (responseCode != 200) {
    throw new RuntimeException("Python service returned status " + responseCode);
}
```

The error text died on that line. The user saw "500 Internal Server Error" whether the cause was the structure of the file, a typo in a column name, or a container that had stopped answering. Diagnosis meant reproducing the case locally and reading the console.

That check was also wrong on its own terms: every code outside `2xx` — redirects included — was treated identically, and a `201` would have counted as a failure.

## The error contract

An error is now a type of its own. `DownstreamServiceException` carries the engine's original HTTP status alongside the message extracted from its body:

```java
public static DownstreamServiceException from(
    final int status,
    final String body,
    final String service
) {
    String message = "";
    if (body != null && !body.isBlank()) {
        message = DownstreamServiceException.message(body);
    }
    if (message.isBlank()) {
        message = String.format("%s returned HTTP %d", service, status);
    }
    return new DownstreamServiceException(status, message);
}
```

Parsing the body assumes nothing about which framework answered: the keys `detail`, `error` and `message` are tried in turn, and the first one that holds a string becomes the message. FastAPI sends `detail`, the service's own handlers send `error`; both are handled the same way. When the body cannot be read at all, what remains is an honest `python-xml-engine returned HTTP 503`.

The outward response is assembled by `ApiResponse.error(status, message)`, and the engine's status survives:

```json
{
  "error": "None of ['Дисциплины'] are in the columns",
  "status": 500
}
```

The success check was corrected to a range at the same time: `responseCode < 200 || responseCode >= 300`.

## The frontend stopped guessing

The page used to display its own text, because the response body could not be trusted. Now it reads the body — with conditions:

```js
async function responseError(response, fallback) {
  const body = await response.text();
  if (!body) {
    return fallback;
  }
  try {
    const payload = JSON.parse(body);
    const message = payload.detail || payload.error || payload.message;
    if (typeof message === "string" && message.trim()) {
      return message;
    }
```

Three details matter. An empty body yields the fallback text rather than an empty dialog. JSON that fails to parse does not take the handler down with it. And the text is inserted as text, not as markup: the message arrives from an external service and ultimately from a user-supplied file, so it must never be interpreted as HTML.

## A record of every request

Both Python engines gained middleware that records each completed request:

```python
@app.middleware("http")
async def log_request(request: Request, call_next):
    """Record every completed HTTP request in the event log."""
    started = time.monotonic()
    response = await call_next(request)
    logger.info(
        "%s %s -> %s in %.3fs",
        request.method,
        request.url.path,
        response.status_code,
        time.monotonic() - started,
    )
    return response
```

Method, path, status code, duration. That is enough to tell "the engine never answered" from "the engine refused in two tenths of a second" — precisely the distinction that could not be drawn before. On the Java side the same role is filled by a `logback.xml` configuration.

## Logs that survive a restart

A log is only useful if it lives until someone opens it. The containers run as an unprivileged user, and the log directory mounted from the host did not belong to them, so writes failed silently.

The fix lives in an entrypoint that runs before the application starts:

```sh
#!/bin/sh
set -eu

log_dir="${LOG_DIR:-/app/logs}"
mkdir -p "$log_dir"
chown -R appuser:appgroup "$log_dir"

exec su-exec appuser:appgroup "$@"
```

The directory is created and handed over, and then `exec` replaces the process with the application already running as the right user — no root left in the parent chain. The Java image uses `su-exec`, the Python images `gosu`; in `docker-compose` the mounts gained a `:z` flag for SELinux systems.

## Dates without a time component

A separate defect concerned the output. Excel stores a date together with a time, and values such as `2001-02-03T14:25:59` were reaching the XML, where the CyberDiploma format does not expect them. The fields `ДатаРожд` and `ДатаРешенияГэк` now pass through normalization:

```python
def date_only(value, field_name: str) -> str:
    """Return an Excel date value without its time component."""
    if pd.isna(value):
        return ""
    parsed = pd.to_datetime(value, errors="coerce", dayfirst=True)
    if pd.isna(parsed):
        raise ValueError(f"{field_name} contains an invalid date: {value}")
    return parsed.date().isoformat()
```

What matters here is not only the truncation but the third branch: an unparseable date no longer slips through silently to become malformed XML, but stops processing with the field and the value named. Refusing at the entrance is cheaper than a document whose defect surfaces at the registrar's desk.

## Tests as part of the contract

Everything above is an agreement, and agreements are easy to break unnoticed. So the update adds ten test files: on the Java side they cover `ApiResponse`, `DownstreamServiceException` and both controllers; on the Python side, the logging configuration, the entry points and the XML generator.

The most telling of them is the date test, which states the requirement outright:

```python
"ДатаРожд": [pd.Timestamp("2001-02-03 14:25:59")],
...
assert birth_date == "2001-02-03", "ДатаРожд contains a time component"
```

All suites are run together by `test-all.ps1`, which creates the virtual environments if they are missing; the contracts themselves are described in `TESTING.md`. The compiled classes under `target/classes`, which had been committed by oversight, were removed at the same time, and a `.gitignore` was added.

## Conclusions

1. An error is as much a part of the interface as a successful response. While `500` remains the only shape a failure takes, every diagnosis begins with reproducing it.
2. Reading someone else's error body is best done against a list of possible keys rather than a single one: cheaper than negotiating a format between services.
3. A message that originated in a user's file stays untrusted data all the way to the screen.
4. Permission to write to the log directory is a property of the container, not of the application — hence an entrypoint rather than code.
5. Validating on the way in beats correcting on the way out: a rejected date costs less than an XML file whose error appears later.

## Availability

The project is open under the MIT licence. The diagnostics can be tried on your own file: a deliberately wrong sheet or date will produce a specific reason rather than a `500`.

- Demo: [пгту-ртф.рф](https://xn----etb9agicel.xn--p1ai/)
- Source: [github.com/nikita-konkin/diploma_supplement_service](https://github.com/nikita-konkin/diploma_supplement_service)
