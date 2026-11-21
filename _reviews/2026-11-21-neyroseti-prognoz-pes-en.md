---
title: "Synthesis and analysis of neural network structures for predicting the total electron content of the Earth's ionosphere"
pair: neyroseti-prognoz-pes
lang: en
date: 2026-11-21
translation_of: 2026-11-21-neyroseti-prognoz-pes.md
summary: "A method for synthesising recurrent neural networks from LSTM and Dense layers selects the structure and hyperparameters on two training samples of TEC data from GNSS reference stations in the Samara region, for 2021 and for 2021–2022; the 2023 data serve for the control evaluation. The network trained on a sample twice as large gives a mean R² of 99.83 % and a MAPE of 1.84 % on the 2023 test for 1–7-day forecasts of TEC at one key station; the error fell almost fourfold."
paper_title: "Synthesis and analysis of neural network structures for predicting the total electron content of the Earth's ionosphere"
paper_authors: "Ryabova N.V., Konkin N.A., Vershinin M.V."
paper_year: 2024
paper_date: "2024"
paper_venue: "All-Russian Open Armand Readings “Modern Problems of Remote Sensing, Radar, Wave Propagation and Diffraction”, Murom, pp. 445–457"
paper_link: "https://www.elibrary.ru/item.asp?id=68558431"
tags: [ionosphere, TEC, neural-networks, LSTM, KerasTuner, GNSS]
---

## Problem and relevance

Changes in ionospheric parameters affect satellite and terrestrial radio communication; they are caused by geomagnetic storms, solar flares, technological radio-frequency emission and other influences. Ionospheric models of various types are used for forecasting, but they have limitations. The authors consider a method for synthesising neural networks for forecasting the total electron content (TEC), meeting modern accuracy requirements, an important task. Neural networks have no universal structure, so for forecasting time series the structure has to be selected.

## Aim and hypothesis

The aim is a method for synthesising neural networks for forecasting ionospheric TEC. The tasks are to prepare the TEC data of GNSS reference stations for 2 years, to develop a structure-synthesis method, to compare forecasts with training samples of different sizes by absolute and relative metrics, and from them to draw conclusions on the structures that improve accuracy. No hypothesis is stated explicitly; in substance the paper tests that structure selection gives an accurate forecast and that a larger training sample lowers the error.

## Materials and methods

The data are measurements from reference GNSS stations of the company Smartnet Geosystems at nine sites in the Samara region (Samara, Koshki, Tolyatti, Chapaevsk, Kinel, Otradny, Krasnoarmeysk, Neftegorsk, Elkhovka). The stations measure every 30 s and write RINEX files, which are converted into TEC at a step of 30 minutes. Ideally a year gives 17,520 values per station; in practice about 14,000 usable ones on average, roughly 80 %. The dataset holds about 27,000 TEC values for each of the 9 stations over three years (2021–2023). Two training samples were formed from it: no. 1 — about 11,700 averaged values for 3 stations for 2021, no. 2 — about 23,000 values for 9 stations for 2021–2022. Twenty per cent of each sample is used for validation during training, and the year 2023 for evaluating the best models. The features are the TEC values shifted by one sample (30 minutes) and time components (day, month, year, weekday, day of month, day of year, quarter); the input has 13 features for sample no. 1 and 25 for no. 2.

The network structure is selected with the Keras Tuner library. The number of LSTM and Dense layers varies from 1 to 10 for each type, the number of neurons from 32 to 512 in steps of 32, the activation of the Dense layer is chosen between SELU and ReLU, and a Dropout layer is switched on at random; the output is one neuron, since the forecast is made for one key station. Fifty iterations of the algorithm of 250 epochs each were run, with stopping when the target metric reaches a plateau; the target metric is MAPE. For each sample the 10 best models were kept, and the best of them was chosen by RMSE, MAE, MAPE and R² on the 2023 data. The forecast horizon varied from one to seven days on January data.

## Results

Sample no. 1: the coefficient of determination R² begins to fall noticeably with a four-day forecast (a drop of 1.8 % after 0.1 % at shorter horizons); MAPE worsens by 0.57 % on average; RMSE and MAE grow monotonically, and all horizons except the seventh stay within the confidence interval of 3.74 TECU.

Sample no. 2: R² averages 99.83 % at all horizons with a variation of 0.06 %; MAPE averages 1.84 % with a variation of 0.22 %. At horizons of one to five days the mean RMSE is 0.22 TECU and the mean MAE 0.15 TECU; the largest values, for a seven-day forecast, are RMSE 0.54 TECU and MAE 0.26 TECU.

According to the plot, the larger sample cut the error almost fourfold and raised the convergence of the series by 9 % on average. The best model for sample no. 1 has 11 layers: an input, six LSTM and four Dense (one of them the output); for sample no. 2 it has seven: an input, two LSTM and four Dense.

## Authors' conclusions

A method for synthesising neural networks for TEC forecasting over different periods has been created. The size of the training sample strongly affects the relative error: doubling it reduces the TEC error almost fourfold and raises the convergence of the series by 4–19 %. A model trained on a limited set stops matching the real TEC course during ionospheric disturbances, and the error grows. The method of choosing the best model by RMSE, MAE, MAPE and R² is, in the authors' words, aimed at improving the efficiency of the forecast.

## Limitations

There is no comparison with the ionospheric models mentioned in the introduction or with simpler baseline forecasts, and there is no comparison that would show the effect of the way the best model is chosen. The two samples differ at once in the number of stations (3 and 9), the number of years (1 and 2) and the number of features (13 and 25), so the contribution of size alone cannot be separated. The sizes of the validation parts (about 4,600 and 2,300) do not agree with 20 % of 11,700 and 23,000, i.e. they appear to be swapped. The evaluation covers one year and one region; how a multi-day forecast is built from features shifted by one sample is not described. The 3.74 TECU confidence interval is not defined, and the gain in convergence is given as 9 % in one place and 4–19 % in another. The Dropout layer is not mentioned in the final architectures.

## Novelty

The paper does not claim novelty explicitly; the authors call creating a new effective method of neural-network synthesis for TEC an important task. In substance it proposes automatic selection of the structure of an LSTM network with Keras Tuner and tests it on data from reference stations in the Samara region.

## Heuristics

- **[explicit]** If there is no universal neural-network structure for the task — synthesise it by searching over the number of layers, neurons and the activation function, because a suitable structure depends on the task.
- **[explicit]** If overfitting must be avoided — add a Dropout layer and limit the number of epochs when the target metric reaches a plateau.
- **[explicit]** If forecast accuracy is not satisfactory — enlarge the training sample, because a model trained on a small set loses its resemblance to the real TEC course during disturbances.
- **[reconstructed]** If the network forecasts for different horizons — check several horizons (1–7 days) and compare absolute and relative metrics, because R² and MAPE behave differently.
- **[reconstructed]** If the best model is chosen from a set of trained ones — evaluate it on a control period used in neither training nor validation (here 2023).

**In one sentence:** Automatic selection of the structure of an LSTM network on data from nine GNSS stations over two years gave a TEC forecast for one key station for 1–7 days with a mean R² of 99.83 % and a MAPE of 1.84 %; the error is almost four times smaller than for a network trained on three stations over one year.
