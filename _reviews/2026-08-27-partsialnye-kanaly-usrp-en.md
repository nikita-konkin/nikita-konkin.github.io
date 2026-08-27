---
title: "Experimental evaluation of key parameters of a set of partial HF communication channels using a USRP platform"
pair: partsialnye-kanaly-usrp
lang: en
date: 2026-08-27
translation_of: 2026-08-27-partsialnye-kanaly-usrp.md
summary: "A passive chirp ionosonde on a USRP N210 estimates SNR and scattering parameters across the whole set of adjacent 3 kHz channels on the Cyprus — Yoshkar-Ola path. 1728 ionograms; during blackouts the transparency band shrinks following the LUF, which tracks the soft X-ray component."
paper_title: "Experimental evaluation of key parameters of a set of partial HF communication channels using a USRP platform"
paper_authors: "Ivanov D.V., Ivanov V.A., Ryabova N.V., Belgibaev R.R., Konkin N.A."
paper_year: 2019
paper_date: "2019"
paper_venue: "BSHFF-2019, section C “Diagnostics of natural inhomogeneous media and mathematical modelling”, pp. 241–244"
paper_link: "https://www.elibrary.ru/item.asp?id=48079621"
tags: [ionosphere, hf-channel, SDR, USRP, scattering, blackouts]
---

## Problem and relevance

Most HF digital data systems work in a 3 kHz band, and multipath dominates their behaviour. Interference between rays at close frequencies produces fading in the time domain, and between rays at close delays in the frequency domain; together these give fading its frequency-selective character. Propagation loss and additive interference force the transmit power up. Hence the need to adapt a system to changing channel parameters from sounding data; the authors name passive sounding as the simplest to implement, improvable through SDR and digital quadrature processing.

## Aim and hypothesis

To study the key parameters of partial HF radio channels and the transparency band of an HF link by passive sounding on a USRP platform. No hypothesis is stated as a testable proposition.

## Materials and methods

The range from the LUF to the MUF is divided into adjacent frequency channels whose width equals the communication signal band, B_ch = 3 kHz, so that the path carries J = INT[(MUF − LUF)/B_ch] channels ordered by centre frequency ω. A narrowband channel is described by the Watterson model; the channel scattering function is written as a sum over N rays with parameters τ_n, F_dn, σ_τn, σ_dn and SNR_n. The channel state is taken to be defined by three key parameters (σ_τn, σ_dn, SNR_n).

The interference level is determined from the median of the samples in a channel: P_N(ω) = 1.44·Me(ω). The signal-to-noise ratio is computed as SNR(ω) = 10 lg[P_SN(ω)/P_N(ω) − 1], where P_SN is the mean level of the signal-plus-noise mixture taken from a cleaned ionogram.

Delay spread σ_τn is determined from the instantaneous squared modulus of the impulse response at −3 dB below the maximum. Frequency spread σ_dn is not measured but computed from σ_τn through a parabolic regression obtained by least squares from simultaneous measurements of delay and frequency spread:

σ_d [Hz] = K0 + K1·σ_τ [ms] + K2·σ_τ² [ms], with K0 = 1.55 Hz, K1 = −0.24 Hz/ms, K2 = 0.33 Hz/ms².

The receiving terminal is a passive chirp ionosonde on a USRP N210 with an LFRX daughterboard: an HF antenna, a built-in time-and-frequency synchronisation module, and a PC running Ubuntu Linux with GNU Radio and dedicated software.

## Results

The experiments were run on the Cyprus — Yoshkar-Ola link, sounding every 5 minutes round the clock; 1728 ionograms from magnetically quiet days were processed. Means and RMS deviations by time of day:

| | Night | Morning | Day | Evening |
|---|---|---|---|---|
| ‹SNR› | 23.61±5.15 | 22.38±4.53 | 21.41±5.07 | 22.69±4.25 |
| ‹σ_τn› | 2.17±0.91 | 2.19±1.01 | 1.90±0.73 | 2.21±0.90 |
| ‹σ_dn› | 2.62±1.61 | 2.66±1.65 | 2.31±1.56 | 2.67±1.98 |

The delay-spread values suit modems at 9600 baud, while the Doppler-spread values limit the rate to 2400 baud; variations in signal-to-noise ratio had the larger effect on throughput.

Blackouts were studied from experiments run through 2014, from January to December; the events were caused by flares of class M7.3 (18.04), M4.0 (24.10) and X2.0 (26.10), with undisturbed geomagnetic conditions. The largest variations in the transparency band accompanied the X2.0 flare. The link's LUF follows the soft X-ray component (λ2 = 0.1–0.8 nm), which the authors take as identifying it as the component governing HF absorption during sudden ionospheric disturbances. Horizontal white lines in the 25…28 MHz range are attributed, by calculation, to hop modes being screened by the spherical surface of the Earth.

## Authors' conclusions

A passive sonde on a USRP platform made it possible to study the key parameters of the entire set of adjacent 3 kHz telephone channels. The scattering parameters obtained correspond to moderately disturbed conditions: by delay they support 9600 baud, while by Doppler frequency they limit the rate to 2400 baud. During blackouts the transparency band shrinks, following mainly the LUF, whose behaviour correlates with the soft X-ray component.

## Limitations

Doppler spread was not measured but reconstructed by regression from the measured delay, so the conclusion about a 2400 baud ceiling rests on equation (4) rather than on direct observation, and two rows of the table are not independent of each other. The year the 1728 ionograms belong to is not stated — the blackouts are dated to 2014 separately. The number of channels J, the frequency range of the path and the antenna type are not given; the correlation between LUF and X-ray flux is shown graphically without a coefficient, as is the comparison with the authors' own earlier data, described as good agreement.

## Novelty

The paper claims a move to a USRP-based passive sonde receiver with a new digital processing method allowing analysis of adjacent partial telephone channels; the advantages named are higher noise immunity in the sounding system and more accurate delay estimation through a high sampling rate.

## Heuristics

- **[explicit]** If a multipath HF channel is described as an ordered set — divide the LUF…MUF range into channels whose width equals the communication signal band (3 kHz), because the parameters are needed in exactly the band the system works in.
- **[reconstructed]** If an interference level is estimated in a channel that also contains signal — use the median of the samples with a scale factor rather than the mean, because the mean is displaced by the very signal being separated out.
- **[reconstructed]** If only one of two scattering parameters can be measured — reconstruct the other by regression from published simultaneous measurements, but state that the result is not an independent observation.
- **[reconstructed]** If the width of a response is measured relative to its maximum — record the level used (here −3 dB), because without it estimates are not comparable across channels or sessions.
- **[reconstructed]** If persistent horizontal bands appear in a time-frequency picture — check the geometry of the path first, because here calculation attributed them to hop modes screened by the Earth's surface rather than to interference.

**In one sentence:** A passive chirp ionosonde on a USRP N210 yields SNR and scattering parameters for the whole set of 3 kHz channels on the Cyprus — Yoshkar-Ola path, and during blackouts the transparency band shrinks following the LUF, which tracks the soft X-ray flux.
