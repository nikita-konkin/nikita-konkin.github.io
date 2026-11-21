---
title: "Comparative analysis of regression and ensemble machine learning methods for the purpose of MUF forecasting"
pair: regressiya-ansambli-mpch
lang: en
date: 2026-11-21
translation_of: 2026-11-21-regressiya-ansambli-mpch.md
summary: "On a dataset of 47 days at a 5-minute step, Lasso, Ridge and Elastic Net regressions and XGBoost with ten tuned parameters are compared, with a 7-day test interval and a training interval of 12 to 40 days. Tuned XGBoost is more accurate on all metrics: on average a gain of 1 MHz in RMSE, 0.07 in R² and 0.07 in MAPE."
paper_title: "Comparative analysis of regression and ensemble machine learning methods for the purpose of MUF forecasting"
paper_authors: "Ryabova N.V., Konkin N.A., Chernov A.A., Ivanova N.V."
paper_year: 2023
paper_date: "2023"
paper_venue: "VI Scientific Forum “Telecommunications: Theory and Technologies” TTT-2023. Proceedings of the XXV International Scientific and Technical Conference, Kazan, pp. 18–20"
paper_link: "https://www.elibrary.ru/item.asp?id=65241331"
tags: [ionosphere, MUF, machine-learning, XGBoost, regularisation, forecasting]
---

## Problem and relevance

Forecasting the maximum usable frequency (MUF) makes it possible to diagnose (exploratory analysis) short-wave communication channels by identifying the availability band. The open question is how much machine-learning models of different complexity, with parameter tuning, differ in the accuracy of such a forecast.

## Aim and hypothesis

The aim is to assess the effectiveness of MUF forecasting by regression models and by the ensemble XGBoost model, with their parameters tuned. No hypothesis is stated explicitly; in substance the paper tests that tuned XGBoost is more accurate than the regressions.

## Materials and methods

Regression models with l1 and l2 regularisation: Lasso, Ridge and Elastic Net. The XGBoost parameters were optimised over ten items. For comparison, results of XGBoost and linear regression without parameter tuning are given. The dataset is 47 days at a 5-minute step, stated in the paper as 338,400 samples. The cross-analysis used a constant forecast (test) interval of 7 days and a changing training interval of 12 to 40 days in steps of 2 days. The metrics are the coefficient of determination R², the mean absolute relative error (MAPE) and the root mean square error (RMSE).

## Results

The tuned XGBoost model was more accurate on all metrics. On average, for each training-set size, it gains 1 MHz in RMSE, 0.07 in R² and 0.07 in MAPE. The dependence of the metrics on the number of days in the training set is shown in Fig. 1; the text gives no values for it.

## Authors' conclusions

In sum, the tuned XGBoost model is more accurate on all metrics. The English abstract only says that the effectiveness of MUF forecasting is studied for regression and ensemble models with parameter selection.

## Limitations

The paper does not say relative to which model the gain is calculated (the best regression or untuned XGBoost), and does not give the metric values for each model. The results of Lasso, Ridge and Elastic Net are not described separately. The path or station, the observation period, the features, the ten tuned parameters themselves and their values are not given. The figure of 338,400 samples does not agree with 47 days at a 5-minute step, ; the paper does not explain the discrepancy. The training size at which the gain is largest or smallest is not discussed.

## Novelty

The paper does not claim novelty explicitly. In substance it compares regularised regressions and XGBoost, tuned and untuned, on MUF forecasting at different training-set lengths.

## Heuristics

- **[reconstructed]** If MUF forecasting models are compared — vary the length of the training set (here from 12 to 40 days) at a constant test interval, because then it shows how accuracy depends on the volume of training.
- **[reconstructed]** If an ensemble model is compared with linear ones — tune the parameters of both the ensemble and the linear models (l1 and l2 regularisation), because otherwise the gain cannot be attributed to the model.
- **[reconstructed]** If a gain in a metric is reported — give the absolute values and the comparison base as well, because a difference alone does not show the quality of a forecast.

**In one sentence:** XGBoost with ten tuned parameters beats Lasso, Ridge, Elastic Net and linear regression on R², MAPE and RMSE (an average gain of 0.07, 0.07 and 1 MHz), but without the underlying metric values and without the path, dates and features.
