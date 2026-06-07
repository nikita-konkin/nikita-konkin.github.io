---
title: "How to Build a Document Automation Service from Three Languages: A Practical Breakdown"
project: diploma_supplement_service
pair: diploma-uchebno-prakticheskaya
platform: VK
type: Technical breakdown
date: 2026-06-01
lang: en
authors:
  - Nikita Konkin
summary: "A practical look at a polyglot service architecture for Excel validation, XML generation, and Docker-based deployment."
translation_of: 2026-06-01-vk-uchebno-prakticheskaya.md
links:
  demo: "https://xn----etb9agicel.xn--p1ai/"
  repo: "https://github.com/nikita-konkin/diploma_supplement_service"
tags: [programming, backend, python, java, docker, microservices, fastapi]
---

Modern server-side systems are increasingly designed not as a single application but as a set of small, independent services written in different languages and tied together by a common protocol. Using a service that automates diploma supplements as an example, this breakdown looks at the engineering decisions behind such a "polyglot" architecture and why it is justified for an applied task.

## The problem

The underlying work is routine: take an Excel grade sheet with subjects, hours, and grades, check it for errors, and export it into a strict XML format. Manual processing is slow and error-prone, so the process is worth automating.

The task splits into two scenarios:

- assembling a pivot table with highlighted problematic cells;
- generating an XML document from a given template.

## Architecture: why three modules instead of one

The system is deliberately split into three independent services rather than a single monolithic application.

- **java-api** — the entry gateway. It accepts HTTP requests and routes tasks. It is built on the lightweight Takes framework: a minimalist layer is sufficient for a gateway, whereas full-weight Spring would be excessive.
- **python-engine** — the table-processing module, built on FastAPI together with pandas and openpyxl. It reads the Excel file, detects inconsistencies, and marks problematic cells with color.
- **python-xml-engine** — an XML generator that works from a template, also on FastAPI.

This separation has a practical payoff: each module can be developed and restarted independently. Python is used where it is strong at data processing, Java in the role of a reliable API layer. Each language is applied to its intended purpose.

## Example: highlighting errors in Excel

The most illustrative fragment is the cell-validation logic. Using openpyxl, the service walks through the file and fills suspicious values with color: empty cells and the `!` and `?` symbols.

```python
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

fill = PatternFill(start_color="FFC7CE",
                   end_color="FFC7CE",
                   fill_type="solid")

for row in ws.iter_rows():
    for cell in row:
        if cell.value in (None, "", "!", "?"):
            cell.fill = fill   # flagged a problem
```

The technique is simple, but it is exactly what saves hours of manual checking: the reviewer only needs to inspect the highlighted cells rather than the whole file.

## Docker: launch with a single command

Three services mean three potential points of failure when setting up the environment. Docker Compose removes that complexity: all modules are described in `docker-compose.yml`, run on a shared network, and start with a single command.

```sh
docker-compose up --build
```

This eliminates the "works only on my machine" situation and the manual installation of Java and Python. Here, a reproducible environment is not a convenience but a requirement for an applied service.

## Takeaways

1. A large task is best split into independent services.
2. Languages can be combined, choosing the right tool for each sub-task.
3. The pandas and openpyxl pairing is effective for working with Excel.
4. Docker Compose turns a heterogeneous stack into one reproducible project.

## Availability

The project is open source under the MIT license and available without registration or restrictions: you can run the live demo, deploy the service locally, or study the source code.

- Demo: [пгту-ртф.рф](https://xn----etb9agicel.xn--p1ai/)
- Source code: [github.com/nikita-konkin/diploma_supplement_service](https://github.com/nikita-konkin/diploma_supplement_service)
