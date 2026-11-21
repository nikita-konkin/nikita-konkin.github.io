---
title: "The phase direction-finding method in unmanned aerial vehicle systems: principles, algorithms and an analysis of modern approaches"
pair: fazovaya-pelengatsiya-bpla
lang: en
date: 2026-11-21
translation_of: 2026-11-21-fazovaya-pelengatsiya-bpla.md
summary: "A review of the phase direction-finding method on unmanned aerial vehicles (UAVs) is given over 2019–2025 publications. The physical basis of the method, the resolution of phase-measurement ambiguity, combined methods and multi-position systems based on a group of UAVs are considered."
paper_title: "The phase direction-finding method in unmanned aerial vehicle systems: principles, algorithms and an analysis of modern approaches"
paper_authors: "Smirnov V.E. (supervisor — Konkin N.A.)"
paper_year: 2026
paper_date: "2026"
paper_venue: "Scientific Progress — Creativity of the Young, 2026, no. 1, pp. 778–781"
paper_link: "https://www.elibrary.ru/item.asp?id=93329718"
tags: [phase-direction-finder, UAV, interferometer, ambiguity-resolution, positioning]
---

## Problem and relevance

The development of unmanned aerial vehicles (UAVs) has created new tasks in radio monitoring and electronic warfare: drones are both objects to be detected and promising carriers of direction-finding equipment, offering high mobility and monitoring of hard-to-reach areas. The phase direction-finding method, based on measuring the phase difference of a signal across spatially separated antenna elements, gives high accuracy of angular coordinates with a comparatively small antenna system.

## Aim and hypothesis

The aim is to analyse the accuracy characteristics of the phase direction-finding method as applied to UAVs and to summarise the methods for improving them. No hypothesis is stated explicitly. The novelty is claimed by the author: a systematisation of methods for improving the accuracy of phase direction finding on UAVs from 2019–2025 publications.

## Materials and methods

The work is built as a review of 2019–2025 publications. The design features of on-board phase direction finders and the problem of resolving phase-measurement ambiguity are considered: the phase difference is determined up to an integer multiple of 2π (2πm, where m is an integer). To resolve it, multi-base antenna systems with bases of different lengths are used — measurements on short bases determine m for the long bases that provide high accuracy. Processing algorithms (spectral analysis, a sliding buffer for increasing the number of estimates), the joint use of the phase and range-difference methods, multi-position systems and machine-learning methods are examined separately.

## Results

The author notes that the phase method is one of the most effective ways to determine the angular coordinates of radio-emission sources with direction-finding equipment on board a UAV. The sliding-buffer algorithm (from the work of Kozhabayeva et al.) increases the number of direction-finding estimates when the observation time is limited; spectral processing separates signals from noise and resolves sources at close frequencies. The joint use of the phase and range-difference methods improves positioning accuracy and the effectiveness of ambiguity resolution, and a group of UAVs in a multi-position system improves accuracy, continuity of tracking and interference immunity.

## The author's conclusions

The author concludes that current research is directed at creating compact broadband antenna systems, developing algorithms for removing phase-measurement ambiguity, optimising carrier trajectories, creating multi-position systems based on a group of UAVs, and improving interference immunity through spectral processing and adaptive filtering.

## Limitations

The review contains no measurements or modelling of its own, and the qualitative conclusions (about "high accuracy" or "effectiveness") are not supported by quantitative figures. The comparison between methods is not formalised: the accuracy, mass and range of the different approaches are not brought into a table. The stated development directions are listed without their limitations or conditions of applicability.

## Novelty

The novelty is claimed by the author: a systematisation of methods for improving the accuracy of phase direction finding on UAVs — processing algorithms, trajectory optimisation and multi-position systems — from an analysis of 2019–2025 publications.

## Heuristics

- **[explicit]** If a phase difference is measured with a 2πm ambiguity — use multi-base antenna systems with bases of different lengths, because the short bases determine the integer m for the long bases that provide accuracy.
- **[reconstructed]** If the observation time is limited — form direction-finding estimates with a sliding buffer, because this increases the number of estimates without lengthening the observation.
- **[reconstructed]** If positioning accuracy and interference immunity are needed — combine several UAVs into a multi-position system, because joint processing from separated carriers improves source tracking.
- **[reconstructed]** If propagation conditions change — consider machine-learning methods for processing direction-finding information, because they allow adapting to changes and improving accuracy at a low signal-to-noise ratio.

**In one sentence:** The phase direction-finding method on board a UAV gives high angular-coordinate accuracy with a small antenna system, and its accuracy is improved by multi-base ambiguity resolution, combination with the range-difference method and multi-position systems of a UAV group.
