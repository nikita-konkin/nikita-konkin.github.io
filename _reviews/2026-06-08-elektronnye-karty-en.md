---
title: "A program complex for building electronic diagnostic maps of the coherence bandwidth of an HF radio channel"
pair: elektronnye-karty
lang: en
date: 2026-06-08
translation_of: 2026-06-08-elektronnye-karty.md
summary: "The CriMiCo'2016 conference paper — a fuller version of the coherence-bandwidth study, running from a parabolic ionosphere model and model ionograms to coherence-bandwidth maps from GPS/GLONASS and IRI data. Unlike the short version, it states both the definition of coherence bandwidth and the formula used to compute it."
paper_title: "A program complex for building electronic diagnostic maps of the coherence bandwidth of an HF radio channel"
paper_authors: "Ivanov V.A., Konkin N.A., Chernov A.A., Ryabova M.I."
paper_year: 2016
paper_date: "September 2016"
paper_venue: "Proceedings of CriMiCo'2016 — 26th Int. Conference on Microwave & Telecommunication Technology, Sevastopol"
paper_link: "https://elibrary.ru/item.asp?id=29787129"
tags: [ionosphere, radio-sounding, GNSS, coherence-bandwidth, modelling, software]
---

## Summary

This is the fuller, conference version of the coherence-bandwidth study for trans-ionospheric and oblique radio channels, presented at CriMiCo'2016. Compared with the short journal note, it gains a great deal in coherence: the paper takes the reader from a physical formulation through to a finished software product and its output maps.

The paper splits into two complementary parts. The first treats oblique propagation: starting from a parabolic ionosphere model — equations relating the frequency and delay of vertical propagation to their equivalents for an oblique path through the path length and the Earth's radius — it builds a *model* ionogram, which is then compared against a measured ionogram from a chirp ionosonde. The second part studies coherence bandwidth under trans-ionospheric sounding: from GPS/GLONASS data and the IRI model it builds coherence-bandwidth maps as animated images.

The key difference from the companion short paper is that the physics is no longer left implicit. There is an explicit definition of coherence bandwidth — the band over which the nonlinear part of the phase accumulates 1 radian at the edges — and a formula for it via the derivative of delay with respect to frequency. There is also a computational bridge from total electron content (TEC) to coherence bandwidth: the band is expressed through frequency, the speed of light, and TEC variations, whose constant component is taken from IRI and whose variable component comes from processing GNSS data. The conversion "black box" that the short version asked the reader to take on trust is here opened up to the level of working relations.

The engineering side is unchanged and recognizable: a three-stage pipeline (RINEX-to-`.dat` conversion via TecSuite, animated TEC maps, recalculation into coherence bandwidth with IRI queries through Wget), orchestration in AutoIt, storage in PostgreSQL, visualization with GNU Plot. But the pipeline now rests on an explicitly written model, and the work reads as a closed chain: model → algorithm → map.

## Strengths

- **Self-contained.** Unlike the short version, this one carries the definition of coherence bandwidth, the formula to compute it, and the propagation model. It can be read without reaching for companion publications to find the central link.
- **Two sounding geometries.** Oblique and trans-ionospheric propagation are treated together, giving a fuller picture of where the approach applies.
- **A qualitative model check.** Comparing the model ionogram with a measured one (Figs. 1 and 3) is a meaningful, if visual, test: the model visibly reproduces the characteristic shape of the measured ionogram.
- **Thought-through data engineering.** Isolating stages behind the `.dat` format, and a PostgreSQL store with labels and region/time selection, are choices aimed at reuse rather than a one-off computation.

## Notes and limitations

The conference-proceedings format imposes natural limits, so these notes are about depth rather than substance:

- **Validation stays qualitative.** The matching ionogram shapes are convincing to the eye, but without quantitative metrics (frequency/delay discrepancy, map error against independent measurements) the accuracy is hard to judge. A single numerical example would noticeably strengthen the conclusions.
- **Coefficients are stated briefly.** The conversion formula carries a coefficient, and the constant TEC component is taken from IRI; exactly how these are chosen, and how sensitive the result is to them, is left out of scope.
- **GUI automation.** Driving TecSuite through AutoIt remains the fragile point — automating a graphical interface is less robust and reproducible than a programmatic one.

## Suggestions

- Add quantitative validation: a discrepancy metric between model and measured ionograms, and a comparison of coherence-bandwidth maps against an independent measurement.
- State the spatial and temporal resolution of the maps and an estimate of their accuracy.
- Disclose the choice of the coefficient in the bandwidth formula and the way the variable TEC component is estimated.
- Where possible, replace GUI automation with programmatic interfaces to make the pipeline more robust.

## Questions for the authors

- How closely do the model and measured ionograms agree quantitatively — is there an estimate of the frequency and delay discrepancy?
- What is the coverage of the coherence-bandwidth maps, and how are regions without GNSS data handled?
- How does the sensitivity to the constant TEC component taken from IRI affect the final bandwidth values?
