---
title: "Assessing the influence of machine-learning predictors on the accuracy of reconstructing TEC variation trends"
pair: prediktory-variatsiy-pes
lang: en
date: 2026-11-21
translation_of: 2026-11-21-prediktory-variatsiy-pes.md
summary: "For winter, spring and summer, 512 combinations of predictor shift steps in the n_d_p format were tried to find those that minimise the TEC reconstruction error. The best combinations gave MSE 0.2–0.4 TECu and MAPE 15–17 % in winter, MSE 0.2–0.4 TECu and MAPE 7–8 % in spring, and MSE 0.15–0.25 TECu and MAPE 4–4.5 % in summer."
paper_title: "Assessing the influence of machine-learning predictors on the accuracy of reconstructing TEC variation trends"
paper_authors: "Konkin N.A., Vershinin M.V."
paper_year: 2025
paper_date: "2025"
paper_venue: "Microwave & Telecommunication Technology, 2025, no. 7, pp. 240–242"
paper_link: "https://www.elibrary.ru/item.asp?id=83095786"
tags: [ionosphere, TEC, gap-filling, predictors, seasonality, machine-learning]
---

## Problem and relevance

Total electron content (TEC) is an integral characteristic of the ionosphere: the total number of free electrons along the ray between a satellite and a ground station. Round-the-clock TEC monitoring is subject to errors, and machine learning is used to reconstruct them. According to the authors, unlike physical models it captures complex trends and seasonality, and adding predictors improves the reconstruction of gaps.

## Aim and hypothesis

The aim is to assess the influence of machine-learning predictors on the accuracy of reconstructing the trends of TEC time variations under different combinations of these predictors. No hypothesis is stated explicitly; in substance the paper tests that suitable shift steps depend on the season.

## Materials and methods

The predictors are set by the n_d_p format: n is the step of a simple shift, d of a differenced shift, p of a percentage differenced shift. The steps were enumerated in nested loops from 6 to 48 with a period of 6, 512 combinations in all. The assessment covers three seasons (winter, spring, summer) with anomaly filtering (±2 standard deviations). Besides the dynamic predictors, time features were used: year, month, day, quarter, hours, minutes and others. Gaps were created artificially. The training window moved by the reconstruction horizon and was 48 samples (one day); the reconstruction range is one sample (30 minutes).

## Results

Winter: the smallest error, MSE 0.2–0.4 TECu and MAPE 15–17 %, occurs at steps from 12_48_42 to 18_36_42; the combination 42_48_30 raises MSE to 1 TECu and MAPE to 27 %. Spring: strong metric fluctuations at steps from 6_6_6 to 24_6_6; the error minimum at steps from 24_6_42 to 42_42_42 — MSE 0.2–0.4 TECu, MAPE 7–8 %; at 42_48_30 MSE rises to 0.5 TECu and MAPE to 10 %. Summer: metric fluctuations at steps from 30_6_18 to 48_48_42; the minimum at steps from 18_6_30 to 24_46_30 — MSE from 0.15 to 0.25 TECu, MAPE from 4 to 4.5 %; at 24_48_30 MSE rises to 0.35 TECu and MAPE to 6 %.

## Authors' conclusions

Each season needs its own set of combinations. Winter is the most stable: steps from 6_6_6 to 42_42_42 give good reconstruction, since minimal solar activity reduces the influence of external factors. Summer is the least stable and needs small steps (from 12_12_12 to 18_18_18). In spring steps from 18_18_18 to 42_42_42 are optimal; a further increase in the step overloads the model and worsens the search for patterns. The abstract words it differently: in winter small (6_6_6 to 18_18_18) and medium (24_24_24 to 36_36_36) steps are acceptable, in spring and summer only medium ones.

## Limitations

The machine-learning model, the station, the year and the number of days in each season are not named. The conclusions on summer disagree: the abstract and the results section point to medium steps, the conclusion to small ones (12_12_12 to 18_18_18), and this is not explained. The metrics are described as ranges read from figures, with no baseline forecast without shifts. The explanations (low solar activity in winter, overloading of the model at large steps) were not tested. The upper bound of the summer range, 24_46_30, contains a step of 46, which is not in the described enumeration from 6 to 48 with a period of 6. One sample is reconstructed, so the result applies to short gaps.

## Novelty

The paper does not claim novelty explicitly. In substance it describes an enumeration of 512 combinations of predictor shift steps and their seasonal optima in TEC reconstruction.

## Heuristics

- **[explicit]** If TEC is reconstructed in different seasons — tune the set of shift steps separately for each season, because the optimal combinations differ.
- **[explicit]** If the season is calm in solar activity (winter) — a wide range of steps is acceptable, because external factors act more weakly.
- **[reconstructed]** If shift steps grow — watch for rising error at extreme combinations (42_48_30), because, in the authors' words, a further increase in the step overloads the model.

**In one sentence:** The best combinations of predictor shift steps depend on the season and give MAPE of 15–17 % in winter, 7–8 % in spring and 4–4.5 % in summer, but the paper's statements on summer contradict each other.
