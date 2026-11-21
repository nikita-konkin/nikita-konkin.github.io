---
title: "Volgatech.Kollektiv: Teaching Workload on the Portal from the Timetable, and a Sign-In Without the Gateway Page"
project: volgatech_corp
pair: volgatech-workload
platform: VK
type: Technical breakdown
date: 2026-11-21
source_from: abd32b8dcdb1a3b599e05018fe766851faedffa2
source_rev: 66f67520d1b78ab4a8b00d52d0cf903dae8ee9c6
lang: en
authors:
  - Nikita Konkin
summary: "Versions 0.5.7 and 0.5.8: a new «Учебная нагрузка» (teaching workload) section fills the monthly form on the corporate portal from the timetable, using only the chosen department's disciplines, listing every change before it saves, and covering several months at once. Signing in to the portal is now a screen of the app, and the section itself had to be recovered from a debug build. Discipline names can also be copied now, and reports save as files."
image: /assets/volgatech_corp/workload-preview.png
translation_of: 2026-11-21-uchebnaya-nagruzka.md
links:
  repo: "https://github.com/nikita-konkin/volgatech.corp"
  demo: "https://konkin-nikita.ru/volgatech.corp/"
tags: [programming, flutter, dart, mobile-development, webview, automation]
---

In the month since the [hourly workload report]({% link _articles/volgatech_corp/2026-10-24-pochasovaya-nagruzka-en.md %}), two versions of Volgatech.Kollektiv have come out. Version 0.5.7 gathers small things that save time every day: a discipline's name copies straight from the timetable, there is a list of all disciplines of the semester, and .docx reports save as files. Version 0.5.8 adds the «Учебная нагрузка» (teaching workload) section: the monthly form on the university portal is filled from the timetable the app already loads.

## A form that was filled in by hand

Every month a teacher enters their teaching workload for the first half of the day on the corporate portal: for each of the department's disciplines, the hours of lectures, practical classes and laboratory classes. The hours come from the same timetable, and until now they were counted by hand. The «Учебная нагрузка» section in the app's menu on Android opens that portal form and fills it in itself.

<div class="screens">
{% include screen.html src="/assets/volgatech_corp/workload-form.webp" caption="The November form: department, academic year, month and hour fields." alt="The «Учебная нагрузка» screen: a «1 семестр» and «2 семестр» switch, lists for department «Информационные технологии», academic year «2026/2027» and month «Ноябрь 2026»; cards for «Базы данных» with a lectures field of 10 hours and «Программирование на Python» with a practical classes field of 6 hours; at the bottom the buttons «Заполнить из расписания», «Несколько месяцев» and «Сохранить на портале»" %}
{% include screen.html src="/assets/volgatech_corp/workload-review.webp" caption="Hours from the timetable by group and date. Other departments' classes are hidden." alt="The «Из расписания» screen: at the top a line saying two disciplines of other departments, 6 hours, are hidden, discrete mathematics and probability theory; below, databases lectures for group ИВТ-21, 6 hours on 03.11, 10.11 and 17.11, mapped to the portal row «Информатика и вычислительная техника · Старший преподаватель», the same for group ИВТ-22 with 4 hours, and Python programming practical classes for ИВТ-31, 6 hours; at the bottom a button to transfer 16 hours to the form" %}
</div>

The «Заполнить из расписания» (fill from the timetable) button takes the classes of the chosen month that have already taken place and adds up the hours by discipline and type of class. Groups taught together count as one class, and its hours are counted once. Only disciplines that appear in the chosen department's form are offered. Classes of other departments are not dropped silently: they are counted in a separate «Скрыто …» (hidden) line with their names and hours.

For each total the app picks a field of the form by itself. A discipline can appear in the form several times, for different degree programmes or posts, so the row can be chosen from a list, skipped, or matched to a discipline that the portal names differently. Fields that are already filled are not offered, and totals mapped to one field add up.

## A check before saving

Saving changes the data on the portal at once, so the app first shows every change as "before → after" with the total of hours. Just before writing, the form is read again: if any of the fields about to change has been edited elsewhere in the meantime, the save stops and asks for the month to be refreshed. A thin bar shows the save's progress, and leaving the section with unsaved hours asks for confirmation.

{% include screen.html src="/assets/volgatech_corp/workload-confirm.webp" max=300 caption="The confirmation: every change field by field, and the total." alt="A «Сохранить на портале?» dialog over the form: November 2026, semester 1; databases lectures 0 → 10 hours; Python programming practical classes 0 → 6 hours; a total of 16 hours in these fields; «Отмена» and «Сохранить» buttons" %}

The form opens on the current month, or on the previous one during the first seven days of a month. The department is the one used last time. The «Несколько месяцев» (several months) button fills several months of the semester at once, with one review and one confirmation for all of them.

## How the app works with the portal form

The form has no programming interface of its own: it is a page of the corporate portal built from Telerik controls. The app loads it into an embedded browser (WebView) that the user never sees and talks to it through a small JavaScript script. The script reads the lists of departments, academic years and months, selects the right option, and reads and fills the hour fields.

A month is switched through the partial update the page itself uses, without reloading the whole portal. To know when the update is over, the script subscribes to the page's request-completion event and counts the responses. Each call to the page is limited to 3 seconds, and waiting for a result to 22 seconds.

Most of the fixes went into making the section work on a slow phone. A lost reply while reading the form is now requested again as long as the waiting budget lasts. A slow answer to the "401 Unauthorized" check after a page load no longer counts as a failure. After submitting, the app waits for the page to confirm that particular submission by its number, and then reads the form again. If the confirmation never comes, for example because the page reloaded in the middle of the call, the save does not hang: the app asks for the month to be refreshed before trying again.

One error came from the portal itself. After a sign-in the gateway appends a marker such as `&AuthResend…` to the page address, and the first load of the form did not recognise its own page. The marker is now dropped in both address checks and kept out of the saved address.

## Signing in to the portal is a screen of the app

Signing in used to open the portal gateway's desktop page, which is awkward on a phone. It is now an ordinary app screen, «Вход на портал»: the login is remembered and the password is stored nowhere. The app fills in the gateway's form in the embedded browser itself, ticks "private computer" and clears the password-change option. A domain the user types is kept as typed, and after submitting, the app waits until the portal has finished its redirects.

{% include screen.html src="/assets/volgatech_corp/workload-sign-in.webp" max=300 caption="Portal sign-in: the same login and password as for university mail." alt="The «Учебная нагрузка» screen with the «Вход на портал» form: a note that the login and password are the same as for university mail, «Логин» and «Пароль» fields, and a «Войти» button" %}

The "wrong login or password" message appears only when the portal itself answered so. This matters: every failed attempt brings the account closer to a lockout, and the app must not take a network failure or an unexpected answer for a wrong password.

## A section recovered from a build

The workload section has an unusual history. It was written on a Mac, built into version 0.5.7 and never pushed to the repository. The sources turned up in a debug APK for Android. A Flutter debug build carries the program's Dart kernel, and the kernel holds the source text of every library byte for byte. 105 files were extracted from it. 98 of them matched the main branch exactly, and the differences fell on the new section. The script for the portal page was among the same APK's assets. Only the tests written on the Mac did not come back, as they never go into a build.

## Version 0.5.7: disciplines and files

- **A discipline's name copies.** Holding a class in the timetable, a row in the week overview or an exam puts its name on the clipboard; with a mouse, a right click does the same.
- **A «Дисциплины» (disciplines) section.** Every discipline of the semester's timetable in alphabetical order, with its groups and the number of lectures, practical and laboratory classes; arrows switch semesters. Names copy one at a time or all at once, one per line.
- **Reports save as files.** The memo and the appendix to form 28 used to go straight to the share menu, and Safari on a Mac cannot save a file from it. «Сформировать .docx» now offers a choice: «Сохранить в файлы» (save to files) on Android, «Скачать» (download) in a browser, or «Отправить…» (send) as before.

## The build

The GitHub Actions builds are pinned to Flutter 3.47.5. The stable channel moved to 3.50.0, which deprecates `material.dart` in favour of `material_ui`, and `flutter analyze` failed on 69 notices in code that passes cleanly on 3.47.5. The iOS build job is gone from the checks, and an Android signing key path starting with `~/` now points to the home folder, so one settings file serves both a Mac and Windows.

## Conclusions

1. When a form has no programming interface, it can be filled through its own page in an embedded browser. Reliability then comes down to waiting: request-completion events, time limits and retries when replies are lost.
2. Before writing into someone else's system, the user should see every change as "before → after", and the app should make sure the original values have not changed. A full list costs less than hunting for a mistake after the save.
3. A wrong-password message must rest on the server's answer, otherwise the app pushes the account towards a lockout.
4. A Flutter debug build keeps the source text. That helped bring the section back, but work is better pushed to the repository at once.

## Availability

From version 0.5.1 on, the app offers the update itself (**Настройки → Обновления**, Settings → Updates). The workload section works only on Android, since it needs the embedded browser.

- Source code and releases: [github.com/nikita-konkin/volgatech.corp](https://github.com/nikita-konkin/volgatech.corp)
- Web version: [konkin-nikita.ru/volgatech.corp](https://konkin-nikita.ru/volgatech.corp/)
