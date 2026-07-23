---
title: "Determination of the optimal channel frequency band for satellite communication systems based on diagnostic maps of the coherence bandwidth"
pair: optimalnaya-polosa-chastot
lang: en
date: 2026-07-23
translation_of: 2026-07-23-optimalnaya-polosa-chastot.md
summary: "The coherence bandwidth is taken as the optimal frequency band of a satellite communication channel, and diagnostic maps from GLONASS/GPS data as the instrument for monitoring it. A three-stage processing pipeline and a map for Mari El and Tatarstan are given."
paper_title: "Determination of the optimal channel frequency band for satellite communication systems based on diagnostic maps of the coherence bandwidth"
paper_authors: "Konkin N.A., Kislitsyn A.A."
paper_year: 2020
paper_date: "2020"
paper_link: "https://www.elibrary.ru/item.asp?id=42831881"
tags: [ionosphere, coherence-bandwidth, satellite-communications, optimal-bandwidth, mapping, TEC]
---

## Problem and relevance

The coherence bandwidth characterises the widest possible frequency band over which dispersion distortion can be neglected — that is, it is the optimal frequency band for trans-ionospheric communication systems. For a communication system to operate at that optimal band, the degree of distortion in broadband trans-ionospheric channels must be monitored and the undistorted transmission band estimated.

## Aim and hypothesis

To develop an algorithm and software for building diagnostic coherence-bandwidth maps from GLONASS/GPS satellite navigation data. No hypothesis is stated.

## Materials and methods

The algorithm is implemented with a set of programs written in AutoIt plus supporting software, and comprises three stages:

1. interpretation and conversion of RINEX files into a text format (the .dat extension);
2. processing and conversion of the .dat files to compute variations in total electron content (TEC), with parallel reception of absolute TEC data;
3. conversion of TEC into the coherence bandwidth and creation of diagnostic maps by the iMapCreate program.

## Results

A coherence-bandwidth map for the regions of Mari El and Tatarstan is given (Fig. 1) with a colour scale of values. The date and time of the map, the range of bandwidth values obtained and numerical estimates of the optimal band are not stated in the paper.

## Authors' conclusions

Under conditions of frequency dispersion, diagnostic maps allow the intensity of diurnal variation in the coherence bandwidth over the region under study to be assessed, in order to determine the current optimal channel frequency band for space communication systems under continuously changing environmental parameters.

## Limitations

The identification of the coherence bandwidth with the optimal frequency band is taken with a reference to [1] and is not derived in the work itself, although it carries the main applied weight; no rule is stated for going from the map to a specific bandwidth value for a communication session. In the English-language block the affiliation is given as Povolzhskiy State University of Telecommunications and Informatics, whereas the Russian gives Volga State University of Technology.

## Novelty

The paper claims the formulation of coherence-bandwidth diagnostic maps as an instrument for determining the optimal frequency band of a satellite communication channel. No demarcation from earlier work by the same group is drawn in the text.

## Heuristics

- **[stated]** If a communication system must operate free of dispersion distortion — then take the coherence bandwidth as the optimal channel frequency band, because by definition it is the limit beyond which distortion cannot be neglected.
- **[reconstructed]** If TEC is being converted into the coherence bandwidth — then obtain both the variations and the absolute values at the same stage, because the conversion requires the absolute quantity and not only its variations.
- **[reconstructed]** If a map is built in order to choose a channel parameter — then put a scale of values on it, because without one the map shows a distribution but yields no number to choose by.
- **[reconstructed]** If a monitoring task is posed for a medium with continuously changing parameters — then plan for repeated map building rather than a one-off calculation, because the quantity being assessed changes over the course of a day.

**In one sentence:** The coherence bandwidth is taken as the optimal channel frequency band, with diagnostic maps from GLONASS/GPS data serving as the instrument for monitoring it over a region.
