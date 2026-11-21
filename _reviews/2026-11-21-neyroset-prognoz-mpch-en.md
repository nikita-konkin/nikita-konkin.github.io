---
title: "Development of a Methodology for Predicting the Maximum Usable Frequency of HF Communication Channels Based on a Neural Network Approach"
pair: neyroset-prognoz-mpch
lang: en
date: 2026-11-21
translation_of: 2026-11-21-neyroset-prognoz-mpch.md
summary: "For the Cyprus — Yoshkar-Ola path (2.6 thousand km), networks of LSTM and Dense layers were synthesized in Keras Tuner with three optimizers (RandomSearch, GridSearch, Bayesian) to forecast the MUF one day ahead over 10 one-day periods. Bayesian optimization was judged best: on average MAE 1.173 MHz, RMSE 1.529 MHz, R² 0.939, MAPE 0.058."
paper_title: "Development of a Methodology for Predicting the Maximum Usable Frequency of HF Communication Channels Based on a Neural Network Approach"
paper_authors: "Ryabova N.V., Konkin N.A., Elchaninova A.S."
paper_year: 2024
paper_date: "2024"
paper_venue: "Infocommunication and Radio Technologies, 2024, vol. 7, no. 4, pp. 691–705"
paper_link: "https://www.elibrary.ru/item.asp?id=68916484"
tags: [HF-link, MUF, neural-network, LSTM, hyperparameter-tuning, bayesian-optimization]
---

## Problem and relevance

The maximum usable frequency (MUF) is the upper limit of the working band of an HF link; it is used to estimate the transparency band and the optimum working frequencies. Because the ionosphere varies, these quantities are random and dynamic, so a radio forecast of temporal trends in the characteristics of the links is needed. The authors earlier forecast the MUF with machine-learning methods (XGBoost, a SARIMA and XGBoost hybrid); here the possibilities of neural networks are examined.

## Aim and hypothesis

The aim is a methodology for synthesizing neural network structures for short-term forecasting of MUF time series. The models are compared by R², MAPE, MAE and RMSE. No hypothesis is stated explicitly; in substance the paper tests that the choice of optimizer affects the structure of the network and the forecast accuracy.

## Materials and methods

The data are a MUF series computed from binary oblique-sounding data by an active HF radio sensor, mid-latitude, the Cyprus — Yoshkar-Ola path 2.6 thousand km long. The dataset covers 99 days (28,512 samples): 89 days for training, 1 day for the test, and 9 more days for checking forecast accuracy, i.e. 10 one-day forecast periods. There are five predictors: shift values (differences of the series with a shift of one and two samples), minutes, hours and day of the year. Stationarity was checked with the augmented Dickey — Fuller test: a statistic of −36.59 at a one-percent critical value of −3.43; the authors conclude that the series is stationary with 99 % confidence. Separately the authors note a nonstationary trend in the test part (mean change of the expectation between days 5 %, peak 12 %).

The structure search used the optimizers RandomSearch, GridSearch and BayesianOptimizator; for each, the 10 best models were saved and the metrics were computed on the test sample. Each forecast period has its own best model, and the published metrics combine the forecasts of the best of ten models of each optimizer. A result is considered good if within the confidence interval of the MUF course (1.92 MHz), and excellent if within 1 MHz.

## Results

Ranges over the 10 periods. RandomSearch: MAE 0.84–2.13 MHz, R² 0.74–0.97; MAE below 1 MHz in one period. GridSearch: MAE 1.07–2.82 MHz, R² 0.53–0.96; MAE above 1 MHz in all periods. Bayesian optimization: MAE 0.84–1.71 MHz, R² 0.87–0.98; MAE below 1 MHz in four periods.

Averages. Bayesian: MAE 1.173 MHz, RMSE 1.529 MHz, R² 0.939, MAPE 0.058. Random search: 1.419 MHz, 1.788 MHz, 0.918, 0.068. Grid search: 1.723 MHz, 2.239 MHz, 0.863, 0.082. Compared with random search, Bayesian optimization raised R² by 2.2 % and lowered MAE by 17.3 %, RMSE by 14.5 % and MAPE by 14.7 %. For Bayesian optimization, only in the first period does RMSE leave the confidence interval; for GridSearch RMSE reaches 3.77 MHz and for RandomSearch 2.77 MHz.

The structures differ. GridSearch gives simple networks: one LSTM layer and an output Dense layer with the elu activation, 1–5 neurons per layer. Bayesian optimization gives 2–4 LSTM layers, 1–8 Dense, 4–7 Dropout, 33 to 487 neurons per layer, and the activations selu, elu, gelu. Random search gives 1–3 LSTM layers, 1–8 Dense, 13 to 505 neurons per layer, and the activations selu and elu.

## Authors' conclusions

A methodology for automatic tuning of hyperparameters (synthesis) of neural networks for short-term MUF forecasting has been developed. Bayesian optimization is the most effective, and the forecast errors lie within the average confidence interval of 1.92 MHz. For high accuracy one needs optimizers that create more complex and diverse structures (Bayesian or random search); for exploratory analysis RandomSearch will do. The methodology, the authors say, shortens training time at a given accuracy and convergence coefficient.

## Limitations

The authors do not discuss limitations. From the outside: one path and 99 days, the dates are not given; there are 10 forecast periods, no statistical test of the differences between optimizers, and the R² ranges of Bayesian and random search overlap. The full initial ranges and settings of the search, the number of epochs, the learning rate and the series step are not given. There is no comparison with the models from the authors' earlier work (XGBoost, SARIMA). The claim of shorter training time is not supported by training time measurements. The mean MAE of the Bayesian model (1.173 MHz) is above the 1 MHz “excellent” threshold. The values by period are given in figures.

## Novelty

The paper does not claim novelty explicitly. In substance, it proposes a methodology for synthesizing LSTM and Dense networks for one-day MUF forecasting and compares three Keras Tuner optimizers by forecast accuracy and by the structure of the models they produce.

## Heuristics

- **[explicit]** If the highest MUF forecast accuracy is needed — choose an optimizer that builds complex and diverse structures (Bayesian or random search), because such networks adapt better to different forecast periods; RandomSearch is enough for exploration.
- **[explicit]** If a series is being prepared for forecasting — check stationarity with the Dickey — Fuller test, because a stationary series is preferable for forecasting.
- **[explicit]** If the influence of temporal trends must be removed — feed the model differences of the series with a shift of 1 and 2 samples, because attention then falls on changes within the series.
- **[explicit]** If forecast quality is to be judged for communication purposes — compare RMSE and MAE with the confidence interval of the MUF course (1.92 MHz) and with the 1 MHz threshold.
- **[reconstructed]** If a network-tuning method is being chosen — compare it over many forecast periods and look at the spread, not only the mean, because the minimum R² is 0.87 for Bayesian optimization, 0.74 for random search and 0.53 for grid search.

**In one sentence:** On 10 one-day MUF forecasts for the Cyprus — Yoshkar-Ola path, networks synthesized by Bayesian optimization with the Keras Tuner library gave on average MAE 1.173 MHz and R² 0.939 and were more accurate than those from random and grid search, although the sample is small and there is no comparison with other models.
