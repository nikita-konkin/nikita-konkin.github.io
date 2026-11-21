---
title: "Analysis of the influence of shift predictors on the accuracy of forecasting the MUF of HF communication lines"
pair: sdvigovye-prediktory-tezisy
lang: en
date: 2026-11-21
translation_of: 2026-11-21-sdvigovye-prediktory-tezisy.md
summary: "On MUF forecasting data from a recurrent neural network, the author tests how shift features (lags of 0, 1, 2 and 3 days) and the season affect accuracy. In winter and autumn the best result comes with no shift and with a 2-day shift (MAPE 0.095–0.101), in spring with a 3-day shift (MAPE 0.091), in summer with a 2-day shift (MAPE 0.101)."
paper_title: "Analysis of the influence of shift predictors on the accuracy of forecasting the MUF of HF communication lines"
paper_authors: "Elchaninova A.S. (supervisor — Konkin N.A.)"
paper_year: 2025
paper_date: "2025"
paper_venue: "Applied Electrodynamics, Photonics and Living Systems — 2025. Abstracts of the XII International Youth Conference, Kazan, pp. 554–556"
paper_link: "https://www.elibrary.ru/item.asp?id=83253100"
tags: [ionosphere, hf-channel, MUF, machine-learning, recurrent-neural-networks, forecasting]
---

## Problem and relevance

An accurate forecast of the maximum usable frequency (MUF) of short-wave (HF) communication links is needed to optimise the operation of radio systems and improve the quality of communication. Recurrent neural networks (RNNs) have proved an effective tool for forecasting time series thanks to their ability to capture complex temporal dependencies. The paper tests how shift features and the season affect the accuracy of such a forecast.

## Aim and hypothesis

The aim is to analyse the accuracy of an RNN forecast of the MUF depending on the shift features used and on seasonal factors. No hypothesis is stated explicitly; in substance the paper tests that the choice of a series lag changes forecast accuracy and that the optimal lag depends on the season.

## Materials and methods

The forecast was made with a recurrent neural network on the basis of horizontal-forecasting data. The features were combinations of shift values (lags) of the time series: a forecast without a shift, and forecasts with shifts of 1, 2 and 3 days. Quality was assessed with the metrics root mean square error (RMSE) and mean absolute percentage error (MAPE). The network architecture, the data volume, the training parameters and the train/test split are not described in the text.

## Results

By the MAPE and RMSE metrics averaged over 7 days, the highest accuracy in winter and autumn is reached without a shift and with a 2-day shift (MAPE 0.095–0.101), in spring with a 3-day shift (MAPE 0.091), and in summer with a 2-day shift (MAPE 0.101). The numerical RMSE values are not given in the text.

## The author's conclusions

The author concludes that the optimal shift feature depends on the season: in winter and autumn it is zero or two days, in spring three days, in summer two days. The work was supported by a Russian Science Foundation grant (project No. 23-19-00145).

## Limitations

The RNN architecture, the volume and period of the data, the train/test split and the forecast horizon are not given. Only MAPE values are reported; RMSE is mentioned but not stated numerically. The differences in MAPE between the best variants for the different seasons are small (0.091–0.101), and their statistical significance was not assessed.

## Novelty

The paper does not claim novelty explicitly. In substance it compares the influence of different shift features and of the season on the accuracy of an RNN forecast of the MUF.

## Heuristics

- **[explicit]** If shift features are being chosen for an MUF forecast — choose the shift separately for each season, because the optimal lag differs between winter and autumn (0 or 2 days), spring (3 days) and summer (2 days).
- **[reconstructed]** If the shifts compared give close MAPE values — assess the significance of the differences, because the spread of 0.091–0.101 may be noise rather than an effect of the shift.
- **[reconstructed]** If only MAPE is reported — add the absolute error in the units of the quantity, because MAPE does not show how large the error is in MHz.

**In one sentence:** The optimal shift feature for an RNN forecast of the MUF depends on the season: 0 or 2 days in winter and autumn (MAPE 0.095–0.101), 3 days in spring (MAPE 0.091), and 2 days in summer (MAPE 0.101).
