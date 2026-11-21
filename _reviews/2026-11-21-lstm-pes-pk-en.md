---
title: "Studying LSTM neural network structures for forecasting TEC and coherence bandwidth at different forecast horizons"
pair: lstm-pes-pk
lang: en
date: 2026-11-21
translation_of: 2026-11-21-lstm-pes-pk.md
summary: "Structures of the recurrent LSTM neural network are examined: five architectures for forecasting the coherence bandwidth and five for forecasting TEC at forecast horizons of 1 to 5 days. The best coherence-bandwidth forecast is obtained at 4 days (R² 0.85, MAPE 0.05), and the best TEC forecast at 5 days (R² 0.73, MAPE 0.13)."
paper_title: "Studying LSTM neural network structures for forecasting TEC and coherence bandwidth at different forecast horizons"
paper_authors: "Elchaninova A.S. (supervisor — Konkin N.A.)"
paper_year: 2024
paper_date: "2024"
paper_venue: "Scientific Progress — Creativity of the Young, 2024, no. 1, pp. 298–300"
paper_link: "https://www.elibrary.ru/item.asp?id=69910526"
tags: [neural-networks, LSTM, TEC, coherence-bandwidth, forecasting, machine-learning]
---

## Problem and relevance

Satellite communication systems need fast and accurate forecasts of the coherence bandwidth and the total electron content (TEC) in order to adapt the system's characteristics to the state of the ionosphere. Existing approaches do not always give the required accuracy and speed, so the author turns to neural networks.

## Aim and hypothesis

The aim is to study recurrent LSTM network structures and to find how the accuracy of TEC and coherence-bandwidth forecasting depends on the network structure at different forecast horizons. No hypothesis is stated explicitly.

## Materials and methods

Five LSTM architectures are examined for the coherence bandwidth and five for TEC at forecast horizons of 1 to 5 days. The coherence-bandwidth models contain 3 to 9 LSTM layers, the TEC models 2 to 9, together with two fully connected Dense layers and one Dropout layer; the number of neurons is 200 to 328 (coherence bandwidth) and 72 to 264 (TEC), with the conclusion giving a range up to 392. The activation functions selu, elu and gelu are used. Testing used a 5-day dataset sampled every half hour, with the mean absolute percentage error MAPE and the coefficient of determination R² as metrics.

## Results

Forecast accuracy over 2–4 days is higher for the coherence bandwidth, and over 1 and 5 days for TEC. The best coherence-bandwidth forecast is reached at 4 days: R² 0.85 and MAPE 0.05 with 7 LSTM layers of 200 neurons, 2 Dense layers of 328 neurons and one Dropout layer. For TEC the best result is at 5 days: R² 0.73 and MAPE 0.13 with 3 LSTM layers of 136 neurons, 2 Dense layers of 264 neurons and one Dropout layer. Each forecast horizon has its own structure: the number of LSTM layers and neurons changes, while the number of Dense layers (two) and Dropout layers (one) does not change. A more accurate coherence-bandwidth forecast needs more layers than a TEC forecast.

## The author's conclusions

Each forecast horizon corresponds to a particular network structure. The most accurate coherence-bandwidth forecast requires more LSTM layers than a TEC forecast.

## Limitations

The source of the TEC and coherence-bandwidth data (stations, observation period) is not described. The neuron range for TEC is given as 72–264, but the conclusion says up to 392, which is inconsistent. The MAPE values 0.05 and 0.13 are given without units (percent or fraction). The metrics of all ten models appear only in Fig. 1, and the text names values only for the two best ones.

## Novelty

The paper does not claim novelty explicitly. In substance it tunes the LSTM structure separately for the coherence bandwidth and for TEC and relates the number of layers and neurons to the forecast horizon.

## Heuristics

- **[explicit]** If different channel parameters (TEC and coherence bandwidth) are forecast — fit a separate network structure to each parameter and horizon, because the optimal number of LSTM layers and neurons differs between them.
- **[explicit]** If the coherence-bandwidth forecast must be accurate — use more LSTM layers than for a TEC forecast, because the coherence bandwidth needs a deeper network.
- **[reconstructed]** If MAPE and R² are compared across forecast horizons — compare architectures at a fixed horizon, because the best structure differs from one horizon to another.

**In one sentence:** Among ten LSTM architectures the best coherence-bandwidth forecast is reached at 4 days (R² 0.85, MAPE 0.05) and the best TEC forecast at 5 days (R² 0.73, MAPE 0.13), with each forecast horizon matching its own network structure.
