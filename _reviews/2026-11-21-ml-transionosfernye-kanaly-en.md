---
title: "Applying machine learning to analyse the parameters of transionospheric communication channels"
pair: ml-transionosfernye-kanaly
lang: en
date: 2026-11-21
translation_of: 2026-11-21-ml-transionosfernye-kanaly.md
summary: "A database of total electron content values spanning several months was built from satellite navigation RINEX files, and the diurnal course of the TEC was forecast with three regression machine-learning methods. Accuracy by R²: the random forest reaches about 96 %, gradient descent 93 %, and linear regression does worst."
paper_title: "Applying machine learning to analyse the parameters of transionospheric communication channels"
paper_authors: "Konkin N.A., Pasova A.D. (supervisor — Ryabova N.V.)"
paper_year: 2021
paper_date: "2021"
paper_venue: "Scientific Progress — Creativity of the Young, 2021, no. 2, pp. 191–194"
paper_link: "https://www.elibrary.ru/item.asp?id=48019197"
tags: [ionosphere, transionospheric-channel, TEC, machine-learning, random-forest, RINEX]
---

## Problem and relevance

Changes in the state of the ionosphere, chiefly in the total electron content (TEC), force the transmitting and receiving equipment of satellite communication channels to be readjusted. The parameters of transionospheric radio channels therefore have to be analysed and their values forecast.

## Aim and hypothesis

The aim is to apply machine-learning methods to forecasting the diurnal variations of the TEC. The tasks are to process satellite navigation RINEX files and derive the TEC from them, to build a database, to choose machine-learning methods, and to construct forecast curves. No hypothesis is stated explicitly.

## Materials and methods

A PostgreSQL database spanning several months was prepared, whose tables hold time, latitude, longitude and the TEC. The data were first examined for correlations between the table columns; dependencies were found between latitude and longitude, latitude and time, longitude and time, and TEC and time. The regression dependency of the TEC on time is the one that matters for the forecast. The gradient-descent, linear-regression and random-forest methods from the Python Scikit-learn library were used. Forecast accuracy was assessed with the R² criterion.

## Results

The highest accuracy is reached by the random forest at about 96 %, and gradient descent reaches 93 %. Linear regression showed the poorest agreement between the forecast and the experimental data; the authors note that its figure can be improved with a polynomial model.

## Authors' conclusions

The result is a large database of experimental TEC values from RINEX files and machine-learning algorithms adapted to the dependency of the TEC on time.

## Limitations

The number of stations, the region, the forecast horizon and step, the sample size and the train/test split are not given. Only two R² values are reported (about 96 % and 93 %), without saying which data they were computed on; no value is given for linear regression. The link between the chosen models and the physics of the transionospheric channel is not spelled out: time is the only predictor named, and the total number of TEC series studied is not stated.

## Novelty

No novelty is claimed explicitly. In substance the paper compares three regression machine-learning methods on forecasting the diurnal course of the TEC derived from RINEX files.

## Heuristics

- **[explicit]** If the relationships in a table must be understood before forecasting — build a correlation matrix and pick the regression dependency, because, as the authors put it, regression dependencies are what matters in the work, and of those found, the link between TEC and time fits that role.
- **[reconstructed]** If linear regression fits the experimental data poorly — move to a polynomial model, because the authors suppose that it would improve this figure.
- **[reconstructed]** If forecast models are compared — state the sample and the horizon on which the metric was computed, because a single R² value is not reproducible without them.

**In one sentence:** On TEC data from RINEX files the random forest forecasts the diurnal course of the TEC more accurately (R² about 96 %) than gradient descent (93 %) and linear regression.
