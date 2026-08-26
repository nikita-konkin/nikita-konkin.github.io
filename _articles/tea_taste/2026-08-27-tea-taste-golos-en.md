---
title: "Tea Taste: Tasting Out Loud — Speech Recognition and the Vocabulary That Holds It"
project: tea_taste
pair: tea-taste-golos
platform: VK
type: Technical breakdown
date: 2026-08-27
source_from:
  tea-taste-api: 3272e20b8dd66371b0995bf4158943e005b8ee05
  tea-taste-frontend: 58745d6a0cab2439ae57e76da1c35d16bf2a6a9b
source_rev:
  tea-taste-api: bfe9830ab61c93dd9c6b8c9ebc42cc860dea7b0e
  tea-taste-frontend: 6875a30e0a1d014bd917ef654daf38a22dc553e4
lang: en
authors:
  - Nikita Konkin
summary: "Voice notes instead of filling in a form: speech recognition through SpeechKit, a transcript parsed into fields against a fixed descriptor vocabulary, a monthly quota, tasting photographs, and separate pages served to search crawlers."
translation_of: 2026-08-27-tea-taste-golos.md
links:
  repo: "https://github.com/nikita-konkin/tea-taste-frontend"
tags: [programming, react, nodejs, express, mongodb, product]
featured: true
---

The previous update settled the question of access: VK ID sign-in, a public feed, an admin panel. What remained was the difficulty the service was built for in the first place. A tasting occupies both hands and full attention — an infusion, an assessment of aroma, an assessment of taste, the next infusion. Filling in a form of several dozen fields at that moment is awkward, and filling it in afterwards from memory is no longer accurate.

This update adds a way around the form: say the impression out loud and get the fields filled in.

## The path of the sound

The recording goes to Yandex SpeechKit for recognition — the asynchronous mode of the third version:

```js
const STT_URL = 'https://stt.api.cloud.yandex.net/stt/v3';
const OPERATION_URL = 'https://operation.api.cloud.yandex.net/operations';
```

The asynchrony is not an optimisation here but a necessity: a track is capped at five minutes (`MAX_TRACK_SECONDS: 300`), and no synchronous answer to a file that size is worth waiting for. The service submits the recording, receives an operation id, and polls it until it is ready.

The model version is pinned explicitly, and the comment in the code explains why:

```js
// Pinned rather than left to the default. Measured on the same recording:
// unset, `deferred-general` and `deferred-general:rc` returned byte-identical
// results, so this is not a quality lever — it is a guard against the
// default moving under us later.
model: 'deferred-general',
```

Pinning does not improve recognition here — it fixes behaviour in place. Those are different goals, and worth not confusing.

## Two halves of a transcript

The most instructive part of this update is a fix to accuracy, and it has nothing to do with recognition quality.

SpeechKit can render what was said in readable form: removing filler words, restoring punctuation. That processing (`literatureText`) is enabled deliberately — its result is what the user is shown. The mistake was in how the text was assembled from the response: the assumption was that when refined fragments arrive, they replace the originals wholesale.

The assumption is false. A refinement arrives **per utterance, and optionally** — the protocol allows some utterances to be refined and others not. Under the old assembly the unrefined ones were simply lost, and the transcript came out shorter than what had been said.

Both halves are now kept, each with its own job: the readable version goes to the user, the unprocessed one goes to field extraction. The reasoning is recorded in a comment directly above the setting:

```js
// Kept ON deliberately, and it is what produces the readable transcript
// the user is shown. Do NOT turn it off to "fix" the numbers: it is also
// what makes SpeechKit send the refinement alongside the raw final, and
// extractRawTranscript below already keeps the unrewritten text for the
// field extraction.
```

The reason for separating the two is substantive: literary processing improves reading, but it can smooth away precisely the words the recording was made for — the names of descriptors.

## From text to fields

The transcript is turned into fields by YandexGPT with structured output against a JSON schema. What matters here is not the call to a model but what constrains it.

The aroma and taste vocabularies live in the database (`AromaDB`, `TasteDB`) as a tree of category → subcategory → descriptor. Before the call the tree is rendered into text and passed in the system prompt, and the model's answer is checked back against it: `validPaths` collects the set of permitted paths, and `keepKnown` discards anything absent from it.

The point of the arrangement is that the model cannot extend the vocabulary. An invented descriptor will not reach a structured field — it fails the check. Nothing spoken is thrown away, though: whatever could not be expressed as a path in the tree is carried into the free-text description (`withUnmatched`). The user sees both what was recognised and what was not.

The model is also allowed to decline. The schema carries an `isTeaTasting` flag, and the prompt instructs plainly: if the recording is not about a tasting at all — a conversation, a to-do list, anything else — return `isTeaTasting: false`, say briefly what it was about, and leave every other field empty. The rule is worth quoting as written:

> Лучше честно ничего не заполнить, чем выдумать.
>
> *Better to honestly fill in nothing than to invent something.*

This ordering preserves the property the service exists for — that tastings remain comparable with one another. Free text generated by a model would destroy that comparability within a few records.

## A quota as protection against someone else's bill

Recognition is paid for by the owner of the SpeechKit account, not by whoever made the recording. The comment in `voiceQuota.js` says so plainly:

```js
// Every second of audio sent for recognition is billed to whoever owns the
// SpeechKit account — not to the person who recorded it. Without a ceiling, one
// user with a four-hour file spends real money, and nothing about the content
// tells you that in advance.
```

Hence the limit: thirty minutes per user per month. The time is reserved **before** submission — refusing after the answer arrives would mean having paid for it already. Exhausting the quota does not lose the recording: it is stored, and can be transcribed next month.

The neighbouring comment deserves attention for its honesty: the check and the write are not atomic, and two jobs starting together could both pass the limit. The constraint is left as it stands deliberately — the overshoot is bounded by a single five-minute track, and an atomic version would make the start-of-month reset much harder to express. A compromise recorded with its price named is more useful than one left unsaid.

## Photographs, and an order that must not vary

A tasting now carries photographs — the classic triptych of dry leaf, liquor, wet leaf. The order is fixed by a constant and, more importantly, explained:

```js
// Mirrors PHOTO_SLOTS / orderPhotos in tea-taste-frontend/src/components/TeaPhotos.jsx:
// the sitemap, the preview image and the crawler HTML all have to pick the same
// first photo the card does, or a shared link shows a picture that is not on
// the page.
const PHOTO_KINDS = ['dry', 'liquor', 'wet'];
```

The order here is not presentation but agreement between four independent consumers: the card, the link preview, the sitemap and the server-rendered markup. A divergence would surface only when a link is shared into a messenger — that is, latest of all, and in front of other people.

## Pages for crawlers

Search engines cope poorly with an application that draws itself in the browser, so the service gained server-side rendering — but only for them:

```js
// Server-rendered HTML for crawlers. nginx maps known bot user-agents onto
// /render<path>; a browser never reaches these routes.
```

The routes are mounted once per language, and a page's language is read back out of `req.originalUrl` rather than taken as a parameter, so that the single source of truth for "what language is this page" stays the URL, exactly as in the application. Metadata on the application side moved from `react-helmet` to a `PageMeta` component of its own.

## The language of the interface

Localisation is handled by middleware that chooses the language of a response. The order of preference is not obvious, and is therefore commented:

```js
// `X-Locale` first, because the app knows something the browser does not: which
// language the page is actually being read at. A reader on a Russian-configured
// browser looking at /en/blog wants the English message, and Accept-Language
// would give them Russian.
```

The header is treated as untrusted input: only an exact match against the known locales counts, never the raw string. The response is marked `Vary` on both headers — without it a shared cache could serve an English message to the next Russian reader.

## Dry leaf without a collection of its own

The most recent change adds two fields: a description of the tea as a whole, and the aroma of the dry leaf — the one judged before any water touches it.

The dry-leaf descriptors did not get a separate store. They reuse the aroma collection with `brewingCount: 0`, a number no infusion document carries. The vocabulary, the pickers and the frequent-value statistics all keep working as before, while every per-infusion loop walks straight past them. It is the same kind of move as encoding the control type into the row key in the diploma service breakdown: metadata placed so that existing code keeps working without a branch.

## Moderation and admitting new users

A tasting can be blocked: the model gained `blocked`, `blockedAt` and `blockedBy` — by whom and when. Registration, meanwhile, is switched at runtime, and the reason is recorded in a comment on the settings model: environment variables would require a redeploy and cannot be flipped from the admin page at the moment it is needed — during a wave of abuse.

## Conclusions

1. Voice input is useful exactly to the degree that its output is constrained. What keeps tastings comparable is not the model but the vocabulary its answer is checked against.
2. Making speech readable and extracting facts from it are different tasks; the text for reading and the text for parsing are worth storing separately.
3. A paid external service needs a limit taken before the call: a refusal issued after the answer has already been paid for.
4. A compromise named and explained in a comment is cheaper to maintain than a quietly correct solution.
5. Agreement about the order of data between independent consumers surfaces latest of all — and so is fixed explicitly.

## Availability

The service is open: [teaform.ru](https://teaform.ru). The voice note is available in the tasting form; the frontend and API sources are on GitHub.

- Source: [github.com/nikita-konkin/tea-taste-frontend](https://github.com/nikita-konkin/tea-taste-frontend)
