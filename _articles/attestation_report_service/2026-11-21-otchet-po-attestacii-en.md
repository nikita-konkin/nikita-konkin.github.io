---
title: "Attestation Report: RITM Sign-In, a Heatmap of Scores, and Links That Leave No Key in the Logs"
project: attestation_report_service
pair: attestation-intro
platform: Web
type: Technical breakdown
date: 2026-11-21
source_rev: edbac6b07df68b62d38761506b11c2f288ace988
lang: en
authors:
  - Nikita Konkin
summary: "The department's reports on student attestation used to be built by command-line scripts. Now they come from a web service: sign-in with a RITM portal account without storing the password, a choice of department and groups, a summary with the change since the previous attestation, a heatmap of scores, short reports in DOCX and PDF of at most 2 MB, and expiring links to a report whose key never reaches the server logs. The service has left the diploma supplement site for a repository of its own and deploys itself after every merge."
image: /assets/attestation_report_service/preview.png
translation_of: 2026-11-21-otchet-po-attestacii.md
links:
  repo: "https://github.com/nikita-konkin/attestation-report-service"
tags: [programming, python, fastapi, security, reports, visualisation]
---

Several times a semester, teachers enter attestation scores on the university's RITM portal: each student gets a score in each discipline, and a score below the minimum means a failed attestation, marked Н/А. After each attestation the department prepares a short report: how many students passed in full, which groups and disciplines have many failures, and where the department stands among the others. These reports used to be built by my scripts on the command line. Since late October they come from the «Отчёт по аттестации» (attestation report) service on the [пгту-ртф.рф](https://xn----etb9agicel.xn--p1ai/attestation) site, which any teacher can use.

The service pulls two of the portal's reports from RITM: the attestation of each group of the department, and the share of passed attestations by department across the university. From them it builds a short report formatted to the Russian GOST standard, detailed reports for bachelor's and master's programmes, and a summary shown right on the page.

All the screenshots below come from a local copy of the service with made-up data: a «ДЕМО» department, «ДЕМ(о)» groups, and students named «Студент1 Тест Тестович» (Student1 Test Testovich).

## Sign-in without storing a password

The first version of the service had accounts of its own: a hash of the site password in the settings, and an optional saved RITM password encrypted with AES-256-GCM under a key derived from the site password. That scheme went away entirely on the same day. Sign-in now uses the RITM account: the portal itself checks the password, the service uses it once and keeps only the portal session in memory. The session is forgotten on logout or after 30 idle minutes. There are no more accounts, hashes or encrypted vault: the safest password is one that is stored nowhere.

The rest of the protection is ordinary but complete:

- a session cookie with the `HttpOnly`, `Secure` and `SameSite=Strict` flags and the path `/attestation`; every request that changes something needs a CSRF token;
- failed sign-ins are limited to 5 per client and 30 in total per 15 minutes, and limited attempts never reach the portal;
- a content security policy of `default-src 'none'`, no inline scripts or styles, and no passwords in the logs;
- the downloaded files hold students' names and scores, so they are deleted after 30 minutes.

The `Secure` flag once caused a puzzling bug. Over plain HTTP a browser does not keep such a cookie, so after a successful sign-in the page silently showed the sign-in form again. Sign-in now redirects to an address with a `?error=none` marker: if the cookie arrived, the page opens as usual and removes the marker, and if it did not, the sign-in form explains that the site has to be opened over HTTPS.

## Department, programmes and groups

At first the service built the report only for its author's department; now it works for any. The page asks for the period (academic year, semester and attestation number), the department from the portal's report on attestation shares, the faculty, and the degree programmes of the groups. The choice is remembered for the department after a successful report, and new groups of the same programmes join the report by themselves.

{% include screen.html src="/assets/attestation_report_service/form.webp" wide=true width=1653 height=1112 caption="Choosing the period, department and groups. Made-up data." alt="The «Отчёт по аттестации кафедры» page styled as a drafting sheet: lists for academic year 2026-2027, odd semester, attestation 2, department «ДЕМО» and faculty «ДФ»; a «Группы кафедры» block with a switch between all groups of the ticked programmes and only the ticked groups, with the programmes «ДЕМ(о)», groups ДЕМ(о)-11 to ДЕМ(о)-41, and «ДЕМм(о)», group ДЕМм(о)-11, ticked; fields for the faculty name in the report header and the head of department; a «Сформировать отчёт» button" %}

A second mode, «Только отмеченные группы» (only the ticked groups), builds a report on one or a few groups. Such a report leaves out what describes the department as a whole: its place among departments, the comparison chart, the section on the department's teachers and the «Итого по кафедре» (department total) line. In this mode the choice of groups is not remembered.

Pulling the data from the portal takes minutes, so a report is built as a background job while the page polls its state. One job runs at a time.

## The summary and its changes

A finished report opens on the same page in tabs: summary, groups, disciplines and teachers. The summary starts with tiles: the number of students and groups, how many passed in full, the share of failed attestations, the share of zero scores, disciplines with no scores entered, and the department's place among the university's departments.

{% include screen.html src="/assets/attestation_report_service/summary.webp" wide=true width=1653 height=1179 caption="The summary: tiles, the share of failed attestations by group with thresholds and circles for the previous attestation, and conclusions. Made-up data." alt="The «Сводка» tab: tiles for 69 students in 5 groups; 39 passed in full, 56.5 % of students, −5.8 percentage points since attestation 1; a failure share of 20.3 %, normal, −3.1 points; zero scores 13.5 %; 1 discipline not entered; department place 3 of 7. Below, a chart of failure shares by group: horizontal bars for ДЕМ(о)-11 at 38.9 %, ДЕМ(о)-21 at 31.3 % with a grey not-entered part, ДЕМ(о)-31 at 5.0 %, ДЕМ(о)-41 at 2.8 % and ДЕМм(о)-11 at 0 %, dashed thresholds at 30 and 50 %, circles for attestation 1 and changes in percentage points on the right. At the bottom, five conclusions in a list" %}

The main chart is the share of failed attestations by group. Each group's bar splits into zero scores and scores below the minimum, and dashed lines mark the thresholds: up to 30 % is normal, up to 50 % calls for attention, and above that it is critical. A circle shows the same group in the previous attestation of the semester, and the change in percentage points is on the right. If the previous attestation is not on disk, the service fetches it from the portal, and if there is none at all, the report is built without a comparison rather than inventing one.

One case is counted apart: «не выставлено» (not entered), a discipline in which the whole group has 0. That is almost certainly not a group-wide failure but scores the teacher has not entered yet. Such a discipline is shown in grey, stays out of the list of critical disciplines, and the conclusions give the failure share both with it and without it. In the example above, one such discipline accounts for 30.8 % of all failures: without it the failure share would be 15.0 % instead of 20.3 %.

## A heatmap of scores

On the «Группы» (groups) tab, every group has a student-by-discipline table with the minimum score in its header. The colour of a cell shows whether the student passed, is close to the minimum (at least 80 % of it), is below the minimum, or got 0. Rows are sorted by the number of failures.

{% include screen.html src="/assets/attestation_report_service/heatmap.webp" wide=true width=1653 height=1215 caption="A group's scores by discipline. A red column almost always means a problem with the discipline, a red row a problem with the student. Made-up data." alt="The card of group ДЕМ(о)-11, first year, bachelor's: 18 students, 8 passed in full, a failure share of 38.9 %, attention status. Below, a table of students' scores by discipline: rows from «Студент18 Т. Т.» with failures in 4 of 4 disciplines down to «Студент9 Т. Т.» with none, four columns with a minimum score of 13, cells in green, yellow, pink and red with zeros; under the table, the list of disciplines, higher mathematics, physics, programming and a foreign language, with made-up teachers and failure counts" %}

A hint above the table says how to read it: a red column almost always means a problem with the discipline, a red row a problem with the student. Tables of disciplines and students with their statuses follow. The charts are drawn by the service's own JavaScript module without inline scripts or styles, so the strict content security policy does not get in its way, and the tooltips work on hover as well as from the keyboard.

The page style is called «Чертёж» (drawing): a sheet on graph paper with a frame and a title block, a narrow drafting typeface, hatched bars and dashed thresholds. The title block holds the department, the attestation number, the user and the date.

## Reports in DOCX and PDF

For each level of study the service builds a short report and a detailed one. In appendix A of the short report each group gets a table with every student's scores, a row of minimum scores and fills for scores below the minimum, zero and not entered, plus the list of disciplines with their teachers. The department's place among departments stays only in the bachelor's report, because the portal's department report has no master's groups.

Every DOCX is converted to PDF through LibreOffice. The service tries picture qualities and picks the best one that keeps the file within 2 MB: the detailed bachelor's report shrinks from 12 to 1.8 MB. Accessibility tags in the PDF are switched off: in a report made almost entirely of tables they inflated the file from 0.2 to 1.3 MB. Without LibreOffice the reports stay in DOCX.

## Links to a report

A finished report can be shared: an `/attestation/share#…` link opens its sections, charts and files without signing in, for 1, 3 or 7 days or with no expiry, until the owner revokes it.

{% include screen.html src="/assets/attestation_report_service/shares.webp" wide=true width=1653 height=467 caption="The list of one's own links: open, show the address, issue a new one, make it permanent or revoke it." alt="The «Ваши ссылки на результаты» section: a note on expiry and revocation and two links titled «ДЕМО: аттестация №2, нечётный семестр 2026-2027», open until 22 November, each with «Открыть», «Показать ссылку», «Новая ссылка», «Сделать постоянной» and «Отозвать» buttons" %}

The link's key, 256 random bits, sits in the address after the «#» sign. Browsers do not send that part of an address to the server, so the key reaches neither the nginx logs nor the Referer header. The page passes it in a separate `X-Share-Token` header and downloads the files with requests from its script. The copy of the report lives in the data volume in a folder named after the key's SHA-256, and it is deleted when the link expires or is revoked. Wrong keys are limited to 30 attempts per client per 15 minutes.

In the list of their links, the owner sees and copies each address, opens the shared report on the same page, and can issue a new address: same report and lifetime, while the old address stops opening at once. So that an address can be shown again, the key is stored next to the copy of the report. This is a deliberate trade-off: anyone who can read that folder can already see the report itself. An expiring link can be made permanent as long as it has not expired. The page asks for confirmation first, because the link shows students' names and scores. An expired link cannot be brought back: its copy of the report is already gone.

## A repository of its own, and deployment

The service grew inside the [diploma supplement service]({% link _articles/diploma_supplement_service/2026-06-01-vk-uchebno-prakticheskaya-en.md %}) as the `python-attestation-engine` folder, and the main Java gateway proxied requests to it. On 26 October it moved to a repository of its own with its commit history kept. The domain stayed the same: the site's nginx sends `/attestation` straight to the service's container, and the gateway no longer needs to know about it.

The site's server sits on the university's local network, where GitHub cannot reach it. So the server asks GitHub instead: every 5 minutes a systemd timer checks whether `main` has a new commit, and if so, builds the image, which runs all the tests along the way. If the build fails, the previous container keeps running, and that commit is not tried again until the next one. A merge into `main` is a deployment to the server.

There is no real student data in the repository. The tests build the portal's exports in memory from made-up names and scores, a fake portal stands in for every call to the real one, and `.gitignore` keeps out XML exports, DOCX, PDF and images.

## Conclusions

1. A password that is stored nowhere needs no protection: the check can be left to the portal, with only its session kept in memory.
2. A key passed after the «#» stays out of the web server's logs and the Referer header. It is a cheap way to keep the keys of links to personal data out of places where they are easy to read.
3. A discipline in which the whole group has 0 has to be shown apart, or scores not yet entered look like a group-wide failure and distort the failure share.
4. A size limit on a PDF is better met by searching picture quality against the limit than by one fixed compression.

## Availability

- The service: [пгту-ртф.рф/attestation](https://xn----etb9agicel.xn--p1ai/attestation), sign-in with a RITM account
- Source code: [github.com/nikita-konkin/attestation-report-service](https://github.com/nikita-konkin/attestation-report-service)
