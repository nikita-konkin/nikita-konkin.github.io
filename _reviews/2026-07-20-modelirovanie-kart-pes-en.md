---
title: "Simulating maps of coherence bands using experimental estimates of the ionospheric total electron content"
pair: modelirovanie-kart-pes
lang: en
date: 2026-07-20
translation_of: 2026-07-20-modelirovanie-kart-pes.md
summary: "A hardware-and-software complex for building regional coherence-bandwidth maps from GLONASS/GPS data, with a separate derivation of how the stochastic TEC error propagates into the bandwidth estimate. Maps for Mari El and Tatarstan, 2016, at 1 GHz."
paper_title: "Simulating maps of coherence bands using experimental estimates of the ionospheric total electron content"
paper_authors: "Ivanov D.V., Ivanov V.A., Ryabova N.V., Ryabova M.I., Kislitsyn A.A., Konkin N.A."
paper_year: 2019
paper_date: "2019"
paper_link: "https://www.elibrary.ru/item.asp?id=48079625"
tags: [ionosphere, coherence-bandwidth, TEC, GNSS, mapping, uncertainty]
---

## Problem and relevance

Dispersion distortion limits the operation of broadband and ultra-wideband trans-ionospheric channels. The coherence bandwidth characterises the widest possible frequency band over which dispersion distortion can be neglected. It is determined by the ionospheric total electron content (TEC), whose value varies with time of day, season, geomagnetic conditions and solar activity. The dispersion parameters are therefore functions of coordinates and time, and require mapping.

## Aim and hypothesis

To create a hardware-and-software complex for building electronic coherence-bandwidth maps for the trans-ionospheric communication channel from GLONASS/GPS global navigation satellite system data. No testable hypothesis is stated in the paper.

## Materials and methods

The coherence bandwidth is computed as B_c = √(4cf³/πk·N̄_t) = μ·N̄_t^(−1/2), where N̄_t is the true TEC, k = 80.5 m³/s² and c is the speed of light. A band is considered optimal when B_ch < B_c holds.

Error propagation is derived separately: the measured TEC is written as N_t = N̄_t ± ΔN_t, giving b_c/B̄_c = √(N̄_t/ΔN_t) and b_c ≈ B̄_c/√(δN_t), where δN_t = ΔN_t/N̄_t is the relative error in determining TEC.

The input data are RINEX files from reference receiver stations supplied by HEXAGON. The complex comprises five core software modules written in AutoIt plus supporting tools — Wget, PostgreSQL, Maperitive and ffmpeg. Maps are built by the iMapCreate program, with a choice of geographic zone and of time span by both date and time of day.

## Results

The study covers Mari El and Tatarstan for 2016. The diagnosed operating frequency of the space communication system is 1 GHz; over the chosen period the ionosphere was magnetically quiet. Maps are given for June and September. Coherence bandwidths are at a minimum during daytime; sharp changes occur in the morning and evening hours, and values reach their maximum at night. Numerical bandwidth values, the spatial and temporal resolution of the maps, the number of stations and the uncertainty are not stated in the paper.

## Authors' conclusions

Diagnostic maps allow the intensity of diurnal bandwidth variation over the region under study to be assessed, and the limiting band for space communication systems to be identified under continuously changing environmental parameters. During daytime the authors propose either restricting the frequency band or addressing the correction of dispersion distortion.

## Limitations

The conclusion about the diurnal cycle follows directly from the B_c ~ N̄_t^(−1/2) dependence and the known behaviour of TEC; no independent comparison against direct measurements is given, and the error propagation derived in the text is never carried onto the maps. The period is described as the summer and winter solstices, while the maps are captioned June and September.

## Novelty

The paper claims the creation of an algorithm and a hardware-and-software complex for building regional electronic coherence-bandwidth maps from experimental TEC data. No demarcation from earlier work is drawn in the text.

## Heuristics

- **[stated]** If a channel band is being chosen for a trans-ionospheric system — then hold to B_ch < B_c, because beyond the coherence bandwidth dispersion distortion can no longer be neglected.
- **[reconstructed]** If a quantity is computed from measured TEC through a square-root dependence — then derive the propagation of the stochastic measurement error into it separately, because the relative TEC error directly sets the error of the result.
- **[reconstructed]** If a map of variability is being built — then record the geophysical conditions of the period (magnetically quiet ionosphere, 1 GHz operating frequency), because outside those conditions the map is not comparable with other periods.
- **[reconstructed]** If variability is being claimed — then present at least two maps at contrasting moments, because a single map cannot distinguish variation from scatter.

**In one sentence:** A hardware-and-software complex builds regional coherence-bandwidth maps from GLONASS/GPS data; bandwidths are smallest by day and largest at night.
