---
title: "ionozond: The Echo Window — Every Sounding's Phase in 1.6 MB Instead of 80"
project: ionozond
pair: ionozond-okno-eha
platform: VK
type: Technical breakdown
date: 2026-10-24
source_from: 4560abfffea003095832864e6fbee8cbf52240fa
source_rev: bbf2481f3af8e29f5c8d7de1df9905e6f588a1f7
lang: en
authors:
  - Nikita Konkin
summary: "The station deletes each capture once its archive verifies, and the archive held power only — so every five minutes the Doppler, the fading and the phase went with the capture. Now an echo window is cut into the archive: the complex signal around the echoes, bit-identical to the reference implementation. How it works, why a capture is deleted only after its window is verified, and how to keep the whole signal."
image: /assets/ionozond/echo-preview.png
translation_of: 2026-10-24-okno-eha.md
links:
  repo: "https://github.com/nikita-konkin/ionozond"
  demo: "https://konkin-nikita.ru/ionozond-playground/"
tags: [ionosphere, chirp-sounding, python, hdf5, signal-processing, data-storage]
---

One sounding of an ionozond station is an 80 MB `.lfs` capture, and at a 300-second repetition period one station produces about 23 GB a day. Such captures cannot be kept forever, so after each sounding the receiver writes an `.h5` archive in the chirpsounder2 format and deletes the capture as soon as the archive reads back. But the archive holds power — a spectrogram. Every five minutes the fast part of the channel went with the capture: the Doppler shift and spread, the fading, and the phase, which carries the group-delay dispersion.

## What the echo window is

After dechirping, the echoes occupy a beat band of a few hundred hertz out of the 40 kHz the capture stores. The echo window shifts that band to zero, low-passes it, decimates it and appends the result to the archive as a separate `echo_window` group. On the captures of the Cyprus station that is 1.57 MB — 1/51 of the capture — and inside the window's band the signal is kept without loss. The archive grows from 1.25 to 2.81 MB a sounding, about 450 MB a day per station.

The window's format is set by a specification of the ionograms-handler processing platform, and the reference implementation lives in its `muf` module. The window in ionozond is held to that reference, not to itself:

- **The same window.** The range span is the union of automatic gating on the power ionogram and the geometry of one- to three-hop modes, plus 150 km. It follows the echo's energy, not only the computed path.
- **The same samples.** Decimation sums the filter taps in the same order as `scipy.signal.upfirdn`, so the result is bit-identical to the reference at complex64. That matters: `muf`'s verifier re-cuts the window with the stored taps and demands identical samples.
- **numpy and h5py only.** SciPy is optional on the station, so the Kaiser filter's taps are computed from the formula in the specification and stored with the window — a reader does not have to agree with this filter designer.

A check on five captures of 4 February 2026, from 03:00 to 18:00 UTC, gave a full match: the same window of 2486–4112 km, decimation by 45, 3595 taps; of 222,304 samples, not one differs. `muf`'s own verifier passes: 82.6 dB of stopband rejection, 0.0006 dB of passband ripple. Cutting the window takes 1.9 seconds, after 1.3 seconds for building the products.

One discrepancy did turn up, and it is instructive. In `muf`'s built-in station table the Cyprus transmitter's coordinates differ from the capture header by 0.6 km, and `muf`'s window shifts by the same 0.6 km. Both windows are valid: the coordinates decide, not the implementation.

## A capture is deleted only after its window is verified

The window makes sense only if the capture is not deleted before the window is safely kept. A review found two paths by which a capture left without that guarantee.

The first was the receiver's own immediate deletion. The window was cut without the full check: reading it back proved the bytes had reached the disk, not that they were the right bytes. The filter, the exact re-cut and the re-derived power — what would catch a shift or a sign error after some future change — ran only with the check. And an archive that already had a window let its capture go with no check at all.

The second path was the scheduled clean-up by retention period and the disk-freeing timer. They decided by the power archive, without looking at the window. A capture the receiver had held back because its window failed was deleted a few hours later anyway — and with it the last copy of the phase.

Now a capture counts as ready for deletion only if its archive holds a verified window. A missing window is cut and verified first; a capture whose cut fails stays. Both paths decide through one and the same function, so they cannot disagree about when a capture may go. The scheduled clean-up spends no more than 15 seconds a pass on this, so that a backlog cannot delay the next sounding. On a copy of one capture, the clean-up cut the window, verified it and released the capture in 5.5 seconds.

## The whole signal

For those who need the whole capture rather than the window, the console's parameters gained a checkbox, "Full signal z in the .h5 archive". It widens the window to the whole band: no shift, no decimation, a single tap — a case the specification already allows. The archive then holds the capture sample for sample and replaces it completely.

{% include screen.html src="/assets/ionozond/params-archive.webp" wide=true width=940 height=250 max=940 caption="An archive with an echo window: about 0.8 GB a day. The interface is in Russian." alt="The “Data storage” section of the console's parameters: “.h5 archive (chirpsounder2 format)” is ticked, with a tooltip above it — about 2.8 MB a sounding: a 0–8000 km spectrogram and the echo window, the complex signal around the echoes with Doppler, fading and phase; at the bottom, the estimate “about 0.8 GB a day at a 300 s period — the capture is deleted after the archive is verified”" %}

{% include screen.html src="/assets/ionozond/params-full.webp" wide=true width=940 height=250 max=940 caption="With the full signal the estimate grows to 20.3 GB a day." alt="The same section with “Full signal z in the .h5 archive” ticked; the estimate at the bottom is about 20.3 GB a day at a 300 s period" %}

On the capture of 4 February, 12:00, the stored signal matched the `.lfs` samples, took 69 MB of 80 in the archive with gzip and byte shuffling, and the ionogram `muf` built from the archive matched the one built from the capture to 0.000000 dB.

The signal is stored inside the window rather than in the root `z` dataset that chirpsounder2 provides — and that is on purpose. `muf` reads a root `z` with the second format version's timing and would label every frequency 7.5 MHz too low. The window carries its own time and sweep parameters.

## Where the window has already helped

The October soundings of the NIC1 — Yoshkar-Ola path are recorded as archives with echo windows. The HF channel simulator reads them from the window rather than from the stored power: the window goes through the original capture's spectrogram again, so the scale and the conversion to carrier-to-noise density stay the same as for an `.lfs`. The simulator is the subject of the next breakdown.

The last fix in this series is small but noticeable: synchronisation with the network storage refused to upload archives when the storage was attached by automount. The mount table then holds two entries at one point — the autofs trigger and the share mounted over it — and the program took the first and treated the share as not mounted. Now, as in the kernel, the later one wins.

## Conclusions

1. Raw data can be deleted only when everything still needed from it is kept: a power archive does not replace the capture, because it loses the phase.
2. Almost all the information about the channel sits in a narrow band: a window of 1/51 of the capture keeps it without loss.
3. Compatibility with a reference is better proven by bit-identical samples than by plots that look alike.
4. The decision "may this be deleted" should be made in one place: two independent rules will sooner or later disagree.

## Availability

The source code is open.

- Source code: [github.com/nikita-konkin/ionozond](https://github.com/nikita-konkin/ionozond)
- Interactive models: [konkin-nikita.ru/ionozond-playground](https://konkin-nikita.ru/ionozond-playground/)
