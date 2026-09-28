---
title: "Otkrytyi Diplom: A Java 11 Prototype, Checked Until the XML Matched Byte for Byte"
project: open_diplom
pair: open-diplom-prototip
platform: VK
type: Technical breakdown
date: 2026-09-29
source_rev: d189450943421b642a10390e4ba9e1027b270200
lang: en
authors:
  - Nikita Konkin
summary: "The draft architecture for an open replacement for CyberDiploma now has a prototype and a repository of its own. What the prototype does, which of the stack criteria are already measured and which are not, how the ported rules were checked against the current service on the whole archive, and why curricula in PDF had to be read by the table's rules."
image: /assets/open_diplom/preview.png
translation_of: 2026-09-29-prototip-na-java-11.md
links:
  repo: "https://github.com/nikita-konkin/open-diplom"
tags: [programming, java, architecture, printing, pdf]
---

In the previous breakdown, the architecture of an open replacement for CyberDiploma was a draft, and the choice of Java 11 a reasoned hypothesis with a named fallback. Now the project has a name, a repository of its own under the Apache 2.0 licence, and a prototype: Otkrytyi Diplom ("Open Diploma").

The prototype is not the MVP. It has no graduate register yet and no printing on blanks. Its job is different: to test the chosen stack against criteria written down in advance, and to port the current service's rules in a way that can be trusted.

## What the prototype does

The program is a single file, `open-diplom.jar`, with an embedded Tomcat 10.1. In desktop mode it listens only on `127.0.0.1`, opens the browser itself and creates a folder with an SQLite database next to it. The pages are plain HTML with no scripts.

- **Importing a faculty grade statement** in `.xls` or `.xlsx`, optionally together with the curriculum — as Excel or as a PDF saved from «Планы», the planning software. Semesters are summed, credits are taken from the curriculum, doubtful rows are flagged for the operator, and the result is stored in the staging area.
- **XML for CyberDiploma**, from the pivot table and the student data — for the transition, while printing stays with CyberDiploma.
- **A printer calibration test sheet** — a PDF with rightward and downward corrections in millimetres.

{% include screen.html src="/assets/open_diplom/import.webp" wide=true width=1650 height=1076 caption="Statement import: credits by hours and by the curriculum, where the final figure came from, and what the operator should check. Here and below — synthetic data from the project's examples." alt="The «statement read» page: a credits table with columns for hours, plan, result, source and what to check, and a grades table for three fictitious students" %}

## Criteria set in advance

The criteria for choosing the stack were written down before the prototype. Now almost all of them have numbers, measured in Linux containers on a Mac, on two architectures: arm64 and x86-64 (under Rosetta emulation):

- **runs with nothing installed:** the trimmed runtime takes 51–56 MB, the program itself 39 MB;
- **start-up time:** 0.3 s on arm64 and 0.7 s on x86-64, against a requirement of under five seconds;
- **memory:** a peak of 243 and 276 MB, against a requirement of under 300 MB;
- **PDF in millimetres:** a field sits where it should in the PDF to within 0.5 mm, and the calibration correction moves it — the tests read the coordinates back from the file.

The most instructive detail concerns memory. With the JVM's default settings the peak was 402 MB — the criterion would have failed. Three launch parameters brought it within bounds: a 128 MB heap, the serial garbage collector, and the C1 compiler only. So the launcher sets them itself, rather than leaving them to the user.

Just as important is what has not been checked yet. The main risk — 32-bit Windows 7 with 2 GB of memory — remains untested: the test machines are postponed. The printout on paper has not been measured either; that needs the printer the blanks are printed on. The prototype keeps what was measured honestly apart from what is assumed.

## A port checked by comparison

The current service's rules — reading the statement, summing semesters, credits from the curriculum, checks on the student data and the XML export — were rewritten from Python into Java. How can one be sure nothing changed in the rewrite?

The first level is tests: there are 91, and 44 of their scenarios were ported from the current service's Python tests. The second is testing by breakage. Errors were introduced into a copy of the code one at a time: the exam's priority was removed, the calibration correction switched off, the state exam placed after the thesis defence, file names read in the wrong encoding. The tests caught every one. One — removing an explicit UTF-8 setting — went unnoticed, and rightly so: Tomcat 10.1 reads names as UTF-8 without it.

The third level is a comparison on real data. Both implementations, Python and Java, were run over all 93 workbooks in the 2019–2026 archive: 105 statement parses, 93 curriculum reads and 60 "pivot table × student data" pairs. The comparison ran locally; the data went nowhere. There were no differences; the resulting XML files matched byte for byte.

Byte-for-byte agreement is a strong claim, and that is exactly what makes it useful: any future change to the rules can be checked by the same comparison.

## What was deliberately left behind

Not everything in the current service deserves to be ported. Matching statement rows against the "list of courses" is a substring heuristic, and it is where the errors found in the review grew from. In the new system, statement rows are matched against the curriculum in the staging area, and the operator confirms the result. Optional courses will be identified by the curriculum's FTD block, not by the list of courses.

A port is a convenient moment not only to keep what works, but to leave behind what worked badly.

## Curricula from PDF

Curricula arrive mostly as PDFs saved from «Планы». Such a file has text but no cells: only letters with coordinates and the lines of the grid. A long course name wraps onto two to four lines above and below the row with its index, and the gap between those lines is the same as between neighbouring rows of the table. The rows cannot be reconstructed from the text alone.

So the plan is read by its grid: table rows are the gaps between horizontal lines, columns the gaps between vertical ones. Column numbers sit differently in different plans, so credits are taken from the first column under the heading «в зачетных единицах» (in credits), and names from the column under «Структура ОП» (programme structure). Block totals are skipped: the Excel version of a plan has none in its name column, so the same plan yields the same credits in both formats.

The result on the archive: all five PDF plans with text were read; two bachelor's plans were checked against Excel plans for the same programmes a year earlier (the 2021 intake against 2022) and agreed in 51 of 51 and 59 of 59 credits. Two more files turned out to be scans with no text — the program refuses them and says so plainly: "this looks like a scan".

## XML fields from the curriculum

Until now, the programme's volume, contact hours, and the credits for internships and the final state attestation were typed into the form by hand for each programme — and typing repeated numbers by hand is exactly where errors are born. Now a «Заполнить из плана» ("fill from the plan") button fills nine fields of ten: the direction and profile, qualification, form and term of study from the plan's title, and the volumes from its totals.

{% include screen.html src="/assets/open_diplom/xml-from-plan.webp" wide=true width=870 height=1222 max=440 caption="Fill from the plan: every field says where its value came from. The chair of the examination board is not in the plan and is typed by hand." alt="The CyberDiploma XML form with fields filled from the curriculum and a note under each field naming its source" %}

Two rules deserve a note. Contact hours are taken from the totals row only if its hours add up: the total equals exams plus classes, and classes equal contact work plus independent work. If they do not, the field stays empty and is flagged. The term of study is the full-time normative term for any form of study — the process owner's decision, and how supplements have been printed in past years. Checked on five plans from 2023–2026: all four numbers matched the printed supplements.

The checks on student data were ported together with the review's main principle — all errors at once, in one list:

{% include screen.html src="/assets/open_diplom/xml-errors.webp" wide=true width=1650 height=495 caption="Errors in the student data gathered into one list: a date that does not exist, a three-digit year, an empty field, and a student with no column in the pivot table." alt="A message reporting four errors in the source data, listed for fictitious students with row numbers in the student data file" %}

## Calibration

Printing on blanks is not implemented yet, but its foundation is in place: a PDF with a field at given millimetres, and printer calibration. The test sheet is printed at 100% scale, then the distance to the cross in the corner is measured with a ruler; the corrections come from a formula printed on the sheet itself. A 10 cm ruler on the sheet checks that the printer did not scale the page.

{% include screen.html src="/assets/open_diplom/test-sheet.webp" wide=true width=1287 height=910 caption="The calibration test sheet: crosses near the edges, the supplement field, the correction formula and a ruler to check the scale." alt="A landscape A4 sheet with crosses in the corners and centre, calibration instructions and a 10-centimetre ruler" %}

## Next

The next steps are ordered by risk. First the test machines: 32-bit Windows 7 and Astra Linux, together with a check of Java 17 on 32-bit Windows — many libraries no longer update for Java 11. Then the test sheet on the printer the blanks are printed on. The package can be made smaller: the program currently carries SQLite libraries for every platform, while only Windows and Linux are needed. And then the start of the MVP: the register's data model and matching the statement against the curriculum in the staging area.

## Conclusions

1. Criteria written down before the prototype turn choosing a stack from an opinion into a measurement. Without them, 402 MB of memory could easily have been judged acceptable.
2. Settings on which meeting the requirements depends should be set by the program, not the user: the launcher fixes the JVM parameters.
3. A port between languages is checked not only by tests but by comparison on real data: byte-for-byte agreement is the strictest and the cheapest criterion.
4. A rewrite is a chance not to carry over what caused errors: the substring heuristic is replaced by matching with the operator's confirmation.
5. A prototype is as useful as it is honest about what was measured and what was not: the main risk — old 32-bit Windows — is named plainly.

## Availability

The project is open under the Apache 2.0 licence; the architecture and decision records are in `docs/architecture/`, the prototype's results in `docs/prototype.md`. The tests use no real data: workbooks and PDFs are built in memory.

- Source: [github.com/nikita-konkin/open-diplom](https://github.com/nikita-konkin/open-diplom)
