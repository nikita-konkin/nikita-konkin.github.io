---
title: "Correlation analysis of predictors of the Earth's ionospheric total electron content"
pair: korrelyatsiya-prediktorov-pes
lang: en
date: 2026-11-21
translation_of: 2026-11-21-korrelyatsiya-prediktorov-pes.md
summary: "Correlations between the total electron content, the maximum usable frequency and the coherence bandwidth of a transionospheric channel were analysed over 40 days of data. The MUF–TEC correlation is highest over one day and falls below 50 % by the ninth day, while the TEC–coherence-bandwidth link is negative and strong on all days."
paper_title: "Correlation analysis of predictors of the Earth's ionospheric total electron content"
paper_authors: "Konkin N.A., Pasova A.D."
paper_year: 2022
paper_date: "2022"
paper_venue: "Scientific Progress — Creativity of the Young, 2022, no. 1, pp. 328–330"
paper_link: "https://www.elibrary.ru/item.asp?id=49901168"
tags: [ionosphere, TEC, MUF, coherence-bandwidth, correlation-analysis, machine-learning]
---

## Problem and relevance

Forecasting the parameters of shortwave and satellite communication systems with machine learning requires data preparation: filtering, treating outliers, recovering missing values and running a correlation analysis of the predictors. Such an analysis shows how the forecasting means affect the final accuracy of the model.

## Aim and hypothesis

The aim is to determine the correlation dependencies between the predictors and, from them, to judge how suitable each line parameter is for analysing the coherence bandwidth. No hypothesis is stated explicitly.

## Materials and methods

The values of the total electron content (TEC), the coherence bandwidth and the maximum usable frequency (MUF) were used as training data. The MUF is usable because the transionospheric lines lie in the skip region of the Cyprus — Yoshkar-Ola shortwave path. The correlation analysis was run on 40 days of data with the Python pandas library, yielding correlation and scatter matrices for one and for forty days.

## Results

The correlation between the MUF and the TEC is highest over one day and almost absent over forty. The dependence of the correlation coefficient on the number of days shows the ninth day as the boundary: there the coefficient falls below the 50 % threshold. The correlation between the TEC and the coherence bandwidth is negative and strong throughout all the days. In the end all the chosen predictors are suitable for analysing the coherence bandwidth; the MUF data combined over at most 8 days will be the most valuable in modelling, while the TEC and coherence bandwidth values are unchanged over any interval.

## Authors' conclusions

The results apply to building models for a single day or to cluster analysis, because the parameters of the HF and transionospheric channels were estimated by accumulation (overlaying) rather than by temporal analysis.

## Limitations

A 50 % threshold and a boundary day are given, but the paper does not say how the threshold was chosen or which correlation coefficient was used (Pearson's or another). Apart from the ranges on the plot, the numerical coefficient values are not named in the text. The station, the observation period and how the data were accumulated over 40 days are not described.

## Novelty

No novelty is claimed explicitly. In substance the paper establishes the allowed accumulation horizon for the predictors (up to 8 days for the MUF) and the sign of the TEC–coherence-bandwidth link for forecasting the coherence bandwidth.

## Heuristics

- **[reconstructed]** If the correlation between predictors falls as the accumulation window grows — cap the window at the day where the coefficient drops below the threshold (here 50 %, the ninth day for the MUF and the TEC), because the authors recommend combining the MUF data over at most 8 days.
- **[reconstructed]** If the link between two predictors keeps its sign and high magnitude on all days — treat it as stable for single-day models or cluster analysis, because in the paper the TEC–coherence-bandwidth link is negative and high on all days.
- **[reconstructed]** If the parameters were estimated by overlaying rather than in time order — apply the result only to single-day models or cluster analysis, because the temporal dynamics are lost that way.

**In one sentence:** All three predictors are suitable for forecasting the coherence bandwidth, but the MUF should be accumulated over no more than 8 days, while the TEC–coherence-bandwidth link is negative and stable.
