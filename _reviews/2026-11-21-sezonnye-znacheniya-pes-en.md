---
title: "Study of the accuracy of seasonal PES values recovery based on machine learning and dynamic predictors"
pair: sezonnye-znacheniya-pes
lang: en
date: 2026-11-21
translation_of: 2026-11-21-sezonnye-znacheniya-pes.md
summary: "An ensemble machine-learning model with dynamic (shifted) predictors restores gaps in total electron content from nine stations in the Samara region for 2021; the restoration of 6, 12, 24 and 48 half-hourly samples is tested for the station in Samara. For 48 samples the forecast metrics on restored and on real data differ by less than 0.6 % in R² and less than 4.3 % in MAE; in summer the standard deviation (MSE) leaves the confidence interval."
paper_title: "Study of the accuracy of seasonal PES values recovery based on machine learning and dynamic predictors"
paper_authors: "Ryabova N.V., Konkin N.A., Vershinin M.V."
paper_year: 2025
paper_date: "2025"
paper_venue: "All-Russian Open Armand Readings “Murom 2025”. Proceedings of the All-Russian Open Conference and Youth School-Conference, Murom, pp. 166–171"
paper_link: "https://www.elibrary.ru/item.asp?id=82921991"
tags: [ionosphere, TEC, GNSS, data-restoration, machine-learning, dynamic-predictors]
---

## Problem and relevance

Total electron content (TEC) data are needed to correct errors in satellite communication and navigation, but they contain gaps. The authors name the causes: equipment failures, ionospheric events (geomagnetic storms, solar flares), interference and multipath propagation, processing errors, and a low density of stations. Traditional ways of filling the gaps — interpolation, physical models, statistics — handle nonlinear dependences poorly, need accurate input parameters and do badly in extreme conditions.

## Aim and hypothesis

The aim is to assess the accuracy and applicability of restoring seasonal TEC values with an ensemble machine-learning method and dynamic predictors, depending on the season and the number of restored samples. The tasks are to develop an algorithm, to process a year of data from a network of GNSS reference stations, to compare accuracy across seasons, and to compare TEC forecasts built on restored and on original data for one station. No hypothesis is stated explicitly; in substance the paper tests that restored data hardly degrade the subsequent forecast.

## Materials and methods

The data are TEC for 2021 from nine GNSS reference stations of the SmartNet network in the Samara region (Samara, Koshki, Tolyatti, Chapaevsk, Kinel, Otradny, Krasnoarmeysk, Neftegorsk, Elkhovka). The stations record every 30 seconds; when RINEX files are converted to CSV the values are averaged to a 30-minute step. The set holds 17,358 samples, 17,520 after the missing time stamps are restored, with one column per station. Anomalous values and random spikes were filtered out.

The algorithm first finds a stretch without gaps for initial training; everything after it (on average 95 % of the samples) becomes the set for restoration. The set is scanned one sample at a time; for a row with gaps a template of the missing columns is built, and the feature matrix and target vector are formed from it. The model is trained and the gaps are filled. Values of neighbouring stations for the restored period may be used.

The features are extended with dynamic predictors of three kinds: shifted, differenced shifted and percentage differenced shifted. Each was shifted up to 48 times (one day back); the number of columns became 1315. The difference is taken between two past values and written to the next sample, not between the current and the previous one.

The test restored 6, 12, 24 and 48 samples for the station in Samara in every season, on real and on restored values. The metrics are R², MAE, MAPE and RMSE; for 48 samples a confidence interval is added. The paper does not name the model; it says only “an ensemble method”.

## Results

For 48 samples, the range the authors consider significant in practice, the difference in R² between restoring from real and from restored data was below 0.6 %: winter 0.068 %, spring 0.298 %, summer 0.587 %, autumn 0.217 %. The difference in MAE was below 4.3 %: winter 0.671 %, spring 1.391 %, summer 1.013 %, autumn 4.256 %.

The standard deviation (the paper's SKO; labelled MSE in the table) stayed inside the confidence interval in winter, spring and autumn. In summer it left it: by Table 1, 0.924 and 0.884 against a bound of 0.460. Summer MAPE stays within the range typical of the other seasons and, according to the conclusion, does not exceed 10 %. Absolute values of R² and MAE are shown only in the plots (Figs 3–4).

## Authors' conclusions

An algorithm for restoring TEC has been developed; the differences in R² and MAE between real and restored data are small in all seasons. The authors tie the summer excursion beyond the confidence interval to greater variability in the summer months, which they explain by maximum geomagnetic and solar activity; no features to account for it were used. A MAPE of up to 10 % is taken as an acceptable level. The abstract adds that hybrid models are suitable for restoring TEC in real time and could be built into space-weather monitoring systems. Future work: features for extreme geomagnetic conditions and a larger dataset for summer.

## Limitations

The model, its parameters and the training/test split are not described. The data cover one year and one tested station (Samara). The explanation of the summer result was not tested: features accounting for geomagnetic and solar activity were not applied. How the confidence interval was built is not explained, and real-time operation is not demonstrated. Interpolation and other simple methods are not included in the comparison. Quality is judged from the difference between forecast metrics on real and on restored data; the text gives no error of the restored samples against the hidden ones.

## Novelty

Not claimed explicitly. The abstract speaks of applying ensemble methods together with dynamic predictors; in substance the paper offers a restoration algorithm based on gap templates and an assessment of its accuracy by season and number of samples.

## Heuristics

- **[explicit]** If restoration starts from scratch — first find a stretch of the data without gaps and train on it, because initial training needs a window without gaps.
- **[explicit]** If shifted predictors are built — take the difference between two past values and write it to the next sample, so that the features contain no data that run ahead of the sample being restored.
- **[explicit]** If the data contain anomalous values and random spikes — filter them out before restoration, to avoid errors in restoration.
- **[explicit]** If the error leaves the confidence interval in a season of high geomagnetic activity — add features for extreme geomagnetic conditions and enlarge the dataset for that season.
- **[reconstructed]** If you need to know whether restoration is good enough — compare the metrics of the subsequent forecast on real and on restored data, separately by season and number of restored samples.

**In one sentence:** An ensemble model with shifted predictors restores 48 half-hourly TEC samples so that forecast metrics on restored data differ from those on real data by less than 0.6 % in R² and less than 4.3 % in MAE, while in summer the error leaves the confidence interval.
