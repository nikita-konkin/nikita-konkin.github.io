---
title: "An Open Replacement for CyberDiploma: An Architecture Shaped by Windows 7"
project: diploma_supplement_service
pair: diploma-arkhitektura-zameny
platform: VK
type: Technical breakdown
date: 2026-09-26
source_from: eeaecfd62af026c2112f584b9a374b1673341645
source_rev: 0505871606b7018dd1d18a1fa6cfe896d9a5443a
lang: en
authors:
  - Nikita Konkin
summary: "A draft architecture for an open system that prepares, checks and prints diplomas. Why the platform requirements ruled out nearly every technology, how one build runs both on an offline PC and on a university server, why import goes through a staging area and printing through PDF in millimetres. The stack is chosen; testing it on the target platforms is still ahead."
translation_of: 2026-09-26-arkhitektura-zameny.md
links:
  repo: "https://github.com/nikita-konkin/diploma_supplement_service"
tags: [programming, architecture, java, astra-linux, printing]
---

The previous breakdowns dealt with the current service — a chain of three services that turns faculty grade statements into XML for CyberDiploma. This one is about what may replace it. Alongside the review, a draft architecture was prepared for an open system that prepares, checks, prints and keeps records of diplomas and their supplements.

It is a document for discussion, not working code. But it is at the draft stage that most of the decisions hardest to change later are made.

## Why a replacement

Today the process works like this. The current service turns grade statements and the curriculum into a pivot table and XML in format 3.5.1. The XML is imported into CyberDiploma, where the registration number, issue date, blank and organisation details are added by hand, and the documents are then printed from FastReport templates onto a printing house's blanks.

The scheme has three shortcomings. CyberDiploma is a closed, paid program with a USB dongle and an encrypted database. Manual steps remain between the systems, and at the joins errors appear that neither side catches. And finally — an awkward admission — the current service itself, three runtimes in Docker, cannot be installed on the university's workstations.

## Requirements that rule out technologies

The draft opens with ten requirements, and three of them determine almost everything else:

- **one build, two modes** — a single computer without a network, and a university server for many users;
- **platforms** — Windows 7 and 8.1, including 32-bit, Windows 10 and 11, Astra Linux, RED OS and Alt;
- **no Docker and no preinstalled runtimes** — a direct consequence of the previous point.

The reason is that universities run computers of all these generations at once. Docker does not work on old and 32-bit Windows, and in closed Astra Linux environments with the closed software environment mode (ZPS) enabled, only signed executables run.

Two of the remaining requirements deserve a mention. The first follows directly from the review: no record is ever lost silently, and every discrepancy is shown to the user. The second: personal data is stored only in the university's own installation, and the open repository may hold synthetic data only.

## One file, two modes

The answer to the first requirement is a modular monolith with a built-in web server and a browser interface. In desktop mode the server listens on `127.0.0.1`, the data lives in an SQLite file, and a browser opens on launch. In server mode the same executable listens on the network, the data is kept in PostgreSQL, and accounts and roles are switched on.

The difference between a computer in a department office and the university server is thus reduced to a listen address and a database. Installing means unpacking and running; updating means replacing one file; a desktop backup is a copy of the database file.

The modules — reference data, curricula, import, the graduate register, checking, printing, export, audit and access — are separated by explicit boundaries and never touch each other's tables directly. The interface is rendered on the server with minimal JavaScript and has to work in Chrome 109 and Firefox ESR 115 — the last versions of those browsers for Windows 7.

Two databases have a price: the code is limited to the subset of SQL that behaves the same in both, the schema changes only through numbered migrations, and the data-layer tests run twice. Three alternatives were rejected: microservices in Docker (as now), a native desktop application, which does not get a server mode for free, and a server-only web app, which does not cover a computer without a network.

## An import that cannot lose a record

The review's main lesson — a student silently dropping out of the XML — is closed in the new system not by a check but by the shape of the process. Import never writes data straight into the register. Uploaded files land in a staging area and pass through stages: layout recognition, normalisation (whitespace, Latin look-alikes, dates, grade codes), matching, a report, confirmation by the user, and only then a write to the register and the audit log.

The report splits records into four groups: "matched", "missing from the statements", "missing from the student data", "ambiguous". While mismatches remain, the import cannot be confirmed: the user fixes the file or links records by hand. Every value keeps a reference to its source — file, sheet and row — so for any field in a document you can see where it came from.

Losing a record silently becomes impossible by construction. The price is one more step: the report has to be read.

The same section draws a conclusion about the current parser. It keeps data in an index string of the form "Name_type_credits", matches on substrings and rewrites the table's index as it goes — which is where the multi-semester defect came from. That code is to be not refactored but rewritten once, as the new system's import module: with an explicit model of a statement row (course, semester, hours, form of assessment, grade), summing of semesters, and matching against the curriculum. The existing tests become the specification of its behaviour.

## Printing in millimetres

Diplomas are printed on printing houses' security blanks: the title page on an A4 landscape sheet, the supplement on four A3 pages. CyberDiploma's templates are FastReport 4 files (`.fr3`, compressed XML) with field coordinates in pixels at 96 dpi. Every printer shifts its output in its own way, and browsers may scale a PDF.

The decision has several parts:

- a template format of its own, with pages and fields in millimetres — coordinates, font, alignment, wrapping, shrinking, and the course table flowing across the supplement's pages;
- the output is a PDF at 1:1 scale with embedded fonts; the image of the blank is used only in the preview;
- per-printer calibration — dx and dy offsets in millimetres, found with a test sheet;
- import of existing `.fr3` templates with converted coordinates: 1 mm = 3.7795 pixels at 96 dpi.

The default font is PT Astra Serif: an open licence and metric compatibility with Times New Roman. Printing-house templates stay out of the open repository until their licences are checked — each university imports its own. The target accuracy is no more than 0.5 mm between text and the blank's field after calibration.

The draft is frank about the hardest part of the MVP: a text layout engine of its own. The rejected options show why it cannot be avoided: printing HTML from a browser depends on the browser and its settings, FastReport is a proprietary Windows component, and printing straight to the printer driver needs a separate implementation for each OS and does not work in server mode.

## Compatibility without breaking in

During the transition the university keeps printing in CyberDiploma. Its database and record files are an encrypted container in a closed format. There is one open way to exchange data: the "ФайлОбменаКиберДиплом" XML, version 3.5.1, which the program imports and which the current service can already generate.

So XML 3.5.1 export is part of the MVP, import of the same XML goes through the staging area, and the closed files are neither parsed nor decrypted. The decision removes the legal risks of circumventing the protection of someone else's format, at a clear price: the issuing history in CyberDiploma cannot be carried over automatically. Also rejected was driving the program's interface automatically, as was done in 2025: it is fragile and depends on the program's version and the screen resolution.

## The stack: Java 11

Three requirements rule out most candidates before convenience is even compared. The tool has to receive security updates and build for Windows 7 x86; run on Astra Linux 1.7 with its old glibc 2.28 and possibly with ZPS; need no runtime installed, while still reading `.xls` and `.xlsx` and producing PDF accurate to the millimetre.

Rejected at once were modern .NET (does not run on Windows 7), Node.js and Electron (long without updates for Windows 7) and Rust (Windows 7 remains only as a tier-3 target). Four options were compared in earnest:

- **Python 3.8 with PyInstaller** — direct reuse of the code, but it is the last version with Windows 7, its support ended in October 2024, a build with pandas exceeds 100 MB, and antivirus software often dislikes single-file builds;
- **Go** — one static file with no glibc dependency, the best option on Linux; but officially only Go 1.20 supports Windows 7, beyond which lies a community fork with a single maintainer, and reading `.xls` in Go is weak;
- **Free Pascal / Lazarus** — excellent portability, but a narrow community and no experience in the team;
- **Java 11 LTS with the runtime bundled** — Liberica JDK 11 officially supports 32- and 64-bit Windows 7 and still receives updates, there is a certified domestic build for Russian Linux distributions, Apache POI is the best library for both Excel formats, and the current service's gateway is already written in Java.

The choice fell on Java 11: it is the only candidate whose mandatory requirements are all met by components that receive security updates. The composition: a runtime trimmed with jlink, an embedded web server, server-rendered HTML with htmx, JDBC and Flyway migrations, Apache POI, and OpenPDF or PDFBox for printing by coordinates.

The price is recorded alongside. The package and its memory use (150–250 MB expected) are larger than Go's. Java 11 has a "ceiling": newer branches of some libraries require Java 17, so their versions are pinned. If the prototype shows that a Java 17 runtime works on 32-bit Windows 7, Java 17 becomes the baseline. The fallback is Go on the Windows 7 fork, should Java not fit the memory and start-up limits.

## What is not yet tested

The draft is still a draft. Six of the seven architecture decisions have the status "proposed"; the stack choice has been accepted by the project owner, but with a reservation — pending a prototype.

The prototype is meant to be the same on every platform: an HTTP server with a page, SQLite reads and writes, reading `.xls` and `.xlsx` in the faculty statements' layout, a PDF with a field at given millimetres in a Cyrillic font, and printing a test sheet. The criteria are set in advance too: runs with nothing installed, starts in under five seconds, uses less than 300 MB of memory, deviates no more than 0.5 mm on paper. The test machines are 32-bit Windows 7 with 2 GB of memory, Astra Linux 1.7 with and without ZPS, and Windows 11. These checks are postponed for now, and until they pass the stack choice is a reasoned hypothesis with a named fallback.

The transition is laid out in stages as well. The current service keeps running. The new system's MVP covers reference data, curricula, import, the register, checking and XML export, while printing stays with CyberDiploma. Then printing: one graduating class is printed in both systems in parallel and the printouts are compared. After the MVP come uploads to FIS FRDO, the federal register of education documents, and templates for other printing houses.

## Conclusions

1. Platform requirements outweigh preferences: Windows 7 x86 and Astra Linux's closed environment ruled out nearly every modern stack before their convenience was even compared.
2. One build for two modes is cheaper than two products: the difference between an offline computer and a university server is reduced to a listen address and a database.
3. Silent loss of a record is better excluded by the shape of the process than by checks layered on top: the staging area will not let an import be confirmed while discrepancies remain.
4. Print accuracy is a property of the whole chain, not of the template: millimetres in the template, PDF at 1:1, printer calibration, and printing without scaling.
5. A stack chosen before a prototype is a hypothesis. It is more honest to record the test criteria and a fallback than to declare the decision final.

## Availability

The draft architecture and the seven architecture decision records are in the repository's `docs/architecture/` directory; the project is open under the MIT licence.

- Source and documentation: [github.com/nikita-konkin/diploma_supplement_service](https://github.com/nikita-konkin/diploma_supplement_service)
