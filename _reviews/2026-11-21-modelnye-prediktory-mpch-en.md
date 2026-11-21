---
title: "Analysis of the influence of derived and model predictors on the accuracy of forecasting maximum usable frequencies of HF radio links"
pair: modelnye-prediktory-mpch
lang: en
date: 2026-11-21
translation_of: 2026-11-21-modelnye-prediktory-mpch.md
summary: "A one-day MUF forecast for Yoshkar-Ola and Brisbane on 2023 data was built with XGBoost, Elastic Net, Huber Regressor and their average, Voting, with predictors selected by importance. The largest contributions came from the IRI-2020 model MUF, the seasonal component and the one-day shift of the series, while specialised feature sets changed accuracy only slightly."
paper_title: "Analysis of the influence of derived and model predictors on the accuracy of forecasting maximum usable frequencies of HF radio links"
paper_authors: "Konkin N.A., Elchaninova A.S."
paper_year: 2025
paper_date: "2025"
paper_venue: "Microwave & Telecommunication Technology, 2025, no. 7, pp. 51–53"
paper_link: "https://www.elibrary.ru/item.asp?id=83095332"
tags: [ionosphere, hf-radio-link, MUF, IRI-2020, predictors, machine-learning]
---

## Problem and relevance

The maximum usable frequency (MUF) of short-wave communication has a pronounced diurnal and seasonal variability linked to the ionosphere, solar activity and geomagnetic disturbances. For machine-learning forecasts, derived features are built — time lags, rolling statistics, trend and seasonality — and model predictors from the International Reference Ionosphere model IRI-2020 are added. The authors ask how these predictors affect forecast accuracy under different geophysical conditions.

## Aim and hypothesis

The aim is a comprehensive analysis of the influence of derived and model predictors on the accuracy of a one-day MUF forecast for receiving stations in Yoshkar-Ola (56°39′ N, 47°53′ E) and Brisbane (27°28′ S, 153°01′ E). No hypothesis is stated explicitly; in substance the paper tests that predictor selection improves the forecast and that one common set suits both stations.

## Materials and methods

MUF data for each season of 2023, 5-minute step. The training part is 18 days, the test part 7 days, with a forecast made in 1-day steps and a fixed training size. Models: XGBoost, Elastic Net (regularised linear regression), Huber Regressor (robust linear regression) and the Voting ensemble, which averages the forecasts of the three.

Predictors: model estimates, including MUF_IRI2020, and derived features shifted by 288 samples (24 hours): the MUF series itself, rolling mean, minimum, maximum and standard deviation in windows of 12, 48 and 288 samples, trend, seasonal and residual components; calendar features hour and minute are added to them. Three stages: assessing accuracy and predictor importance with the three models; forming individual sets (set1) for each station and a universal set (set2), forecasting with Voting; comparing the results.

## Results

Without predictor selection the metrics averaged over 7 days for the two stations lie in these ranges: MAE from 1.280 to 3.422 MHz, MAPE from 0.085 to 0.195, R² from −4.560 to 0.959. For Yoshkar-Ola Elastic Net is best: MAE from 1.280 to 1.534 MHz, MAPE from 0.072 to 0.097. For Brisbane the best were Huber (MAE from 1.649 to 3.033 MHz, MAPE from 0.076 to 0.177) and XGBoost (MAE from 1.706 to 3.356 MHz, MAPE from 0.084 to 0.186).

With the Voting ensemble: for set1 (the paper names the station — Brisbane) MAE from 1.679 to 3.159 MHz, MAPE from 0.119 to 0.180, R² from −3.951 to 0.954; for set2 (the station is not named explicitly for these values) MAE from 1.321 to 3.243 MHz, MAPE from 0.086 to 0.189, R² from −3.421 to 0.957. The largest contributions for Yoshkar-Ola came from the seasonal component, MUF_IRI2020 and the one-day value of the MUF; for Brisbane, from MUF_IRI2020 and the minimum with the standard deviation in the 288-sample window.

## Authors' conclusions

The most significant predictors were identified for each station. Combining the models by Voting did not lead to a significant gain or loss of accuracy compared with the base models; the specialised sets changed accuracy only slightly.

## Limitations

The results of set1 for Yoshkar-Ola and of set2 by station are not given separately; the metrics are given as ranges, without tying them to a season. Negative R² values (down to −4.560) point to configurations worse than the plain mean but are not analysed. MAPE for set1 at Brisbane (from 0.119) is higher than for the base Huber and XGBoost (from 0.076 and 0.084), which the conclusion does not reflect. An 18-day training sample is short for seasonal effects, and the period is one year. The overall MAPE range starting at 0.085 does not agree with the lower values given later, 0.072, 0.076 and 0.084; the paper does not explain what the ranges cover. The phrase “(more than 6 %)” in the conclusion is not explained.

## Novelty

The paper does not claim novelty explicitly. In substance it compares individual and universal predictor sets, including the IRI-2020 model MUF, for two stations at different latitudes.

## Heuristics

- **[reconstructed]** If features must be chosen for a MUF forecast — first assess the importance of all predictors with three different models, then build compact sets from them, because the significant features differ between stations.
- **[reconstructed]** If a MUF forecast is built for stations at different latitudes — check whether one feature set suits both, because the importance of features differed between Yoshkar-Ola and Brisbane.
- **[reconstructed]** If averaging an ensemble does not change accuracy — choose by simplicity and stability instead of adding models, because there is no gain.

**In one sentence:** The IRI-2020 model MUF, the seasonal component and the one-day shift of the series proved the main predictors of a one-day MUF forecast, while specialised feature sets and the Voting ensemble changed accuracy hardly at all.
