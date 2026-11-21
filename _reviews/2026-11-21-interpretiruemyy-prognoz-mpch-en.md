---
title: "Interpretable Forecasting of the Maximum Usable Frequency of HF Radio Links Using Mid-Latitude Ionosonde Data"
pair: interpretiruemyy-prognoz-mpch
lang: en
date: 2026-11-21
translation_of: 2026-11-21-interpretiruemyy-prognoz-mpch.md
summary: "Using ionosonde data from four mid-latitude GIRO stations for December 2024 to November 2025, SHAP is applied to the feature structure of three models (ElasticNet, RandomForest, XGBoost) forecasting the MUF 24 hours ahead. In winter the lagged features carry 35–54 % of the total importance, in summer the share of the diurnal component hour_cos grows (27–46 % at AT138 and NI135); the summer R² of the machine-learning models at AT138 is close to zero."
paper_title: "Interpretable Forecasting of the Maximum Usable Frequency of HF Radio Links Using Mid-Latitude Ionosonde Data"
paper_authors: "Korotkova N.A., Konkin N.A."
paper_year: 2026
paper_date: "2026"
paper_venue: "Infocommunication and Radio Technologies, 2026, vol. 9, no. 6, pp. 1149–1170"
paper_link: "https://www.elibrary.ru/item.asp?id=93447831"
tags: [ionosphere, MUF, machine-learning, SHAP, interpretability, ionosonde]
---

## Problem and relevance

The critical frequency of the F2 layer (foF2) and the maximum usable frequency (MUF) are key parameters for planning HF communication; the MUF sets the upper limit of working frequencies of an HF link. The IRI-2020 model shows systematic biases: for the NICOSIA station in 2024–2025 the model median of foF2 was 9.04 MHz against an observed 7.30 MHz (an overestimate of 24 %); the analytical model based on total electron content (TEC) and the height hmF2 gives 5.42 MHz. Machine-learning models capture nonlinear relations, but a single error value does not show which features they rely on.

## Aim and hypothesis

The aim is to link the seasonal dynamics of the ionosphere with the structure of the features that machine learning uses when forecasting the MUF. No hypothesis is stated explicitly; in substance the paper tests that the feature structure changes with the season and that this picture repeats across models of different architecture. The authors use SHAP not as proof of a physical mechanism but as a way to compare the features of the models and of the physical baselines.

## Materials and methods

The data come from DPS-4D ionosondes of four stations of the GIRO network at a 15-minute step, December 2024 to November 2025: ATHENS (AT138, 38.0° N), El Arenosillo (EA036, 37.1° N), NICOSIA (NI135, 35.0° N) and San Vito (VT139, 40.6° N). Samples with a confidence score CS ≥ 50 or CS = 999 were kept. The target is the MUF 24 hours ahead, smoothed with a causal one-sided Savitzky — Golay filter. Features were selected anew for each training split; in the first evaluation split, 22 to 28 features were kept across the four stations: the lagged foF2_state and MUFD_state, hmF2, scaleF2, B0, B1, a TEC proxy, the cyclic time encodings (hour_sin, hour_cos, month_sin, month_cos) and others.

The models are ElasticNet, RandomForest and XGBoost (hyperparameters tuned by Optuna). The scheme is walk-forward: training on the preceding 7, 21 or 28 days, a forecast for the next 24 hours; the main analysis uses the 21-day window. The reference baselines are IRI-2020 and an analytical model based on TEC, hmF2 and a fixed layer thickness; their features were not fed to the models. Feature importance is the normalized mean |SHAP| over the test sample as a percentage of the sum, smoothed over 14 days.

## Results

The median R² for the 21-day window: AT138 0.697, EA036 0.537, NI135 0.671, VT139 0.571. In winter at AT138 XGBoost and RandomForest give R² 0.926 and RMSE 2.80 MHz, IRI-2020 gives R² 0.823 and RMSE 4.331 MHz. In summer R² at AT138 is close to zero (0.070–0.156) at an RMSE of 3.15–3.30 MHz, close to the winter level; IRI-2020 has R² −0.530. At EA036 in summer IRI-2020 (R² 0.293) and ElasticNet (0.240) beat RandomForest and XGBoost. At VT139 in winter ElasticNet gives R² 0.478 and XGBoost 0.884.

The feature structure repeats across the three models. In winter the lagged variables carry 35–54 % of the total importance; in summer their share falls (to 9.5–16.5 % at AT138) and hour_cos becomes the leading feature: 27–46 % at AT138 and NI135. At EA036 hour_sin is more prominent in summer (19–25 %), and the authors suggest a shift of the daily MUF maximum relative to noon. At VT139 hour_cos stays the leader all year (23–47 % according to the paper's conclusion). At NI135 RandomForest and XGBoost give TEC 18.8 % and 19.5 % in winter, ElasticNet 3.2 %. A high TEC share does not mean high quality: in the analytical baseline at NI135 it is 81.8 % in summer at R² −1.36. The picture holds for windows of 7 and 28 days.

## Authors' conclusions

The seasonal restructuring of the feature structure is stable across models and windows, but its physical interpretation needs checking. The share of lagged features may serve as a diagnostic indicator of the seasonal regime: a drop to 20–25 % may point to a summer regime with lower day-to-day predictability. A single model without station-specific adaptation may be unstable; the thresholds need testing, the SHAP profiles need comparing with independent geophysical parameters, and the network of stations needs widening.

## Limitations

The authors call the results preliminary: the 20–25 % threshold and the 3–6 hour shift estimate at EA036 are still to be verified, and the SHAP profile is regarded as diagnostic. From the outside: one year and four stations; at AT138 in summer the R² of the machine-learning models is close to zero, so the feature structure describes models that explain little of the day-to-day variability. In Table 13 for VT139 the hour_cos share for ElasticNet is 20.90 % in summer and 22.00 % in autumn, below the lower bound of 23 % in the conclusion. The smoothing parameters, the layer thickness in the analytical baseline, the Optuna search space and the test-sample sizes are not given. There are no confidence intervals or tests of significance of the differences.

## Novelty

The paper does not claim novelty explicitly. In substance, the feature structure of MUF forecasting models by season and station is compared with that of two physical baselines.

## Heuristics

- **[explicit]** If you need to understand what a model relies on — compute the share of |SHAP| per feature instead of judging by a single error, because the error does not show which features drove the result.
- **[explicit]** If a pattern is offered as robust — check it on several models and training windows, because a common seasonal course lowers the chance that one algorithm is responsible.
- **[explicit]** If the forecast is built on a rolling scheme — use walk-forward and causal smoothing, because future values then stay out of training.
- **[reconstructed]** If RMSE is close to the winter level while R² is near zero — the forecast carries no information on day-to-day variability, so judge quality by both metrics.

**In one sentence:** SHAP analysis showed that in 24-hour MUF forecasting the models rely on lagged features in winter (35–54 % of importance) and on the diurnal component hour_cos in summer (27–46 % at AT138 and NI135), but the summer R² of the machine-learning models at AT138 is near zero and the authors regard the conclusions as preliminary.
