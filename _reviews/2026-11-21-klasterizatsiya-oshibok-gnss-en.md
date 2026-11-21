---
title: "The dependence of GNSS pseudorange-error clustering quality on geomagnetic observation conditions"
pair: klasterizatsiya-oshibok-gnss
lang: en
date: 2026-11-21
translation_of: 2026-11-21-klasterizatsiya-oshibok-gnss.md
summary: "On real data from the AKSU station (November 2025 — March 2026) three pseudorange-anomaly methods — DBSCAN, IQR and Isolation Forest — are compared in quiet and disturbed periods. The hypothesis that geomagnetic storms degrade clustering was not confirmed: the Mann–Whitney test found no significant differences (p ≥ 0.806), and DBSCAN showed the best precision–recall balance on average (F1 ≈ 53.8%)."
paper_title: "The dependence of GNSS pseudorange-error clustering quality on geomagnetic observation conditions"
paper_authors: "Kombarov K.N. (supervisor — Konkin N.A.)"
paper_year: 2026
paper_date: "2026"
paper_venue: "Scientific Progress — Creativity of the Young, 2026, no. 1, pp. 716–719"
paper_link: "https://www.elibrary.ru/item.asp?id=93329697"
tags: [GNSS, pseudorange, clustering, DBSCAN, isolation-forest, geomagnetic-storm]
---

## Problem and relevance

The positioning quality of global navigation satellite systems (GNSS) depends on how well the signal-processing algorithms single out anomalous pseudorange outliers. Geomagnetic storms add ionospheric and equipment error and, as is assumed, may degrade the work of such algorithms.

## Aim and hypothesis

The aim is to study how the clustering quality of GNSS pseudorange errors depends on the geomagnetic observation conditions. The hypothesis is explicit: in periods of geomagnetic storms the clustering accuracy is statistically significantly lower than in quiet periods.

## Materials and methods

Observations from the AKSU station (SmartNet) from November 2025 to March 2026 were used: 6 days with geomagnetic storms and 5 without, labelled by an expert as “quiet” and “storm”. Three outlier-detection methods are compared: DBSCAN (density clustering), the interquartile-range method IQR (points beyond 1.5×IQR from the quartiles) and Isolation Forest (isolating anomalies on random trees). Precision, recall and F1 were computed for each; the comparison was made per date and on average over the groups. The hypothesis was tested with the Mann–Whitney U test at α = 0.05; the null hypothesis is that there is no difference between quiet and disturbed conditions. The test involves 5 quiet and 4 disturbed epochs with an expert score above 0.

## Results

On average over the epochs with an expert score above 0, DBSCAN gives the best balance of precision and recall (Precision ≈ 53.2%, Recall ≈ 63.6%, F1 ≈ 53.8%), IQR the highest recall (≈ 68.1%) at the cost of false alarms (Precision ≈ 43.3%, F1 ≈ 45.8%), and Isolation Forest the lowest effectiveness (Precision ≈ 38.8%, Recall ≈ 56.0%, F1 ≈ 42.9%). There is no stable drop in quality in storm periods: in the quiet epoch of 14.11.2025 DBSCAN reached F1 = 75%, while in the storm epoch of 03.12.2025 it reached F1 = 100%; the spread of the metrics within each group overlaps. In March 2026 (expert score 0) all three algorithms fired falsely: DBSCAN marked 5 and 5 points, IQR 88 and 167, Isolation Forest 22 and 22, and the author concludes that the algorithms are prone to false alarms regardless of geomagnetic activity. The Mann–Whitney test on the F1 measure found no statistically significant difference between the groups for any algorithm (H₀ not rejected): DBSCAN U = 8.5 (p = 0.806), IQR U = 11.5 (p = 0.806), Isolation Forest U = 11.0 (p = 0.902).

## The author's conclusions

DBSCAN is the most balanced algorithm for singling out GNSS pseudorange anomalies. The author concludes that geomagnetic storms do not cause a systematic drop in clustering quality: the metrics are volatile in both quiet and disturbed conditions. The hypothesis that storms reliably degrade the algorithms is not confirmed: no significant differences between the groups were found (p ≥ 0.806).

## Limitations

The amount of data is small: the test rests on 5 quiet and 4 disturbed epochs, and the step from the 6 storm days stated at the outset to the 4 epochs with an expert score above 0 is not explained. The metrics are computed against the expert labels, and the criteria for assigning an epoch to “storm” or “quiet” are not given. The exact algorithm parameters (for instance, the radius and minimum number of points of DBSCAN) are not provided. Only the F1 measure is used in the significance test, and the samples of 5 and 4 epochs are small; the power of the test is not discussed.

## Novelty

The paper claims no novelty explicitly. In substance it compares three pseudorange-anomaly methods on real AKSU data and statistically tests the hypothesis that geomagnetic storms affect clustering quality.

## Heuristics

- **[reconstructed]** If anomalous GNSS pseudorange outliers are to be singled out — start with DBSCAN, because on these data it gave the best balance of precision and recall compared with IQR and Isolation Forest.
- **[explicit]** If the samples are small and the distribution of the metrics is not guaranteed to be normal — test the group difference with the Mann–Whitney U test, because it does not require normality.
- **[reconstructed]** If clustering metrics are compared day by day — look at the spread within the groups, not only at the means, because high volatility masks a possible effect.
- **[reconstructed]** If an algorithm reports outliers where the expert score is 0 — check it for false alarms separately, because false alarms may be independent of geomagnetic activity.

**In one sentence:** On AKSU data from November 2025 to March 2026 the Mann–Whitney test found no significant difference in the clustering quality of pseudorange errors between quiet and storm periods (p ≥ 0.806), and DBSCAN showed the best balance of precision and recall (F1 ≈ 53.8%).
