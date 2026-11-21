---
title: "Study of the Applicability of Machine Learning Methods for Reconstructing Total Electron Content Time Series"
pair: primenimost-ml-pes
lang: en
date: 2026-11-21
translation_of: 2026-11-21-primenimost-ml-pes.md
summary: "Three methods for reconstructing the total electron content (TEC) series of the Kinel station for 2023 are compared: LSTM, random forest (RF) and SARIMA. The random forest is judged best, with RMSE 0.29–0.70 TECU and R² 0.98–0.99 in January, February and April, while the LSTM's R² fell to 0.73 in February and SARIMA gave the largest errors in January and April."
paper_title: "Study of the Applicability of Machine Learning Methods for Reconstructing Total Electron Content Time Series"
paper_authors: "Ryabova N.V., Konkin N.A., Vershinin M.V."
paper_year: 2025
paper_date: "2025"
paper_venue: "Vestnik of Volga State University of Technology. Ser.: Radio Engineering and Infocommunication Systems, 2025, no. 2 (66), pp. 41–50"
paper_link: "https://www.elibrary.ru/item.asp?id=87229552"
tags: [TEC, GNSS, data-reconstruction, machine-learning, LSTM, random-forest]
---

## Problem and relevance

Series of ionospheric total electron content (TEC) obtained from GLONASS monitoring contain gaps. The authors name four causes: loss of signal at a low satellite elevation angle, receiver faults, algorithmic processing errors, and extreme space weather — geomagnetic storms and solar flares. A reconstructed series is needed to forecast the state of the ionosphere and to adjust communication channels.

## Aim and hypothesis

The aim is to study the applicability of machine-learning methods for reconstructing missing values of the TEC time course by comparing the accuracy of the methods by MAE, MAPE, RMSE and R². No hypothesis is stated explicitly; in substance the paper tests that machine-learning methods reconstruct a nonlinear seasonal course more accurately than standard mathematical methods.

## Materials and methods

The data are TEC values from the mid-latitude station Kinel (Samara region) for 2023 at a 30-minute step; the total is about 16 thousand samples, and nine stations are mentioned. Three models are compared: the recurrent network LSTM, the random forest (RF) and the statistical model SARIMA. LSTM and RF received a feature vector containing TEC and additional features; SARIMA uses only the preceding samples of the series and the number of samples to be produced.

The training set contained two days of TEC data from eight neighboring GNSS reference stations: 96 samples for training and 48 for testing. The authors stress that they take the minimum available training volume with no gaps. The hyperparameters, the way gaps were simulated and the split by month are not described. Results are given for January, February and April.

## Results

SARIMA reproduces the overall shape of the series but in January and April gives the largest errors. In January: RMSE 1.88 TECU, MAE 1.53 TECU, MAPE about 28.3 %, R² 0.93; in April: RMSE 3.10, MAE 2.62, MAPE about 11.7 %, R² 0.94. The share of explained variance averaged over the three months is 95.1 %.

LSTM gave the best result of all models in January: RMSE 0.35 TECU, MAE 0.27 TECU, MAPE 4.5 %, R² 0.99. In February, when ionospheric changes became irregular, RMSE rose to 8.9, MAE to 4.43, MAPE to 10.8 %, and R² dropped to 0.73. In April RMSE was 1.91 and R² 0.98.

The random forest in all three months keeps RMSE in the range 0.29–0.70, MAE 0.24–0.55, MAPE no higher than 13.2 %, R² 0.98–0.99. The authors give the mean R² over the three periods as 0.995 and the mean RMSE as about 0.54 TECU.
## Authors' conclusions

For practical reconstruction of missing TEC values, ensemble decision-tree methods are the most justified: the random forest combines ease of implementation, accuracy (mean RMSE about 0.54 TECU), the ability to adapt to irregular events, and explains more than 99 % of the TEC variation. LSTM remains promising under predominantly regular trends; SARIMA suits preliminary analysis and monitoring of seasonal fluctuations.

## Limitations

The authors note the limited robustness of LSTM to sharp jumps during disturbances of the Earth's magnetic field. From the outside: one observation site, three months of one year; testing on 48 samples (one day). From the description, the test samples follow the training ones, so the task is closer to a next-day forecast than to filling a gap inside a series; how the gaps were created is not stated. The model parameters are not given. The conclusion of accuracy “above 95 %” does not agree with the LSTM's R² of 0.73 in February, and the random forest's mean R² of 0.995 lies above the upper bound of the 0.98–0.99 range given next to it.

## Novelty

The paper does not claim novelty explicitly. In substance, its contribution is a comparison of three methods (LSTM, random forest, SARIMA) by four metrics on the TEC series of one mid-latitude station over three months of 2023.

## Heuristics

- **[explicit]** If you must choose a method for reconstructing a TEC series — start from the specifics of the task, the nature of the gaps and the available computing resources, because each method has its own strengths and weaknesses.
- **[explicit]** If model quality is compared — split the data into training and test sets, because this gives an objective estimate of the ability to forecast new data.
- **[explicit]** If a series contains irregular disturbances — prefer a tree ensemble to a recurrent network, because the random forest is more robust to outliers and unpredictable changes.
- **[explicit]** If a model has to be trained on a short gap-free stretch — take the minimum available volume (here two days), because the training sample must have no missing values, and two days are needed by some models, SARIMA in particular.
- **[reconstructed]** If methods are compared over several months — look at the spread of metrics across months and not only the mean, because LSTM is best in January (R² 0.99) and noticeably worse in February (R² 0.73).

**In one sentence:** On three months of 2023 at the Kinel station, the random forest reconstructs the TEC course with RMSE 0.29–0.70 TECU and R² 0.98–0.99, LSTM is best in January but loses accuracy under irregular changes, and SARIMA gives the largest errors in January and April.
