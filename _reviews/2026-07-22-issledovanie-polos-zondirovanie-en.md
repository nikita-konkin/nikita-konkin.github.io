---
title: "A study of coherence bandwidths in trans-ionospheric sounding"
pair: issledovanie-polos-zondirovanie
lang: en
date: 2026-07-22
translation_of: 2026-07-22-issledovanie-polos-zondirovanie.md
summary: "Software and an AutoIt algorithm for building electronic diagnostic coherence-bandwidth maps from GPS/GLONASS data, with a PostgreSQL database used as an index over the intermediate .dat files."
paper_title: "A study of coherence bandwidths in trans-ionospheric sounding"
paper_authors: "Konkin N.A. (supervisor — Chernov A.A.)"
paper_year: 2019
paper_date: "2019"
paper_link: "https://www.elibrary.ru/item.asp?id=41468023"
tags: [ionosphere, coherence-bandwidth, trans-ionospheric-sounding, PostgreSQL, AutoIt, mapping]
---

## Problem and relevance

As a propagation medium the ionosphere substantially affects navigation, ranging and communication systems, and its influence on the quality of satellite and decametre communication signals has long been noted. Given the variability of the ionosphere, radio sounding methods that yield information about its state in real time take the leading role in its study. The authors tie further progress to improving measurement techniques through the development of algorithms for processing experimental data, mathematical modelling and digital methods of secondary processing.

## Aim and hypothesis

To develop techniques and algorithms for studying coherence bandwidths in oblique and trans-ionospheric sounding of the Earth's ionosphere. No hypothesis is stated.

## Materials and methods

The algorithm draws on data from oblique and trans-ionospheric sounding with GPS/GLONASS signals, collected into a single base of RINEX files, and is implemented in AutoIt.

At the first stage RINEX files are converted into the .dat format by the TecSuite program, whose operation is automated from AutoIt; in parallel, information about these .dat files is written into a PostgreSQL database, with the record labelled differently depending on whether the files existed previously or had only just been converted. The database serves fast access to the required files and the systematisation of the information obtained. Access is provided by a dedicated query to PostgreSQL, composed by the operator according to the territory of interest and the time span; the query assembles a folder containing the necessary .dat files.

At the second stage the assembled set is automatically reprocessed into the format required for map building. Coherence-bandwidth maps are built from the resulting information in the .dat elements automatically by means of GNU Plot.

## Results

One coherence-bandwidth map is given (Fig. 1): longitude on the abscissa, latitude on the ordinate, with coloured points marking the locations where the bandwidth value was measured. The map is presented as an animated .gif image in which the points move dynamically and change colour according to the level of TEC, their movement depending on time and coordinates. The authors note that similar maps can be built for any part of the globe given the corresponding GLONASS/GPS data. The region, the date and the range of bandwidth values obtained are not stated in the paper.

## Authors' conclusions

Software for studying coherence bandwidths in trans-ionospheric sounding has been developed, and an algorithm for creating electronic diagnostic coherence-bandwidth maps has been developed and implemented.

## Limitations

The conclusion claims results from computational and full-scale experiments, yet their conditions and numerical values are absent from the text. The sole reference [1] concerns the mathematical simulation of chirp radio wave propagation and does not support the statement about implementation in AutoIt to which it is attached; the colour scheme of the map is tied to the level of TEC while the map itself is called a coherence-bandwidth map.

## Novelty

The development of software and of a map-building algorithm is claimed. No demarcation from earlier work on the topic is drawn in the text, and the stated aim coincides with the title of a separate publication in the same area.

## Heuristics

- **[stated]** If source files are converted into a working format — then write information about the resulting files into a database in parallel, because otherwise there is no complete picture of how much data and which data are available for map building.
- **[stated]** If some files existed before conversion — then label them separately in the database, because this distinguishes inherited from newly obtained data.
- **[reconstructed]** If a selection is needed by territory and time span — then form it as a database query that assembles a folder of files, because this separates data selection from computation and makes the selection repeatable.
- **[reconstructed]** If the pipeline includes third-party software with no automation interface — then drive it through GUI automation, because that brings it into the automated flow without rewriting it.

**In one sentence:** AutoIt software builds coherence-bandwidth maps from GPS/GLONASS data, using PostgreSQL as an index over the intermediate .dat files.
