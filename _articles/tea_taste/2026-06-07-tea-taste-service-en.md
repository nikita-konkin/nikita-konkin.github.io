---
title: "Tea Taste: Turning a Tea Tasting into Reproducible Data"
project: tea_taste
platform: VK
type: Technical breakdown
date: 2026-06-07
lang: en
authors:
  - Nikita Konkin
summary: "A breakdown of the idea and features of Tea Taste — a web app that records brewing parameters and sensory impressions across infusions and turns a subjective tea evaluation into a structured record."
translation_of: 2026-06-07-tea-taste-service.md
links:
  repo: "https://github.com/nikita-konkin/tea-taste-frontend"
tags: [programming, react, nodejs, express, mongodb, product]
---

A tea tasting usually survives only in memory and a few scattered notes: water, temperature, steeping time, impressions. Such information is hard to compare and almost impossible to reproduce. Tea Taste addresses exactly this problem — it turns a subjective tea evaluation into a structured record that can be compared with others and repeated.

## The idea

The project rests on a simple observation: the impression from a cup of tea consists of two parts that differ in nature. The first is the objective brewing parameters: variety, dose, water, temperature, teaware, method. The second is the subjective sensory experience: aroma and taste, which moreover change from one infusion to the next.

The app deliberately separates these two parts. The objective parameters are set once for the whole tasting, while the sensory evaluation is recorded separately for each infusion. This makes it possible to describe the same brew honestly: not "the tea is good," but "the third infusion at 90 °C gave a denser aroma than the first."

## The data model

A tasting record consists of several related entities tied together by a session identifier (`sessionId`):

- **Tea (`teaform`)** — the brewing parameters: name, country, shop, type, dose, water brand and volume, temperature, price per gram, brewing method, teaware, a publication flag, and the average rating.
- **Infusion (`brewing`)** — a single brew within a session: a text description, the infusion's time and rating, and an ordinal number (`brewingCount`).
- **Aroma (`aroma`)** and **taste (`taste`)** — recorded in stages (`stage1`, `stage2`, `stage3`), reflecting how the bouquet develops within a single infusion.

This structure stores not a single averaged impression but the full picture: how the tea unfolds over several infusions.

## Features

**A multi-step form.** Input is split into two stages: first the tea and brewing parameters, then the sensory evaluation. The draft is saved in `localStorage`, so accidentally closing the tab does not lose the entered data.

**Autocomplete dictionaries.** The fields for name, country, shop, water, teaware, and brewing method draw on prepared lists — from Chinese varieties (Longjing, Tieguanyin, Da Hong Pao) to retail brands and water labels. This speeds up input and keeps names consistent, which matters for later comparison.

**Per-infusion rating.** Each infusion has its own rating on a scale up to ten, set with custom tea-bowl icons, and its own description. The infusion ratings combine into the tea's average rating.

**A built-in timer.** A timer with a sound signal is provided for steeping an infusion — a small but practical detail: the hands are busy with the teapot, not a stopwatch.

**A public feed.** A tasting can be marked as public and published. On the API side, public and private data are separated into distinct routes.

## Architecture

The project is split into a frontend and a backend.

- **Frontend** — a single-page application on React (Create React App) and Material UI. The forms are built on `react-hook-form`, routing on `react-router`, and protected sections are available only after signing in.
- **Backend** — a REST API on Node.js and Express, storing data in MongoDB through Mongoose. Authentication is implemented with JWT and password hashing (`bcryptjs`), input is validated with `celebrate`, and baseline protection comes from `helmet`, request rate limiting, and CORS configuration.

Both services are packaged in Docker, which makes spinning up the environment reproducible.

## What comes next

The key value of Tea Taste is not an individual record but the accumulated body of comparable tastings. On that basis it is natural to develop comparisons of brews of the same variety, analytics by water and temperature parameters, and brewing recommendations. The current version lays down the data structure for exactly that.

- Repository (frontend): [github.com/nikita-konkin/tea-taste-frontend](https://github.com/nikita-konkin/tea-taste-frontend)
- Repository (API): [github.com/nikita-konkin/tea-taste-api](https://github.com/nikita-konkin/tea-taste-api)
