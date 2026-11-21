---
title: "Study of applicability of LSTM neural networks for predicting the characteristics of short-wave communication channels"
pair: lstm-kv-kanaly
lang: en
date: 2026-11-21
translation_of: 2026-11-21-lstm-kv-kanaly.md
summary: "The structure of an LSTM network was chosen with Keras Tuner and a Bayesian optimiser and then tested on one-day MUF forecasts for the Cyprus — Yoshkar-Ola path on datasets of 57 and 99 days. R² is 0.94–0.98 for the homogeneous dataset and 0.74–0.97 for the heterogeneous one, while an MAE below 1 MHz was obtained only in part of the periods."
paper_title: "Study of applicability of LSTM neural networks for predicting the characteristics of short-wave communication channels"
paper_authors: "Ryabova N.V., Konkin N.A., Elchaninova A.S."
paper_year: 2024
paper_date: "2024"
paper_venue: "VII Scientific Forum “Telecommunications: Theory and Technologies” TTT-2024. Proceedings of the XXI International Scientific and Technical Conference, Samara, pp. 71–72"
paper_link: "https://www.elibrary.ru/item.asp?id=75254072"
tags: [ionosphere, hf-channel, MUF, LSTM-network, short-term-forecast, hyperparameter-tuning]
---

## Problem and relevance

Modern diagnostics of short-wave channels use software-defined radio systems and artificial intelligence for data processing. For reliable communication, a short-term forecast of the time series of the maximum usable frequency (MUF) is important.

## Aim and hypothesis

The aim is to synthesise a neural network for short-term forecasting of MUF series and to test its applicability. No hypothesis is stated explicitly; in substance the paper tests that an LSTM network with an automatically chosen structure forecasts the MUF with high accuracy.

## Materials and methods

The experiment runs in several stages. First the data are processed: binary data are collected, the MUF is calculated and time series are prepared. Two datasets are formed for the mid-latitude path Cyprus — Yoshkar-Ola: a homogeneous dataset No. 1 of 57 days (50 for training, 7 for testing) and a heterogeneous dataset No. 2 of 99 days (89 for training, 10 for testing).

The LSTM structure is then synthesised with the Keras Tuner library with a Bayesian optimiser. The five best models are compared by mean absolute error (MAE) to pick the most effective structure. Its accuracy is assessed on the test sample: a one-day forecast, then an analysis by R², mean absolute percentage error (MAPE), MAE and RMSE.

## Results

In dataset No. 1 two periods stand out with the lowest error, where the MAE is below 1 MHz. In dataset No. 2 three periods gave an MAE “within 1 MHz”. In Fig. 1 the test intervals are shown day by day: 01.03.2023 to 07.03.2023 for dataset No. 1 and 31.03.2023 to 09.04.2023 for dataset No. 2. According to the English abstract, R² ranges from 0.94 to 0.98 for the homogeneous dataset and from 0.74 to 0.97 for the heterogeneous one. The Russian text gives no R² values, nor MAE and RMSE values for the remaining days.

## Authors' conclusions

The values obtained indicate high forecast accuracy on both datasets, which, in the authors' view, confirms the effectiveness of the methods and of the LSTM model for short-term MUF forecasting.

## Limitations

The structure of the chosen network (number of layers and neurons, input window length), the features and the optimiser settings are not described. An MAE below 1 MHz was reached in two periods out of seven in one dataset and “within 1 MHz” in three out of ten in the other, so the conclusion of high accuracy for the whole set rests on incomplete data. There is no comparison with other models or with a simple “same as yesterday” forecast. One path and the period of March–April 2023 are covered. The lower bound of R² for the heterogeneous dataset, 0.74, is clearly lower than for the homogeneous one; the paper does not analyse the reason.

## Novelty

The paper does not claim novelty explicitly. In substance it describes the use of automatic structure selection for an LSTM network in one-day MUF forecasting on two datasets with different trend behaviour.

## Heuristics

- **[reconstructed]** If the structure of a neural network is not known in advance — choose it with a Bayesian optimiser (Keras Tuner) and compare several best structures by MAE, because the choice then does not depend on manual tuning.
- **[reconstructed]** If MUF series differ in the homogeneity of their trend — test the model on both types of series, because quality drops on the heterogeneous dataset (R² down to 0.74).
- **[reconstructed]** If forecast quality is described by the share of good periods — report metric values for every day, because otherwise the claim of accuracy cannot be checked.

**In one sentence:** An LSTM network with an automatically chosen structure forecasts the MUF one day ahead with R² of 0.94–0.98 on a homogeneous and 0.74–0.97 on a heterogeneous dataset, but an MAE below 1 MHz was obtained only in part of the periods.
