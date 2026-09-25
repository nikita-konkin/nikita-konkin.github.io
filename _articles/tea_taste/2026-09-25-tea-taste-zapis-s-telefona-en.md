---
title: "Tea Taste: Recordings From a Phone, and a Failure Nothing Reported"
project: tea_taste
pair: tea-taste-zapis-s-telefona
platform: VK
type: Technical breakdown
date: 2026-09-25
source_from:
  tea-taste-api: bfe9830ab61c93dd9c6b8c9ebc42cc860dea7b0e
  tea-taste-frontend: 6875a30e0a1d014bd917ef654daf38a22dc553e4
source_rev:
  tea-taste-api: 3895a6003b8e0e31f468b0d8b05e177ea54c93ad
  tea-taste-frontend: 9dbedb92b62d038b069c62fc1c9d18d92a7bca45
lang: en
authors:
  - Nikita Konkin
summary: "Importing recordings made outside the app: how a single recording of a whole tasting cost the parse every descriptor, why recognition loses the infusion's number rather than the word, and how a silent merge of infusions was made visible. Plus a linter the project listed but never had."
translation_of: 2026-09-25-tea-taste-zapis-s-telefona.md
links:
  repo: "https://github.com/nikita-konkin/tea-taste-frontend"
tags: [programming, react, nodejs, express, mongodb, product]
---

The previous breakdown covered voice notes: recording in the browser, recognition, and parsing the transcript into fields against a fixed vocabulary. It assumed the recording was made in the app. In practice a tasting is often recorded on a phone — separately, with no form open.

This update accepts such recordings. The upload itself turned out simple; what was interesting was what a real recording exposed.

## A per-infusion recording needed nothing

The upload endpoint already accepted m4a, mp3, wav, ogg and aac and transcoded whatever arrived. So importing a recording of a single infusion required no change on the server: the infusion number comes from which block of the form the file was dropped into — exactly as for a recording made in the app.

One interface restriction was fixed along the way. A browser without `MediaRecorder` showed only a message saying it could not record audio — and in doing so hid an import that needs no microphone at all. Recording is no longer a precondition for choosing a file.

## When the whole tasting is one file

The hard case was a different one: a single file covering the entire tasting. Such a recording has no infusion number — the infusions are inside it, named out loud.

Left with `brewingNumber: 0`, it was grouped with the general note "about the tea" and labelled `[О чае]` for the parse. On a real recording this cost the descriptors outright: the model read the whole tasting as one general remark and returned not a single aroma and not a single taste.

So the segment gained a flag of its own, `whole`. Such a recording forms a separate recognition group, is labelled `[Вся сессия]` ("whole session"), and comes with a rule: split it on the numbers the speaker names, and carry nothing from it into the description of the tea itself.

```js
if (whole) return `[Вся сессия] ${transcript}`;
```

The label looks like a detail, but it decides how the model reads the entire text.

## What recognition loses

The same recording showed a pattern worth recording: recognition loses not the word "infusion" but the number beside it. Five infusions spoken as "N пролив" came through intact. The sixth, spoken as "в шестом проливе" (in the sixth infusion), came back as "в простом проливе" (in the simple infusion) — and that infusion merged into its neighbour.

The second observation concerns vocabulary. "немного грачит" is "горчит" — bitterness: a word heard in every tasting, which SpeechKit does not know in this sense. It was added to the correction rule alongside other tasting words that recognition mangles.

## A tension a prompt cannot resolve

The most instructive thing in this update is an honestly recorded compromise. Strengthening the splitting rule recovered the sixth infusion but lost every descriptor. Strengthening the descriptor rule brought the descriptors back but merged that infusion again.

The choice went to the descriptors: per infusion, they are worth more. And the structural answer lies outside the model's prompt — in consistent phrasing. The guide now asks for each infusion to be named the same way, at the start of the note: "пролив N".

## A failure that is now reported

The real problem was not even the merge, but that it happened silently. The sixth infusion disappeared, and nothing on screen said so.

The suggestions panel now compares the number of infusions found with the number in the form, and reports a mismatch directly:

> Нашлось {n} проливов из {total}. Проверьте, что номер каждого пролива назван вслух — ненайденный пролив молча сливается с предыдущим.
>
> *Found {n} infusions of {total}. Check that each infusion's number is said out loud — an infusion that is not found silently merges into the one before it.*

Fixing recognition itself is not possible; making its failure visible is. Those are different tasks, and here the second one turned out to be achievable.

## A linter that was never there

The second half of the update is about hygiene, and it starts with a discovery: the API had a `lint` script with no linter behind it. `npx eslint .` in a project with neither eslint nor a configuration.

Once airbnb-base was installed, the autofix took care of quotes, semicolons and spacing, and 64 findings had to be worked through by hand. Most were tidying, but three were real defects:

- `routes/index.js` — express-generator scaffolding that never got deleted. It assigns `express = require('express').Router()` and then calls `router.get`, so requiring it throws `ReferenceError`, and it renders a view through an engine the app does not have. Nothing required it. Deleted.
- `NODE_ENV == 'production'` in the cookie options of both sign-in paths — beside `secure: NODE_ENV === 'production'` on the next line. For a string environment the result is the same, but the pair reads as a deliberate distinction that is not one.
- `formJsonLd` took `brewings` and never used them.

Six airbnb rules are turned off, with the reason for each written beside it. Three concern line wrapping: measured, they made up most of a 3,500-line autofix diff, and not one of those lines read better afterwards.

On the frontend, airbnb was deliberately not adopted. The source is split between tabs and four spaces by file, and reindenting the whole repository would bury every real finding under thousands of whitespace lines. Eleven effect-dependency warnings were kept — they are mount-only effects — but each now carries a line saying which kind it is, so that the next one to appear is a real question rather than more of the same noise.

## A dependency that worked by accident

`uuid` was imported by two components and never declared in `package.json`. It resolved only because npm hoisted a transitive copy to the top level of `node_modules`. A lockfile refresh that stopped hoisting it would have broken the build without a single change of the project's own. The dependency is now declared.

Five packages nothing imported were removed. The bundle size did not change — 297.94 kB gzipped: an unimported package was never in it. The gain lies elsewhere — install time, lockfile size and supply-chain surface.

In both repositories the linter now runs in CI before the tests: it is faster, and a lint error is usually a typo the tests would take three minutes to find.

## Conclusions

1. Making a failure visible is often easier than removing its cause. Recognition merging infusions cannot be fixed, but it can be reported.
2. How input is labelled decides how a model reads it. The same recording under `[О чае]` and under `[Вся сессия]` gives opposite results.
3. Recognition loses first what is phrased inconsistently. Uniform phrasing is more reliable than a more elaborate prompt.
4. A script with nothing behind it is worse than no script: it creates the confidence that a check exists.
5. What works by accident does not work: a dependency resolved by hoisting a transitive copy was held up by the internals of someone else's tool.

## Availability

The service is open: [teaform.ru](https://teaform.ru). Importing a recording is available in every infusion block, and importing a whole tasting is its own page under «Дегустация» (Tasting).

- Source: [github.com/nikita-konkin/tea-taste-frontend](https://github.com/nikita-konkin/tea-taste-frontend)
