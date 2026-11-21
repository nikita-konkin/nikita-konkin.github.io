---
title: "Correlation analysis of heliogeophysical characteristics for the analysis of transionospheric effects"
pair: geliogeofizika-korrelyatsiya
lang: en
date: 2026-11-21
translation_of: 2026-11-21-geliogeofizika-korrelyatsiya.md
summary: "The author assembles a one-year set of heliogeophysical indicators at a 3-hour step (2,920 samples) and computes its correlation matrix with pandas. The largest coefficients in the two groups discussed are Kp–ap (r ≈ 0.82) and F10.7obs–F10.7adj (r ≈ 0.987), on which the indicator groups (Kp, ap, Ap) and (SN, F10.7obs, F10.7adj) are singled out as a basis for modelling transionospheric effects."
paper_title: "Correlation analysis of heliogeophysical characteristics for the analysis of transionospheric effects"
paper_authors: "Vershinin M.V. (supervisor — Konkin N.A.)"
paper_year: 2026
paper_date: "2026"
paper_venue: "Scientific Progress — Creativity of the Young, 2026, no. 1, pp. 696–698"
paper_link: "https://www.elibrary.ru/item.asp?id=93329690"
tags: [ionosphere, transionospheric-channel, heliogeophysical-indicators, correlation-analysis, geomagnetic-activity, Kp-index]
---

## Problem and relevance

Transionospheric radio channels carry data over long distances; reliable operation requires continuous assessment of propagation changes and correction of the link parameters. The main factors acting on the ionosphere are the motion of the link objects and heliogeophysical indicators, from which ionospheric delays and phase shifts are forecast and compensated.

## Aim and hypothesis

The aim is to analyse the heliogeophysical indicators through a correlation matrix for the analysis of transionospheric effects. The tasks are to collect and process the characteristics and determine their relationship with the target geomagnetic-activity parameter, the Kp index. No hypothesis is stated explicitly.

## Materials and methods

The set includes the indicators Kp, ap, Ap, BSR, dB, SN, F10.7obs, F10.7adj, Bz-med, Bz-min, Bz-max and Phi-mean, plus the seasonal factor Month. The author assembled a one-year dataset at a 3-hour step — 2,920 samples — processed it for anomalies and gaps, and computed the correlation matrix with pandas in Python; the treatment is not described.

## Results

A high positive correlation is observed between Kp and ap (r ≈ 0.82), between Kp and Ap r ≈ 0.68, and between ap and Ap r ≈ 0.72. The solar indicators F10.7obs and F10.7adj are linked almost perfectly (r ≈ 0.987), and both correlate strongly with SN (r ≈ 0.64…0.69); the other indicators are not discussed. Two tightly coupled groups are singled out — (Kp, ap, Ap) and (SN, F10.7obs, F10.7adj) — forming a consistent field of conditions that affect transionospheric effects.

## The author's conclusions

The dataset combines orbital parameters (Month, Phi-mean) and heliogeophysical indicators (Kp, Bz, F10.7); with it, in the author's view, ionospheric distortions can be forecast. The strong correlations of the geomagnetic (r ≈ 0.82 and 0.72) and solar (r ≈ 0.987) indicators confirm the importance of the combinations (Kp, ap, Ap) and (SN, F10.7obs, F10.7adj) for modelling transionospheric effects and improving link reliability.

## Limitations

The study is limited to a single correlation matrix; the coefficients are quoted approximately (with ≈) without a significance test or confidence intervals. The indicators BSR, dB, Bz-med, Bz-min, Bz-max, Phi-mean and Month are in the set, but their correlations are not discussed. The need for dynamic corrections stated in the abstract is not implemented: no forecasting model is built. The link between the indicators and transionospheric effects is asserted rather than measured.

## Novelty

The paper claims no novelty explicitly. In substance it provides a correlation summary of a set of heliogeophysical indicators over a one-year series at a 3-hour step and singles out groups of strongly related indicators.

## Heuristics

- **[explicit]** If the reliability of a transionospheric link is to be improved — introduce dynamic corrections to the link parameters, because the ionospheric conditions change.
- **[reconstructed]** If the indicators within a set are strongly correlated — treat them as a group and take their combinations into account in modelling, because the author stresses the importance of indicator combinations.
- **[reconstructed]** If correlations are the basis for selecting predictors — first test their significance, because approximate estimates without a test do not guarantee a stable relationship.

**In one sentence:** A one-year series of 2,920 samples of heliogeophysical indicators is reduced to a correlation matrix whose largest coefficients among those discussed are Kp–ap (r ≈ 0.82) and F10.7obs–F10.7adj (r ≈ 0.987), singling out the groups (Kp, ap, Ap) and (SN, F10.7obs, F10.7adj) as a basis for modelling transionospheric effects.
