---
title: "Machine learning for analyzing the availability of a shortwave communication channel"
pair: dostupnost-kv-kanala
lang: en
date: 2026-11-21
translation_of: 2026-11-21-dostupnost-kv-kanala.md
summary: "A Voting Regressor ensemble of ElasticNet, Huber and XGBoost forecasts the MUF on the Cyprus – Yoshkar-Ola path, and channel availability for 2023 is computed from the real and forecast MUF. Mean annual availability from the forecast was 93.46 % against 93.23 % from real data, with seasonal differences from −0.44 to +0.47 percentage points."
paper_title: "Machine learning for analyzing the availability of a shortwave communication channel"
paper_authors: "Konkin N.A., Vershinin M.V."
paper_year: 2025
paper_date: "2025"
paper_venue: "GraphiCon 2025. Proceedings of the 35th International Conference on Computer Graphics and Machine Vision, Yoshkar-Ola, pp. 505–513"
paper_link: "https://www.elibrary.ru/item.asp?id=88853642"
tags: [hf-channel, MUF, channel-availability, machine-learning, ensemble-models, adaptive-communication]
---

## Problem and relevance

The availability of an HF radio channel falls because of interference, signal fading and multipath propagation. Transmitting on a fixed frequency at a constant rate with an unchanged error-correcting code, one can send files of no more than 10 Kbyte at an average information rate of about 100 bit/s and a bit error probability of 10⁻³–10⁻⁵ (BPSK without multiplexing). Reliability is raised by adapting to the conditions: the working frequency, transmission rate, code redundancy, guard-interval length and other parameters are changed. This needs the MUF in advance, and the authors propose to obtain its forecast with machine-learning methods.

## Aim and hypothesis

The aim is to assess the availability of the Cyprus – Yoshkar-Ola HF channel from real and forecast MUF values (the Comb_Voting_Huber_p-10_mae model) and to compare the results. The tasks are an assessment method, its implementation in Python with the Pandas and Scipy libraries, computation on data, a comparison of real and forecast values, and a conclusion on the applicability of machine learning. No hypothesis is stated explicitly; in substance the paper tests that availability from the forecast MUF is close to availability from the real one.

## Materials and methods

The data were obtained on the Cyprus – Yoshkar-Ola path, about 2700 km long, by oblique sounding with software-defined radio (SDR) receivers at a step of 5 minutes, i.e. 288 measurements a day. The period is 22 January to 31 December 2023; the paper names 99072 samples for a full year (344 days × 288) and 98784 samples for the stated period.

The MUF forecast is made by a Voting Regressor that averages three models: ElasticNet, Huber and XGBoost. Only the Huber Regressor had its hyperparameters tuned, including the threshold δ (epsilon); to guard against overfitting, early stopping on the validation MAE is used — training stops if there is no improvement in 10 iterations. The features, the forecast horizon and the split into training and test parts are not described.

Availability is computed. The optimum radio frequency is 0.85 of the MUF. From it the free-space loss and ionospheric absorption are calculated; fading is modelled with a Rayleigh distribution with parameter 0.7, the fade depth is 8 dB, the receiver noise figure 8 dB, the noise temperature 290 K and the coding gain 5 dB. From the SNR the BPSK bit error probability is found through the complementary error function, and availability is the share of samples in which it does not exceed 10⁻⁵. The same computation is run for the real and the forecast MUF, and the results are compared by availability, SNR and bit error rate (BER) with MAE and MSE; deviations are shown on “date — time of day” heat maps.

## Results

Availability by season, per cent (real, forecast; difference in percentage points): spring — 92.47, 92.03, −0.44; summer — 94.09, 94.56, +0.47; autumn — 92.45, 92.63, +0.18; in the “winter” row — 93.23, 93.46, +0.23. Mean annual availability is 93.23 % from the real MUF and 93.46 % from the forecast one. The mean corrected SNR is 11.79 dB for real data and 11.73 dB for forecast data (a difference of 0.06 dB); the RMS error of the SNR forecast is about 4.18 dB. The BER averages 2.76·10⁻⁴ for both the real and the forecast course; the MAE of the BER forecast is no more than 5·10⁻⁴.

The heat maps show deviations of availability higher by day than by night in all seasons: the median daytime deviation is up to 8.33 %, the maximum up to 50 % in autumn and winter; at night the median is 0 % (4.17 % in summer), the maximum 25 to 42 %, the winter mean 2.43 %. The daily window in which about 80 % of the periods with nonzero deviations are concentrated widens in spring from 8 to 24 hours, stays at 24 hours in summer, narrows in autumn from 18 to 10 hours and in winter from 15 to 7.

## Authors' conclusions

The MUF forecast reproduces availability, SNR and BER with accuracy sufficient for practical use in adaptive radio communication systems; for the MUF the authors claim a deviation of less than 0.5 %. The model slightly overestimates availability in summer and autumn and underestimates it in spring. The authors explain seasonal and diurnal differences by solar activity and geomagnetic disturbances; the next step is to take solar-activity indices into account.

## Limitations

The error of the MUF forecast itself is not given as a number, although a deviation of less than 0.5 % is claimed for the MUF; only the availability differences (from −0.44 to +0.47 percentage points) are given as numbers. Availability is obtained by computation with assumed fading and loss parameters, not by measuring BER on the path. The winter values coincide with the annual ones, and how the annual figure was obtained is not explained. The features, forecast horizon and data split are not described, and the meaning of “p-10” in the model name is not explained. The contribution of each of the three ensemble models and a comparison with other forecasts or with a simple baseline are not shown. A link between deviations and solar activity is asserted, but activity indices are not used in the computation. One path and one year are covered.

## Novelty

The paper does not claim novelty explicitly. In substance it proposes a method that compares HF channel availability from the real and the forecast MUF course for one path over one year.

## Heuristics

- **[explicit]** If an ensemble has to be made robust to outliers — tune only the component most sensitive to them (Huber: the epsilon parameter and early stopping on the validation MAE), because the ensemble already gives a boost and tuning all the models would be excessive and costly.
- **[explicit]** If the MUF forecast is meant for adaptive communication — choose the working frequency as 0.85 of the MUF rather than the MUF itself, because the MUF varies with time of day, season and solar activity.
- **[reconstructed]** If the quality of a MUF forecast is checked for adaptive communication — compare not only the MUF but also availability, SNR and BER on the real and forecast course, because those are what the user cares about.
- **[reconstructed]** If the error depends on time of day and season — look at “date — time of day” heat maps, because the mean annual difference of 0.23 percentage points hides daytime deviations of up to 50 %.
- **[reconstructed]** If forecast and real availability are compared — compute it by season, because the sign of the difference changes (−0.44 in spring, +0.47 in summer) and in the annual figure seasonal deviations of opposite sign may offset each other.

**In one sentence:** The availability of the Cyprus – Yoshkar-Ola HF channel for 2023, computed from a MUF forecast by an ElasticNet, Huber and XGBoost ensemble, came to 93.46 % against 93.23 % from the real MUF.
