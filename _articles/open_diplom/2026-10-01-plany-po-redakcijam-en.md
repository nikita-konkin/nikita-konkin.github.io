---
title: "Otkrytyi Diplom: Curricula by Admission Year and Edition"
project: open_diplom
pair: open-diplom-plany
platform: VK
type: Technical breakdown
date: 2026-10-01
source_from: d189450943421b642a10390e4ba9e1027b270200
source_rev: 3b48894d122f88b399e64fc3114a048a66f4245b
lang: en
authors:
  - Nikita Konkin
summary: "In Otkrytyi Diplom the curriculum has become an entity of its own: plans are stored by programme, form of study and admission year, every correction is saved as a new edition, checksums verify a plan when it is loaded, and a plan that exists only as a scan is entered as a difference from a similar one. How it works and how it was checked on real plans."
image: /assets/open_diplom/plans-preview.png
translation_of: 2026-10-01-plany-po-redakcijam.md
links:
  repo: "https://github.com/nikita-konkin/open-diplom"
tags: [programming, java, architecture, data, docker]
---

Until now the curriculum was an auxiliary file in Otkrytyi Diplom: it was attached to a grade statement, the program took credits and totals from it, and that was the end of its role. Now a plan is stored in the database as an entity of its own — by programme, form of study and admission year, with a history of corrections. The decision is recorded in ADR-0008, and the prototype has gained a "Curricula" section.

{% include screen.html src="/assets/open_diplom/plans-list.webp" wide=true width=1400 height=700 caption="The «Учебные планы» (Curricula) section: loading a plan and the list of saved plans with form of study, admission year, edition number and the count of checksum errors. Here and below, a synthetic plan from the project's tests." alt="The Curricula page: a file upload form and a table of two plans of one programme, full-time, admission years 2021 and 2022" %}

## Why the plan belongs in the database

Checking the archive showed two things. First, a plan changes from year to year, but only a little. Between neighbouring admission years the credits of every discipline matched — 51 of 51 and 59 of 59 for two bachelor's programmes — and a master's plan matched the next year's in every column of every row. Second, the forms of study of a single year differ more. The part-time master's programme has its semesters shifted by one and 122 contact hours instead of 820; the part-time bachelor's programme has its technological practice as one row of 9 credits, while the full-time one has two rows, of 6 and 3.

Hence the task: to see exactly what changed, and not to enter the plan anew every year. Typing numbers from the plan into the summary table for every graduation is exactly where errors are born.

One more circumstance gets in the way: of the archive's 43 PDF plans, only five have text. The rest are scans, which can only be retyped.

## Programme, plan, edition

The data model has three levels:

- **programme** — the field-of-study code and the profile; profiles are compared ignoring case and punctuation;
- **curriculum** — a programme, a form of study and an admission year; every year has its own plan, even if it matches last year's;
- **edition** — an immutable snapshot of a plan.

Loading a plan with the same key again creates a new edition only if at least one cell or the header differs; the SHA-256 of the header and all rows is compared. The same file loaded again gets the answer "already loaded". A saved edition never changes: a correction is saved as a new edition that refers to the one it was based on. So a graduating class checked against a plan can always refer to the edition it was checked against.

Rows are stored as printed in the plan: the index, the name, the semesters of five forms of assessment, three credit columns and five hour columns. A row's key is its position, not its index, because the index is not unique even within one plan: «Б.3.1.1» is printed both on the final qualification work and on the state exam.

The plan's structure — a row's parent, its block, the leaves, elective alternatives, the printed name of a practice — is not stored but computed on reading. So an old edition does not depend on how an old version of the program parsed it: fixing the parsing rules changes the display, not the data.

{% include screen.html src="/assets/open_diplom/plans-edition.webp" wide=true width=1400 height=1279 caption="A plan edition: header, totals, checksums and the differences from the nearest plan — the same profile and form for the previous admission year." alt="The «Учебный план, редакция 1» page with the plan header, a totals table, the message that checksums hold and a list of changes: Mathematics credits 8 → 7, Physics credits 4 → 5 and a pass/fail replaced by a graded credit" %}

## Checksums

The plan checks itself. In every row, credits equal the credits for exams plus the credits for classes, hours equal credits times 36, and class hours equal contact work plus independent work. In the structure, every row equals the sum of the rows nested in it, and the programme's volume equals the sum of blocks 1–3. A wrong number is reported once — at the row above it, not along the whole chain of parents.

A loaded file is saved in any case, and the number of errors is recorded in the edition and shown in the list of plans. A correction whose sums do not hold can be saved only if the operator explicitly confirms it.

{% include screen.html src="/assets/open_diplom/plans-edit-check.webp" wide=true width=1400 height=668 caption="A correction that breaks the sums: the practice has 9 credits instead of 6. The program names three discrepancies and shows what changed against the original edition." alt="The plan editing page with three checksum errors on the pre-graduation and industrial practice and a list of changes «з.е.: 6 → 9»" %}

Checking real plans found one false alarm, and it is instructive. The hours of the "part formed by the participants" were off by exactly 328. These are the physical culture electives: they have hours but no credits, and «Планы», the planning software, leaves them out of the part's sum. Now a row without credits stays out of the sums — the way the source itself counts.

## Comparison with the nearest plan

Every edition is compared with the programme's nearest plan: the same form for the nearest previous year, or, if there is none, another form for the same year. Elements are matched by their printed name, not by index, so a renumbered discipline remains the same discipline. The comparison shows what was added and removed, where credits and forms of assessment changed, and how the totals changed.

On real plans the comparison confirmed what would otherwise have had to be found by eye: the master's plans of two neighbouring years matched entirely, while comparing the full-time and part-time forms of one year showed the semesters shifted by one and classroom hours going from 820 to 122.

## A plan that exists only as a scan

Recognising scans — with OCR or a small model — was considered and postponed. Another route turned out cheaper: «Создать на основе», "Create from". The operator takes the nearest plan and corrects only the differences, and the checksums confirm the result. If the form of study is different, the contact and independent hours are cleared: they depend on the form, while the remaining hours follow from the credits. The operator types in the total hours from the document.

{% include screen.html src="/assets/open_diplom/plans-derive.webp" wide=true width=1400 height=1209 caption="«Создать на основе»: a part-time plan made from a full-time one. The hours that depend on the form of study are cleared, and the program asks for them from the document." alt="The «Новый план на основе редакции 1» page: a warning about cleared contact and independent hours, a header with the part-time form and a table of rows to edit" %}

It was checked on a real case: the part-time bachelor's plan for 2021 exists only as a scan. It was created from the full-time plan of the same year: the technological practice was merged into one row of 9 credits, the second row removed, and the contact and independent hours typed into the totals row. The sums held, the comparison showed exactly this correction, and all 55 elements matched the scan.

## How it was checked

Seven real plans — five PDFs with text and two Excel files — were loaded through the pages, and the sums hold for all of them. The only remaining warning is a module heading without numbers. The Excel and PDF versions of one plan matched row by row in every column. Loading the same PDF again was recognised as "already loaded", and a scan was refused with a hint about "Create from". The checks ran locally; real plans never reach the repository, since the tests build plans in memory.

There are now 128 tests instead of 91, and they were again checked by breaking the code. The tests caught three planted errors: counting rows without credits in the sums, finding a parent by index prefix without the dot — which put the second «Б.3.1.1» under the first — and carrying contact hours over to a plan of another form.

One breakage went unnoticed, and rightly so. The explicit limit on the number of form fields was removed from the settings: Tomcat 10.1.60 defaults to 10,000, and the form of a 70-row plan has about 1,200 fields. The setting stays anyway: if a Tomcat update brings a lower default, a long plan must not be silently cut off. A separate test with a form of over 1,500 fields guards it.

## Server and container

The prototype still runs as a single file on a workstation, but it can now be installed on a server too. A new `context-path` setting publishes the program under a prefix behind a reverse proxy, for example at `https://example.org/open-diplom/`: page links are relative to a `<base>` with the prefix, redirects start from it, and the routes do not see it. The prefix is empty by default, so a desktop run is unchanged.

For servers that already run Docker there is an image. Its build runs every test, including printing and reading PDF plans: for them the image gets the Liberation Serif font, which has the metrics of Times New Roman. The program itself runs in the container as an unprivileged user and keeps its database in the `/data` volume.

## Next

The next stage is the graduating class: binding it to a specific edition of the plan and matching grade-statement rows to plan elements in the staging area. The links "statement row → plan element" will be stored at the programme level, so that next year's plan picks them up by itself. One limitation is already known: "Create from" carries the semesters over as they are, while the part-time form numbers them differently. The diploma supplement does not need semesters, but they should be corrected in the plan from the document.

## Conclusions

1. A document that changes from year to year is worth storing as editions rather than overwriting; otherwise it is lost which version a result was checked against.
2. Structure is better computed on reading than stored: then fixing the parsing rules does not require rewriting old data.
3. Checksums turn manual entry from a risk into a verifiable operation — and are themselves checked on real data: the 328-hour false alarm surfaced only there.
4. A scan does not have to be recognised. Entering the difference from a similar plan, verified by the sums, is cheaper and more reliable.
5. A setting the tests cannot break is not necessarily redundant: the explicit field limit protects against a future update, and a separate test pins it down.

## Availability

The project is open under the Apache 2.0 licence. The decision on storing plans is `docs/architecture/adr/0008-curricula-by-editions.md`; the results of the checks are in `docs/prototype.md`.

- Source code: [github.com/nikita-konkin/open-diplom](https://github.com/nikita-konkin/open-diplom)
