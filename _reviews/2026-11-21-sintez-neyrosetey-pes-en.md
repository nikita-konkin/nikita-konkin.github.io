---
title: "Synthesis of neural network structures for forecasting the total electron content of the Earth's ionosphere"
pair: sintez-neyrosetey-pes
lang: en
date: 2026-11-21
translation_of: 2026-11-21-sintez-neyrosetey-pes.md
summary: "The author developed an algorithm that searches over the structure of a neural network (LSTM, Dropout, Dense) and its hyperparameters for forecasting total electron content (TEC) with Keras Tuner: 100 trials of 250 epochs were run and the 10 best models selected. The relative error (MAPE) of the best model was 4.88 % in training and 7.85 % in validation."
paper_title: "Synthesis of neural network structures for forecasting the total electron content of the Earth's ionosphere"
paper_authors: "Vershinin M.V. (supervisor — Konkin N.A.)"
paper_year: 2024
paper_date: "2024"
paper_venue: "Scientific Progress — Creativity of the Young, 2024, no. 1, pp. 290–292"
paper_link: "https://www.elibrary.ru/item.asp?id=69910523"
tags: [ionosphere, TEC, neural-networks, LSTM, hyperparameters, forecasting]
---

## Problem and relevance

Choosing the hyperparameters of a neural network by hand is complicated and laborious. The author regards automatic selection for a model working with total electron content (TEC) data as a promising direction of development.

## Aim and hypothesis

The aim is to develop an algorithm that selects the structure and hyperparameters of a machine-learning model: the number of layers of each kind, the number of neurons per layer and the activation function of each fully connected (Dense) layer. The task is to find the best combination for TEC forecasting. No hypothesis is stated in the paper.

## Materials and methods

The TEC data, their source, period and sampling step are not described. The network follows a scheme: LSTM layers first, then a Dropout layer that may be included with a random probability, and fully connected (Dense) layers last. Models were evaluated on data outside the training sample. The search used the Keras Tuner library, which allows following the progress and the result of the algorithm; TensorBoard was used to visualize and assess the result. The criteria are MAPE (the main one), MAE and RMSE. Search ranges: the number of layers of each kind from 2 to 10 in steps of 2, neurons per layer from 32 to 512 in steps of 32, and the activation of the fully connected layers either SELU or ReLU.

## Results

100 trials of 250 epochs were run, and 10 best models were selected. For the best one the relative error was 4.88 % in training and 7.85 % in validation. The training MAPE curve falls and stays at about the same level after 100 epochs; the validation curve jumps a lot, but its trend line goes down. The structure of the best model is one input layer, one LSTM and 8 fully connected layers, one of them the output. The metrics of the other nine models, and the MAE and RMSE of the best one, are not given in the text.

## The author's conclusions

10 best models were obtained; in the author's view, the error of the best one indicates a sufficiently good predictive ability.

## Limitations

The data, the forecast horizon and the split into training and validation parts are not described. There is no comparison with a simple model or other work, so 4.88 % and 7.85 % do not show whether the error is small for this task; the criterion for a “sufficiently good” ability is not named. The gap between training and validation errors and the jumps of the validation curve are not discussed. The number of layers of each kind was searched from 2 to 10, yet the best model has one LSTM; the paper does not explain how these fit together. The composition given for the best model names no Dropout layer; how many neurons it has and which activation was chosen is not stated.

## Novelty

The paper does not claim novelty explicitly. Its contribution is an algorithm for automatic selection of the structure and hyperparameters of an LSTM network for TEC forecasting on Keras Tuner, and its outcome: the 10 best models out of 100 trials.

## Heuristics

- **[explicit]** If choosing hyperparameters by hand is slow — switch to automatic selection, because it is named a promising direction for TEC data.
- **[explicit]** If models are compared on predictive ability — evaluate them on data outside the training sample, because the estimate is more objective.
- **[reconstructed]** If the space of structures is large — fix the skeleton (LSTM first, optional Dropout, fully connected layers last) and search the number of layers, neurons and the activation, because in the paper the structure is fixed as this sequence of layers, while their number, the neuron counts and the activation are searched.
- **[reconstructed]** If the training error has stopped falling — check whether a large reserve of epochs is needed, because here MAPE levelled off after 100 of 250 epochs.

**In one sentence:** A Keras Tuner algorithm selected for TEC forecasting a network of one LSTM and 8 fully connected layers with a MAPE of 4.88 % in training and 7.85 % in validation, but the data and a baseline comparison are not described in the paper.
