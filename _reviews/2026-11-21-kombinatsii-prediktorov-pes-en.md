---
title: "Studying the accuracy of recovering seasonal TEC values with a machine-learning method and different predictor combinations"
pair: kombinatsii-prediktorov-pes
lang: en
date: 2026-11-21
translation_of: 2026-11-21-kombinatsii-prediktorov-pes.md
summary: "The accuracy of recovering seasonal TEC values is compared across different combinations of dynamic predictors — shifted, differentiated and percentage ones. The best accuracy is reached at predictor steps from 6 to 24 (mean absolute error within 0.21, mean-square deviation within 0.5 TECu), and a further increase in the step lowers R² from 0.9 to 0.7."
paper_title: "Studying the accuracy of recovering seasonal TEC values with a machine-learning method and different predictor combinations"
paper_authors: "Vershinin M.V. (supervisor — Konkin N.A.)"
paper_year: 2025
paper_date: "2025"
paper_venue: "Scientific Progress — Creativity of the Young, 2025, no. 1, pp. 481–483"
paper_link: "https://www.elibrary.ru/item.asp?id=83009905"
tags: [ionosphere, TEC, machine-learning, dynamic-predictors, data-recovery]
---

## Problem and relevance

The total electron content (TEC) is an integral characteristic of the ionosphere on which radio propagation, navigation and satellite systems depend. TEC data can be lost through instrument failures, geomagnetic storms or a sparse monitoring network, so they have to be recovered.

## Aim and hypothesis

The aim is a comparative analysis of the accuracy of recovering TEC values with different combinations of machine-learning dynamic predictors. The tasks are to prepare a dataset with predictor combinations and to carry out the comparative analysis. No hypothesis is stated explicitly.

## Materials and methods

To recover TEC, a set of predictors is formed. The dynamic predictors are shifted (a shift of historical TEC values by n samples forward), differentiated shifted (the difference between two past values) and percentage differentiated shifted (the percentage difference between two past values); they are added as separate columns without changing the source data. A combination is written in the n_d_p format, where n, d, p are the steps of the simple, differentiated and percentage shifts. The text says the step ranged from 12 to 48 with a step of 12, while Figure 1 uses a range from 6 to 48 with a step of 6. The name of the specific ensemble machine-learning method is not given in the text.

## Results

The comparative analysis showed that the highest accuracy is reached at predictor steps from 6 to 24: the mean absolute error is within 0.21 and the mean-square deviation within 0.5 TECu. A further increase in the step raises MAPE by 0.1 and MSE by 0.4 TECu and lowers the coefficient of determination R² from 0.9 to 0.7.

## The author's conclusions

The best combination of dynamic predictors is at steps from 6 to 24; increasing the step markedly worsens the recovery accuracy.

## Limitations

The name of the ensemble machine-learning method used is not given. There is a mismatch in the step range: the text says 12–48 with a step of 12, while Figure 1 uses 6–48 with a step of 6. The metrics are called "mean absolute error" and "mean-square deviation" in one place and MAPE and MSE in another. Accuracy is assessed from a single figure without a numerical table.

## Novelty

The paper does not claim novelty explicitly. In substance it enumerates combinations of three kinds of dynamic predictor and shows how their step affects the accuracy of TEC recovery.

## Heuristics

- **[explicit]** If the source data are scarce — add dynamic predictors (shifted, differentiated, percentage) as separate columns, because they enlarge the dataset without changing the source values.
- **[explicit]** If predictor steps are being tuned — keep them in the 6–24 range, because beyond it MAPE and MSE rise and R² falls from 0.9 to 0.7.
- **[reconstructed]** If predictor combinations are compared — encode them in the compact n_d_p format, because this lets the step combinations be enumerated on a single plot.

**In one sentence:** The accuracy of recovering seasonal TEC values is highest at dynamic-predictor steps from 6 to 24 (mean absolute error within 0.21, mean-square deviation within 0.5 TECu), and increasing the step lowers R² from 0.9 to 0.7.
