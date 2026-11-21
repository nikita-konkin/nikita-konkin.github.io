---
title: "Forecasting the planetary Kp-index with a regression machine-learning method"
pair: kp-indeks-regressiya
lang: en
date: 2026-11-21
translation_of: 2026-11-21-kp-indeks-regressiya.md
summary: "A forecast of the planetary Kp-index is built with scikit-learn linear regression on 2023 data (2,920 samples at a 3-hour step) with 16 features. The model reaches MAE 0.79 Kp and RMSE 1.52 Kp, against the solar-astronomy laboratory forecast of IKI and ISEF with 1.62 Kp RMSE and 1.33 Kp MAE on average."
paper_title: "Forecasting the planetary Kp-index with a regression machine-learning method"
paper_authors: "Korotkova N.A. (supervisor — Konkin N.A.)"
paper_year: 2025
paper_date: "2025"
paper_venue: "Applied Electrodynamics, Photonics and Living Systems — 2025. Abstracts of the XII International Youth Conference, Kazan, pp. 556–558"
paper_link: "https://www.elibrary.ru/item.asp?id=83253102"
tags: [geomagnetic-activity, Kp-index, machine-learning, linear-regression, forecasting]
---

## Problem and relevance

The planetary Kp-index is a key indicator of geomagnetic activity and matters for forecasting the influence of solar disturbances on infocommunication systems. Traditional forecasting methods are limited by the difficulty of accounting for all factors and by high computational costs, whereas machine learning can analyse large volumes of data and improve forecast accuracy.

## Aim and hypothesis

The aim is to develop a method for forecasting the planetary Kp-index based on a regression machine-learning method. No hypothesis is stated explicitly; in substance the paper tests that linear regression gives a forecast comparable to or better than the laboratory's reference forecast.

## Materials and methods

The scikit-learn linear regression method (Linear Regression) was used. The dataset contains the Kp, ap, D and F10.7 indices for 2023 — 2,920 samples at a 3-hour step. Temporal features (year, month, day, hour) and shift features (shifts and differences of the Kp, ap, D and F10.7 values) were prepared; 16 features in total. The algorithm includes building the dataset and the features, setting the forecast horizon and forecasting with an expanding training window. Quality was assessed with the RMSE, MAE, MSE and R² metrics. The data were collected from the IKI and ISEF site over one week of each month of 2023.

## Results

On average the reference forecast per month came to 1.62 Kp in RMSE and 1.33 Kp in MAE. The linear-regression model showed an MAE of 0.79 Kp and an RMSE of 1.52 Kp. Comparing the two forecasts shows an error reduction of 0.1 Kp in RMSE and 0.534 Kp in MAE. The advantage differs by season: RMSE fell by 0.21 Kp in summer and by 0.27 Kp in winter.

## The author's conclusions

The author concludes that a method for forecasting the Kp-index based on linear regression has been developed and that it shows a seasonal advantage over the IKI and ISEF laboratory forecasts: RMSE fell by 0.21 Kp in summer and by 0.27 Kp in winter.

## Limitations

The forecast horizon and the train/test split are not stated explicitly. It is not explained what exactly is taken as the laboratory's reference forecast and how it is computed: the text calls it the Xras forecast, and how it is built is not disclosed. The comparison covers only one method (linear regression); the MSE and R² metrics are declared but not reported numerically. The claims of a "seasonal advantage" are made without saying how the data were divided into seasons.

## Novelty

The paper does not claim novelty explicitly. In substance it proposes a method for forecasting the Kp-index with linear regression on temporal and shift features and compares it with the laboratory's reference forecast.

## Heuristics

- **[reconstructed]** If a forecast is built on geomagnetic series — add shift features (shifts and differences of the values), because shifts and differences give the model the recent history of the series; in this work they and the temporal features made up the 16 features.
- **[reconstructed]** If a model is judged only by averaged metrics — also report per-quarter or per-month values, because the overall advantage is made up of contributions that differ by season.
- **[reconstructed]** If two forecasts are compared — describe the reference forecast explicitly, because otherwise the difference in errors cannot be attributed to the model's merits.

**In one sentence:** Linear regression on 16 temporal and shift features forecasts the Kp-index with MAE 0.79 Kp and RMSE 1.52 Kp, which is 0.534 Kp better in MAE and 0.1 Kp better in RMSE than the reference forecast of the IKI and ISEF laboratory.
