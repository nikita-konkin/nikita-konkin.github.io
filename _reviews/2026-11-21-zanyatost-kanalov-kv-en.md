---
title: "Analysis of occupancy of channels with bandwidths of 3 to 24 kHz in the task of cognitive HF radio"
pair: zanyatost-kanalov-kv
lang: en
date: 2026-11-21
translation_of: 2026-11-21-zanyatost-kanalov-kv.md
summary: "A method is developed for estimating the occupancy of HF channels with bandwidths of 3, 6, 12 and 24 kHz in the 3–28 MHz range from the noise level, and tested in Yoshkar-Ola in March 2020 on a laboratory prototype based on software-defined radio. The most occupied daytime segments are 3–10 MHz and 26–28 MHz, and occupancy generally falls with frequency."
paper_title: "Analysis of occupancy of channels with bandwidths of 3 to 24 kHz in the task of cognitive HF radio"
paper_authors: "Ivanov D.V., Ivanov V.A., Belgibaev R.R., Konkin N.A."
paper_year: 2020
paper_date: "2020"
paper_venue: "Microwave & Telecommunication Technology, 2020, no. 1-2, pp. 96–97"
paper_link: "https://www.elibrary.ru/item.asp?id=45711479"
tags: [hf-channel, spectrum-occupancy, cognitive-radio, wideband-communication, software-defined-radio]
---

## Problem and relevance

HF communication is valued for its survivability and autonomy, but the narrow frequency range and users' wish for higher data rates raise the problem of even use of HF frequencies. A rate of 9600 baud has been reached in channels wider than 3 kHz; further growth requires wider bandwidths. US standards for wideband HF communication (WBHF) provide for bandwidths up to 24 kHz, in future up to 48 kHz, in steps of 3 kHz, with rates from 75 baud to 120 kbaud. Estimating the state of channels from propagation conditions remains unsolved; methods are needed for estimating spectrum occupancy, analysing it and managing it dynamically.

## Aim and hypothesis

The aim is to raise the efficiency of information transfer over an HF channel with bandwidths of 3–24 kHz: to develop methods and algorithms for estimating channel occupancy from noise-level data, in order to adapt a digital HF communication system from sounding data. No hypothesis is stated explicitly.

## Materials and methods

Occupancy is estimated for a frequency-ordered set of channels with bandwidths of 3, 6, 12 and 24 kHz in the 3–28 MHz range from experimental data with a spectral resolution of 281 Hz. The noise power spectral density (PSD) in a 3 kHz channel is the mean over 8 neighbouring samples; in channels of 6, 12 and 24 kHz the number of averaged samples is 2, 4 and 8 times larger. For a stable estimate, 381 spectra were averaged (a mean over 1 s). For the analysis, variational series of samples were built for megahertz segments; the minimum PSD value for normalisation was found by averaging the first 10 samples of the series. Samples exceeding a threshold of 10 dB were counted as occupied (level 0), the rest as free (level 1). For a generalised availability estimate the CMA metric was introduced — the ratio of the number of channels available during a minute to the total number of channels in the segment.

The experiments were carried out in Yoshkar-Ola in March 2020 on a laboratory prototype of a software–hardware system for monitoring interference, based on software-defined radio (SDR). The critical frequency of the ionosphere during the observations was 9 MHz. The data were processed in PTC Mathcad 15.

## Results

Fig. 1 shows normalised variational series for 3 kHz channels by megahertz segment. Channels are most occupied in the 3–10 MHz and 26–28 MHz ranges; occupancy falls as frequency rises. In the 3–4 MHz range (near-vertical incidence skywave, NVIS, mode) occupancy is higher. The authors link the interference at 7–10 MHz to broadcasting stations with a range of up to 2000 km, and the rise in occupancy at 26–28 MHz to the work of civil services. The text gives no numerical occupancy values or CMA values.

## Authors' conclusions

Methods for estimating spectrum occupancy, analysing and interpreting it have been scientifically substantiated; a laboratory prototype of a monitoring system with resolutions of 3, 6, 12 and 24 kHz has been created. For Yoshkar-Ola the most occupied daytime segments are 3–10 MHz and 26–28 MHz; in NVIS mode the load is higher. The authors conclude that the feasibility of wideband communication with bandwidths up to 24 kHz, able to raise the data rate substantially, has been shown experimentally.

## Limitations

The observations cover one month and one site; the number of sessions and the length of records are not given, and the time of day is mentioned only as “daytime” in the conclusions. The example in Fig. 1 is given for the 3 kHz band only; results for 6, 12 and 24 kHz and CMA values are not shown. The sources of interference are named without verification. The conclusion about feasibility with bandwidths up to 24 kHz and about a higher rate rests on an occupancy estimate, and the paper does not describe any tests of transmission in wide bandwidths. The claim of “scientific substantiation” of the methods is not elaborated in the text.

## Novelty

The paper does not claim novelty explicitly. In substance it describes estimating the occupancy of HF channels in four bandwidths from the noise level, and measurements for Yoshkar-Ola on a laboratory SDR prototype.

## Heuristics

- **[reconstructed]** If the occupancy of a channel wider than 3 kHz is to be estimated — average the PSD over a number of samples proportional to the bandwidth (2, 4 and 8 times more), because a wider channel contains more spectral samples (a 3 kHz channel has 8).
- **[reconstructed]** If a channel must be classed as occupied or free — normalise the PSD to the minimum value and compare it with a 10 dB threshold, because the threshold is counted from the minimum PSD value.
- **[reconstructed]** If wideband HF communication is planned under conditions close to the Yoshkar-Ola measurements — look for free channels outside 3–10 MHz and 26–28 MHz, because there channels are the most occupied by day.

**In one sentence:** Measurements in Yoshkar-Ola in March 2020, using a threshold of 10 dB above the minimum PSD, showed that the most occupied daytime HF channels lie in the 3–10 MHz and 26–28 MHz segments, but the paper has no numerical occupancy estimates and no tests of transmission in wide bandwidths.
