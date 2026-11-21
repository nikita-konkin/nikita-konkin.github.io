---
title: "Algorithm of estimation of the degree of dispersion distortion of microwave radio signals on the basis of data on the coherence band"
pair: dispersionnye-iskazheniya-svch
lang: en
date: 2026-11-21
translation_of: 2026-11-21-dispersionnye-iskazheniya-svch.md
summary: "For broadband transionospheric channels, expressions are obtained for the coherence band — the band at whose edges the nonlinear phase advance due to dispersion does not exceed 1 radian — and an algorithm is developed for building regional maps of this band from GLONASS and GPS receiver data. The curves of the coherence band against relative frequency for day and night differ from the mean by no more than 20 %; the paper gives no numerical results for the maps."
paper_title: "Algorithm of estimation of the degree of dispersion distortion of microwave radio signals on the basis of data on the coherence band"
paper_authors: "Ivanov D.V., Ivanov V.A., Ryabova N.V., Ryabova M.I., Kislitsyn A.A., Chernov A.A., Konkin N.A."
paper_year: 2017
paper_date: "2017"
paper_venue: "Radiolocation, Navigation, Communication. Proceedings of the XXIII International Scientific and Technical Conference, Voronezh, pp. 541–549"
paper_link: "https://www.elibrary.ru/item.asp?id=29307442"
tags: [ionosphere, transionospheric-channel, frequency-dispersion, coherence-band, TEC, GNSS]
---

## Problem and relevance

Widening the signal bandwidth in space communication and in radar sensing of the Earth from space can lead to dispersion distortion of the characteristics of transionospheric channels and of the signals themselves, up to complete “destruction” of the signal. Frequency dispersion is the dependence of a wave's phase velocity on frequency; because the spectral components have different phase velocities, the phase-frequency response of the spectrum is disturbed. Distortion is usually assessed from the impulse response and the instantaneous power delay profile (PDP), equal to the square of the impulse-response envelope. Broadband systems need monitoring of the degree of this distortion.

## Aim and hypothesis

The aim is a comprehensive study of dispersion distortion of the PDP of transionospheric channels and of methods of controlling it by monitoring, based on regional maps of the coherence band built from satellite navigation data. Channel parameters have to be linked to the coherence band, and an algorithm and software have to be developed for maps from GLONASS and GPS data. No hypothesis is stated explicitly; in substance the paper tests that the degree of distortion can be assessed by the coherence band and that control can be run with maps from GNSS receiver data.

## Materials and methods

The phase-frequency response (PFR) of the channel is expanded in powers of the deviation from the mean frequency; the parameters of phase dispersion of the first, second and third orders are introduced, and then a dispersion characteristic containing only these parameters. For transionospheric propagation the refractive index is expanded in a Taylor series in powers of the square of the ratio of the plasma frequency to the wave frequency, from which the phase advance and its first three frequency derivatives are derived. Terms of the phase advance can be dropped if the advance they cause is much smaller than 2π (for engineering use, smaller than one). The PFR is split into linear and nonlinear parts; it is the nonlinear part that distorts the PDP. If third-order dispersion can be neglected, the nonlinear part is parabolic in frequency (Fig. 1 — slopes of 30, 60 and 120 µs/MHz).

The coherence band is the band of frequencies at whose edges the advance of the nonlinear part of the phase due to dispersion does not exceed 1 radian. For general solutions the calculations are made in relative frequencies — the ratio of the frequency to the critical frequency of the ionosphere; a general expression is given for second-order dispersion, and a separate formula for the coherence band is derived for the high-frequency approximation. The maps are built by an AutoIt program: RINEX files from different receivers are converted to the .dat format by the TecSuite program, information on the files is written to a PostgreSQL database, an operator query by territory and period forms a set of files, and GNU Plot builds animated maps in .gif format: longitude on the abscissa, latitude on the ordinate, coloured points marking the places of measurement.

## Results

Analytical expressions are obtained for the parameters of frequency dispersion under different approximations of the refractive index and phase advance, and expressions for the coherence band. A calculation for day and night (Fig. 2) showed that the dependences of the coherence band on relative frequency differ from the mean by no more than 20 %; the authors conclude that this dependence is of a general nature. An example coherence-band map is shown (Fig. 4); there are no numerical values or comparison of the maps with measured distortion in the text.

## Authors' conclusions

Analytical expressions are obtained for the parameters of frequency dispersion and for the coherence band of broadband transionospheric channels — the edge of the band of frequencies undistorted by dispersion, as a function of the electron-density profile. An algorithm and software are created for regional coherence-band maps, for following the degree of distortion and the effect of geophysical factors on it. In the authors' view, the results will widen the possibilities of broadband radio systems in dispersive media and raise their noise immunity.

## Limitations

The conclusions rest on analytical estimates and one example map; no check against measured PDP distortion is described. It is not said for which region, date and stations the map is built, or how a calculation by the formula linking the coherence band to the TEC in the high-frequency approximation is applied in building the map; the colour of the points on the map is tied to the TEC level. The statement about higher noise immunity remains an assumption.

## Novelty

The paper does not claim novelty explicitly. In substance it derives expressions for the coherence band of a transionospheric channel and creates an algorithm for building regional maps of this band from GNSS data.

## Heuristics

- **[explicit]** If the significance of dispersion distortion has to be assessed — use the coherence band: the band at whose edges the advance of the nonlinear part of the phase does not exceed 1 radian.
- **[explicit]** If a phase formula has many terms — for engineering estimates drop those whose phase advance is smaller than one.
- **[explicit]** If general solutions for a channel are needed — compute in relative frequencies (the ratio to the critical frequency), because the day and night curves differ from the mean by no more than 20 %.
- **[explicit]** If a broadband system needs monitoring of distortion — build regional coherence-band maps from GNSS receiving-station data and keep a database of the files, so that it is known which data are available for the maps.

**In one sentence:** The coherence band of a transionospheric channel, the band with a nonlinear phase advance of at most 1 radian, makes it possible to assess dispersion distortion, and maps of this band from GLONASS and GPS data are built by an AutoIt program.
