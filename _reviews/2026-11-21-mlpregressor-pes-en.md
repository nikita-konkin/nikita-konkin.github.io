---
title: "Influence of MLPRegressor neural network hyperparameters on the accuracy of TEC forecasting in a transionospheric radio channel"
pair: mlpregressor-pes
lang: en
date: 2026-11-21
translation_of: 2026-11-21-mlpregressor-pes.md
summary: "The author compared twelve combinations of activation function and solver of the MLPRegressor neural network, with the number of hidden-layer iterations growing from 5 to 200, for forecasting total electron content (TEC) from 10 stations in the Samara region. The (tanh, adam) model was the best, with a coefficient of determination from 0.8755 to 0.7034; it is more accurate than (logistic, adam) by 0.04 in R² and by 0.28 TECU in RMSE."
paper_title: "Influence of MLPRegressor neural network hyperparameters on the accuracy of TEC forecasting in a transionospheric radio channel"
paper_authors: "Elchaninova A.S. (supervisor — Konkin N.A.)"
paper_year: 2023
paper_date: "2023"
paper_venue: "Scientific Progress — Creativity of the Young, 2023, no. 2, pp. 12–14"
paper_link: "https://www.elibrary.ru/item.asp?id=54740358"
tags: [ionosphere, TEC, transionospheric-channel, neural-networks, MLPRegressor, hyperparameters]
---

## Problem and relevance

Total electron content (TEC) is one indicator of the state of the ionosphere, and transionospheric radio channels are part of the telecommunication infrastructure. Radio sounding is used to assess the state of the channel and adapt systems to changing conditions. The author sets the task of introducing new diagnostic models and raising the accuracy of TEC forecasts.

## Aim and hypothesis

The aim is to study how the hyperparameters of the MLPRegressor multilayer perceptron affect the accuracy of TEC forecasting. No hypothesis is stated in the paper.

## Materials and methods

The dataset was compiled from 10 stations of the Samara region within a radius of 100 km. The data were split into an array X with time and an array y with TEC values; the training part is 48 samples, or 2 days. Twelve combinations of activation function (identity, logistic, tanh, relu) and solver (lbfgs, sgd, adam) were tried, with the number of hidden-layer iterations growing from 5 to 200. Accuracy was assessed with MSE, R², MAE and RMSE.

## Results

The models (logistic, adam) and (tanh, adam) are named the best. For (tanh, adam) the coefficient of determination lies between 0.8755 and 0.7034. It is more accurate than (logistic, adam): by 0.57 TECU in MSE, 0.04 in R², 0.26 TECU in MAE and 0.28 TECU in RMSE. The author writes that the forecast error lies within the confidence interval but does not give the interval. The metric curves over iterations are shown only in the figure.

## The author's conclusions

The model with the parameter set (tanh, adam) is the most accurate. The abstract proposes a variant of it with 30 hidden layers; the main text does not repeat this value.

## Limitations

The observation period, the sampling step and the size of the test part are not given; the only feature is time. It is unclear what a “hidden-layer iteration” is — the number of layers, neurons or training steps — and where the value 30 comes from. The confidence interval is not defined, there is no baseline forecast, repeated runs are not mentioned, and the difference between the two best models in R² is 0.04. MSE is given in TECU rather than in the square of that unit.

## Novelty

The paper does not claim novelty explicitly. Its contribution is a comparative search over combinations of activation function and solver for MLPRegressor on TEC data from one region.

## Heuristics

- **[reconstructed]** If a neural network is being tuned — search the activation function and the solver together, because the best two were pairs with the same solver, adam, and different activations.
- **[reconstructed]** If accuracy changes with the number of iterations — report the range rather than a single value, because R² of the best model lies between 0.8755 and 0.7034.
- **[reconstructed]** If models are close — compute several metrics and compare the differences in each, because the best model's advantage shows in all four: 0.57, 0.04, 0.26 and 0.28.

**In one sentence:** A search over combinations of activation function and solver in MLPRegressor for TEC forecasting from 10 stations singled out the (tanh, adam) model, with R² from 0.8755 to 0.7034, as slightly more accurate than (logistic, adam).
