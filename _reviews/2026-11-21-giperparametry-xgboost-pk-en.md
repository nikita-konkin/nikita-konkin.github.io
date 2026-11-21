---
title: "Tuning hyperparameters of the XGBoost machine-learning model to forecast the coherence bandwidth"
pair: giperparametry-xgboost-pk
lang: en
date: 2026-11-21
translation_of: 2026-11-21-giperparametry-xgboost-pk.md
summary: "Twenty sets of hyperparameters of the XGBoost model were tuned on a twenty-day coherence-bandwidth dataset with a 30-minute step. The coefficient of determination rose from 0.658 without tuning to 0.759 with the colsample_bytree hyperparameter, and the mean absolute error fell from 17,989,720.99 to 14,316,831.65 Hz."
paper_title: "Tuning hyperparameters of the XGBoost machine-learning model to forecast the coherence bandwidth"
paper_authors: "Antropova E.M. (supervisor — Konkin N.A.)"
paper_year: 2023
paper_date: "2023"
paper_venue: "Scientific Progress — Creativity of the Young, 2023, no. 2, pp. 3–5"
paper_link: "https://www.elibrary.ru/item.asp?id=54740355"
tags: [machine-learning, XGBoost, hyperparameters, coherence-bandwidth, transionospheric-channel, time-series]
---

## Problem and relevance

Machine learning solves data-processing tasks, including those on time series. To make models work better, their hyperparameters are adapted; among the known ones the paper lists max_depth, min_child_weight, gamma, colsample_bytree and eta.

## Aim and hypothesis

The aim is to develop a method for tuning the hyperparameters of the XGBoost model to forecast the coherence bandwidth of a transionospheric line. The tasks are to develop a method for short-term (within one day) forecasting of the coherence bandwidth and to write supporting Python scripts. No hypothesis is stated explicitly.

## Materials and methods

XGBoost is based on decision trees and extreme gradient boosting; the model trains on supervised data xi and forecasts the target variable yi. The objective function consists of the training loss and a regularization term. The experiment ran on a twenty-day coherence-bandwidth dataset with a 30-minute step; training and test samples were prepared. The methods name the root-mean-square error and the mean absolute error, while the plot and the conclusion report R² and the mean absolute error.

## Results

A forecast without hyperparameter tuning and 20 sets with hyperparameters were obtained. Without tuning the coefficient of determination R² is 0.658 and the mean absolute error is 17,989,720.99 Hz. With tuning, the best values — R² 0.759 and a mean absolute error of 14,316,831.65 Hz — were obtained with the colsample_bytree hyperparameter.

## The author's conclusions

The XGBoost hyperparameters were tuned to raise the forecasting accuracy for coherence-bandwidth time series of transionospheric channels. The colsample_bytree hyperparameter gives the best result.

## Limitations

The concrete values of the hyperparameters in the 20 sets are not given — only the best one (colsample_bytree) is named. The root-mean-square error mentioned in the methods is not reported numerically in the results. The mean-absolute-error figures, on the order of 14–18 million hertz, are given without explaining the units against the expected coherence bandwidth, and the text calls the “highest” error values those that are in fact lower than the initial ones. The train/test split is not described.

## Novelty

No novelty is claimed explicitly. In substance the paper proposes a method for tuning XGBoost hyperparameters to forecast the coherence bandwidth, and Python scripts that implement it.

## Heuristics

- **[explicit]** If a model trained without hyperparameter tuning is not accurate enough — tune the hyperparameters, because this raises R² and lowers the mean absolute error.
- **[reconstructed]** If a hyperparameter must be chosen for a first check — start with colsample_bytree, because the best reported result is tied to it; the paper has no separate assessment of how strongly each hyperparameter matters.
- **[reconstructed]** If model variants are compared — assess them by R² and the mean absolute error together, because one metric can change independently of the other.

**In one sentence:** Tuning the XGBoost hyperparameters on a twenty-day coherence-bandwidth series raises R² from 0.658 to 0.759 and lowers the mean absolute error to 14,316,831.65 Hz, with colsample_bytree giving the best result.
