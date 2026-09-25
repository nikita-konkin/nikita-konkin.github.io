---
title: "The Diploma Service: 27 Defects From a Review, and Why the Worst Were Silent"
project: diploma_supplement_service
pair: diploma-revizija-defektov
platform: VK
type: Engineering update
date: 2026-09-25
source_from: eeaecfd62af026c2112f584b9a374b1673341645
source_rev: 0505871606b7018dd1d18a1fa6cfe896d9a5443a
lang: en
authors:
  - Nikita Konkin
summary: "A code review and a reconciliation against real input data produced 27 defects. The worst class was silent: a student dropped out of the XML with no error. How silent gaps became explicit errors, why the date fix from the previous breakdown was itself a defect, and how the rule for multi-semester courses was first decided and then written into code."
translation_of: 2026-09-25-revizija-defektov.md
links:
  demo: "https://xn----etb9agicel.xn--p1ai/"
  repo: "https://github.com/nikita-konkin/diploma_supplement_service"
tags: [programming, python, java, validation, security, personal-data]
---

The previous breakdown was about errors at the boundaries between services: how a meaningful refusal stopped collapsing into a "500". It dealt with cases where the system knows it has failed. This update is about the opposite cases: where the system fails and does not know it.

## A review and a reconciliation

The starting point was a full code review, backed by a reconciliation against real input data from a graduation — pivot tables, student information files, the generated XML and the printed supplements. The result was a list of 27 defects, with priorities and references to lines of code.

The priorities follow consequences, not the difficulty of the fix:

- **P0** — wrong or incomplete data reaches an education document, or personal data leaks;
- **P1** — a failure, unsafe behaviour, or an unclear error on real input;
- **P2** — inaccuracy in rare cases, interface inconvenience.

Which defects ended up in P0 is telling. Nearly all of them share one property: the system produced a result without saying it was incomplete.

## A student who dropped out silently

The chief one looked like this. If a student from the information file could not be found among the columns of the pivot table, the generator wrote a warning to the log and moved on. The XML was produced without an error — just without that student.

A warning in a log is worse than nothing here: it gives the appearance that the failure has been accounted for, while no one will ever see it. The document goes out incomplete all the same.

Now a skip is impossible. Every problem with the source data is collected into a single exception and returned together:

```python
class DataValidationError(ValueError):
    """Problems in the uploaded data, reported together."""

    def __init__(self, problems: List[str]):
        self.problems = problems
        super().__init__(
            f'Найдено ошибок в исходных данных: {len(problems)}\n'
            + '\n'.join(f'- {problem}' for problem in problems)
        )
```

The response is a single 400, and the page shows it as a list. Collecting every error at once, rather than stopping at the first, matters: the person checking fixes the file in one pass, not in as many passes as there are errors.

## Surname, initials and look-alike letters

The student dropping out was a consequence; the cause was the matching. A student was looked up among the pivot columns by surname alone — people sharing a surname could not be told apart. And a name typed with stray Latin letters did not match the same name in Cyrillic: a Latin "A" and a Cyrillic "А" look identical but are different characters.

Matching now uses surname and initials, is case-insensitive, treats "ё" and "е" as the same letter, and folds Latin look-alikes to Cyrillic:

```python
LOOKALIKES = str.maketrans('AaBCcEeHKMOoPpTXxYyËë', 'АаВСсЕеНКМОоРрТХхУуЁё')
```

The result of the match is checked in both directions. If a student has no column — an error, "no column with grades". If several fit — an error listing them, rather than taking whichever came first. And if two students claim the same column, that is an error too: without that check, both would receive the same grades.

## No `nan` in a document

An empty table cell becomes `nan` in pandas, an empty date `NaT`, and these values were reaching the XML as text. Now they are never written. Before export the required fields, dates, four-digit years and grades are checked: only codes 2 to 7 are allowed.

```python
GRADE_CODES = {2, 3, 4, 5, 6, 7}
```

Names mixing Latin and Cyrillic within a single word are flagged separately — the sign of a typo that no one will see by eye.

## A fix that was itself a defect

The previous breakdown has to be corrected here. In it, the `date_only` function was presented as the solution to the date problem — dropping the time and refusing an unparseable value:

```python
parsed = pd.to_datetime(value, errors="coerce", dayfirst=True)
```

`dayfirst=True` is there so that "03.02.2001" reads as 3 February rather than 2 March. But it acts on an ISO date too: the string "2001-02-03" was also read with its parts swapped — as 2 March.

The test shown in that breakdown did not catch this, and the reason is instructive. It passed the value `pd.Timestamp("2001-02-03 14:25:59")` — a ready-made date object, which `dayfirst` does not affect. The faulty path was the one for text dates, and the test exercised a different path. The test was green and never touched the defect.

Text dates are now parsed only against explicitly given formats:

```python
DATE_TEXT_FORMATS = (
    (re.compile(r'^\d{1,2}\.\d{1,2}\.\d{4}$'), '%d.%m.%Y'),
    (re.compile(r'^\d{4}-\d{2}-\d{2}$'), '%Y-%m-%d'),
    (re.compile(r'^\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}(:\d{2})?$'), 'ISO8601'),
)
```

The format is chosen from the shape of the string, not guessed. A date stored in a cell as a number is now refused with a request to set the cell's format to "Date" — instead of being silently interpreted.

## The gateway boundary

The second group of defects concerned the gateway that receives files. It had two hand-written multipart parsers and two HTTP clients — and no size limit at all. Now there is one parser, and the limit is checked before the request body is read: above `MAX_UPLOAD_MB` (20 MB by default) it returns 413 rather than spending memory reading.

One detail deserved attention of its own. Form part headers are now read as UTF-8: browsers send Cyrillic file names as they are, and the framework's own multipart reader rejects such names.

The Python services no longer publish their ports or accept requests from a browser: CORS is off, and only the gateway can reach them. Along with that, the unused `/config` and `/validate` endpoints and debug code were removed. Reading `.xls` was added alongside `.xlsx`, with the reader chosen by the file's content rather than its extension.

## Personal data

A separate P0 is reserved for leaks of personal data. Logs now contain row numbers rather than surnames: a row number is enough to find an error, whereas a surname in a log is a copy of personal data that outlives its need. Spreadsheets with student information are excluded from the repository by rule: only test fixtures are tracked.

## A question of rule

The most instructive defect turned out not to be technical. A course that ran over several semesters occupies several rows of the statement, each with its own hours and form of assessment. The parser converted each row to credits separately, and one of them reached the pivot along with its grade: 72 hours with a pass/fail test and 108 hours with an exam became "2 credits, passed".

This could not be fixed without deciding how it should work: whether to sum the hours of all semesters, and which grade counts as final. That is a question of rule, not of code, and the defect waited for a decision from the process owner: code written before the decision would have fixed an arbitrary answer in place.

The decision has been made, and the rule now lives in the code. The semester rows of one course are merged; its credits are the hours of all its rows, course work included, divided by 36 and rounded; the final grade is the last exam grade or, if there was no exam, the last grade received.

```python
def credits_of(hours: float) -> int:
    """Credits for hours; 106 h of a 3-credit discipline round to 3."""
    return int(hours / HOURS_PER_CREDIT + 0.5)
```

The hours rule was checked against curricula: for 89 courses of two 2025 groups it matched the curriculum in every case. But agreement on a sample is not a guarantee, so the curriculum itself was made the source of truth. It can be uploaded as a third file, and credits are then taken from its "Всего" (total) column. If there is no curriculum, or the course is not found in it, the credits from the statement's hours remain and the row is highlighted in orange. A new sheet, "Проверка з.е." (credit check), lists for every row where its credits came from and what is worth checking: a mismatch with the curriculum, fractional credits in the curriculum, hours not divisible by 36, a semester with no grade.

The review's main motif recurs here: where a result cannot be guaranteed, it should report its uncertainty rather than stay silent.

## Next

Alongside the review, a draft architecture was prepared for an open-source replacement of CyberDiploma — a modular monolith with a local web interface, a single build for a standalone PC and for a server, and seven recorded architectural decisions. It will get a breakdown of its own.

## Conclusions

1. The worst defect is not the one that crashes, but the one that silently produces an incomplete result. A crash is visible; an incomplete document is not.
2. A warning in a log is no substitute for an error: it records the failure where no one will read it.
3. Input errors are worth collecting all at once. Stopping at the first turns fixing a file into a loop over the number of errors.
4. A green test proves only what it checks. A date test on a ready-made object said nothing about parsing text.
5. A question of rule cannot be settled by code: first the process owner's decision, then the implementation — checked against the primary source, not only against its own arithmetic.

## Availability

The project is open under the MIT licence; the defect list and the draft architecture are in the repository's `docs/` directory.

- Demo: [пгту-ртф.рф](https://xn----etb9agicel.xn--p1ai/)
- Source: [github.com/nikita-konkin/diploma_supplement_service](https://github.com/nikita-konkin/diploma_supplement_service)
