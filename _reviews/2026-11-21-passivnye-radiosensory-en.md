---
title: "Intelligent diagnostic system with a mode for predicting the parameters of broadband radio channels based on data from GNSS passive radio sensors"
pair: passivnye-radiosensory
lang: en
date: 2026-11-21
translation_of: 2026-11-21-passivnye-radiosensory.md
summary: "A recurrent LSTM neural network is applied to forecast the coherence bandwidth of a transionospheric radio channel from GNSS passive radio sensor data covering 261 days. The authors report a mean absolute percentage error below 5 % and a coefficient of determination above 89 %."
paper_title: "Intelligent diagnostic system with a mode for predicting the parameters of broadband radio channels based on data from GNSS passive radio sensors"
paper_authors: "Kislitsyn A.A., Ryabova N.V., Kislitsyna M.A., Konkin N.A."
paper_year: 2024
paper_date: "2024"
paper_venue: "BSHFF-2024. Interaction of Fields and Radiation with Matter. Proceedings of the XVIII Conference of Young Scientists, Irkutsk, pp. 265–267"
paper_link: "https://www.elibrary.ru/item.asp?id=73539250"
tags: [ionosphere, GNSS, TEC, coherence-bandwidth, LSTM-network, broadband-communication]
---

## Problem and relevance

Satellite communication passes through variable layers of the atmosphere and the ionosphere. According to the authors, intra-mode dispersion of the group delay in the channel hinders the broadband systems WGS (Wideband Global Satcom) and HTS (High Throughput Satellites), and the problem reduces to the variability of geophysical factors, above all the total electron content (TEC) of the ionosphere. Reliable methods for diagnosing and forecasting TEC and channel parameters are therefore needed.

## Aim and hypothesis

The aim is to develop intelligent methods for diagnosing the parameters of broadband transionospheric radio channels, with a forecasting mode based on artificial neural networks. No hypothesis is stated explicitly; in substance the paper tests that a recurrent LSTM network forecasts the coherence bandwidth accurately.

## Materials and methods

Diagnostics rely on passive radio sensors of global navigation satellite systems (GNSS) in the 1100…1610 MHz band. Data in RINEX format are converted, from phase and code measurements, into current TEC values (in TECU, 1 TECU = 10¹⁶ m⁻²), and from these the diurnal variations of the group-delay dispersion coefficient GDD and the current coherence bandwidth of the channel are obtained. In the formulas the factors are split into a geophysical and a frequency part; the second, the relative frequency RF, converts parameters from the reference frequency to any working frequency.

The system works in two modes: analysis (diagnostics and adaptation of the limiting channel bandwidth) and forecasting (a specialised LSTM network). Processing and training were done in Python with Keras and TensorFlow. The test used field-experiment data from transionospheric radio links: phase and code measurements over 261 days. The forecast was evaluated at horizons from one to seven days, and training the network took 20 epochs. The metrics are the mean absolute error (MAE), the coefficient of determination R² and the mean absolute percentage error (MAPE).

## Results

Fig. 2 of the paper shows the course of the coherence bandwidth during training, validation and forecasting. The text gives two numerical results: on the test sample MAPE is below 5 % and R² above 89 %. Exact metric values, their spread and their dependence on the horizon (from one to seven days) are not given, only the thresholds.

## Authors' conclusions

A method for diagnosing and forecasting the parameters of broadband transionospheric radio channels has been developed on the basis of an intelligent system with passive GNSS sensors. The system showed high forecast accuracy: MAPE below 5 % at R² above 89 %. The authors call the ability of the network to learn from experimental data a key element in optimising the operation of infocommunication systems.

## Limitations

The network architecture, the features, the length of the input window and the split of data into training, validation and test parts are not described. The radio links, the sensors and the observation period (apart from the number of days) are not named. Metrics are given as thresholds and are not separated by forecast horizon. There is no comparison with other models or with a simple baseline forecast, so the verdict “high accuracy” has no reference point. The claim about the role of the approach in optimising communication systems is not tested in the paper.

## Novelty

The authors call the approach new and speak of developing a method, but the paper does not say what exactly is new. In substance the contribution is the combination of passive GNSS-based diagnostics with a neural-network forecast of the coherence bandwidth.

## Heuristics

- **[explicit]** If channel parameters must be carried over from the reference frequency to another working frequency — split the expressions into a geophysical and a frequency factor and convert through the relative frequency RF, because the geophysical part is set through TEC by a single value at the reference frequency.
- **[reconstructed]** If the parameters of a broadband channel are governed by TEC — derive them from GNSS-based TEC rather than measuring the channel directly, because in the paper the channel parameters are computed from TEC obtained from passive GNSS sensor data.
- **[reconstructed]** If forecast quality is reported as thresholds — add metric values for each horizon, because accuracy at one day and at seven days can differ markedly.

**In one sentence:** A recurrent LSTM network applied to data from passive GNSS sensors (source measurements over 261 days) forecasts the coherence bandwidth of a transionospheric channel with MAPE below 5 % and R² above 89 %, but without exact values and without comparison to other models.
