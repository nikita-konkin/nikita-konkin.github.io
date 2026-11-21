---
title: "Forecasting coherence bands of a transionospheric radio channel for the mineral resources sector of Sakhalin Oblast during seismic activity"
pair: polosy-kogerentnosti-sakhalin
lang: en
date: 2026-11-21
translation_of: 2026-11-21-polosy-kogerentnosti-sakhalin.md
summary: "Three boosting ensemble algorithms are compared for forecasting the coherence band from a 28-day half-hourly series of the SAHA station (Sakhalinsk). XGBRegressor averages R² 0.769, MAE 7.86 MHz and RMSE 8.96 MHz; GradientBoostingRegressor improves R² by 0.8 %, MAE by 3 % and RMSE by 13.5 %."
paper_title: "Forecasting coherence bands of a transionospheric radio channel for the mineral resources sector of Sakhalin Oblast during seismic activity"
paper_authors: "Elchaninova A.S. (supervisor — Konkin N.A.)"
paper_year: 2023
paper_date: "2023"
paper_venue: "Topical Issues of Subsoil Use. Abstracts of the XIX International Forum-Contest of Students and Young Researchers, Saint Petersburg, pp. 39–41"
paper_link: "https://www.elibrary.ru/item.asp?id=54518465"
tags: [coherence-band, transionospheric-channel, TEC, seismic-activity, machine-learning, boosting]
---

## Problem and relevance

Managing mineral resources enterprises requires transionospheric communication. Earthquakes in seismically active regions change the total electron content (TEC), which narrows the coherence bands and degrades the transmission of information. The author proposes forecasting coherence bands with the most accurate machine-learning algorithm.

## Aim and hypothesis

The aim is to test a method of forecasting coherence bands for Sakhalin. No hypothesis is stated explicitly; in substance the paper tests which of three algorithms is more accurate and how much training data is needed.

## Materials and methods

The data come from the ground station SAHA (Sakhalinsk): a 28-day set with a half-hour step. The dependent variable is the coherence band; the independent ones are time and its derivatives. The test part did not change and was 1 day (48 samples), while the training part grew from 2 to 27 days. AdaBoostRegressor, GradientBoostingRegressor and XGBRegressor were trained — boosting ensemble models. Quality was assessed by R², the mean absolute error (MAE) and the root-mean-square error (RMSE).

## Results

GradientBoostingRegressor and XGBRegressor are the most accurate. For XGBRegressor the averages are R² 0.769, MAE 7.86 MHz, RMSE 8.96 MHz. GradientBoostingRegressor raises R² by 0.8 % and lowers MAE by 3 % and RMSE by 13.5 %. The errors lie within the mean confidence interval of 11.8 ∙ 10⁶, whose unit is not stated. According to the cross-analysis, the threshold accuracy is reached at 67 % of the dataset; the author links this to seasonal variations.

## The author's conclusions

The method has been tested for Sakhalin. On averaged indicators GradientBoostingRegressor is more accurate than XGBRegressor. To improve the result, hyperparameters should be tuned and additional predictors of the series created.

## Limitations

Hyperparameter tuning is not described in the method, and the only features named are time and its derivatives; the author recommends both tuning and additional predictors. The paper gives no dates for the series and no information on whether earthquakes occurred in that period, so the link between the forecast and seismicity is not demonstrated. The caption of Fig. 1 reports results of three algorithms “for 10 days”; it does not show that the figure plots the metrics against the size of the training part, and the 67 % threshold is stated only in the conclusion. The unit of the mean confidence interval is not stated. The difference between the best models is small, and neither spread nor repeated runs are given; the data are from one station and there is no baseline forecast for comparison.

## Novelty

The paper does not claim novelty explicitly. Its contribution is a test of coherence-band forecasting with three boosting algorithms on data from a seismically active region.

## Heuristics

- **[explicit]** If the coherence band depends on time — take it as the dependent variable and time and its derivatives as the independent ones, because the task reduces to regression.
- **[reconstructed]** If you need to know how much history is enough — keep the test part fixed (one day) and vary the training part, because errors are then comparable.
- **[explicit]** If accuracy is insufficient — tune the hyperparameters and add predictors of the series.

**In one sentence:** On 28 days of SAHA station data, boosting models forecast the coherence band, and GradientBoostingRegressor is more accurate than XGBRegressor (whose RMSE is 8.96 MHz, while the former is lower by 13.5 %), but the paper does not show the link with seismicity.
