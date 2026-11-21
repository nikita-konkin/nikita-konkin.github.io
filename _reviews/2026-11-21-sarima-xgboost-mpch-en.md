---
title: "Prediction of MUF HF radio communication based on the hybrid method of the ARIMA model and the machine learning method XGBoost"
pair: sarima-xgboost-mpch
lang: en
date: 2026-11-21
translation_of: 2026-11-21-sarima-xgboost-mpch.md
summary: "A hybrid method for short-term MUF forecasting from a 25-day series at a 5-minute step (a 2.6 thousand km path) uses SARIMA for horizons shorter than 25 minutes and tuned XGBoost for longer ones, up to 75 minutes. Averaged over horizons, the MAE of SARIMA is 0.42 MHz and that of XGBoost 0.35 MHz; for the hybrid the author gives 0.23 MHz in MAE and 0.25 MHz in RMSE."
paper_title: "Prediction of MUF HF radio communication based on the hybrid method of the ARIMA model and the machine learning method XGBoost"
paper_authors: "Konkin N.A."
paper_year: 2023
paper_date: "2023"
paper_venue: "Radio Wave Propagation. Proceedings of the XXVIII All-Russian Open Scientific Conference, Yoshkar-Ola, pp. 228–231"
paper_link: "https://www.elibrary.ru/item.asp?id=54474194"
tags: [ionosphere, hf-channel, MUF, SARIMA, XGBoost, short-term-forecast]
---

## Problem and relevance

The active HF radio sensor developed at Volga State University of Technology builds frequency dependences of group delay from the received signal. From them the band of frequencies available for HF communication is estimated, and its upper limit is the maximum usable frequency (MUF). The calculation of optimum working frequencies depends on the MUF. Because of ionospheric variability the upper limit of the band is random, so machine-learning forecasting of the MUF is needed.

## Aim and hypothesis

The aim is to determine the optimal periods of short-term MUF forecasting and the matching methods by MAE and RMSE, comparing the statistical model SARIMA with the machine-learning model XGBoost. The tasks are to develop a hybrid method and algorithm, implement it in Python, and compare forecasts of diurnal MUF variations over different periods. No hypothesis is stated explicitly; in substance the paper tests that different horizons suit different models and that their combination is more accurate than either alone.

## Materials and methods

The data are MUF obtained by automatic processing of ionograms from sensor diagnostics of HF radio channels, from the data bank of the university. They come from slant sounding of a mid-latitude path 2.6 thousand km long; the sample is 25 days at a 5-minute step. Missing and anomalous samples are interpolated.

SARIMA is tuned with `pmdarima.auto_arima`; the XGBoost parameters (number of trees, learning step eta, gamma and others) are tuned with the hyperopt library. The training sample is on average 90 % of the series; the parameters are tuned so that the model series matches the training one by 98–100 %. The rest is used for validation. Forecast horizons run from 5 to 75 minutes in steps of 10 minutes; a cross-validation with a test sample of the matching length was carried out. The upper horizon was set by the available computing resources. The metrics are MAE and RMSE; relative ones are not needed because a single series is studied.

## Results

Averaged over all horizons, the best results belong to SARIMA and XGBoost with tuned parameters: MAE 0.42 MHz and 0.35 MHz respectively. SARIMA has the smallest error at the 25-minute horizon; at the others tuned XGBoost leads. For horizons shorter than 25 minutes SARIMA has on average R² 0.99 and MAE 0.001 MHz. Results of XGBoost without tuning are shown in Fig. 2 (the numbers are not in the text).

## The author's conclusions

A hybrid method has been developed: SARIMA for forecasts over intervals shorter than 25 minutes and tuned XGBoost for longer ones. The algorithm is implemented in Python. The hybrid approach, in the author's words, gives an average error of 0.23 MHz in MAE and 0.25 MHz in RMSE, a gain of 0.16 MHz in MAE and 0.2 MHz in RMSE relative to the results of tuned XGBoost and SARIMA; the abstract says “twice” in MAE.

## Limitations

The series is short (25 days), one path, dates not given, the training share is given only as an average (90 %). The text names the horizons both as “from 5 to 75 minutes” and as “from 3 to 15 samples”, but with a series step of 5 minutes the lower bound of 3 samples does not fit a 5-minute horizon. The SARIMA orders and the XGBoost parameter values are not given. The hybrid's values (0.23 and 0.25 MHz) appear only in the conclusion: the results section has no separate measurement of the hybrid. The 25-minute boundary is described ambiguously: SARIMA is named best at the 25-minute horizon, while the hybrid uses it “below 25 minutes”. The claimed “twice” fits the numbers only loosely: from 0.42 and 0.35 MHz to 0.23 MHz. The top horizon of 75 minutes is limited by resources, as the author admits. A simple baseline from the last values is not considered in the paper.

## Novelty

Novelty is not claimed explicitly. The proposal is to choose the model by forecast horizon: SARIMA over short intervals, tuned XGBoost over long ones; the method is packaged as a class of Python programs.

## Heuristics

- **[explicit]** If the MUF forecast horizon is shorter than 25 minutes — use SARIMA, and for longer horizons XGBoost with tuned parameters, because at such horizons SARIMA gives on average R² 0.99 and MAE 0.001 MHz.
- **[explicit]** If one and the same series is forecast — absolute metrics (MAE, RMSE) suffice, because relative ones are not needed.
- **[explicit]** If the series has gaps and anomalous samples — interpolate them before training the models.
- **[reconstructed]** If model quality depends on the horizon — compute the error for each horizon separately and switch models where the error curves cross.
- **[reconstructed]** If XGBoost has tunable parameters — tune them rather than keep the defaults, because the summary names the tuned version as best.

**In one sentence:** The author proposes forecasting the MUF up to 75 minutes ahead with SARIMA over short intervals and tuned XGBoost over long ones, and reports an average error of 0.23 MHz in MAE for this hybrid.
