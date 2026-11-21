---
title: "Research of the neural network of LSTM type for predicting TEC of a transionospheric radio channel"
pair: lstm-transionosfernyy-kanal
lang: en
date: 2026-11-21
translation_of: 2026-11-21-lstm-transionosfernyy-kanal.md
summary: "Three LSTM architectures are compared for forecasting TEC from the ELHV station data for 291 days of 2021. The most accurate were architecture No. 2 at 20 epochs (MAPE from 0.146 to 0.391) and architecture No. 3 at 100 epochs (MAPE from 0.172 to 0.390)."
paper_title: "Research of the neural network of LSTM type for predicting TEC of a transionospheric radio channel"
paper_authors: "Elchaninova A.S., Konkin N.A., Chernov A.A."
paper_year: 2023
paper_date: "2023"
paper_venue: "VI Scientific Forum “Telecommunications: Theory and Technologies” TTT-2023. Proceedings of the XXV International Scientific and Technical Conference, Kazan, pp. 129–131"
paper_link: "https://www.elibrary.ru/item.asp?id=65241412"
tags: [ionosphere, TEC, transionospheric-channel, LSTM-network, network-architecture, GNSS]
---

## Problem and relevance

According to the English abstract, forecasting the total electron content (TEC) plays an important role in diagnosing the system characteristics of a radio channel. To improve forecast accuracy, the task of selecting an LSTM neural network model is considered.

## Aim and hypothesis

The aim is to choose an LSTM architecture for TEC forecasting. To this end the literature on neural-network forecasting of time series was analysed. No hypothesis is stated explicitly; in substance the paper tests that forecast accuracy depends on the architecture and the number of epochs.

## Materials and methods

Three architectures are considered: No. 1 — three LSTM layers and three Dense layers; No. 2 — one LSTM layer and five Dense layers; No. 3 — two LSTM layers and two Dense layers. The output Dense layer has one neuron in all cases. The data are navigation data of the ground satellite station ELHV (Elkhovka) for 291 days of 2021. Forecast accuracy was assessed by the mean absolute percentage error (MAPE).

## Results

The most accurate forecast came from architecture No. 2 at 20 epochs, with MAPE ranging from 0.146 to 0.391, and architecture No. 3 at 100 epochs, with MAPE ranging from 0.172 to 0.390. Architecture No. 2 raises the mean coefficient of determination by 0.043 relative to architecture No. 3. Fig. 1 shows part of the TEC forecast results by the MAPE metric for 10 days.

## Authors' conclusions

The model of the second architecture at 20 epochs and the model of the third architecture at 100 epochs have the greatest accuracy. The second-architecture model also gives a somewhat higher mean R².

## Limitations

The results of architecture No. 1 and the values at other numbers of epochs are not given. The paper does not say over what the MAPE ranges are taken (days, runs or other splits) or in what form MAPE is expressed. R² values are not given, only the difference of 0.043. The number of neurons in the layers, the input window length, the forecast horizon, the split into training and test parts and the features are not described. There is no comparison with other types of models or with a simple forecast. One station and one year are used.

## Novelty

The paper does not claim novelty explicitly. In substance it compares three LSTM architectures and two numbers of epochs on TEC forecasting at one station.

## Heuristics

- **[reconstructed]** If an architecture is chosen for a TEC series — compare several structures (number of LSTM and Dense layers) at different numbers of epochs, because the best structure may reach its quality at a different amount of training.
- **[reconstructed]** If two architectures give similar accuracy at different numbers of epochs — compare them with the number of epochs in mind, because architecture No. 2 at 20 epochs does not trail architecture No. 3 at 100 epochs.
- **[reconstructed]** If quality is given as a range — state what data it is taken over, because otherwise it cannot be compared with other work.

**In one sentence:** Of three LSTM architectures, the most accurate TEC forecast for the ELHV station came from No. 2 at 20 epochs (MAPE from 0.146 to 0.391) and No. 3 at 100 epochs (from 0.172 to 0.390), with the first better by 0.043 in mean R².
