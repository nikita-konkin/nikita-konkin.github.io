---
title: "ionostation: Oblique Ionospheric Sounding on an Open Page"
project: ionostation_public
pair: ionostation-onlajn
platform: VK
type: Technical breakdown
date: 2026-11-16
source_rev: 54afea30e55080f082f79260b794ca8d45bd6236
lang: en
authors:
  - Nikita Konkin
summary: "The results of oblique chirp sounding are now open to everyone at ionostation.volgatech-itrc.ru: the sounding in progress, about 10 seconds behind, the latest ionogram and a strip of the past day, series of the maximum and lowest observed frequencies with forecast curves, and a table that compares an experimental MUF forecast with simple reference methods. The processing hub stays on its closed network: the public side only copies a folder of static files and serves it."
image: /assets/ionostation_public/preview.png
translation_of: 2026-11-16-ionostation-onlajn.md
links:
  demo: "https://ionostation.volgatech-itrc.ru/"
tags: [ionosphere, chirp-sounding, muf, forecasting, docker, nginx, security]
---

The hub that receives and processes oblique chirp soundings runs on the station's closed network. Until now its results were visible only to those with access to that network. Now the hub has an open page, [ionostation.volgatech-itrc.ru](https://ionostation.volgatech-itrc.ru/). It shows the sounding in progress, the latest ionograms, a month of frequency series and a forecast of the maximum observed frequency (MUF).

For now the page carries one path, NIC2 — Yoshkar-Ola: a transmitter in Nicosia, Cyprus, and a receiver in Yoshkar-Ola, 2,588 km apart over the ground. The sweep runs from 7.5 to 31.4 MHz.

## What the page shows

The top block shows the sounding in progress. The picture refreshes every 10 seconds and fills from left to right as the sweep moves up in frequency. Below it are the frequency reached and the share of the band covered.

{% include screen.html src="/assets/ionostation_public/now-en.webp" wide=true width=1413 height=801 caption="A sounding started at 23:00 UTC on 15 November, part-way through the sweep. The trace has already ended at the MUF near 12 MHz; past it there is only noise." alt="The 'Sounding in progress' block: a dark purple ionogram filled across most of its width, with the unfilled part black on the right; in the lower left corner a bright trace of two rays that bends back near 12 MHz, and noise over the rest of the field. The caption gives Nicosia, Cyprus → Yoshkar-Ola, the frequency reached out of 7.5–31.4 MHz, and the start time 2026-11-15 23:00 UTC; a progress bar runs below" %}

Below comes the latest complete ionogram, with its MUF and lowest observed frequency (LOF), and a strip of thumbnails for the past day. A click on a thumbnail brings up its ionogram.

{% include screen.html src="/assets/ionostation_public/latest-en.webp" wide=true width=1413 height=953 caption="The latest ionogram, 22:40 UTC on 15 November: MUF 11.7 MHz, LOF 8.0 MHz. Below is the strip for the past day." alt="An ionogram titled NIC2 - yoshkar-ola (oblique), 2026-11-15 22:40:15Z: virtual range from 2,600 to 3,050 km against frequency from 8 to 31 MHz, SNR in colour from 20 to 70 dB; a bright trace of the low and high rays meets near 12 MHz at about 2,800 km. The caption reads MUF 11.7, LOF 8.0 MHz. Below are seven thumbnails from 22:40 back to 16:55" %}

The main chart shows the MUF and LOF over 1, 7 or 30 days. It can be dragged in time and zoomed with the wheel, a pinch or the buttons. Forecast curves are drawn over the measurements: the model in use with a ±σ band, persistence, 27-day recurrence, the average daily cycle and the IRI model. Hollow circles mark a MUF at the top of the sweep: in those hours the true MUF may lie above 31.4 MHz, and the point gives only a lower bound.

{% include screen.html src="/assets/ionostation_public/series-en.webp" wide=true width=1413 height=704 caption="MUF and LOF for 9–16 November with the forecast curves. By day the MUF reaches the top of the sweep, by night it falls to 10–12 MHz; the dashed vertical line is the present moment, and to its right is the forecast for the next day." alt="A frequency chart from 0 to 40 MHz over dates from 09.11 to 16.11: blue MUF dots with a daily cycle from 10–12 MHz at night to 31 MHz by day, hollow circles at the 31 MHz ceiling, orange LOF dots near 8 MHz with daytime rises to 15 MHz; over them a solid purple model curve and dashed lines for persistence, 27-day recurrence, the daily cycle and IRI; right of a dashed vertical line at 16.11 only the forecast curves continue" %}

## The forecast and its reference methods

The last block is an experimental MUF forecast one day ahead. The page warns plainly that the model is still being evaluated. So the forecast is not shown alone but in a table beside simple reference methods: the MUF will be what it was a day ago; what it was one solar rotation, 27 days, ago; the average daily cycle; the climatological IRI model. For each method the table gives the mean absolute error over the whole period and over the last day, the share of variation explained, R², and the number of forecast and measurement pairs.

{% include screen.html src="/assets/ionostation_public/forecast-en.webp" wide=true width=1413 height=962 caption="The one-day-ahead forecast at the time of the capture: a model issued at 22:48 UTC on 15 November and trained on data for 1–14 November, against four reference methods." alt="A 'Forecast made 1 day ahead' table: rolling-20261115T224500 — error 1.25 MHz, last 24 h 1.45, R² 0.95, 1,269 comparisons; persistence — 2.03, 1.11, 0.83, 5,488; IRI — 2.12, 2.27, 0.85, 5,983; 27-day recurrence — 2.42, 1.90, 0.84, 1,121; daily cycle — 2.48, 2.98, 0.82, 5,983. Notes on the columns follow" %}

At the time of the capture the model leads on mean error, 1.25 MHz against 2.03 for persistence and 2.12 for IRI, and on R², 0.95. Over the last day, though, persistence did better: 1.11 MHz against 1.45. The model was also scored on 1,269 pairs and the reference methods on thousands, so its lead is preliminary. That is exactly why the table is on the page: a single number without reference methods would say nothing.

## How publishing works

The main rule is that the hub is never exposed. Its publishing service writes a folder of static files, and only what is explicitly allowed goes into it: images, series, the forecast and the state of the current sounding. The public side is a separate Docker stack on an open server. It only copies that folder and serves it, and its access to the source is read-only.

The stack has three containers.

- **pull** copies the current sounding every 10 seconds and the complete results every 5 minutes.
- **archive** copies the archive of past soundings' echo windows once an hour, on a loop of its own. A first copy of the archive can take many hours, and in a shared loop it would hold up the live picture.
- **web** is nginx serving the copied folder.

If updates stop, the page keeps showing its last copy, and the header shows whether the station is reachable and when the last update arrived. Until the first copy arrives, nginx serves a waiting page of its own.

## A server that can only hand out files

The nginx setup is kept to a minimum. The web container's configuration has no `proxy_pass`: the hub's API is not part of the public site, so a request for it has nowhere to go. The site answers only GET and HEAD; a POST gets 403.

The content security policy allows scripts, styles and images only from the site itself, forbids framing the page elsewhere and forbids form submission. The one relaxation is `wasm-unsafe-eval`. It lets the page run WebAssembly from its own address, which is how the browser will read past soundings' echo windows from HDF5 files. The archive section will appear on the page once the hub starts publishing those windows; copying and caching for it are already in place.

Caching follows from how files are named. An ionogram, a frame of the current sounding and an echo window are named after their sounding's time and are never rewritten, so they are cached for a year as immutable. The JSON files with the series and the state are rewritten on every pass and revalidated on every request.

Both halves of the stack are tested inside their own images against a local folder: what pull copies, and what web answers.

## Conclusions

1. An open page does not require opening the hub: a folder of static files that receives only what is allowed is enough.
2. The slow archive copy runs on its own loop so that it cannot delay the live picture.
3. A server with no proxying to the hub, only GET and a strict content policy exposes almost nothing: it has nothing to forward and nowhere to write.
4. An experimental forecast is shown more honestly beside simple reference methods: the table shows where the model wins and where it does not yet.

## Availability

- The page: [ionostation.volgatech-itrc.ru](https://ionostation.volgatech-itrc.ru/)
- Models and explanations of oblique chirp sounding: [the ionozond playground](https://konkin-nikita.ru/ionozond-playground/)
