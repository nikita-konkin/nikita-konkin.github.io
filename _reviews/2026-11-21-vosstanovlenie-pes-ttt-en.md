---
title: "Reconstructing TEC values using machine learning methods"
pair: vosstanovlenie-pes-ttt
lang: en
date: 2026-11-21
translation_of: 2026-11-21-vosstanovlenie-pes-ttt.md
summary: "An LSTM network, a SARIMA model and a random forest are compared on reconstructing the TEC course at the Kinel station from 2023 data. LSTM does best: RMSE 0.639, MAE 0.259 TECU, R² 0.986; the random forest has R² 0.972 and SARIMA 0.813."
paper_title: "Reconstructing TEC values using machine learning methods"
paper_authors: "Konkin N.A., Vershinin M.V."
paper_year: 2024
paper_date: "2024"
paper_venue: "VII Scientific Forum “Telecommunications: Theory and Technologies” TTT-2024. Proceedings of the XXI International Scientific and Technical Conference, Samara, pp. 73–74"
paper_link: "https://www.elibrary.ru/item.asp?id=75254138"
tags: [ionosphere, TEC, gap-filling, machine-learning, LSTM-network, GNSS]
---

## Problem and relevance

Total electron content (TEC) data depend on the season, and the authors call their reconstruction a priority task when datasets for machine learning are prepared. According to the English abstract, simple mathematical methods cannot synthesise missing values well, whereas machine learning adapts to the data and finds patterns in seasonal series.

## Aim and hypothesis

The aim is to develop methods for reconstructing the time course of TEC with different machine-learning methods. No hypothesis is stated explicitly; in substance the paper tests that a neural network reconstructs the TEC course more accurately than a statistical model and a random forest.

## Materials and methods

TEC values for 2023 from mid-latitude stations of the Samara region are used; the target station is at Kinel. The dataset holds 4000 values. Three models are compared: a recurrent LSTM network, a seasonal autoregressive integrated moving average model (SARIMA) and a random forest.

The algorithm reconstructed samples of the TEC course from earlier data and data of neighbouring stations. The LSTM network, optimised in advance, received a matrix of 25 features: values from neighbouring GNSS stations, time and shift predictors, 4000 values each. SARIMA parameters were also tuned. The training sample contained past data of the target station for 2 days of 48 samples each. For the random forest, 48 samples from one day were used, and the depth of the tree, optimal in quality and computing cost, equals 100 nodes. The output of each model was compared with the real TEC course. The metrics are RMSE, R² and MAE.

## Results

The LSTM network gave the best result: RMSE 0.639, MAE 0.259 TECU, R² 0.986. Random forest: RMSE 0.844, MAE 0.590 TECU, R² 0.972. SARIMA was markedly weaker: RMSE 3.13, MAE 2.366 TECU, R² 0.813. Fig. 1 compares the diurnal TEC course reconstructed by the three methods with the true one.

## Authors' conclusions

The LSTM network gives the smallest error and the highest accuracy of the three methods; the random forest trails slightly and SARIMA markedly. The English abstract adds that machine learning is the preferred method for accounting for patterns in seasonal data.

## Limitations

One target station and one year are used. The paper does not describe how the gaps were created, how many there were, what share of the dataset the test part makes up, or over what the metrics are averaged. The inputs of the models are described differently: 25 features (values of neighbouring stations, time and shift predictors) for LSTM, 2 days of 48 samples of the target station in the training sample, one day (48 samples) for the random forest; whether the comparison is on equal terms is not discussed. The units of RMSE are not given. The phrase about a tree depth “equal to 100 nodes” is ambiguous: it is unclear whether 100 limits the depth or the number of nodes. The LSTM architecture and SARIMA parameters are not listed. The stated aim, “methods of reconstruction”, is carried out as a comparison of three ready-made models.

## Novelty

The paper does not claim novelty explicitly. In substance it is a comparison of LSTM, SARIMA and a random forest on reconstructing the TEC course from Samara-region station data.

## Heuristics

- **[reconstructed]** If TEC is reconstructed at a station that has neighbours — feed the model the neighbouring stations' values together with time and shift predictors, because LSTM with this 25-feature matrix gave the best result; the contribution of the feature set was not tested separately.
- **[reconstructed]** If a method is chosen for a series with a diurnal course — compare a neural network with both a seasonal-series model and decision trees, because their errors differ several-fold (RMSE 0.639 and 3.13).
- **[reconstructed]** If models are compared on one task — give them the same volume and composition of input data, because otherwise the difference in metrics cannot be attributed to the method.

**In one sentence:** An LSTM network reconstructed the diurnal TEC course at the Kinel station more accurately than a random forest and SARIMA (R² 0.986, 0.972 and 0.813), but the models were compared on different inputs and at a single station.
