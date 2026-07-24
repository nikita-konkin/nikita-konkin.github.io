---
title: "ICT: from slant TEC to ionosphere maps — the IonMaps method"
project: ict_platform
pair: ict-ionmaps
platform: Web
type: Technical breakdown
date: 2026-07-24
lang: en
authors:
  - Nikita Konkin
summary: "How the IonMaps module in ICT turns TEC-suite parquet output into regional maps of vertical total electron content: VTEC restoration from slant TEC, interpolation (linear, kriging, LPI), derived propagation fields, and accuracy validation by leave-one-station-out cross-validation."
translation_of: 2026-07-24-ict-ionmaps.md
tags: [programming, python, gnss, ionosphere, tec, kriging]
featured: true
---

The June article carried data from RINEX archives through total electron content, coherence bands, and DuckDB analytics. All of that is per-station time series. The next question is spatial: what does the ionosphere look like over a region at a given moment? The new IonMaps module answers it by turning TEC-suite parquet output into regional maps of vertical TEC and several derived propagation fields. The method is a compact implementation of the standard thin-shell mapping used by global TEC maps (Mannucci et al.; Schaer), adapted to a regional network without external calibration catalogues.

## From slant to vertical TEC

The input is slant TEC per station–satellite link: phase `TEC_phase` (precise but ambiguous) and code `TEC_code` (absolute but noisy), plus elevation, azimuth, and the receiver position from the parquet header. Samples below the elevation cutoff `θ_min = 20°` are dropped.

Each link is split into continuous phase arcs: a gap longer than 1.5× the sampling interval (or a validity-flag break) starts a new arc. Then phase is levelled to code: each arc is shifted by `median(TEC_code − TEC_phase)`, giving `STEC = TEC_phase + shift`. That puts phase precision on an absolute level; arcs shorter than three valid samples are discarded.

The inter-frequency receiver bias is estimated by minimum standard deviation: a grid search minimises the scatter of night-time VTEC — a single-site technique in the spirit of the GEONET bias estimation. Satellite biases are not assimilated (there are no external DCB catalogues), so the VTEC scale is relative: spatial structure and dynamics are correct, but the absolute level may carry a common offset of a few TECU. That is an honest limitation of the method, not an error swept under the rug.

Finally, STEC is projected to the vertical with the single-layer model at `h_ion = 350 km`: `VTEC = STEC / M(χ)`, where `M(χ) = 1/√(1 − sin²χ)` and χ is the zenith angle at the ionospheric pierce point. Pierce-point coordinates come from elevation, azimuth, and the shell height; negative VTEC is clipped to zero.

## Building the map

Samples are binned into `ΔT = 15 min` frames — an order of magnitude finer than the two-hour cadence of the global IGS maps — leaving one averaged point per station per frame. The field is then interpolated onto a regular 1° grid by one of three selectable principles:

- **linear** (default) — Delaunay triangulation with linear interpolation inside the convex hull and nearest-neighbour fill outside; fast and predictable;
- **kriging** — ordinary kriging on the sphere with an exponential variogram fitted to each frame's own semivariogram. Kriging weights noisy samples through the nugget effect and relaxes to the field mean away from data instead of building nearest-neighbour plateaus;
- **LPI** — local polynomial interpolation: at each grid node a degree-1 polynomial is fitted with a Gaussian weight (σ = 200 km), switching to degree 2 where the neighbourhood holds at least seven effective stations. Comparative studies rank kriging and LPI among the two most accurate local methods for ionosphere mapping.

The field is physically meaningful only near measurements, so cells farther than `R_cov = 300 km` from the nearest pierce point are masked; the mask is evaluated at render resolution, so the boundary is a smooth union of circles rather than a pixel staircase. On top of that comes Gaussian smoothing with `σ ≈ 1` grid cell (about 100 km at a 1° step, matching the published mid-latitude TEC decorrelation scale of 80–130 km). The colour scale uses the 5–95% quantiles of the selection, or explicit bounds for cross-frame comparability.

## Derived propagation fields

Here the map meets the coherence-band theme the whole platform is built around. Pointwise transforms of the VTEC grid (`N_t = VTEC·10¹⁶ el/m²`, frequencies from the signal-band table for GPS, GLONASS, Galileo, and BeiDou) give:

- **GDD** — the group-delay dispersion magnitude [ns/GHz];
- **B_k** — the coherence bandwidth [MHz];
- **|∇VTEC|** — the horizontal gradient magnitude [TECU / 100 km], with a per-latitude correction of the longitudinal step.

So a single map yields both the electron content and the quantities that decide the fate of a signal passing through that medium.

## Accuracy validation: leave-one-station-out

Map quality is checked by leave-one-station-out cross-validation. In every frame each station is removed in turn, the field is predicted at its pierce point from the remaining stations with the same interpolator, and the prediction errors (bias, MAE, RMSE in TECU) are aggregated overall, per station, and per frame; `interpolation=both` compares linear against kriging. Reference accuracy levels for regional networks are 0.5–1 TECU in quiet conditions and 1.5–2 TECU in disturbed ones. Excluded points that fall outside the coverage radius of the remaining stations are not counted.

In practice the error budget is dominated by residual receiver calibration, not by the interpolator — so LOSO doubles as an automatic station QC tool: a station whose removal barely changes the field is fine; one whose residuals blow up is poorly calibrated. `show_accuracy=true` prints the per-frame RMSE directly on the rendered map.

## Output formats

The result is served so it can be both viewed and dropped into a report: animation as GIF, MP4 (H.264), or WebM (VP9); an interactive Plotly snapshot; a static PNG/SVG frame up to 600 dpi for publications; a validation report in JSON/CSV; and station coordinates with proximity grouping for the UI. These are all endpoints under `/tec-map/*`, and the full engineering reference lives in `docs/tec_map_service_overview.md`.

## Takeaway

Where the June article left a pipeline that produced per-station numbers, IonMaps closes it onto a spatial picture with a built-in accuracy budget. The module lives inside the same ConverterHub web orchestrator (FastAPI and HTMX), reads the same parquet output, and shows maps and validation through the same interface — so the whole path from a RINEX archive to a validated regional map stays one reproducible system.

- Repository (orchestrator): [github.com/nikita-konkin/ict-hub](https://github.com/nikita-konkin/ict-hub)
