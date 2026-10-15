---
title: "conf-kit: A Chat Bot Builds the Conference Programme, the Schema Catches the Mistakes"
project: conf_kit
pair: conf-kit-vvedenie
platform: VK
type: Technical breakdown
date: 2026-10-15
source_rev: b5a922972c2eb7e8db60091e7ff63e13742bfdcd
lang: en
authors:
  - Nikita Konkin
summary: "In two days a jury page for one conference grew into a service for events: the programme as a checked document, an API for chat bots, a builder for phone and desktop, a public programme, A4 documents, a talk competition and talk applications. How the programme is checked, what a local model managed, and where the line between the bot and the human runs."
image: /assets/conf_kit/preview.png
translation_of: 2026-10-15-conf-kit.md
links:
  repo: "https://github.com/nikita-konkin/jury-score"
tags: [programming, javascript, pocketbase, llm, mobile-ui, conferences]
---

The project began on 7 October as a jury page for the RWP-2026 conference: an expert scored talks on six criteria, and an Apps Script backend stored the scores. The next day conf-kit grew out of it — a service for conferences and events. The old tool is kept in `legacy/jury-score/`, and its old link still works.

The service's main scenario is unusual: a chat bot builds the programme. It receives the event's materials — the list of talks, the time rules, the rooms — and assembles the whole programme through the API, and a person receives an invitation link to the finished draft. Everything else — the builder, the public programme, the documents, the jury and the applications — works with what came out.

## The programme as a document

For a bot and a person to work on one programme, it is described as a document: the `conf.program/v1` format with a JSON Schema. The event, rooms, sections, days, sessions and items — talks, plenary talks, breaks, lunches, ceremonies.

The document is normalised first. A time of "14.30" becomes "14:30", authors given as one string are split at the commas, and unknown fields are not lost but moved to `extra` with a warning. A time that is not stated explicitly is computed from the time rules: 15 minutes per talk, 30 per plenary talk, 15 per break, 45 per lunch.

Then the programme is checked: no room is booked twice, no speaker is in two places at once, time does not run backwards. Each error names an exact path — for example `days[0].sessions[3].items[0]` — so that a person or a bot can fix it.

The schema is tested on real programmes. The RRV-2023 fixture has five days, up to five parallel sections in different rooms, poster talks and off-site events, 164 items in all. Its warnings are genuine flaws of the source: three speakers missing from their authors and a dinner without a venue. RWP-2026 has a variant with one section's times taken as in the source PDF; the check finds `TIME_BACKWARDS` and `TIME_OVERLAP` in it with exact paths.

PocketBase on SQLite stores the programmes. Each replacement of a programme is a new version, and any version can be restored.

## The bot builds, a person accepts

A bot works with an API key. A `POST /api/v1/events` request creates a draft and returns an invitation link, valid for 14 days. A person opens it, sees a preview and accepts the draft into their account. Drafts nobody accepts are deleted after 30 days.

Bots have three ways in: `llms.txt` with instructions, `openapi.json` for GPT Actions, and an MCP server for Claude, LM Studio and other clients, over stdio and HTTP. For a bot without tools there is a "Create from a chat bot's answer" mode: the JSON from its answer is pasted into the page. Bots can leave feedback, and the API's changelog is available to them at a separate address.

A local worker runs separately. On the organiser's computer it parses applications and letters with a model in LM Studio; its connection to the server is outgoing only. The result goes through the same normalisation and checks, and the owner applies it as a new version of the programme.

How well a model understands the schema is measured by `tests/bots/local_bench.mjs`. In two runs of qwen3.5-9b in LM Studio, a short seminar-school programme — two days and 14 items — came out valid at the first attempt, in about 90 seconds. The real 30-item RWP-2026 programme never did: after two attempts there were still time overlaps, speakers in two places and double-booked rooms, and in one attempt the model returned no JSON at all. The project plan sets a threshold of at least 80 % valid documents at the first or second attempt; so far two results out of four are valid.

The measurement shows why the check exists: a bot's mistake does not slip into the programme silently but goes back to the bot with an exact path, for the second attempt.

## The programme for participants

<div class="screens">
{% include screen.html src="/assets/conf_kit/public-now.webp" caption="The public programme: “now” and “next” by the event's clock." alt="The programme of an “Autumn School of Radiophysics” on a phone: buttons to apply for a talk, share and add to the calendar, a “Now” block with a talk at 11:15 and “Next” with a talk at 11:30 and lunch at 12:00, search and tabs for 18 and 19 November" %}
{% include screen.html src="/assets/conf_kit/public-dark.webp" caption="The dark theme: the current talk is highlighted and has an “add to calendar” button." alt="A session's talks in the dark theme: past ones are dimmed, the current talk at 11:15 is framed, and each talk shows its code s1-1, s1-2, its section, an “online” mark and its end time" %}
{% include screen.html src="/assets/conf_kit/apply-form.webp" caption="A talk application — no account needed." alt="The talk application form: the organiser's note about abstracts, fields for the speaker, authors and talk title, and choices of section and form of participation" %}
</div>

Here and below the screenshots show a made-up "Autumn School of Radiophysics" in a made-up town of Ensk; all names, organisations and addresses are invented. The interface is in Russian.

A participant sees what is on now and what comes next — by the event's clock, not the phone's. The programme can be searched and filtered by section and form of participation, subscribed to in a calendar (the subscription updates itself), or a single talk can be added to the calendar. Changes arrive without reloading the page, and a copy of the programme stays in the browser in case the connection drops.

The public programme and the jury share a budget of at most 80 KB of gzipped JavaScript; the main file now takes 32.7 KB. Browsers from 2018 onwards are supported: the build targets Chrome 61, Firefox 60 and Safari 12, and the deployment check opens the pages in Chrome 62 and Firefox 60. A browser that lacks what the page needs shows a message rather than a blank page.

## The builder

<div class="screens">
{% include screen.html src="/assets/conf_kit/editor-session.webp" caption="The builder on a phone: a session and its items." alt="Session no. 1 in the builder: 10:45, room 305, chair and secretary, an “Order” button and a list of six items with times and speakers" %}
{% include screen.html src="/assets/conf_kit/editor-sheet.webp" caption="Editing a talk in a bottom sheet." alt="A bottom sheet for item s1-2: type “Talk”, title, speaker, comma-separated authors, organisation and buttons for done, move, copy and delete" %}
</div>

On a phone the programme is built level by level: days, sessions, items. Editing happens in bottom sheets, order is changed with buttons, and check errors show on the spot. There is undo, a draft survives a page reload, and the version history allows a rollback. Talks can be loaded from a table — `.xlsx`, `.csv` or `.docx` — and a new event can be created from an old one as a template.

{% include screen.html src="/assets/conf_kit/desk-editor.webp" wide=true width=1600 height=1000 caption="Desktop: the tree of days and sessions, the items, and a preview of the printed programme that updates as you edit." alt="The builder on a wide screen in three columns: on the left the tree of 18 and 19 November with sessions and a hint about keyboard shortcuts, in the middle session no. 1 and its talks, on the right “As it will be printed” — the programme as an official document" %}

From 900 pixels wide the builder spreads into three columns: the tree of days and sessions, the list of items and a preview of the printed programme. Edit sheets open as a side panel, items can be dragged with the mouse within a session and into another one, and keyboard shortcuts work — Ctrl+S, Ctrl+Z, Esc and Alt+↑/↓. A separate table gathers the programme's people and finds different spellings of one name.

## Documents

<div class="screens screens-wide">
{% include screen.html src="/assets/conf_kit/print-door.webp" wide=true width=890 height=900 caption="A door sign: one session on a landscape sheet." alt="Preview of an A4 sheet: Wednesday 18 November 2026, 09:30–10:35, “room 210” in large type, “Plenary session” and a table of three items with times" %}
{% include screen.html src="/assets/conf_kit/print-cert.webp" wide=true width=890 height=900 caption="A participant's certificate with the talk's title." alt="Preview of a certificate: the school's name, “Certificate of participation”, the speaker's name, “gave a talk” and the plenary talk's title, the dates and a line for the organising committee chair's signature" %}
</div>

The programme yields A4 documents with a preview right on the phone: the programme laid out as an official conference programme, door signs for each session, section minutes, participants' certificates, the competition results and diplomas. They can be printed, turned into PDF on the server — Gotenberg does that — or exported to Word.

## The jury and applications

<div class="screens">
{% include screen.html src="/assets/conf_kit/jury-card.webp" caption="The jury: an expert scores talks by criterion." alt="An expert's screen: 1 of 13 scored, everything sent, section tabs, the first talk scored 18 out of 20 and marked saved, the second talk opened with its authors and first criterion" %}
{% include screen.html src="/assets/conf_kit/jury-results.webp" caption="Results for the jury's administrator." alt="The results tab: talks ranked by the average total score, first place 17 points from four experts, second 16.67 from three" %}
</div>

A jury expert signs in from a link with their surname and a commission code like `k7m2-p9x4` — no account. The code is designed to be dictated and typed on a phone. Scores are kept on the phone and sent to the server by themselves, including after the connection drops; a talk that did not take place is marked separately.

The administrator sees the ranking, the places within sections and statistics, downloads a CSV and deletes mistaken scores — they go to an archive rather than vanish. The ranking counts only fully completed scores without a "did not take place" or "abstain" mark.

{% include screen.html src="/assets/conf_kit/desk-jury.webp" wide=true width=1600 height=1000 caption="The jury ranking on desktop: average score, number of experts, spread and averages by criterion." alt="The ranking table: place, speaker, talk, section, average score, number of experts, minimum and maximum and averages for the four criteria K1–K4; first place has 17 points" %}

A participant applies for a talk without an account. The form names the operator of personal data and asks for consent to process it. A hidden field and a minimum filling time of three seconds protect it from spam: no person fills the form faster. From a link the participant sees the status of their application and the reason for a refusal, and can withdraw it.

The owner accepts an application into a session, and it becomes a talk in a new version of the programme. Participants' contacts never enter the programme and are erased a year after the event.

## Deployment and testing

The service is deployed with `docker compose`: Caddy with HTTPS, PocketBase, the MCP server and Gotenberg without network access. The project plan puts the server in Russia: participants' personal data must be stored there under Federal Law 152-FZ.

Tests run at four levels: unit tests, the API against a temporary PocketBase, the MCP server, and end-to-end scenarios in Playwright. The end-to-end scenarios check the layout on a 320-pixel screen: no horizontal scrolling, and no button or field below 44 pixels. A separate check brings up the whole stack in Docker, gets a PDF through Gotenberg and opens the pages in old browsers.

## Conclusions

1. A programme described as a document with a schema lets the work be split: a bot builds, the check finds errors with exact paths, a person accepts.
2. Real programmes are the best test of a schema: the flaws of the sources become expected warnings.
3. The measurement on a local model shows the gap between a training programme and a real one: the short one is built at the first attempt, the real one not yet.
4. A bot cannot publish a programme by itself: a draft becomes a programme only after a person accepts the invitation.
5. Participants' personal data has an expiry date: contacts never enter the programme and are erased after a year.

## Availability

The source code is open. The API description, the schema and the development plan are in the repository; checking it needs Node.js, PocketBase and Playwright.

- Source code: [github.com/nikita-konkin/jury-score](https://github.com/nikita-konkin/jury-score)
