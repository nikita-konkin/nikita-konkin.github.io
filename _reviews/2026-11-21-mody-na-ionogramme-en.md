---
title: "Echo signal detection on ionograms of ionospheric sounding with the use of machine learning methods"
pair: mody-na-ionogramme
lang: en
date: 2026-11-21
translation_of: 2026-11-21-mody-na-ionogramme.md
summary: "Oblique-sounding ionograms from the Cyprus – Yoshkar-Ola path are cleaned with whitening and median equalisation, after which k-means clustering in the RGB colour space picks out the received signal modes. Preprocessing narrows the spread of samples from 50 to 2 dB, and the smallest loss of useful signal was obtained with 11 clusters."
paper_title: "Echo signal detection on ionograms of ionospheric sounding with the use of machine learning methods"
paper_authors: "Ivanov V.A., Konkin N.A., Ovchinnikov V.V., Ryabova M.I."
paper_year: 2025
paper_date: "2025"
paper_venue: "GraphiCon 2025. Proceedings of the 35th International Conference on Computer Graphics and Machine Vision, Yoshkar-Ola, pp. 13–21"
paper_link: "https://www.elibrary.ru/item.asp?id=88853579"
tags: [ionosphere, ionogram, oblique-sounding, clustering, k-means, machine-learning]
---

## Problem and relevance

Ionograms from vertical and oblique sounding are the main source of information on the multidimensional structure of the medium in which an HF signal propagates. Using them is hindered by noise of natural and man-made origin and by the variability of the ionosphere. Interference is of two kinds: fluctuation and concentrated. The bands of concentrated interference are usually 3 kHz wide or a multiple of it, and the stationarity time of their variations is mostly not less than 10 s. Cognitive radio systems and autonomous radio sensors need automatic ionogram analysis in order to choose frequency channels with the best signal-to-noise ratio (SNR); for that, the image must first be cleaned of interference.

## Aim and hypothesis

The aim is to develop and test in field experiments a method for automatic detection of the modes of the received signal on oblique-sounding ionograms in the presence of fluctuation and concentrated interference. The method must suppress interference by adaptive processing before signal compression, normalise the distribution of amplitude samples and automatically segment the ionogram into clusters with different SNR. No hypothesis is stated explicitly; in substance the paper tests that classical filtering combined with k-means clustering extracts the useful signal without the long training and labelled samples that neural-network solutions need.

## Materials and methods

The data are oblique-sounding ionograms recorded in field experiments on the mid-latitude Cyprus – Yoshkar-Ola path. The number of ionograms and the dates of measurement are not given.

Processing runs in three steps. Whitening equalisation is done before signal compression in the receiver: the power spectrum is averaged over samples within the interference stationarity time (10 s), and the averaged spectrum is used to equalise the following spectra. The ionogram matrix then undergoes median equalisation: each column is divided by its median, which moves the middle of its distribution to zero on the logarithmic scale. After that the ionogram is converted with OpenCV into a three-dimensional array (height, width, three RGB components), and the `kmeans` function is applied to it. It is configured by the number of clusters, the number of iterations before stopping, the number of restarts with different initial centres and the way the initial centres are chosen. The number of clusters varied from 5 to 11. The cluster with the useful signal is chosen automatically: the mean SNR is computed over the points of each cluster, and the two clusters with the highest value are taken.

## Results

Whitening reduced the spread of noise samples from 50 to 12 dB, and median equalisation brought it down to 2 dB. After such processing the variational series for the whole matrix almost coincides with the series for the column with the highest values; the authors use this as grounds for training the algorithm on such images.

A larger number of clusters delineates the boundaries of low-SNR modes more precisely. With 8–11 clusters the useful region is defined by at least three clusters: a central one with the highest SNR and two side ones with medium and minimum levels. With 5–7 clusters it is expedient to select a single cluster; it captures markedly more signal with an SNR of 2–5 dB, but the side components can no longer be adjusted by adding or removing clusters. In the example with 11 clusters, 8 of the 11 were removed and samples with an SNR below 25 dB were taken off the image; if the low-level clusters are kept, the algorithm detects a signal with an SNR of 2–5 dB. The smallest loss of useful signal was obtained with 11 clusters. The results are shown on ionogram images; the paper gives no numerical estimates of segmentation quality.

## Authors' conclusions

A combined method is proposed: whitening equalisation of the HF signal, median equalisation after compression and cluster analysis of the image. Both equalisation stages standardise the distribution of “signal plus noise” samples and cut the spread from 50 to 2 dB. With 5–7 clusters one is selected, with 8–11 three; the minimum signal loss comes with 11 clusters. The method can be built into cognitive radio sensors and adaptive radio communication systems, and the authors see further development in convolutional neural networks or hybrid schemes with preliminary clustering.

## Limitations

The number of ionograms, their dates and the measurement conditions are not given. Segmentation quality is not measured: there is no share of lost signal and no detection errors, and the choice of 11 clusters rests on the look of the images. An advantage over neural networks is claimed, but there is no comparison with them or with other cleaning methods. The paper does not explain how the 25 dB threshold was chosen, and the `kmeans` parameter values are not given. The whitening algorithm lets through some concentrated interference of up to 10–15 dB; its effect on clustering is not discussed. Computing the MUF, the lowest usable frequency and the optimum working frequency from the cleaned image is called possible but is not shown.

## Novelty

The authors write that the new element will be a combined method with a machine-learning algorithm that can run automatically and determines the frequency dependence of the SNR for the whole set of HF channels. The paper refers to an earlier work of 2022 [10] on a close topic; what has been added to it is not stated.

## Heuristics

- **[explicit]** If an ionogram is noisy with concentrated and fluctuation interference — apply whitening and then median equalisation before clustering, because they standardise the distribution of samples and narrow the spread from 50 to 2 dB.
- **[explicit]** If fast, interpretable segmentation is needed without long training and labelled data — use k-means rather than a neural network.
- **[explicit]** If the number of clusters has to be chosen — select one cluster with 5–7, three with 8–11, because with few clusters the side components of the signal cannot be corrected; 11 clusters give the smallest signal loss.
- **[explicit]** If the useful cluster has to be found automatically — compute the mean SNR over the points of each cluster and take the two highest.

**In one sentence:** Whitening and median equalisation narrow the spread of ionogram samples from 50 to 2 dB, after which k-means with 11 clusters picks out the signal modes on the Cyprus – Yoshkar-Ola path with the smallest losses.
