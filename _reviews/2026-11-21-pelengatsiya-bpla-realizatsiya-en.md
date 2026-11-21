---
title: "Analysis of the practical implementation of a radio-frequency direction-finding system for unmanned aerial vehicles"
pair: pelengatsiya-bpla-realizatsiya
lang: en
date: 2026-11-21
translation_of: 2026-11-21-pelengatsiya-bpla-realizatsiya.md
summary: "A radio-frequency direction-finding system for unmanned aerial vehicles (UAVs) based on software-defined radio (SDR) and the MUSIC algorithm is analysed. In experiments by Martian and co-authors with a DJI Mavic Air drone the mean direction error was 1.15° in the static case and 1.86° in the dynamic case."
paper_title: "Analysis of the practical implementation of a radio-frequency direction-finding system for unmanned aerial vehicles"
paper_authors: "Kozichko V.M. (supervisor — Konkin N.A.)"
paper_year: 2026
paper_date: "2026"
paper_venue: "Scientific Progress — Creativity of the Young, 2026, no. 1, pp. 710–712"
paper_link: "https://www.elibrary.ru/item.asp?id=93329695"
tags: [UAV, direction-finding, software-defined-radio, SDR, MUSIC, airspace-security]
---

## Problem and relevance

The growth of the civil unmanned-aerial-vehicle (UAV) market creates a parallel market for systems to detect and neutralise them. Existing detection methods are limited: optical ones depend on visibility, acoustic ones on range, and radar ones are only partly usable because of their high cost. Radio-frequency (RF) direction finding uses a drone's own control, telemetry and video signals and works as a passive, all-weather and comparatively cheap method.

## Aim and hypothesis

The aim is to analyse the architecture, algorithms and experimental results of one RF direction-finding system in order to judge its suitability for airspace-protection tasks. No hypothesis is stated explicitly.

## Materials and methods

The architecture proposed by Alexandru Martian's research group is examined. The hardware platform is a four-channel phase-coherent USRP (Universal Software Radio Peripheral) receiver with software tuning to the 2.4 and 5.8 GHz bands. The algorithmic core is the MUSIC (Multiple Signal Classification) subspace method, which separates the signal and noise subspaces and determines the directions to radiation sources. The experimental part was carried out in the work of Martian and co-authors [1] on a commercial DJI Mavic Air UAV in two scenarios: static (hovering) and dynamic (movement along a prescribed trajectory).

## Results

In the static mode the mean direction error was 1.15°, and in the dynamic mode 1.86°. The author compares these values with alternative approaches: a system based on a uniform circular array showed an error of 1.5–2.5°, and a Kalman-filter method about 2°. In the author's view, accuracy of 1–2° is enough for pointing electro-optical and thermal sensors and for triangulating sources from data at separated sites.

## The author's conclusions

The author concludes that RF direction finding based on SDR and the MUSIC algorithm is a technically mature and economically effective solution for detecting and tracking UAVs, and that the approach's advantages are passivity and concealment, all-weather operation, low deployment cost and high accuracy.

## Limitations

The experimental figures (1.15° and 1.86°) were not obtained by the author but taken from the reviewed publication [1]; the work contains no measurements of its own. The test conditions (distance, number of trials, spread of the estimates) are not described. The paper calls the same value of 1.86° a mean error (p. 711) and a standard deviation (p. 712). The comparison with the circular array and the Kalman filter is made without stating common conditions, so the comparability of the errors is not shown. The text contains a typo in the MUSIC expansion ("SIgnal").

## Novelty

The paper does not claim novelty explicitly. In substance it is an analytical review of one published RF direction-finding system: its hardware platform, its algorithm and its experimental results.

## Heuristics

- **[explicit]** If a passive all-weather drone detector is needed — consider RF direction finding on SDR, because it uses the drone's own control and telemetry signals and is cheaper than radar.
- **[reconstructed]** If the errors of different direction finders are compared — state common measurement conditions, because otherwise a sub-degree difference cannot be attributed to the method's quality.
- **[reconstructed]** If someone else's system is reviewed — separate one's own results from the borrowed ones, because the experimental numbers belong to the source publication, not to the review.

**In one sentence:** An RF direction-finding system on a four-channel USRP SDR receiver with the MUSIC algorithm determines the direction to a DJI Mavic Air drone with a mean error of 1.15° in the static case and 1.86° in the dynamic case.
