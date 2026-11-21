---
title: "Investigation of the forecast accuracy of HF communication channel MUF depending on seasonal variations and lagged predictors"
pair: sdvigovye-prediktory-mpch
lang: en
date: 2026-11-21
translation_of: 2026-11-21-sdvigovye-prediktory-mpch.md
summary: "Recurrent neural networks (LSTM-MLP) forecast the MUF of an HF channel for up to 7 days with shifted (lagged) predictors of 0 to 3 days and in two data formats, horizontal and vertical, for February, May, August and November. The lowest averaged error of the horizontal structure is an RMSE of 1.760 MHz in November at a 2-day shift and 1.896 MHz in February at a 3-day shift; accuracy is higher where the partial autocorrelation of the series is higher."
paper_title: "Investigation of the forecast accuracy of HF communication channel MUF depending on seasonal variations and lagged predictors"
paper_authors: "Konkin N.A., Elchaninova A.S."
paper_year: 2025
paper_date: "2025"
paper_venue: "Radio Wave Propagation. Proceedings of the XXIX All-Russian Open Scientific Conference, Kazan, pp. 523–527"
paper_link: "https://www.elibrary.ru/item.asp?id=83020611"
tags: [ionosphere, hf-channel, MUF, recurrent-neural-networks, lagged-predictors, seasonality]
---

## Problem and relevance

The maximum usable frequency (MUF) determines the choice of the working band of ionospheric HF communication. Planning sessions needs an operational MUF forecast with a relative error of no more than 10 %. The ionosphere changes over the day and over the seasons. Physical models (ITU-R P.533, the REC533 method) do not capture local variations of the ionosphere, while statistical and neural methods need a lot of data to adapt to abrupt seasonal changes.

## Aim and hypothesis

The aim is to analyse how seasonal factors, shifted (lagged) predictors and the data format (h and v) affect the accuracy of MUF forecasts by recurrent neural networks. No hypothesis is stated explicitly; in substance the paper tests that shifted features raise accuracy where the series is strongly autocorrelated.

## Materials and methods

The source data are measured MUF values of HF channels over a long interval; the path, the period and the equipment are not given. The series was cleaned of noise and outliers and the missing samples were restored.

The data are arranged in two formats. In the horizontal (h) format the values of all predictors at one moment are recorded together. In the vertical (v) format each predictor carries a sequence of values over several previous steps. A shift is one day at a 5-minute step (288 samples); shifts from 0 to 3 were examined. The training sample is 18 days, the validation sample 1 day, the test sample 1 to 7 days.

The models are recurrent and fully connected networks (LSTM-MLP) with tuned numbers of layers, neurons and activation functions. The metrics are MAE, RMSE, MAPE and R². The periods are February, May, August and November. Seasonal differences are explained through partial autocorrelation (PACF; above 0.5 means strong correlation) and approximate entropy (ApEn; below 0.1 a stationary series, above 0.2 a complex non-stationary one).

## Results

The lowest error averaged over 7 days for the h structure, as the text of the paper gives it: February — RMSE 1.896 MHz, MAPE 0.100 at a 3-day shift; May — 2.161 MHz and 0.086 (3 days); August — 2.239 MHz and 0.095 (3 days); November — 1.760 MHz and 0.097 (2 days). For the v structure: February — 1.868 MHz and 0.090 (3 days); May — 2.183 MHz and 0.090 (1 day); August — 2.761 MHz and 0.114 (1 day); November — 2.995 MHz and 0.165 (2 days).

PACF lies at 0.604–0.804 (h) and 0.532–0.791 (v) in winter, and at 0.581–0.956 (h) and 0.185–0.830 (v) in autumn; in spring and summer it does not exceed 0.053. Averaged RMSE of the h structure: winter 1.896–1.938 MHz, autumn 1.750–1.896, spring 2.161–2.343, summer 2.191–2.634. For the v structure: winter 1.868–2.761, spring 2.183–3.244, summer 2.761–3.113, autumn 2.995–8.460 MHz; in autumn at a 1-day shift the accuracy is low.

## Authors' conclusions

Shifted features raise accuracy because they account for autocorrelation; features only weakly related to the current value may degrade it. For operational MUF forecasting, recurrent models on the horizontal structure with shifts (preferably 2–3 days) are advisable, especially in winter and autumn, when autocorrelation is high. The higher the PACF, the higher the model's accuracy when shifts are applied; the lower the PACF, the lower that accuracy.

## Limitations

The source and period of the data, the network architecture and the hyperparameters are not described. The result without shifts (0) is not given in numbers in the text, so the size of the gain from shifts cannot be judged from it. One month per season and one split were used. The link between PACF and accuracy is shown on four seasons, without a coefficient. The explanation of the autumn result for the v structure (“no correlation”) is not tested: PACF for the v structure in autumn lies in the range 0.185–0.830. The minima of the h structure in the text (2.239 MHz in summer and 1.760 MHz in autumn) do not match the lower bounds of the ranges in Table 1 (2.191 and 1.750 MHz); the paper does not explain this. The role of entropy is stated ambiguously: the abstract speaks of low entropy, the text of higher non-stationarity. MAPE values are given as fractions; the 10 % threshold is named in the introduction but not compared with the results.

## Novelty

The authors see novelty in the systematic treatment of seasonality, time shifts and data formats when training recurrent MUF forecasting models; they see practical value in more reliable planning of HF sessions.

## Heuristics

- **[explicit]** If the series is strongly autocorrelated in a season (PACF above 0.5) — add shifted features, because, in the authors' words, the higher the PACF, the higher the model's accuracy when shifts are applied.
- **[explicit]** If the forecast is needed in winter or autumn — use the horizontal data structure with shifts of 2–3 days.
- **[explicit]** If a new shift carries information only weakly related to the current value — do not add it, because it degrades the forecast.
- **[reconstructed]** If the properties of a season are not known in advance — compute the PACF and ApEn of the series before training to decide whether shifts are needed.
- **[reconstructed]** If data formats are compared — evaluate them separately by season, because the vertical structure gave an RMSE of up to 8.460 MHz in autumn but was comparable to the horizontal one in winter.

**In one sentence:** Shifted features and the horizontal data structure give a recurrent network its lowest averaged MUF forecast error in winter and autumn (RMSE 1.760–1.896 MHz), when the partial autocorrelation of the series is high.
