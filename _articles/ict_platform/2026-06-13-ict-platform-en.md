---
title: "ICT: a platform for processing ionospheric sounding data"
project: ict_platform
pair: ict-platform
translation_of: 2026-06-13-ict-platform.md
platform: Web
type: Technical overview
date: 2026-06-13
source_rev: aa4783748915ad1a5ab67311393adbfbe7b52715
lang: en
authors:
  - Nikita Konkin
summary: "An overview of the idea and structure of ICT — a set of containerised services that carry GNSS data from RINEX archives to total electron content, coherence bands, maps, and analytics, making the whole path reproducible."
tags: [programming, python, fastapi, docker, gnss, ionosphere, data]
featured: true
---

Data from global navigation systems (GPS, GLONASS) carries more than coordinates: it also encodes the state of the ionosphere — the medium the signal travels through. Extracting that information from raw observations and bringing it to a form fit for analysis takes many heterogeneous steps: unpacking archives, converting formats, computing electron content, statistics, visualization. ICT gathers these steps into a single platform and makes the whole path reproducible.

## The goal

Historically this kind of processing was a loose collection of separate utilities, scripts, and manual operations, glued together through a graphical interface and intermediate files. It works, but it scales poorly and is hard to repeat: reproducing the same result six months later means manually replaying the entire chain by hand.

ICT addresses exactly this — it turns a scattered set of tools into a connected pipeline where every stage is isolated, containerised, and invoked uniformly. The goal is not a new processing method but making existing methods routinely reproducible: the same input always yields the same output, and running any step comes down to a button press or an API call.

## What the platform is made of

ICT is built as a set of small services, each responsible for its own segment of the data path.

- **TEC extraction.** The base layer turns RINEX archives into slant total electron content (TEC) values for every station–satellite pair, preserving the observation geometry. This is the input for everything else.
- **Absolute electron content.** A dedicated service runs the computation of absolute vertical TEC from the prepared data, organising input and output along a year / day / station scheme.
- **Columnar storage.** A converter translates text `.dat` files into the Parquet format and back, while preserving the service headers in metadata. The columnar format speeds up subsequent queries and analytics by an order of magnitude.
- **Analytics backend.** A DuckDB-based service runs queries directly over the Parquet files with no intermediate conversions: TEC and coherence-band time series, statistics with Student confidence intervals, ready-made plots, and export to JSON, CSV, or XLSX.
- **Map building.** A prototype produces animated vertical-TEC maps over a station network, interpolating at the ionospheric pierce points over an OpenStreetMap basemap.
- **Web orchestrator.** On top of all this sits a web interface that launches the converter containers, passes them parameters, streams logs in real time, and keeps a run log: who ran what, with which flags, and with what result.
- **Internal access layer.** An nginx reverse proxy provides access to the services within a private network under readable names.

The coherence band — a parameter describing the state of a wideband radio channel — is computed here from absolute TEC and passes through the same query, statistics, and plotting machinery as every other quantity.

## The technology stack

The platform is built on Python 3.12. The web services use FastAPI; the orchestrator interface is built with HTMX, streaming logs over Server-Sent Events — which gives a reactive UI without a heavy JavaScript framework and without a build step. Analytics rests on DuckDB over Parquet (PyArrow); plotting uses matplotlib and Plotly. Run metadata is stored in SQLite via SQLAlchemy. Everything is packaged in Docker and orchestrated with Docker Compose; the outer layer is nginx. To run legacy Windows computation programs inside a Linux container, Wine is used. Each service comes with its own pytest suite.

The choice of tools follows a single idea — simplicity of operation. Columnar Parquet instead of a relational database for heavy queries, DuckDB with no separate server, HTMX instead of a SPA, SSE instead of WebSockets where only a one-way stream is needed: each decision removes one more moving part.

## The link to research

The idea for the platform grew out of practical work with ionospheric radio channels. Earlier versions of such processing were built around automating graphical utilities and a relational database — a working approach, but a brittle and poorly reproducible one. ICT can be seen as a modern reimagining of the same pipeline: the same physical quantities — TEC and coherence band — but obtained through programmatic interfaces, containers, and columnar storage rather than by driving someone else's GUI.

## What comes next

The present value of ICT is that the scattered processing steps have become a single, repeatable process. The structure it sets up — isolated services sharing common data formats — lets the platform grow piece by piece: adding new converters with a single registry entry, extending the analytics with new metrics, and connecting additional data sources without rewriting the rest.
