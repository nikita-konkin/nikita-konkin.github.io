---
title: "Analysis of design principles and promising development directions of radio-frequency direction-finding systems based on unmanned aerial vehicles"
pair: pelengatsiya-bpla-printsipy
lang: en
date: 2026-11-21
translation_of: 2026-11-21-pelengatsiya-bpla-printsipy.md
summary: "A systematic review of 2020–2025 publications compares the amplitude, phase and correlation direction-finding methods and virtual antenna arrays for use on unmanned aerial vehicles. The hypothesis that virtual antenna arrays best meet the constraints of airborne basing is confirmed."
paper_title: "Analysis of design principles and promising development directions of radio-frequency direction-finding systems based on unmanned aerial vehicles"
paper_authors: "Kozichko V.M. (supervisor — Konkin N.A.)"
paper_year: 2026
paper_date: "2026"
paper_venue: "Scientific Progress — Creativity of the Young, 2026, no. 1, pp. 713–715"
paper_link: "https://www.elibrary.ru/item.asp?id=93329696"
tags: [UAV, direction-finding, virtual-antenna-arrays, passive-radar, phase-method]
---

## Problem and relevance

There is a growing need to monitor a wide range of digital signals — from control and telemetry channels to radio-beacon and communication signals. Radio-frequency direction finding holds a special place because of its passive mode of operation, and the greatest interest lies in implementing highly mobile direction-finding complexes on unmanned aerial vehicles (UAVs).

## Aim and hypothesis

The aim is to analyse and systematise the design principles of airborne direction finders. The hypothesis is stated explicitly: virtual antenna arrays best meet the constraints of airborne basing compared with traditional methods. The novelty, as the author claims, lies in jointly comparing direction-finding methods with regard to the specific constraints of airborne basing.

## Materials and methods

The method of a systematic review of 2020–2025 publications was used. Four approaches are compared by accuracy (in degrees), frequency range (in GHz) and mass (in grams): amplitude — accuracy 5–15°, range 0.4–6 GHz, mass under 200 g; phase — 1–3°, 0.4–6 GHz, over 500 g; correlation — 0.5–2°, 0.4–6 GHz, over 1 kg; virtual antenna arrays — 1–3°, 0.8–6 GHz, 300–500 g. Application areas are considered separately: search-and-rescue operations, counter-drone work and observing a group of objects.

## Results

Amplitude direction finders are simple to implement but unsuitable for rapidly moving targets. Phase methods are accurate but need complex calibration. The technology of virtual antenna arrays based on virtual magnetic dipoles is recognised as the most promising: it compensates the field distortions caused by the UAV body and radome and allows cheap dielectrically opaque materials without loss of accuracy. For search-and-rescue tasks it is important to account for how the direction-finding range depends on flight altitude, and for groups of objects, algorithms for identifying bearings are needed.

## The author's conclusions

The author concludes that the hypothesis is confirmed: virtual antenna arrays best meet the constraints of airborne basing, giving a compromise between the carrier's size-and-mass characteristics and direction-finding accuracy. The author suggests directing further research at improving interference immunity and developing adaptive calibration algorithms for on-board antenna systems.

## Limitations

Table 1 cites sources for every row, but how the accuracy, range and mass values were obtained is not described, so the numerical comparisons are hard to verify. The abstract speaks of “inexpensive radio-transparent materials”, while the main text speaks of “cheap dielectrically opaque” ones. The review relies on secondary data with no measurements or modelling of its own. Table 1 gives the mass and accuracy of all four approaches, but the paper states no quantitative criterion by which the mass-versus-accuracy compromise of virtual arrays is judged the best.

## Novelty

The novelty is claimed by the author: a systematisation and comparison of direction-finding methods with an emphasis on the specific constraints of airborne basing, which had not been considered jointly in available reviews.

## Heuristics

- **[explicit]** If a direction finder is placed on a UAV — prefer virtual antenna arrays on virtual magnetic dipoles, because they compensate the field distortions from the body and radome and are compatible with cheap opaque materials.
- **[reconstructed]** If a direction finder must track fast targets — do not rely on the amplitude method alone, because it is unsuitable for rapidly moving objects.
- **[reconstructed]** If a review includes a quantitative table — describe how the values were obtained, because otherwise the accuracy, range and mass cannot be re-checked.

**In one sentence:** From the 2020–2025 review, the virtual-antenna-array technology on virtual magnetic dipoles is judged the most suitable for UAV direction finders, since it combines 1–3° accuracy with a mass of 300–500 g and allows cheap opaque materials.
