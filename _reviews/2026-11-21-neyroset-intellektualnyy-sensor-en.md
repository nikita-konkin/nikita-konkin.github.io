---
title: "Specialized Neural Network Integrated in Intelligent Sensor for Predicting the Parameters of Wideband Transionospheric Radio Channels"
pair: neyroset-intellektualnyy-sensor
lang: en
date: 2026-11-21
translation_of: 2026-11-21-neyroset-intellektualnyy-sensor.md
summary: "To forecast the coherence bandwidth of a transionospheric radio channel 1–7 days ahead from passive GNSS radio sensor data (261 days of measurements), an LSTM architecture was selected automatically: two recurrent layers, five fully connected layers and a fully connected output layer with one neuron. Averaged over a weekly period on the test sample, MAE is 18.2 MHz, R² 0.89, MAPE 6 %."
paper_title: "Specialized Neural Network Integrated in Intelligent Sensor for Predicting the Parameters of Wideband Transionospheric Radio Channels"
paper_authors: "Ivanov D.V., Kislitsyn A.A., Konkin N.A., Elchaninova A.S., Chernov A.A."
paper_year: 2023
paper_date: "2023"
paper_venue: "Vestnik of Volga State University of Technology. Ser.: Radio Engineering and Infocommunication Systems, 2023, no. 4 (60), pp. 50–63"
paper_link: "https://www.elibrary.ru/item.asp?id=59942296"
tags: [ionosphere, transionospheric-channel, coherence-bandwidth, neural-network, LSTM, GNSS]
---

## Problem and relevance

Wideband satellite communication systems need an advance estimate of the coherence bandwidth of a transionospheric radio channel: stable data transmission depends on it when the propagation medium varies. The authors write that existing methods of forecasting this bandwidth are often not accurate enough or demand large computing resources. The architecture of recurrent networks is not universal: the number of layers, neurons, activation and optimization functions has to be tuned to the particular series, and manual tuning is slow and inefficient.

## Aim and hypothesis

The aim is to develop methods of analyzing and forecasting the dynamics of coherence bandwidths of wideband transionospheric radio channels with artificial neural networks. No hypothesis is stated explicitly; in substance the paper tests that an automatically selected LSTM network gives an accurate forecast of the coherence bandwidth at a horizon of 1–7 days.

## Materials and methods

The coherence bandwidth is computed from the total electron content (TEC), which is obtained from phase and code measurements of navigation satellite signals in the 1100…1610 MHz band. The link to group-delay dispersion and the conversion to the working frequency are given by formulas (1)–(3), the reference frequency is 1 GHz.

The data are measurements of passive GNSS radio sensors over 261 days. Single gaps are interpolated and high-frequency variations are removed with the Hodrick — Prescott filter. The target series (the course of the coherence bandwidth) and nine predictors are formed: minutes, hours, day of the week, season, month number, day of the year, and coherence bandwidth values of neighboring stations. The validation sample is 10 % (29 days), the test sample is from 1 to 7 days, and the training sample is the remainder (247–254 days); a separate model is trained for each horizon. Hyperparameters were selected in Keras Tuner by Bayesian optimization: neurons in steps of 4, from 64 to 300 in LSTM layers and from 32 to 240 in Dense layers. The ten best models by MAPE were tested at horizons of 1–7 days.

## Results

The architecture found: input (9,1); LSTM with 260 and 184 neurons; five fully connected (Dense) layers with the SELU activation function with 184, 152, 152, 80 and 32 neurons; an output fully connected layer with one neuron; the Adam optimizer with a learning rate of 0.001. The accuracy in training and validation by MAPE was below 5 % (3.3 % on average). According to the text, training at horizons of 1–7 days takes 20 epochs on average; the spread of the error grows as the horizon approaches seven days.

The forecast accuracy falls within the confidence intervals for all horizons except six days. By R², the models for 1 and 6 days have medium accuracy (76 % on average) and the others high accuracy (94 % on average). Averaged over a weekly period on the test sample: MAE 18.2 MHz, R² 0.89, MAPE 6 %.

## Authors' conclusions

An approach to forecasting the coherence bandwidth has been developed; an algorithm of data preparation and training and a network structure have been created. In the authors' view the chosen architecture is optimal, highly accurate under intramode dispersion and anthropogenic noise, and makes it possible to adjust the parameters of satellite communication systems according to the forecast coherence bandwidth.

## Limitations

The authors do not name limitations directly. From the outside: the network was tested on one series of measurements over 261 days; the year, the stations and their number are not stated. During the search various structures were trained and evaluated, and ten promising models were selected by MAPE, but there is no separate comparison with an independent baseline architecture or method, so “optimal” is not backed by such a comparison. The sample sizes (training 247–254, validation 29, test 1–7 days) do not fit a series of 261 days, and the paper does not explain this. The test MAPE is 6 %, while the text says “below 5 %”. The number of epochs is given twice, differently: 300 was chosen at the tuning stage, while 20 on average is given for the trial of 1–7-day forecasts; the link between the stages is not explained. For horizons of 1 and 6 days R² is lower than for the others, and the reason is not explained. The range of coherence bandwidth values to which the MAE of 18.2 MHz refers is not given.

## Novelty

Novelty is not claimed explicitly; the authors write that an “approach has been developed” and an “algorithm created”. In substance, the work combines computing the coherence bandwidth from the TEC of passive GNSS sensors with automatic synthesis of an LSTM network to forecast it 1–7 days ahead.

## Heuristics

- **[explicit]** If the architecture of a recurrent network is unknown in advance — select the number of layers, neurons, and activation and optimization functions automatically (Keras Tuner), because manual selection is slow and inefficient.
- **[explicit]** If forecasts are needed for different horizons — train a separate model for each, because changing the size of the test sample changes the training sample too.
- **[explicit]** If a series has single gaps and high-frequency variations — interpolate the gaps and smooth the series with the Hodrick — Prescott filter before training.
- **[reconstructed]** If a series has a diurnal and seasonal structure — add time predictors (hour, day of the week, season, month, day of the year) and series from neighboring stations to the target series.
- **[reconstructed]** If forecast quality is to be judged honestly — look at the metrics for each horizon, because at 1 and 6 days R² (76 % on average) is lower than at the others (94 % on average).

**In one sentence:** An automatically selected LSTM network of two recurrent layers, five fully connected layers and a fully connected output layer forecasts the coherence bandwidth of a transionospheric channel from GNSS data 1–7 days ahead with MAE 18.2 MHz, R² 0.89 and MAPE 6 % (averaged over a weekly period on the test sample), but the paper has no independent comparison with a baseline architecture.
