---
title: "IonoPotok: AbsolTEC and MapTEC Without Windows XP — Native Converters and Maps of TEC Variations"
project: ict_platform
pair: ict-absoltec-maptec
platform: Web
type: Technical breakdown
date: 2026-11-21
source_from: ae9c38f928de8c490843624a122538551e65a198
source_rev: 3d8de5053f186245309692f5533126bba34a3e0a
lang: en
authors:
  - Nikita Konkin
summary: "Two old Windows programs that GNSS data processing relied on, AbsolTEC (2017) for absolute total electron content and MapTEC (2014) for maps of its variations, now have native Python implementations built from the published methods. The compatibility mode differs from the original program by hundredths of a TECU, and the TuRBOTEC model from the paper by about 1–2 TECU, by design. TEC variations in three period bands are written to Parquet and shown on IonMaps maps."
image: /assets/ict_platform/dtec-preview.png
translation_of: 2026-11-21-absoltec-maptec.md
links:
  repo: "https://github.com/nikita-konkin/ict-hub"
tags: [ionosphere, gnss, tec, python, signal-processing, visualisation]
---

Two programs that matter for GNSS data processing existed only as Windows programs without source code. AbsolTEC, from 2017, estimates the absolute total electron content (TEC) above a station; MapTEC, from 2014, draws maps of TEC variations. In IonoPotok, AbsolTEC ran in a Windows XP virtual machine inside a Docker container, as described in the [breakdown of the orchestrator]({% link _articles/ict_platform/2026-10-01-ict-orkestrator-en.md %}). Between 18 and 21 November both programs got native Python implementations, and TEC variations got maps of their own in IonMaps.

## Why replace AbsolTEC

The original AbsolTEC is a 32-bit Windows program of 843 KB, built in April 2017. It runs under Wine or in a virtual machine, and that is where the failures piled up. One job on the server kept failing with exit code 9020 from the Windows XP guest, and the cause was never found. Another job reported success although some stations were never processed. Those errors are fixed in the hub itself: station failures are kept, and a batch job no longer claims a false success. But the dependency on Windows would have stayed without a replacement.

The native implementation neither calls the original program nor patches it. It runs without Windows, can compute on a one-minute grid, and is available in the hub as a separate AbsTEC Native converter. The old run in the virtual machine stays in place.

## A method from published papers

The AbsolTEC algorithm turned out to be the published single-station method of the Irkutsk group at the Institute of Solar-Terrestrial Physics (ISTP SB RAS). It is described in papers by Yu. V. Yasyukevich and co-authors from 2015 in Geomagnetism and Aeronomy and Results in Physics, and its successor, the TuRBOTEC model, in a 2020 paper in Sensors. The implementation follows them.

Above the station, vertical TEC is expanded in a second-order Taylor series in longitude, latitude and time: the value itself, its gradients and their quadratic terms, seven coefficients in all. Each slant TEC observation also gets a combined hardware delay of the satellite and the receiver for that pair. A slant value is converted to vertical by the mapping function of a single-layer ionosphere model with an Earth radius of 6371 km, a layer height of 450 km and a correction coefficient of 0.97 for mid-latitudes. The solution is sought in ±1 hour windows, and an observation weighs less the lower its satellite and the further it lies from the centre of the window.

Phase measurements are more precise than code measurements but carry an unknown constant. So on each continuous arc the phase is levelled to the code by one offset: the mean of the "code minus phase" differences, weighted by the inverse of the mapping function. The paper's printed formula for this step carries a stray factor, and the implementation follows the meaning rather than the typo.

The TuRBOTEC model adds two improvements, each switched on separately. The correction coefficient depends on the station's latitude: 0.87 within 25° of the equator, 0.97 at mid-latitudes and 0.94 above 65°. The solution can be non-negative: least squares with bounds require vertical TEC to be at least 0.5 TECU and each satellite's delay to stay below that satellite's smallest observed slant TEC minus the same 0.5 TECU. According to the paper, the bounded solution differs from the unbounded one by more than 1 TECU in about 9 % of epochs.

## Two modes, and a comparison with the original

The converter has two modes. The legacy-2017 mode repeats the peculiarities of the 2017 program: decimation to 30 seconds, a 10° arc threshold, a 124-second gap, a cap on input length, spike repair, and even an Earth radius of 6371302.0 m that appears in no published source. The published mode follows the paper consistently: 6371 km and 450 km everywhere, a pierce-point longitude that respects the quadrant, arcs split by the validity flag, and no length cap.

The comparison used data from the AKSU station for days 032–036 of 2025: both programs got identical GPS and GLONASS observation files, a 30-minute grid, a 10° elevation cutoff and a coefficient of 0.97. All seven coefficients and the delays were compared, with no interpolation.

{% include screen.html src="/assets/ict_platform/abstec-diff-en.webp" wide=true width=1839 height=919 max=920 caption="Root-mean-square difference of vertical TEC from the 2017 program, by day. Day 034 is incomplete: both programs have gaps, and 9 shared epochs were compared." alt="A horizontal bar chart for days 032, 033, 034, 035 and 036. The blue bars of the legacy-2017 mode are barely visible: 0.013, 0.021, 0.035, 0.010 and 0.023 TECU. The orange bars of the TuRBOTEC model from the paper: 1.63, 1.25, 0.25, 0.96 and 1.21 TECU" %}

The legacy-2017 mode differs from the original by hundredths of a TECU: a root-mean-square difference from 0.010 to 0.035 TECU, at most 0.044 TECU, and a correlation coefficient of no less than 0.999996. Even so, it failed strict acceptance with a tolerance of 0.001 TECU on every day, so the converter remains experimental. The model from the paper differs by 0.96–1.63 TECU on the complete days: it is a different scientific model, and nobody expected it to match the original.

The limitations are stated plainly: one station and five days, input RINEX 3.04 headers that had to be relabelled as 3.03, and the physical accuracy of both models against external sources, such as ionosphere models and TEC maps, not yet checked.

{% include screen.html src="/assets/ict_platform/abstec-native-form-en.webp" wide=true width=941 height=1850 max=420 caption="The AbsTEC Native converter form: mode, latitude-dependent coefficient, non-negative solution, and the number of stations processed in parallel." alt="Part of the AbsTEC Native form: model “published (TuRBOTEC model)”, a 0.5 h time step, a 10° elevation cutoff, a coefficient of 0.97, a 1 h window half-width, Latitude-Dependent Alpha and Non-Negative Bounded Solve ticked, an empty shell height field, and Parallel Jobs set to 4" %}

## All 48 cores of the server

On the server, the new converter took all 48 cores, although the server is shared. The OpenBLAS library inside the image started a busy-waiting thread for every core of the machine, and the hub created job containers with no CPU limit, so the hub's own limit of 12 cores did not apply to them. It is the same BLAS-thread trap as in the [previous breakdown]({% link _articles/ict_platform/2026-10-12-ict-karty-bystree-en.md %}), only in another container.

OpenBLAS in the image now runs in a single thread, and the "Parallel Jobs" setting decides the number of cores; on the solver tests this is also about 2.5 times faster than the default. Every container the hub starts is limited by the `CONVERTER_CPUS` setting: 12 cores by default, 0 to lift the limit, and a value above the machine's core count is clamped, because Docker rejects such a limit.

## From MapTEC to TEC variations

MapTEC, a 2014 program from ISTP SB RAS, draws maps of filtered TEC variations at ionospheric pierce points on a thin shell 300 km high. The reconstruction first explained why the archived maps were empty: the `DT.dia` format description shipped with the program expected seven fields at fixed positions that crossed the real field boundaries of the observation files. The result was 2,881 empty files and not one of four map epochs filled. An exact match with the original could not be reached: a 40-sample time shift remained.

So the converter was built anew under a new name, TEC Variations, or dTEC. The processing goes like this:

1. The slant TEC series is split into arcs at loss of lock, long gaps and elevations below 30°.
2. Gaps of up to two samples are filled by linear interpolation.
3. A quadratic trend is subtracted from phase TEC: it absorbs the unknown phase constant and the smooth curvature.
4. The residual passes a fourth-order Butterworth band-pass filter twice, forwards and backwards, so there is no phase shift. The arc's edges are protected by a reflected extension.
5. The slant variation is converted to vertical on a 300 km shell.

The default period bands are 2–10, 10–20 and 20–60 minutes, as in the SIMuRG system. The result is one Parquet table per station and day: time, station, satellite, elevation and azimuth, pierce-point coordinates, the slant-to-vertical factor, the arc number and the variations in three bands.

{% include screen.html src="/assets/ict_platform/tec-variations-form-en.webp" wide=true width=941 height=864 max=420 caption="The TEC Variations converter form: allowed gap, filter, period bands and elevation cutoff." alt="Part of the TEC Variations form: Maximum absent points set to 2, filter butterworth, period bands 2-10,10-20,20-60 minutes and an elevation cutoff of 30°, each with a short hint" %}

The new filter was checked against MapTEC's old running-mean method on an archived day, 30 April 2015: 220 tracks, and 104,682 rows with identical observation keys from both methods. The root-mean-square of the variations from the Butterworth filter is lower in all three bands, 0.015, 0.018 and 0.045 TECU, while the old method gives 0.020, 0.025 and 0.099 TECU respectively. The old method, on the other hand, returns values where the new filter leaves an arc's edge empty. For comparison, the old running means can be switched on as a separate mode.

## Maps of variations in IonMaps

IonMaps has a new data source, "TEC variations (dTEC)". Dates, stations and bands come straight from the Parquet tables. A chosen band and moment give a snapshot, and an interval gives a GIF, MP4 or WebM animation built as a background job. On each frame, every station–satellite pair shows its nearest sample within half the frame step, and a point with no value in the band stays empty.

{% include screen.html src="/assets/ict_platform/dtec-map-en.webp" wide=true width=1600 height=1049 caption="A snapshot of TEC variations in the 20–60 minute band at 03:00 UTC: 128 pierce points on a 350 km shell. Synthetic data: 16 made-up stations and a simulated travelling disturbance with a 30-minute period." alt="An IonMaps snapshot under the Run TEC map button: points on axes of longitude 42–55° and latitude 53–59°, coloured by TEC variation on a symmetric scale from blue (−0.2 TECU) to red (+0.2 TECU)" %}

The default frame step is one minute. The symmetric scale is chosen automatically by default, from the 98th percentile of the absolute variation in the data window but never narrower than ±0.01 TECU, and it can be set by hand. One request covers up to 40 stations and 1,440 frames.

The last link is the DAT → Parquet converter. It used to know nothing of AbsTEC Native results, so they never reached the data analysis section. It now has an "AbsTEC Native output" source that writes to the same Parquet tree as the old AbsTEC, with an identical table schema.

## Conclusions

1. Reconstructing an old program from published papers also checks the papers: a stray factor turned up in a printed formula, and an Earth radius found in no source turned up in the program.
2. Agreement to hundredths of a TECU is not acceptance yet. The strict tolerance was not met, so the new converter runs beside the old one rather than in its place.
3. BLAS threads must be limited in every image, and job containers separately from the hub's container: the hub's limit does not extend to the containers it starts.
4. A zero-phase band-pass filter defines its band edges explicitly. The price is empty arc edges, and it is better to show them honestly on a map than to fill them in.

## Availability

The AbsTEC Native and TEC Variations converters are described in the repository's README, and the methods and comparisons in its `docs` folder.

- Source code: [github.com/nikita-konkin/ict-hub](https://github.com/nikita-konkin/ict-hub)
