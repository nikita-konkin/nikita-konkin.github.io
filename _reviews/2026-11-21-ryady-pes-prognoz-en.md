---
title: "Recovery and Prediction of Total Electron Content Time Series Using Machine Learning"
pair: ryady-pes-prognoz
lang: en
date: 2026-11-21
translation_of: 2026-11-21-ryady-pes-prognoz.md
summary: "For TEC series from a network of nine GNSS stations in the Samara region for 2021–2023, a random forest with dynamic shift predictors recovers gaps of up to a day (R² > 98.4 %, MAPE < 4.3 %), and an automatically synthesized LSTM network trained on the extended sample keeps R² ≈ 98 % at horizons of up to seven days. Extending the training sample cut RMSE roughly fourfold; the largest errors fell in March 2023 (RMSE up to 19.5 TECU)."
paper_title: "Recovery and Prediction of Total Electron Content Time Series Using Machine Learning"
paper_authors: "Ryabova N.V., Ovchinnikov V.V., Vershinin M.V., Konkin N.A., Elchaninova A.S., Stankevich S.S."
paper_year: 2025
paper_date: "2025"
paper_venue: "Vestnik of Volga State University of Technology. Ser.: Radio Engineering and Infocommunication Systems, 2025, no. 4 (68), pp. 6–17"
paper_link: "https://www.elibrary.ru/item.asp?id=89058955"
tags: [TEC, GNSS, data-recovery, forecasting, LSTM, random-forest]
---

## Problem and relevance

Continuous data on the total electron content (TEC) of the ionosphere are needed to correct dispersion distortions in wideband satellite communication systems. TEC series have gaps caused by equipment failures, geomagnetic storms and limits of measurement networks, and interpolation and physical models, in the authors' view, adapt poorly to nonlinear dependences. Compensating the delay in advance also requires a TEC forecast.

## Aim and hypothesis

The aim is to develop and test an integrated approach to recovering and forecasting variations of TEC with machine learning. No hypothesis is stated explicitly; in substance the paper tests that enlarging the training sample raises the accuracy and stability of the LSTM forecast.

## Materials and methods

The data are TEC for 2021–2023 from nine mid-latitude GNSS reference stations of Smartnet Geosystems LLC in the Samara region, at a 30-minute step. Two samples: no. 1, about 11,700 values for 2021 from three stations; no. 2, about 23,000 values for 2021–2022 from nine stations. The 2023 data are for independent testing. The metrics are R², MAE, MAPE and RMSE.

Recovery: the algorithm finds the longest gap-free stretch for initial training and fills gaps of up to 48 samples (one day) with a random forest. The features are values from neighboring stations and dynamic predictors: shift, differenced and percentage-differenced values over earlier periods of up to 48 samples. For testing, gaps were created artificially.

Forecasting: the LSTM synthesis searches over 1 to 10 layers (Input, LSTM, Dropout, Dense), 32 to 512 neurons in steps of 32, and the activations SELU and ReLU in fully connected (Dense) layers; the output is one neuron, a forecast for one target station.

## Results

Recovery: for all seasons the difference in R² between recovery on current data and on previously recovered data did not exceed 0.6 %. The confidence intervals confirmed the method's stability in winter, spring and autumn; in summer the root mean square error exceeded the interval bounds roughly twofold, which the authors attribute to raised geomagnetic activity.

The forecast was tested for January to April 2023. For sample no. 1 a network of 11 layers was synthesized (Input, six LSTM, four Dense); for sample no. 2, one of seven (Input, two LSTM, four Dense). In the first week of January the best forecast for sample no. 1 had R² 0.92 and the worst 0.60; for sample no. 2 the best R² was 0.98 and the worst 0.64. The largest error (RMSE 19.5 TECU) fell in the second week of March 2023; even with sample no. 2, the March RMSE at the peak did not go below 13.8 TECU. The model on sample no. 2 converges markedly better: RMSE is about fourfold smaller. At horizons of up to seven days its R² stays around 98 %, while the model on sample no. 1 deteriorates noticeably after four days. In March the model on sample no. 2 still systematically underestimates peaks; the authors link this to the absence of direct solar and geomagnetic activity indices among the features.

## Authors' conclusions

The recovery algorithm showed R² > 98.4 % and seasonal stability and suits building complete historical TEC series. Growth in the volume and spatiotemporal diversity of the training sample — the number of stations and the length of observation — is the key factor in the accuracy and stability of forecasts at long horizons. The main errors of both methods are tied to periods of raised geomagnetic activity; the priority direction for further work is to add solar and geomagnetic activity indices to the features.

## Limitations

The authors admit underestimated peaks in disturbed periods and a sample too small for extreme conditions; they see the remedy in a multi-year sample and geophysical indices. From the outside: one regional network; metrics by month are in graphs, and only a few numbers appear in the text. The Russian abstract gives R² > 98.4 %, the English one R² > 99.4 %. The paper does not say over which periods and with what aggregation the nearly fourfold drop in RMSE was obtained; it is not visible in the March peaks (19.5 and 13.8 TECU). The worst forecasts have R² 0.60 and 0.64, and R² ≈ 98 % at horizons of up to seven days is given without a breakdown by horizon. There is no baseline forecast; the full list of LSTM features and the window length are not described, only shift predictors and decomposition of the timestamp are mentioned.

## Novelty

Novelty is not claimed explicitly; the authors call the approaches “developed”. In substance, the paper proposes a gap-recovery algorithm using a random forest with dynamic shift predictors from neighboring stations, and a method for automatic synthesis of LSTM architectures for TEC series.

## Heuristics

- **[explicit]** If gaps in a series must be recovered — take the longest continuous gap-free stretch for initial training, because the model can be trained on it without filling.
- **[explicit]** If the forecast degrades at a long horizon — widen the training sample in stations and years, because that raised stability up to seven days.
- **[explicit]** If the main errors fall on geomagnetic disturbances — add solar and geomagnetic activity indices to the features, because the authors link the underestimated peaks to the absence of such indices.
- **[reconstructed]** If the recovery accuracy must be assessed — create gaps artificially and keep the full series as the reference, because real gaps have nothing to be checked against.
- **[reconstructed]** If the right network architecture is unknown in advance — select it automatically for each sample, because samples no. 1 and no. 2 gave different depths (11 and 7 layers).

**In one sentence:** A random forest with dynamic shift predictors recovers TEC gaps of up to a day with R² > 98.4 %, and the synthesized LSTM network on the extended sample keeps R² around 98 % at seven days, but in the geomagnetically disturbed March 2023 errors reach RMSE 19.5 TECU.
