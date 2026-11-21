---
title: "Studying the behavior of the ionosphere in different climatic zones"
pair: ionosfera-klimaticheskie-zony
lang: en
date: 2026-11-21
translation_of: 2026-11-21-ionosfera-klimaticheskie-zony.md
summary: "The author describes the structure of the ionosphere, its layers and latitude bands, and then compares Russian cities from different climatic zones. The conclusion is qualitative: ionospheric density is higher in the south, while in mid-latitudes its variability is attributed to geomagnetic storms and solar flares."
paper_title: "Studying the behavior of the ionosphere in different climatic zones"
paper_authors: "Antropova E.M. (supervisor — Konkin N.A.)"
paper_year: 2024
paper_date: "2024"
paper_venue: "Scientific Progress — Creativity of the Young, 2024, no. 1, pp. 279–281"
paper_link: "https://www.elibrary.ru/item.asp?id=69910519"
tags: [ionosphere, climatic-zones, ionospheric-layers, ionospheric-disturbances, radio-communication]
---

## Problem and relevance

The ionosphere is the upper part of the atmosphere with a high level of ionization, on which the propagation of radio waves depends. Its state varies with altitude, latitude and solar and magnetospheric processes, so for reliable radio communication it matters how the ionosphere behaves in different climatic zones.

## Aim and hypothesis

The aim is to study the state of the ionosphere in different climatic zones and regions using machine-learning regression models. No hypothesis is stated explicitly.

## Materials and methods

The paper describes the ionosphere: the lower boundary at 50–60 km, the upper boundary at about 1000 km, and three regions of maximum electron density — D (about 80 km), E (about 110 km) and the F layer, split into F1 (about 170 km) and F2 (about 300 km); the author notes that these values are approximate and that layer heights can vary considerably. By latitude it distinguishes the equatorial (0–35°), mid-latitude (±35–55°), subauroral (55–65°) and high-latitude (auroral zone and polar cap) ionosphere. It describes disturbances: sudden ionospheric disturbances (SID) in the E and D regions from X-ray bursts (a 50–200 % rise in electron density in E), polar cap absorption from protons above 10 MeV, and substorms that produce sporadic Es layers. For comparison it takes the cities Murmansk (subarctic belt), Yaroslavl and Yoshkar-Ola, Sevastopol, Astrakhan and Sochi. The TEC data and the specific machine-learning models are not described in the text.

## Results

The theoretical analysis yields two regularities. In the southern regions of Russia the ionospheric density increases, which raises the ionization of the atmosphere. In mid-latitudes the variability of the ionosphere is attributed to geomagnetic storms, solar flares and other factors. The paper gives no numerical results for the regression models.

## The author's conclusions

The author gives no separate conclusion; the result is limited to the regularities stated for the southern and mid-latitudes.

## Limitations

The stated use of machine-learning regression models is not shown in the text: there are no TEC data, no description of the models and no metrics. The comparison of cities with climatic zones is qualitative, and no quantitative ionospheric characteristics are given per zone.

## Novelty

The paper does not claim novelty explicitly. In substance it is a survey of the structure and disturbances of the ionosphere with an attempt to relate them to the climatic zones of Russia.

## Heuristics

- **[reconstructed]** If the ionosphere is analyzed by region — group the observation points by latitude band, because the ionosphere's response to solar and magnetospheric forcing depends on latitude.
- **[reconstructed]** If different kinds of ionospheric disturbance must be told apart — separate polar cap absorption from sudden disturbances (SID), because in the paper the former is tied to solar protons and the D region and lasts up to several days, while the latter are tied to X-ray radiation in the E and D regions and last several minutes.

**In one sentence:** The paper describes the layers, latitude bands and disturbances of the ionosphere and reduces its behavior in the climatic zones of Russia to two qualitative regularities, without carrying the machine-learning regression models it names through to a numerical result.
