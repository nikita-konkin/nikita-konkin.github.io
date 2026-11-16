---
title: "The ionozond Playground: A Mode's Frequency Response by Subchannel, and a Layer Instead of a Spline"
project: ionozond_playground
pair: ionozond-chh-podkanaly
platform: VK
type: Technical breakdown
date: 2026-11-16
source_from: fead14b39311be6edcbe363db79a4ea17cf6f2e1
source_rev: b1e77dac4886ddddf373453f38d0e09018310fe4
lang: en
authors:
  - Nikita Konkin
summary: "A new playground page reads one mode's amplitude and phase response straight off the recording of a real sounding: each window of the beat signal gives an instantaneous delay power profile, and the complex value at its peak is one sample of the frequency response. Overlapping windows keep the phase unwrapped where back-to-back windows lose whole turns, and they reveal the beating of the o and x waves. The simulator notes gain a block diagram of muf.sim and a section on drawing the 1F family from a fitted layer."
image: /assets/ionozond_playground/fr-preview.png
translation_of: 2026-11-16-chh-po-podkanalam.md
links:
  repo: "https://github.com/nikita-konkin/ionozond-playground"
  demo: "https://konkin-nikita.ru/ionozond-playground/"
tags: [ionosphere, chirp-sounding, hf-channel, frequency-response, javascript, visualisation]
---

An ionogram is power: each of its cells keeps the squared magnitude of a spectrum, and the phase is thrown away. That is not enough to judge an HF channel. A modem cares about the whole frequency response, amplitude and phase alike: the phase response shows how the group delay changes across the band, which is the dispersion within a mode. In the previous post about the playground, dispersion was read off the slope of a trace on the ionogram. A new page, "Subchannel response", gets it from the phase of the recording itself.

The data are the echo windows of four soundings on the NIC1 — Yoshkar-Ola path on 17 October 2026, at 06:00, 09:00, 12:00 and 18:00 UTC: 4 MHz of complex beat-signal samples per sounding, 419 kB in all. The page does all the computing itself, in the browser.

## A profile's peak as a response sample

The beat-signal recording is cut into Hann windows of length T. On a rising sweep at k = 100 kHz/s a window covers a subchannel B = kT wide. The window's spectrum is an instantaneous delay power profile. Inside a gate around the chosen mode's delay-frequency curve, the bin with the most power is taken. Its magnitude is a sample of the mode's amplitude response in that subchannel, and its angle a sample of the phase response.

The subchannel can be set from 5.12 to 102.4 kHz. Windows follow one another or overlap by 50, 75 or 90 %, down to one window per recorded sample. Without overlap there is one response sample per subchannel, and the plots come out as steps. With overlap the samples are almost continuous.

{% include screen.html src="/assets/ionozond_playground/fr-controls-en.webp" wide=true width=1413 height=1039 caption="The 06:00 UTC sounding of 17 October: a 20.48 kHz subchannel, 50 % overlap, the 19.5–20.5 MHz stretch. Below is the sounding's real ionogram with the 4 MHz of data, the chosen stretch and the MUF of 22.95 MHz marked." alt="A settings panel: soundings at 06:00, 09:00, 12:00 and 18:00; modes F, F#2, 2F and 2F#2; subchannels from 5.12 to 102.4 kHz; overlap of 0, 50, 75 and 90 % or at every sample; sliders for the 1 MHz stretch and the gate's shift and half-width; the gate centred on the curve or held at one delay. Below, an ionogram from 10 to 23 MHz in frequency and 8,500 to 10,500 µs in delay with an f/MUF scale on top, a light band over 18–22 MHz, an orange box for the stretch near 20 MHz and a dashed MUF line" %}

For this stretch the page puts the key numbers in cards. A window lasts 0.205 s, and a delay bin 1/(kT) is 48.8 µs, or 14.65 km. With 50 % overlap the response step is 10.24 kHz, 98 samples per megahertz against 49 without overlap. The median signal-to-noise ratio at the peak is 27.2 dB. The dispersion from the phase curvature is 24.7 µs/MHz, and from the trace's slope on the ionogram 30.0 µs/MHz.

## A phase that keeps its turns

To unwrap the phase along frequency, every window must share one phase reference. An FFT's phase is counted from the start of its window, and with overlap this adds a term that depends on the window's shift. So the spectrum is computed in the absolute time of the sweep, and the peak value is referred to one fixed delay τ₀ for all windows. A peak that moves into the next delay bin then causes no phase jump, and neighbouring windows differ by 2π(τ − τ₀)·k·Δt.

This gives the condition for an unambiguous phase: the step stays below π while |τ − τ₀| < 1/(2k·Δt). Without overlap Δt = T, and the margin is half a delay bin. For a mode with noticeable dispersion the delay moves further than that over a megahertz, and the stepped phase response loses whole turns. A 50 % overlap doubles the margin, and a window at every recorded sample (1.125 ms, or 112.5 Hz of sweep) pushes the limit out to 4.4 ms.

The difference shows near the MUF, where the trace bends steeply. In the same 06:00 sounding, with a 20.48 kHz subchannel over 20.9–21.9 MHz, back-to-back windows lose the phase in 38 steps out of 48, and sliding windows in 7 out of 8,888.

{% include screen.html src="/assets/ionozond_playground/fr-response-en.webp" wide=true width=1413 height=1073 caption="Amplitude and phase response of mode F over 19.5–20.5 MHz. Grey steps are back-to-back windows, the line is 50 % overlap. The phase is shown with the linear term for τ₀ = 9,324 µs removed." alt="Two plots against frequency from 19.5 to 20.5 MHz. At the top, the amplitude response in dB above noise: values from 15 to 35 dB with dips near 19.75 and 20.15 MHz, a grey stepped curve and a teal line running together. At the bottom, the phase response in radians: a smooth arc from 2 rad to a maximum of about 19 rad at 20.05 MHz and down to −3 rad; steps and line agree, with no whole-turn errors. A dashed vertical line at 20.0 MHz marks the selected window" %}

The bend of the phase response is the dispersion within the mode, and its slope is how far the group delay differs from τ₀. On this stretch, far from the MUF, the phase changes smoothly and the steps lose nothing: with 50 % overlap 1 step in 97 exceeds π/2, without it 4 in 48. The dips of up to 15 dB in the amplitude response are fading.

## What overlap does not give, and what it does

Overlap does not improve resolution. Each response sample is still an average over its own subchannel B wide, the delay step stays 1/(kT), and neighbouring samples are strongly correlated. A window at every sample is the same as the second compression along the delay curve with a Hann filter of length T, which board 2 of the simulator notes walks through.

What overlap does show is the beating of two rays that fall into one delay bin, such as the ordinary and extraordinary waves. Their sum varies along frequency with a period of 1/Δτ. With a delay difference of 30 µs the period is 33 kHz. Back-to-back 20 kHz windows give a sample every 20 kHz and cannot resolve that period, while 90 % overlap gives one every 2 kHz. The beat period gives an estimate of Δτ.

A wide subchannel separates the waves in another way. At 102.4 kHz the delay bin narrows to about 10 µs, or 3 km, and the o and x waves fall into different bins as soon as their delays differ by more than that. But the window then lasts about a second, longer than the coherence time, and the peak smears: the Doppler spread shifts the bin by νD/k (1 Hz is 10 µs), and the mode's dispersion by |dτ/df|·B. Widening the subchannel pays only while both terms stay below 1/B.

To follow one of the two peaks, the gate can be shifted, narrowed, or held at one delay over the whole stretch, and its edges are drawn on the delay map. This was needed because the mode curve from the simulator's state does not always sit exactly on the echo. Above the map the page shows the sounding's real ionogram with the chosen stretch and the MUF, and gives frequency as a share of the MUF as well.

Reading a response off a rising sweep comes with a basic caveat. A megahertz of sweep takes 10 seconds, so along frequency the channel's selectivity is mixed with 10 seconds of fading: a coherence time of about 0.5 s corresponds to 50 kHz of sweep. The page shows H(f, t) along the diagonal f = f₀ + kt, not an instantaneous response. That is why it does not match the simulator's |H(f, t)| map at a single carrier, where frequency and time are kept apart.

## A block diagram of the simulator

The simulator notes gain a "Block diagram" section. It is drawn in SVG from one bilingual description and shows every FFT, inverse FFT, multiplication, sum and complex conjugation on the way from a real sounding to the result. The lanes run in order: the channel state from a real sounding, the fast part of the state, the fading of one path, the channel at one carrier, the synthetic sounding, and states over time with the line for a modem. Each lane is described in words below the figure.

{% include screen.html src="/assets/ionozond_playground/blocks-lane1-en.webp" wide=true width=1368 height=1002 caption="Lane 1: from the received sweep to the ChannelState. In the live loop the 1F family is drawn from a fitted layer." alt="A five-row block diagram. Row 1, in the receiver: the received sweep r(t), the ADC, multiplication by the complex-conjugate reference chirp, a low-pass filter and decimation, the beat signal x[n] in an .lfs file. Row 2: windows of 8,192 samples, multiplication by a Hann window, FFT, fftshift, squared magnitude, normalisation by 4 ln 2 times the median. Row 3: delay τ = −fb/k, conversion to dB, the ionogram P(f, τ), interference removal, an SNR ≥ 13 dB contour. Row 4: power-weighted segment centres, non-crossing traces, hop count and ray, a spline with one extremum or 1F from the layer. Row 5, per mode: GDD and TOD, C/N₀, delay spread, Doppler from F.1487. The result is the ChannelState" %}

## 1F from a layer, not from a trace

Until now each mode was described by a spline through the points of its trace. Where echoes lie tens of kilometres apart, a trace can jump from one to another, and the spline followed the jump rather than the echo. Now the live loop draws the 1F family from a model. A quasi-parabolic layer over a spherical Earth is fitted to the echo points. For such a layer a ray's ground range and group path have closed forms (Croft and Hoogasian, 1968). Low take-off angles give the low ray, which rises towards the MUF, and high ones the high ray, which meets it from above.

The fit is a search. The MUF is sought within 3 % of the one found from the trace, the height of the maximum between 150 and 500 km, and the half-thickness between 30 and 200 km: first in 10 km steps, then on a finer grid. The range offset is free within ±500 km, because a receiver clock error shifts all echoes alike. The winning layer is the one with the largest total echo weight within 15 km of either ray. The notes state the limitation plainly: the offset and the height of the maximum partly stand in for each other, so the fitted layer is a curve consistent with the delay-frequency trace, not a measured profile of the ionosphere.

The state keeps two modes, 1F and 1F-high. The band of each is the longest run of echo within 15 km of its ray, with gaps no wider than 1.5 MHz. The block diagram marks where these rays enter the synthetic sounding: lane 4 takes each mode's delay curve, and for the 1F family that curve is the layer's low or high ray.

## Russian wording and references

In places the Russian pages read like a translation, so the terminology was rewritten: loan-word jargon for dechirp, sweep, bin, the "nose" of a trace, equaliser and persistence gave way to native Russian terms, and the synthetic "copies" are now called synthetic soundings. The four Russian boards were redrawn with the new labels.

A "Publications" section has appeared: 17 works of the PGTU — MarSTU research school. Short citations in the models and the wiki link to its entries.

## Conclusions

1. The complex value at the peak of an instantaneous delay profile is a sample of the mode's frequency response, so a sounding's recording yields phase as well as power.
2. Overlapping windows do not raise resolution, but they keep the phase unambiguous where back-to-back windows lose turns, and they make the beating of the o and x waves visible.
3. On a rising sweep frequency and time are tied, so such a response is a diagonal cut through H(f, t), not an instantaneous channel response.
4. A layer model removes the trace's jumps but remains a curve consistent with the delay-frequency trace: its parameters cannot be read as a profile of the ionosphere.

## Availability

- The playground: [konkin-nikita.ru/ionozond-playground](https://konkin-nikita.ru/ionozond-playground/), the "Subchannel response" and "Simulator: notes" pages
- The playground's source: [github.com/nikita-konkin/ionozond-playground](https://github.com/nikita-konkin/ionozond-playground)
