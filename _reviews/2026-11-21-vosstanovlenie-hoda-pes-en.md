---
title: "Reconstructing TEC values using machine learning methods"
pair: vosstanovlenie-hoda-pes
lang: en
date: 2026-11-21
translation_of: 2026-11-21-vosstanovlenie-hoda-pes.md
summary: "The LSTM, SARIMA and random forest models restore 48 half-hourly samples of total electron content (TEC) at the Kinel station for 2023, trained on two days of data whose set included eight neighbouring GNSS stations. The mean R² of the random forest is 0.995, of SARIMA 0.951; LSTM did best in winter, the random forest in spring."
paper_title: "Reconstructing TEC values using machine learning methods"
paper_authors: "Ryabova N.V., Konkin N.A., Vershinin M.V."
paper_year: 2024
paper_date: "2024"
paper_venue: "Radio Wave Propagation. Proceedings of the I All-Russian Youth School-Conference in memory of D.S. Lukin, Yoshkar-Ola, pp. 113–117"
paper_link: "https://www.elibrary.ru/item.asp?id=75116659"
tags: [ionosphere, TEC, data-restoration, seasonality, machine-learning, LSTM]
---

## Problem and relevance

Restoring missing values improves the accuracy of decisions built on those data. Simple regression models ignore the seasonal component, which distorts the restoration and lowers forecast accuracy. Seasonality is handled by specialised models such as SARIMA and by machine-learning methods. The authors regard restoring total electron content (TEC) as a promising direction for transionospheric radio channels.

## Aim and hypothesis

The aim is to apply different machine-learning methods to restoring missing seasonal values and to compare accuracy by method. The tasks are to review methods and pick suitable ones, to develop a restoration algorithm, to compare the models with real data by MAE, MAPE, RMSE and R², and to conclude on the applicability of the methods to series with a seasonal dependence. No hypothesis is stated explicitly; in substance the paper tests which of three models restores the TEC course best from a small training sample.

## Materials and methods

The data are TEC of a station in the city of Kinel, Samara region, for 2023. Three models were chosen: the recurrent network LSTM, the seasonal autoregressive model SARIMA and a random forest (RF). Each model received two days of TEC as input. The training set included data from eight neighbouring GNSS reference stations at a half-hour step: 96 samples for training and 48 for testing. SARIMA needs no feature matrix, only the earlier samples of the key station; at test time only the number of samples to restore is specified.

The training volume is the minimum available: gap-free data immediately before the lost values. The data are split into training and test parts to assess restoration on data outside training. The comparison uses absolute and relative metrics: MAE, MAPE, RMSE and R².

## Results

In the plots for the winter and spring seasons every model restored the series. SARIMA repeated the shape of the series, but its similarity to the real TEC course, in the authors' view, is not sufficient for further use, unlike LSTM and RF. The random forest proved best in all periods. The mean R² is 0.951 for SARIMA and 0.995 for RF; the difference, by the authors' estimate, is 5 %. LSTM did best in winter, RF in spring; the R² of the random forest stays around 0.99, that of LSTM around 0.9. Numerical values of MAE, MAPE and RMSE are in Fig. 3 and not given in the text.

## Authors' conclusions

Restoring TEC is promising for transionospheric radio channels; machine-learning methods give a restoration accuracy above 95 % compared with traditional ones. All three models showed high accuracy with a limited training sample; SARIMA was the least accurate, the average difference in MAE between it and the other two models reaching 30 %.

## Limitations

The target station is one (Kinel) and the year is one, while the training set also included eight neighbouring stations; the test is 48 samples (one day), and the dates of the tested periods and the names of the months are not given in the text. Model parameters and architectures are not described. For LSTM there are no numbers beyond the general order of R². The claimed superiority over “traditional methods” rests on a comparison with SARIMA alone; simple approaches such as interpolation are not considered. The observation that LSTM is better in winter and RF in spring is made on two seasons without any significance estimate.

## Novelty

Not claimed explicitly. The contribution is a comparison of three models of different nature on restoring TEC from a limited training sample.

## Heuristics

- **[explicit]** If a series has a seasonal component — use models that account for it (SARIMA, machine learning) rather than simple regression, because regression distorts the restoration.
- **[explicit]** If the data are split into training and test parts — make the samples non-overlapping, to assess restoration on data outside training.
- **[explicit]** If gaps must be filled — take the minimum available training volume without gaps immediately before the lost values.
- **[reconstructed]** If a series is seasonal and it is unknown which model is better — compare models of different nature (statistical, recurrent, ensemble) season by season, because model quality changes by season: LSTM did best in winter, RF in spring.

**In one sentence:** From two days of data the random forest restored the TEC course best (mean R² 0.995), LSTM, in the authors' view, also coped with the task, and SARIMA lagged behind (mean R² 0.951).
