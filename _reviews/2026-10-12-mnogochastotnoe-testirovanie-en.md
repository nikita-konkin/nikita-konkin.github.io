---
title: "Method for simultaneous multi-carrier testing of ionospheric HF radio channels with remote data processing and analysis"
pair: mnogochastotnoe-testirovanie
lang: en
date: 2026-10-12
translation_of: 2026-10-12-mnogochastotnoe-testirovanie.md
summary: "An ionosonde on a USRP N210 transmits a multi-carrier signal of eight orthogonal subcarriers in a 200 kHz band, each with a 13-chip Barker code, and measures the impulse response of every partial channel at once. Control of the sounder and secondary processing are moved to a server with a PostgreSQL database and a thin client; on an 80 km near-vertical path the diurnal courses of the MUF and the optimum working frequency were obtained and working frequencies of 3.877 and 5 MHz recommended."
paper_title: "Method for simultaneous multi-carrier testing of ionospheric HF radio channels with remote data processing and analysis"
paper_authors: "Ivanov D.V., Ivanov V.A., Elsukov A.A., Konkin N.A."
paper_year: 2021
paper_date: "December 2021"
paper_venue: "Vestnik of Volga State University of Technology. Ser.: Radio Engineering and Infocommunication Systems, 2021, No 4 (52), pp. 6–23"
paper_link: "https://www.elibrary.ru/item.asp?id=48122911"
tags: [ionosphere, hf-channel, SDR, USRP, OFDM, sounding, remote-control]
---

## Problem and relevance

Noise-like composite signals that form radio pulses simultaneously on a grid of subcarriers (FDM, or OFDM when the subcarriers are orthogonal) improve communication, radar and sounding. In HF communication a partial channel occupies about 3 kHz, and a multiple of such channels gives a multiple increase in modem throughput. Cognitive HF communication needs to know the state of the whole set of channels at once, while existing ionosondes transmit their sounding frequencies one after another. Besides, processing parameters have to be changed to suit the task, and remote control of an experiment — including from mobile devices — the authors describe as almost undeveloped.

## Aim and hypothesis

The aim is to develop a method for simultaneous multi-carrier testing of ionospheric HF radio channels on near-vertical incidence skywave (NVIS) links with remote control of data processing and analysis. No hypothesis is stated as a testable claim.

## Materials and methods

**Signal.** A long multi-carrier pulse consists of N orthogonal partials, each of M chips of duration T_ch with phases following a pseudo-random sequence. Chips on two subcarriers are orthogonal when the subcarriers are 1/T_ch apart. The spectrum is described by a piecewise-constant model: neighbouring spectra cross at 2/π ≈ 0.64, and the effective band of a chip is 1/T_ch. A multi-carrier chip is defined by N complex samples and synthesised with a discrete Fourier transform.

**Channel.** The received spectrum equals the transmitted one multiplied by the channel's frequency response; matched filtering gives a cross-correlation function proportional to the impulse response of the partial channel. The frequency response is written as a sum over propagation modes, and the phase of each mode is expanded in a Taylor series in slow time and frequency — this brings the Doppler shift and the group delay into the model. The squared magnitude of the impulse response gives the instantaneous power delay profile, its mean over slow time the power delay profile, and its spectrum over slow time the scattering function. Coherent accumulation of N_a samples with an FFT gives a gain of 10 lg N_a dB.

**System.** The sounder is a software-defined device on a USRP N210 controlled by a PC. The server application handles authorisation, exchange with clients over a configurable protocol, request processing, changes to the ionosonde's schedule and delivery of results. The processing server keeps in PostgreSQL the lowest, maximum usable and optimum working frequencies computed from ionograms; the sounder's settings sit in a configuration table that the client changes with queries, and the results of secondary processing are cached. The client is thin: an interface for login and control, the ionogram and plots. The networking library is written in Java, runs on Android, Windows, Linux and macOS, exchanges messages asynchronously and encrypts the channel with AES, DES and RSA.

**Sounder parameters.** An MCPSK signal, 2–16 MHz, eight subcarriers in a 200 kHz band, a Barker code with M = 13, a chip of 40 µs and a bit of 520 µs, a height resolution of 1 km and a mode resolution of 6 km, coherent accumulation of up to 16,384 pulses, heights of 80–800 km, a power of 10 W. The parameters agree with each other: 13 chips of 40 µs give 520 µs, a subcarrier spacing of 1/T_ch = 25 kHz fits eight subcarriers into 200 kHz, and 40 µs correspond to a range resolution of 6 km.

{% include screen.html src="/assets/science/barker-spectrum-en.webp" wide=true width=2400 height=960 max=1000 caption="Spectral amplitude density of a 13-chip bit and of a single chip. Recomputed from the paper's formulas in place of Fig. 3: the peak at zero equals the sum of the Barker code, 5, and the level of the rectangular model is √13 ≈ 3.6." alt="Two curves on a frequency axis from −2B_b to 2B_b. Dashed: the main lobe of a single chip with a maximum of 1. Solid: the bit spectrum with a peak of 5 at zero and ripples of about 3–3.6 within ±B_b/2, where a rectangle of height 3.6 is drawn" %}

## Results

The method was tried out on the sounder integrated into the remote-control network. An ionogram of simultaneous multi-carrier vertical sounding in Yoshkar-Ola was obtained with a low-power MCPSK signal with a 200 kHz band. On the 80 km near-vertical tactical path from Yalchik to Yoshkar-Ola, diurnal courses of the MUF and the optimum working frequency were obtained on a remote request at steps of 15 minutes and 1 hour; the coarser step smooths the diurnal course and lets the time of switching between the night and day frequencies be estimated.

{% include screen.html src="/assets/science/mcpsk-ionogram.webp" wide=true width=928 height=732 max=620 caption="Ionogram of simultaneous multi-carrier sounding in Yoshkar-Ola with an MCPSK signal of 200 kHz bandwidth — Fig. 7 of the paper." alt="An ionogram: frequency 2–8 MHz, virtual height 100–650 km, amplitude up to 18 dB in colour. Two reflected traces rise from a height of about 230 km to 400 km near frequencies of about 6 and 7 MHz" %}

The recommended working frequencies for the path are 3.877 MHz at night and 5 MHz by day; the switching times were 21:07, 05:22 and 21:52. The authors confirm the result with calculations using the International Reference Ionosphere.

## Authors' conclusions

A method has been developed for simultaneous multi-carrier sounding of the ionosphere and testing of many HF radio channels with remote control of data processing and analysis, as part of an approach to an intelligent system for diagnosing the HF channel and for machine learning of an HF communication system. Methods and algorithms for remote control of the sounder when the task changes, a network protocol and a software architecture were developed. The practical significance lies in cognitive HF communication: more even use of partial channels, noise immunity, modem throughput and lower radiated power.

## Limitations

The statement that the maximum amplitudes of the bit and chip spectra "differ by 3.6 = √M times" is imprecise: the peak of the spectrum of a 13-chip Barker bit equals the sum of the code, i.e. 5, as the paper's own Fig. 3 shows, while √13 ≈ 3.6 is the level of the equal-area rectangle, i.e. the RMS value within the band. For energy, the ratio M = 13 holds on average over the band, not at the peak.

Simultaneity refers to the eight subcarriers within 200 kHz; how the whole 2–16 MHz range is covered and how long a full ionogram takes are not described. The ionogram is from vertical sounding in Yoshkar-Ola, while the diurnal courses are from the 80 km oblique path; the dates and season of the observations are not given, nor are the numbers of the comparison with the International Reference Ionosphere. The remote-control part describes an architecture but contains no measurements of latency, reliability or load. DES, now considered obsolete, is listed among the encryption algorithms; PostgreSQL's client library is called "libqt", apparently instead of libpq.

## Novelty

The paper claims a developing approach to client-server remote control of a sounding system and of data processing, and a method for simultaneous multi-carrier testing of HF radio channels with a signal of orthogonal subcarriers and phase-coded chips.

## Heuristics

- **[explicit]** If the partials of a multi-carrier signal must not interfere — keep the subcarrier spacing exactly 1/T_ch: orthogonality depends on this ratio alone.
- **[explicit]** If the channel's impulse response is needed — obtain it by matched filtering: the cross-correlation of the received and transmitted partials is proportional to it.
- **[explicit]** If the signal is weak — accumulate N_a samples coherently: the gain is 10 lg N_a dB, about 42 dB for 16,384 pulses.
- **[reconstructed]** If a sounder's parameters are given as a list — check them for consistency: here 13 × 40 µs = 520 µs, 1/40 µs = 25 kHz × 8 = 200 kHz, and 40 µs give 6 km in range.
- **[reconstructed]** If a processing result is expensive and requested again — cache it on the server and hand it to the thin client ready-made.

**In one sentence:** Eight orthogonal Barker-coded subcarriers on a USRP N210 let many HF channels be tested at once, and a server with PostgreSQL and a thin client take control of the sounder and processing beyond the laboratory; on an 80 km path this gave diurnal courses of the MUF and the optimum working frequency and working frequencies of 3.877 and 5 MHz.
