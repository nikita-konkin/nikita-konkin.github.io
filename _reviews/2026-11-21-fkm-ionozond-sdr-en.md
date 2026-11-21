---
title: "Phase-coded ionosonde on a universal SDR platform for frequency provision of NVIS communication"
pair: fkm-ionozond-sdr
lang: en
date: 2026-11-21
translation_of: 2026-11-21-fkm-ionozond-sdr.md
summary: "A single-site vertical ionosonde with a phase-coded signal is built on the USRP N210 platform; it measures the channel scattering function, the signal-to-noise ratio and the scattering parameters, and from them chooses a working frequency or modem for short-range HF communication. The fill factor of the phase-coded signal is 0.098, so at equal radiated power and equal analysis time its energy is half that of an interrupted chirp signal; an example daily course shows the MUF dropping by about 1 MHz around 14:45."
paper_title: "Phase-coded ionosonde on a universal SDR platform for frequency provision of NVIS communication"
paper_authors: "Elsukov A.A., Ivanov D.V., Ovchinnikov V.V., Konkin N.A., Ryabova M.I."
paper_year: 2019
paper_date: "2019"
paper_venue: "Systems of Synchronization, Generation and Processing of Signals, 2019, vol. 10, no. 1, pp. 11–16"
paper_link: "https://www.elibrary.ru/item.asp?id=37146055"
tags: [ionosphere, ionosonde, phase-coded-signal, NVIS, software-defined-radio, scattering-function]
---

## Problem and relevance

In regions with difficult terrain, HF communication in the near-vertical-incidence skywave (NVIS) mode is used; it is considered suitable at ranges below 400 km. It is needed, among other things, in rescue operations and when satellite infrastructure is destroyed. HF link efficiency is raised by sounding the multidimensional channel — a set of partial channels 3 kHz wide, ordered by working frequency: the channel with the highest signal-to-noise ratio (SNR) and the least scattering is chosen from them, and the modem follows from it. This needs digital signal-processing algorithms, and software-defined radio (SDR) makes it possible to implement them in software.

## Aim and hypothesis

The aim is to build on the USRP platform a single-site vertical ionosonde with a phase-coded signal, to substantiate and implement algorithms for measuring the channel scattering function and channel parameters, and to propose an algorithm for frequency provision of short-range HF communication. No hypothesis is stated explicitly; in substance the paper tests that a phase-coded signal with an energy budget close to an interrupted chirp (FMICW) is suitable for prompt choice of a channel or modem.

## Materials and methods

The energy of a sounding signal is set by its power and duration, and with receive pauses taken into account by the fill factor kf: Tef = Ta·kf, Es = Ps·Ta·kf. A continuous chirp signal (FMCW) has kf = 1 but needs two antennas; with one antenna the signal is made more complex, to FMICW, and according to the cited work its kf is 0.2. For the phase-coded signal the group signal lasts about 0.6 ms (reception of the first reflection from the E layer at about 90 km), the reception time is 6.6 ms (ranges up to 1000 km, reception of three-hop modes), the chip is not shorter than about 30 µs, so the number of chips is L ≤ 18 and kf ≈ 0.1.

The compressed signal gives the channel impulse response, and from it the channel scattering function as a function of delay and Doppler shift; its “width” in delay and in Doppler shift defines the scattering parameters στ and σd. The instantaneous power delay profile (PDP) averaged over the analysis time is used to estimate the SNR: a threshold separates signal from noise and is set by median filtering and the CFAR method. An ionogram is a set of PDPs ordered by frequency.

The ionosonde is built on the USRP N210 on the “ADC to the antenna” principle, where the DUC shifts the transmitted signal to the working frequency and the DDC extracts the complex envelope of the received signal, with frequencies up to 25 MHz at 16-bit amplitude. It uses an LZY-22+ amplifier and a wideband horizontal dipole for 2…30 MHz on the university roof. Signal parameters: a Barker code of 13 elements of 40 µs, coherent accumulation of 4…8192 compressed pulses, peak power 19 W, bandwidth 25 kHz, analysis period 0.02–41.94 s, fill factor 0.098, height range 78–768 km, height resolution 6 km. The frequency-provision algorithm compares the current SNR and delay scattering with the modem characteristic function (MCF) under STANAG 4539; it also sets limits for frequency scattering. For 2400, 600, 150 and 75 bit/s these are an SNR of 14, 3, −3 and −7 dB, frequency scattering of 4, 12, 10 and 40 Hz, and delay scattering of 5, 5, 5 and 16 ms.

## Results

The ionosonde works in two modes: channel (PDP and scattering function of one channel) and panoramic (ionogram, transparency band, and SNR and delay scattering for each channel). The number of partial channels is estimated as (MUF − LUF)[kHz]/3[kHz]; for the whole decametre band about 9000 are named.

In an example daily course (Fig. 3), a negative ionospheric disturbance occurred around 14:45: the MUF fell by about 1 MHz. With a channel chosen by the 0.85 MUF rule without sounding, short-range communication would have been broken, while a system built on the phase-coded ionosonde promptly finds new partial channels. At mid-latitudes the scattering parameters lie within the permitted MCF values of a 2400 baud modem and below most of the time, so the SNR remains critical; in the transitional time of day the delay scattering changes almost twofold, and the Doppler scattering over a still wider range.

## Authors' conclusions

A phase-coded ionosonde has been created for prompt control of NVIS frequencies: it estimates in real time the transparency band, the SNR and the scattering parameters over a set of partial channels, assigns the optimal ones and estimates the transmission rate. Algorithms for synthesis and processing of a multi-frequency phase-coded signal are presented. The sounding results verified the models and algorithms and tested the software. The approaches suit prospective short-range cognitive HF systems in regions with difficult terrain.

## Limitations

The authors themselves show that at equal radiated power and equal analysis time the energy of the phase-coded signal is half that of FMICW; the experiment has no comparison of the two ionosondes. The experiment is described by a single daily course, with no date or conditions; numerical series of SNR and scattering are not given in the text (the daily dependences are shown in Fig. 3); the only number given is the 1 MHz MUF drop. The ionosonde is vertical and at one point, while the conclusions concern an NVIS link; there are no measurements on the link itself. The “certain advantages” of the phase-coded ionosonde are not listed in the conclusion.

## Novelty

The paper does not claim novelty explicitly. In substance it describes an ionosonde with a phase-coded signal on an SDR platform with an algorithm for choosing a working frequency or modem by the MCF.

## Heuristics

- **[explicit]** If a channel is chosen for a modem — compare the current SNR and delay scattering with the MCF: the channel is conditioned if the parameters stay within its limits.
- **[explicit]** If the SNR must be estimated from the PDP — separate signal and noise with a threshold set by median filtering and CFAR.
- **[explicit]** If the working frequency is chosen by 0.85 MUF without current sounding — communication may be broken by a negative disturbance (in the example the MUF fell by about 1 MHz), so sound promptly.
- **[explicit]** If reception and transmission share one antenna — the sounding signal has to be interrupted, because continuous FMCW needs two antennas; the price is a lower fill factor (0.2 for FMICW, about 0.1 for the phase-coded signal).
- **[explicit]** If the state of a channel must be monitored at mid-latitudes — control the SNR first and check the scattering in the transitional time of day, because then the delay scattering changes almost twofold and the Doppler scattering over a still wider range.

**In one sentence:** A phase-coded ionosonde on the USRP N210 with a fill factor of 0.098 measures the scattering function, SNR and scattering and lets a working frequency or modem be chosen for short-range HF communication, but at equal radiated power and equal analysis time its signal energy is half that of FMICW.
