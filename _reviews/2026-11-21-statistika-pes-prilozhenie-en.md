---
title: "An application for statistical analysis of total electron content values"
pair: statistika-pes-prilozhenie
lang: en
date: 2026-11-21
translation_of: 2026-11-21-statistika-pes-prilozhenie.md
summary: "A prototype JavaScript web application was developed for the statistical analysis of total electron content values by station and time range. The application computes means and variance, plots the TEC, and exports the statistics to .csv and the plots to .png."
paper_title: "An application for statistical analysis of total electron content values"
paper_authors: "Shtyrkin I.O. (supervisor — Konkin N.A.)"
paper_year: 2023
paper_date: "2023"
paper_venue: "Scientific Progress — Creativity of the Young, 2023, no. 2, pp. 26–28"
paper_link: "https://www.elibrary.ru/item.asp?id=54740363"
tags: [TEC, statistical-analysis, web-application, JavaScript, transionospheric-sounding, interface]
---

## Problem and relevance

To analyse the state of the channel to a satellite, transionospheric sounding is used, whose characteristic is the total electron content (TEC): the total number of electrons in a column of unit cross-section through the ionosphere. The TEC changes under solar ultraviolet radiation, geomagnetic storms and atmospheric waves rising from the lower atmosphere, so its values need statistical analysis.

## Aim and hypothesis

The aim is to build a web application for the statistical analysis of TEC values by the stations and time range of interest. No hypothesis is stated: the work is engineering.

## Materials and methods

The application is written in JavaScript. In block 1 the user sets the time intervals and stations for which the TEC data files are loaded. In block 2 the means for the days and the variance are computed with the formula s² = (n·Σx² − (Σx)²)/(n·(n−1)), where n is the sample size and Σx the sum of all values; the mean is x = Σx/n. Block 3 plots the TEC for the days and downloads it as .png, and block 4 exports the statistical characteristics as .csv. Blocks 5–7 do the same for the station means: computing the means, the plot with .png export, and the .csv export of the statistics.

## Results

A prototype application was developed for computing the statistical characteristics of the TEC by station and time range, with plots of the TEC against the chosen time and stations.

## The author's conclusions

The result is a working prototype that computes the statistical characteristics of the TEC and plots it for the chosen stations and time.

## Limitations

The application is described as a prototype; no numerical results, no comparison with computation in other tools and no testing details are given. The paper does not say where the TEC files come from or in what format they arrive.

## Novelty

No novelty is claimed explicitly. In substance the paper offers a web tool that combines loading TEC data, computing means and variance, plotting, and exporting the results to .csv and .png.

## Heuristics

- **[reconstructed]** If TEC values are analysed across different stations and days — split the interface into blocks for loading, computing statistics and showing plots, because this is how the interface of the described application is built.
- **[reconstructed]** If the result must be saved — export the plots as .png and the statistics as .csv, because these formats suit reports and later analysis.

**In one sentence:** A prototype JavaScript web application computes the means and variance of TEC values for chosen stations and days, plots them, and exports the results to .csv and .png.
