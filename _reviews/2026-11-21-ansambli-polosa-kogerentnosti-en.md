---
title: "Selection of ensemble machine learning models for predicting the coherence band of trans-ionospheric communication channels"
pair: ansambli-polosa-kogerentnosti
lang: en
date: 2026-11-21
translation_of: 2026-11-21-ansambli-polosa-kogerentnosti.md
summary: "XGBoost, AdaBoost and gradient boosting (GBR) forecast the coherence band of a transionospheric channel from a 270-day GLONASS series at a 30-minute step for spring, summer and autumn. AdaBoost is, by the authors' estimate, the most accurate: R² 0.93 in spring, 0.83 in summer and 0.92 in autumn, at an MAE of 8.9, 16 and 15 MHz."
paper_title: "Selection of ensemble machine learning models for predicting the coherence band of trans-ionospheric communication channels"
paper_authors: "Antropova E.M., Konkin N.A."
paper_year: 2023
paper_date: "2023"
paper_venue: "All-Russian Open Armand Readings “Modern Problems of Remote Sensing, Radar, Wave Propagation and Diffraction”, Murom, pp. 275–283"
paper_link: "https://www.elibrary.ru/item.asp?id=54509563"
tags: [ionosphere, transionospheric-channel, coherence-band, ensembles, AdaBoost, GLONASS]
---

## Problem and relevance

The values of the coherence band of transionospheric communication channels form a time series. The authors turn to machine learning because it processes a series from the input data rather than from a mathematical model known in advance. In the works they reviewed, ensemble methods were the most popular. The coherence band, as the conclusion puts it, sets the limiting frequency band in which a satellite-communication signal has minimal loss and distortion.

## Aim and hypothesis

The aim is to select ensemble machine-learning models for forecasting time series of the coherence band. The tasks are to develop a method for short-term (within a day) forecasting on several models with subsequent comparison, to create a software package in Python, and to determine the more accurate algorithm by MAE and R². No hypothesis is stated explicitly; in substance three ensemble models are compared and the best is sought.

## Materials and methods

The data for computing the coherence band come from GLONASS navigation data, which the method collects by means of the SmartNet reference-station network; the authors attribute the series used to a Leica GR30 station in Yoshkar-Ola. The data are stored in RINEX format on the university server, and the computed values in the department's local database. The series spans 270 days at a 30-minute step, 12,960 values. Erroneously computed values and outliers were interpolated and the series was approximated.

The models are XGBoost, AdaBoost and gradient boosting (Gradient Boosting Regression, GBR). Additional independent features: hour, day of month, quarter, month, day of year, day, week of year. Three seasons are shown: spring, summer, autumn. The confidence interval of the series is built with a sliding window with a step of two samples, the step chosen from the autocorrelation function of the series. The metrics are MAE and R²; a model with R² above 0.8 is considered sufficiently accurate.

## Results

Spring: confidence interval 21 MHz; MAE of XGBoost 11 MHz, AdaBoost 8.9, GBR 9.6; R² 0.92, 0.93 and 0.93. Summer: interval 16 MHz; MAE 21, 16 and 19 MHz; R² 0.77, 0.83 and 0.59. Autumn: interval 26 MHz; MAE 15, 15 and 17 MHz; R² 0.87, 0.92 and 0.89.

By the authors' estimate, AdaBoost is more accurate in MAE by 1.2 MHz in spring, 4.2 MHz in summer and 1.9 MHz in autumn, and in R² by 0.01, 0.14 and 0.04 (relative to what, the text does not say). In spring and autumn the MAE of all models fits inside the confidence interval, in summer only that of AdaBoost does. Only AdaBoost passes the threshold R² above 0.8 in all three seasons; in spring and autumn all three models pass it.

## Authors' conclusions

The models have been selected: the authors call AdaBoost more accurate on all parameters for all three seasons. The authors attribute the summer errors exceeding the interval to the noisiness of the seasonal series. The method makes it possible to forecast the coherence band, which sets the limiting frequency band of a transionospheric signal.

## Limitations

Winter is not covered and no reason is given. Model parameters, the training/test split and the in-day forecast horizon are not stated; the 270-day period is not dated. The data come from one station. The differences between models are small (0.01 in R² in spring), and there is no significance estimate or repeated runs. The phrase “more accurate on all parameters” does not quite match the values given: in spring AdaBoost and GBR share the best R² (0.93), in autumn AdaBoost and XGBoost share the best MAE (15 MHz). The mean level of the coherence band is not given, so the relative error (MAE 8.9–21 MHz) cannot be judged. The attribution of summer errors to noise is not tested. There is no baseline forecast for comparison.

## Novelty

Not claimed explicitly. The abstract names a result: a Python program for selecting machine-learning models for forecasting the coherence band; in substance three ensemble models are compared.

## Heuristics

- **[explicit]** If a window step is needed for the confidence interval of a series — take it from the autocorrelation function of the series.
- **[explicit]** If the series carries time stamps — add calendar features (hour, day of month, quarter, month, day of year, week of year) to raise model accuracy.
- **[explicit]** If a criterion of sufficient accuracy is needed — treat a model with R² above 0.8 as sufficiently accurate.
- **[reconstructed]** If model errors are compared with the width of the series' confidence interval — note whether the model's MAE leaves the interval, because this shows whether the model's error exceeds the spread of the series itself; here, in summer, only the MAE of AdaBoost stays inside it.
- **[reconstructed]** If model quality is assessed by season — look also at the spread between models, because it is largest in summer (R² from 0.59 to 0.83).

**In one sentence:** On a 270-day series of the coherence band AdaBoost reached R² of 0.93, 0.83 and 0.92 in spring, summer and autumn and, by the authors' estimate, proved more accurate than XGBoost and gradient boosting.
