---
title: "Finding statistical regularities in TEC data during disturbed and quiet ionospheric periods"
pair: statistika-vozmushcheniy-pes
lang: en
date: 2026-11-21
translation_of: 2026-11-21-statistika-vozmushcheniy-pes.md
summary: "The expectation, variance and standard deviation are applied; for each day of 2022 the mean TEC from stations at different distances from the equator is computed and matched against the days of magnetic storms. On quiet days the mean TEC was about 11.98 TECU, it rose to 16 TECU before a storm, and during solar activity it fell by 4 TECU on average."
paper_title: "Finding statistical regularities in TEC data during disturbed and quiet ionospheric periods"
paper_authors: "Zhabkina Yu.A. (supervisor — Konkin N.A.)"
paper_year: 2024
paper_date: "2024"
paper_venue: "Scientific Progress — Creativity of the Young, 2024, no. 1, pp. 301–303"
paper_link: "https://www.elibrary.ru/item.asp?id=69910527"
tags: [ionosphere, TEC, statistical-analysis, magnetic-storms, solar-activity]
---

## Problem and relevance

The total electron content (TEC) is the number of electrons along a column of one square meter in cross section; its unit is the TECU (1 TECU = 10¹⁶ m⁻²). Changes in TEC affect the quality of radio communication; according to the author, studying them makes it possible to predict magnetic storms, so it matters how solar activity acts on TEC.

## Aim and hypothesis

The aim is to find statistical regularities in TEC data when analyzing periods of disturbed and quiet ionosphere. The tasks are to study the influence of solar activity on TEC and to find the regularities. No hypothesis is stated explicitly.

## Materials and methods

To find the regularities, the expectation, variance and standard deviation are computed. For each day of 2022 the mean TEC obtained from stations at different distances from the equator is calculated, and a plot of this value against the date is built for each month. The days of magnetic storms are taken from the solar astronomy laboratory website.

## Results

During periods of solar activity the TEC values decrease in most cases; the average drop across all stations was 4 TECU. On quiet days the values are even and may rise, reaching their peak at the moment a magnetic storm appears. An example is the plot for August 2022: during the storm a decrease in TEC is visible, and before it the TEC rises in some cases and falls in others. The author suggests that the flow of charged particles from the Sun increases, which may raise the electron density and may cause a decrease in TEC, since the radio signal has a harder time passing through the denser medium.

## The author's conclusions

On quiet days the mean TEC over all months of 2022 was about 11.98 TECU; before a storm it rose to 16 TECU, and at the moment of solar activity it fell by 4 units.

## Limitations

The daily computation of the variance and standard deviation is not described in the text; Fig. 1 shows the expectation against the date. Storm prediction is not tested in the paper. The stations, their coordinates and number are not given, nor is the way disturbed days are identified. The conclusion linking TEC to storms rests on a visual inspection of the plots, with no quantitative measure of the relationship. The example is limited to August 2022.

## Novelty

The paper does not claim novelty explicitly. In substance it applies basic statistics (expectation, variance, standard deviation) to TEC series and matches them against the days of magnetic storms.

## Heuristics

- **[explicit]** If TEC behavior is to be compared across periods — compute the expectation, variance and standard deviation, because they characterize the central tendency, the variation and the spread of a random variable.
- **[reconstructed]** If TEC is considered across stations at different latitudes — average the values over all stations, because the average drop across stations smooths local differences.
- **[reconstructed]** If a link to a magnetic storm is checked — mark the storm day separately on the plot, because TEC behaves differently before and during a storm: a decrease is visible during the storm, while before it TEC rises in some cases and falls in others.

**In one sentence:** In the 2022 data the mean TEC on quiet days was about 11.98 TECU, rose to 16 TECU before a magnetic storm, and fell by 4 TECU on average at the moment of solar activity.
