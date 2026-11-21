---
title: "Forecasting the planetary Kp index with an ensemble machine-learning regression method"
pair: kp-indeks-ansambl
lang: en
date: 2026-11-21
translation_of: 2026-11-21-kp-indeks-ansambl.md
summary: "The author forecast the planetary Kp index three hours ahead using a random forest with an expanding training window. In summer, the model recorded a root mean squared error of 0.88 Kp and a mean absolute error of 0.71 Kp, compared with 1.39 Kp and 1.18 Kp for Xras."
paper_title: "Forecasting the planetary Kp index with an ensemble machine-learning regression method"
paper_authors: "Korotkova N.A. (supervisor — Konkin N.A.)"
paper_year: 2025
paper_date: "2025"
paper_venue: "Scientific Progress — Creativity of the Young, 2025, no. 1, pp. 492–494"
paper_link: "https://www.elibrary.ru/item.asp?id=83009909"
tags: [geomagnetic-activity, Kp-index, machine-learning, random-forest, time-series]
---

## Problem and relevance

The planetary Kp index measures geomagnetic activity. Forecasts of the index help assess how solar disturbances affect information and communication systems. The author identifies the difficulty of accounting for all relevant factors and the computational cost as limitations of traditional forecasting methods.

## Aim and hypothesis

The author develops an ensemble regression method to forecast the Kp index and compares it with forecasts from the solar astronomy laboratory (Xras). The paper does not say what hypothesis was tested.

## Materials and methods

The study used 2023 series for Kp, ap, D, F10.7, Bz-med, Bz-min and Bz-max sampled every 3 hours. The author prepared lagged values and differences from these series and used year, month, day and hour as calendar features. The paper reports that the model used 8 features.

The random forest was scikit-learn's RandomForestRegressor. The algorithm diagram shows training starting with 168 observations, followed by a forecast 1 observation ahead and an expansion of the training window by 1 observation. Summer forecasts 3 hours ahead were saved by month. The comparison with Xras used root mean squared error (RMSE) and mean absolute error (MAE).

## Results

The author reports average errors of 0.88 Kp in RMSE and 0.71 Kp in MAE for the random forest. In the summer comparison, the corresponding Xras errors were 1.39 Kp and 1.18 Kp.

## The author's conclusions

The author concludes that the random forest is more accurate than the Xras forecast for the summer period studied. The method forecasts three hours ahead and expands the training window at each step.

## Limitations

The paper gives a count of 2920 observations. The wording leaves it unclear whether this count covers the full 2023 series or the summer subset. The paper does not say which 8 features entered the model or how forecast issue times and horizons were aligned. The stated error reductions (0.48 Kp in RMSE and 1.16 Kp in MAE) are inconsistent with the reported averages.

## Novelty

The paper makes no explicit novelty claim. It uses a random forest with an expanding training window to forecast the Kp index and compares it with Xras.

## Heuristics

- **[reconstructed]** If testing a model in a sequence of forecasts, add each observation to the training set once its forecast has been issued and the observation has arrived, because this preserves the order in which observations become available.

**In one sentence:** A random forest with an expanding training window gave smaller average errors than Xras for three-hour Kp forecasts during the summer period studied.
