---
title: "Ensemble machine learning methods for predicting characteristics of shortwave ionospheric communication channels"
pair: ansambli-kv-kanaly
lang: en
date: 2026-11-21
translation_of: 2026-11-21-ansambli-kv-kanaly.md
summary: "XGBoost, Elastic Net, Huber regression and random forest, together with the Stacking and Voting ensembles, forecast the MUF 24 hours ahead in four seasons on two datasets: the Cyprus — Yoshkar-Ola path and Australian space-weather data. A single XGBoost gave the best results (MAPE 7.5 %, RMSE 1.570 MHz in autumn on the first set; 6.6 % and 0.577 MHz in summer on the second), and Voting was more accurate than Stacking."
paper_title: "Ensemble machine learning methods for predicting characteristics of shortwave ionospheric communication channels"
paper_authors: "Konkin N.A. (supervisor — Ryabova N.V.)"
paper_year: 2025
paper_date: "2025"
paper_venue: "Applied Electrodynamics, Photonics and Living Systems — 2025. Abstracts of the XII International Youth Conference, Kazan, pp. 40–45"
paper_link: "https://www.elibrary.ru/item.asp?id=83252837"
tags: [ionosphere, hf-channel, MUF, ensembles, stacking, XGBoost]
---

## Problem and relevance

Shortwave ionospheric channels serve long-range radio communication where there is no satellite infrastructure or where it is vulnerable. Their operation depends on the state of the ionosphere, which changes with solar activity, geomagnetic disturbances, and daily and seasonal cycles. Physical-statistical models (IRI, ITS), according to the author, adapt poorly to fast changes, lose accuracy in storms and over local anomalies, need heavy computation and ignore nonlinear relations. Machine learning picks up complex patterns in time series but requires choosing a model and its parameters.

## Aim and hypothesis

The aim is to develop and assess an ensemble approach to forecasting the maximum usable frequency (MUF) based on stacking. No hypothesis is stated explicitly; in substance the paper tests that ensembles are more accurate than single models.

## Materials and methods

Implemented in Python. Four models: XGBRegressor, Elastic Net, Huber Regression and Random Forest Regression. Three approaches: each model trained separately; stacking, where the base models XGBoost, Elastic Net and Huber regression produce meta-features for a meta-model, a random forest; and voting, a plain average of the base models' forecasts without a meta-model. Metrics: MAE, RMSE, MAPE.

The forecast covers 24 hours at a 30-minute step; the paper says the test sample spans 18 days and the training sample 7. Dataset no. 1 is slant sounding of the Cyprus — Yoshkar-Ola path with the sensor-diagnostics equipment of Volga State University of Technology; dataset no. 2 is data of the Australian Space Weather Forecasting Centre for a path in Australia. There are 22 predictors: derivatives of the MUF course (seasonal, random and trend components, a moving average) and time stamps. Test periods in 2023: winter 30.01–05.02, spring 30.04–05.05, summer 23.08–31.08, autumn 30.10–05.11.

## Results

Approximate entropy ApEn (pattern length 2, threshold 0.2) of the series in dataset no. 1: spring 0.300, summer 0.320, autumn 0.20, winter 0.240; in dataset no. 2: spring 0.082, summer 0.088, autumn 0.094, winter 0.100.

Dataset no. 1. XGBoost is the most accurate in autumn: MAPE 7.5 %, RMSE 1.570 MHz. Voting gives consistently low errors, in winter MAPE 9.0 % and RMSE 1.691 MHz. Huber regression is the worst in spring: MAPE 19.5 %, RMSE 4.241 MHz. On average the accuracy of Stacking is lower than that of Voting by 0.2 MHz in RMSE and 1 % in MAPE.

Dataset no. 2. The smallest errors are again XGBoost's, in summer: MAPE 6.6 %, RMSE 0.577 MHz. In winter Elastic Net is the weakest (MAPE 12.3 %, RMSE 1.004 MHz); Voting is also weaker, and Stacking got MAPE 10.8 % and RMSE 0.924 MHz. On average Stacking trails Voting by 0.21 MHz in RMSE and 2 % in MAPE.

## The author's conclusions

An ensemble approach based on stacking has been developed; Stacking and Voting showed advantages over single models in the winter seasons. According to the conclusion, ensembles raise forecast accuracy by 13 %, mainly on data with relatively low entropy (within 0.1 ApEn); the abstract puts the gain at 1–2 % in MAPE.

## Limitations

Only selected error values are given; the full results are in the figures. Model parameters and the exact split are not stated, and the 18-day test and 7-day training sizes look swapped. The figures for the ensemble gain disagree (1–2 % in the abstract, 13 % in the conclusion), and in the results text the best values belong to the single XGBoost, with Stacking worse than Voting. The claimed advantage of ensembles in winter is not borne out by dataset no. 2, where Voting and Stacking were weak in winter. The test periods are separate intervals of one year, given by dates. The link between accuracy and entropy is given only as an observation. There is no direct comparison with a simple baseline forecast.

## Novelty

Not claimed explicitly. The contribution is a comparison of four models and two ensembles, stacking and voting, in MUF forecasting by season on two datasets.

## Heuristics

- **[explicit]** If the series has low entropy (ApEn within 0.1) — apply ensemble methods, because on such data, according to the author's conclusion, they raise accuracy.
- **[reconstructed]** If ensembles are compared with one another — include plain averaging (voting), because here it was more accurate than stacking at lower complexity.
- **[reconstructed]** If model quality depends on the season — assess the models season by season, because the best and the worst model change from season to season (Huber regression is the worst in spring, XGBoost the best in autumn and summer).
- **[reconstructed]** If a conclusion rests on one path — check it on a second, independent dataset, because the seasonal pattern of error differs between the two sets.

**In one sentence:** On two datasets the best 24-hour MUF forecasts come from a single XGBoost, and of the ensembles Voting beats Stacking; the author ties the ensemble gain mainly to low-entropy data, but the paper does not show in which cases it was observed.
