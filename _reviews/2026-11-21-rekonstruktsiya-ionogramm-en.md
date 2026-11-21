---
title: "Determining ionospheric parameters from reconstructed ground-based sounding ionograms"
pair: rekonstruktsiya-ionogramm
lang: en
date: 2026-11-21
translation_of: 2026-11-21-rekonstruktsiya-ionogramm.md
summary: "A method is proposed for reconstructing the electron density profile and the total electron content of the ionosphere from oblique-sounding ionograms: the IRI model supplies the initial guess, and the synthesized ionogram is fitted to the measured one by least squares. The iterations continue until the error is no more than 25 µs, the resolving power of the ionosonde."
paper_title: "Determining ionospheric parameters from reconstructed ground-based sounding ionograms"
paper_authors: "Konkin N.A., Sekretarev A.M. (supervisor — Ryabova M.I.)"
paper_year: 2015
paper_date: "2015"
paper_venue: "Scientific Progress — Creativity of the Young. Proceedings of the X International Youth Conference on Natural Sciences and Engineering, Yoshkar-Ola, pp. 21–23"
paper_link: "https://www.elibrary.ru/item.asp?id=24966170"
tags: [ionosphere, ionogram, oblique-sounding, electron-density, TEC, reconstruction]
---

## Problem and relevance

To assess how geophysical conditions in the ionosphere affect the characteristics of a radio channel, the electron density profile and the total electron content (TEC) have to be reconstructed from oblique-sounding ionograms near the control point of sounding.

## Aim and hypothesis

The aim is to develop a method for determining ionospheric parameters from reconstructed ground-based sounding ionograms. No hypothesis is stated explicitly; in substance the paper assumes that an iterative fit of a synthesized ionogram to the measured one yields an electron density profile; the authors add that quasi-vertical sounding ionograms can be computed from it.

## Materials and methods

The method has three steps: obtaining and cleaning the experimental oblique-sounding ionogram; building the dispersion characteristic of the multidimensional radio channel; and determining and synthesizing a model of the electron density profile Ne(h) and the TEC near the control point. The initial profile parameters come from the international reference ionosphere model IRI for the time and place of the control point. From them a profile is computed and an oblique-sounding ionogram is synthesized and compared with the measured one. The modelled and measured ionograms are fitted by least squares; the iterations continue until the approximation error is no more than 25 µs.

## Results

The figures show the measured and synthesized ionograms; the authors note their good agreement. The authors state that quasi-vertical sounding ionograms for the area of the control point can be computed from the resulting electron density profile; the computation itself is not shown in the paper.

## Authors' conclusions

A method for determining ionospheric parameters from reconstructed ground-based sounding ionograms was developed.

## Limitations

The numerical results are limited to the 25 µs error threshold and the qualitative "good agreement": the fitting metrics, the path, the period and the sounding equipment are not given. The reconstruction relies on the IRI model as the initial guess, and the sensitivity of the final profile to the accuracy of that model is not studied in the paper.

## Novelty

No novelty is claimed explicitly. In substance the paper proposes a chain: the IRI model as the initial guess plus an iterative least-squares fit of the synthesized ionogram to the measured one down to a 25 µs threshold.

## Heuristics

- **[reconstructed]** If an electron density profile must be reconstructed from an oblique-sounding ionogram — take the initial guess from the IRI model for the time and place of the control point, because the procedure of successive approximations starts from it.
- **[explicit]** If a synthesized ionogram is fitted to a measured one — stop the iterations at a least-squares error comparable to the resolving power of the ionosonde (25 µs), because further refinement is no longer distinguishable by the instrument.
- **[reconstructed]** If the fit yields a profile — check it on a different task, for example by computing quasi-vertical sounding ionograms, because matching one ionogram does not yet confirm the profile.

**In one sentence:** From an oblique-sounding ionogram the electron density profile and the TEC are reconstructed by an iterative least-squares fit of a synthesized ionogram to the measured one, starting from the IRI model and stopping at an error of no more than 25 µs.
