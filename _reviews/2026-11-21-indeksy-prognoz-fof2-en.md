---
title: "Comparative analysis of the influence of geomagnetic and solar indices on forecasting the critical frequency of the ionospheric F2 layer using machine learning"
pair: indeksy-prognoz-fof2
lang: en
date: 2026-11-21
translation_of: 2026-11-21-indeksy-prognoz-fof2.md
summary: "A one-day foF2 forecast from June–August 2023 data (26,496 samples) was built with a random forest and XGBoost using geomagnetic and solar indices, varying the resampling step from 10 to 30 minutes. The random forest at a 15-minute step gave MAE 0.39, RMSE 0.48, MAPE 6.63 % and R² 0.92, with about 62 % of the importance carried by the smoothed foF2 value."
paper_title: "Comparative analysis of the influence of geomagnetic and solar indices on forecasting the critical frequency of the ionospheric F2 layer using machine learning"
paper_authors: "Korotkova N.A., Konkin N.A."
paper_year: 2025
paper_date: "2025"
paper_venue: "Microwave & Telecommunication Technology, 2025, no. 7, pp. 37–38"
paper_link: "https://www.elibrary.ru/item.asp?id=83095325"
tags: [ionosphere, foF2, geomagnetic-indices, solar-indices, random-forest, XGBoost]
---

## Problem and relevance

The critical frequency of the F2 layer (foF2) varies under solar and geomagnetic activity, which makes modelling hard. Empirical ionospheric models, the authors say, are limited by the nonlinearity of the processes and by the different time scales of the input data. In addition, foF2 is measured every 5 minutes while external indices are updated every 3 hours, and it is unclear which indices have the greatest predictive power in nonlinear models.

## Aim and hypothesis

The aim is to compare the influence of geomagnetic and solar indices on foF2 forecasting with machine-learning methods. No hypothesis is stated explicitly; in substance the paper tests that forecast accuracy depends on the indices and that a suitable data aggregation step strengthens their influence.

## Materials and methods

Data: foF2 and the indices for June, July and August 2023, 26,496 samples at a 5-minute step. Solar indices are F10.7, the sunspot number SN and the integral characteristic Phi-mean; geomagnetic ones are Kp, Ap, D and the interplanetary field parameters Bz-med, Bz-min, Bz-max. The foF2 series is split by the Hodrick — Prescott filter into a trend and a cyclic part, and the smoothed value served as the target variable.

Two models are chosen: RandomForestRegressor and XGBoost. The procedure has three stages: building a set of time and shift features; then a forecast with an expanding training window (a one-day forecast of 288 samples for each month); then evaluation by MAE, RMSE, MAPE and R². To reconcile the sampling rates, the original 5-minute step was aggregated to 10, 15, 20, 25 and 30 minutes.

## Results

Summer averages: RandomForestRegressor has the smallest errors at a 15-minute step — MAE 0.3898, RMSE 0.4812. XGBoost has its minimum at a 30-minute step — MAE 0.3793, RMSE 0.45. In XGBoost feature importance (30 minutes) the smoothed foF2 gives 62 %, Bz-med and Bz-max on average about 5 %, Phi-mean 4.8 %, the other indices 0.35 %. For the random forest (15 minutes) the smoothed foF2 is 62.58 %, Ap 0.95 %, SN 0.77 %, the rest 0.48 %.

## Authors' conclusions

A method for forecasting the critical frequency with machine-learning models has been developed; a dependence of forecast accuracy on geomagnetic and solar indices was shown. The smallest error came from the random forest at a 15-minute step: MAE 0.39, RMSE 0.48, MAPE 6.63 %, the highest R² of 0.92. The significant features of this model are the smoothed foF2, Ap and SN.

## Limitations

The conclusion that accuracy depends on the indices is not backed by a comparison with a forecast without indices. The main contribution (about 62 %) comes from the smoothed and lagged foF2; the share of the indices is small. The statement that the random forest gave the smallest error disagrees with the numbers given: XGBoost has MAE 0.3793 and RMSE 0.45, which are lower. XGBoost's R² and MAPE are not given as numbers in the text; Figure 1 compares these metrics. The measuring station for foF2, the units of the errors and the composition of the test interval are not named; the metrics may have been computed on the smoothed series, which is not specified. The period is three summer months of one year.

## Novelty

The paper does not claim novelty explicitly. In substance it compares the contributions of solar and geomagnetic indices to the foF2 forecast at different data aggregation steps.

## Heuristics

- **[explicit]** If the sampling of the target series and of external indices differs — tune the time aggregation step, because it affects the contribution of external indices and forecast quality.
- **[explicit]** If the foF2 series has short-term fluctuations — smooth it with the Hodrick — Prescott filter and take the trend part as the target, because this reduces the influence of noise.
- **[reconstructed]** If the contribution of external indices is being assessed — compare the model with and without them, because feature importance alone does not prove that accuracy depends on them.

**In one sentence:** A random forest with the smoothed foF2 and indices at a 15-minute step forecasts foF2 a day ahead with R² 0.92 and MAPE 6.63 %, but about 62 % of the importance sits with the smoothed foF2, and the contribution of the indices is not checked against a model without them.
