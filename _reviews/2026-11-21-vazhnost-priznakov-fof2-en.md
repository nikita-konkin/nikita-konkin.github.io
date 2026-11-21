---
title: "Analysis of feature importance in machine-learning forecasts of foF2 and MUF compared with IRI-2020 and an analytical model"
pair: vazhnost-priznakov-fof2
lang: en
date: 2026-11-21
translation_of: 2026-11-21-vazhnost-priznakov-fof2.md
summary: "The author compared 24 h forecasts of the F2-layer critical frequency and the maximum usable frequency using observations from the Nicosia ionosonde. RandomForest achieved a higher coefficient of determination than IRI-2020 in all four seasons, and hour_cos became the leading feature in summer with a 70–85% share of feature importance."
paper_title: "Analysis of feature importance in machine-learning forecasts of foF2 and MUF compared with IRI-2020 and an analytical model"
paper_authors: "Korotkova N.A. (supervisor — Konkin N.A.)"
paper_year: 2026
paper_date: "2026"
paper_venue: "Scientific Progress — Creativity of the Young, 2026, no. 1, pp. 719–722"
paper_link: "https://www.elibrary.ru/item.asp?id=93329698"
tags: [ionosphere, foF2, MUF, machine-learning, RandomForest, feature-importance]
---

## Problem and relevance

The F2-layer critical frequency (foF2) and the maximum usable frequency (MUF) are used to plan shortwave radio links. According to the author, the International Reference Ionosphere model IRI-2020 loses accuracy during geomagnetic disturbances.

## Aim and hypothesis

The author compares forecasts of foF2 and MUF from machine learning, IRI-2020 and an analytical model. A second aim is to track seasonal changes in feature importance. The paper does not say what hypothesis was tested.

## Materials and methods

Hourly observations from the DPS-4D NICOSIA ionosonde (NI135) came from DIDBase, the archive of the Global Ionospheric Radio Observatory (GIRO), and covered December 2024 to November 2025. RandomForest, XGBoost and ElasticNet forecast both frequencies 24 h ahead in each season using rolling training windows of 7, 14, 21 and 30 days. Inputs included 22 ionospheric parameters and trigonometric features representing daily and annual cycles. Training excluded IRI features.

IRI-2020 was run through PyIRI at F10.7 = 150 SFU (solar flux units). MUF was calculated as M(3000)F2 × foF2. The analytical model recovered foF2 from total electron content (TEC) and M(3000)F2 from hmF2 using the Shimazaki formula. The author measured forecast performance with the coefficient of determination, R², and RandomForest feature importance with the weighted mean decrease in variance over the ensemble nodes (MDI).

## Results

For foF2, the text gives RandomForest R² values of 0.87–0.89 in winter and 0.41–0.53 in summer. It reports R² ≈ 0.58 in winter and values from −0.96 to −1.32 in summer for IRI-2020. For MUF, the text reports the largest RandomForest lead over IRI-2020 in summer (ΔR² ≈ +0.30). TEC led in winter and autumn (80–90%), and hour_cos, the cosine encoding of the hour, led in summer (70–85%). The author reports the same seasonal feature rankings for MUF.

## The author's conclusions

The author concludes that RandomForest achieves higher R² than IRI-2020 for both frequencies in all four seasons. The author reports the largest gap for foF2 in spring (R² of 0.28–0.66 for RandomForest and −0.87 for IRI-2020). The author attributes the change in the leading summer feature to the sporadic E layer screening the F2 layer and weakening the relationship between TEC and foF2.

## Limitations

The comparison covers one station and one year of observations. The paper does not say how the 1.8% advantage reported in the abstract was calculated. The sentence comparing the analytical model with IRI-2020 in summer is ambiguous.

## Novelty

The paper makes no explicit novelty claim. It combines a seasonal comparison of forecasts for two frequencies with a RandomForest feature importance analysis.

## Heuristics

- **[reconstructed]** If forecasting across several seasons, assess feature importance by season because a daily-cycle feature can overtake a measured parameter.

**In one sentence:** In the seasonal 24 h forecasts, RandomForest achieved higher R² than IRI-2020, and hour_cos overtook TEC as the leading feature in summer.
