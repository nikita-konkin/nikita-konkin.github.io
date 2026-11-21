---
title: "Comparative analysis and justification of the choice of face recognition methods and software for the security systems of educational institutions"
pair: raspoznavanie-lits
lang: en
date: 2026-11-21
translation_of: 2026-11-21-raspoznavanie-lits.md
summary: "The authors compare the face recognition frameworks DeepFace and InsightFace for access control in educational institutions. According to the figures quoted in the paper, InsightFace reaches 99.8–99.83 % accuracy on the LFW corpus and DeepFace about 97.35 %, so InsightFace is chosen for systems with many users."
paper_title: "Comparative analysis and justification of the choice of face recognition methods and software for the security systems of educational institutions"
paper_authors: "Fomichev D.A., Mikheev S.E. (supervisor — Konkin N.A.)"
paper_year: 2026
paper_date: "2026"
paper_venue: "Scientific Progress — Creativity of the Young, 2026, no. 1, pp. 785–787"
paper_link: "https://www.elibrary.ru/item.asp?id=93329720"
tags: [face-recognition, computer-vision, neural-networks, biometrics, access-control, InsightFace]
---

## Problem and relevance

Educational institutions need reliable access control. Traditional identification depends on the human factor, allows passes to be handed to third parties and limits how fast people can be processed. Computer vision and machine learning can automate identification, but, the authors say, there is no well-founded choice of face recognition tools for educational institutions.

## Aim and hypothesis

The aim is to justify the choice of a face recognition method and software for access control. No hypothesis is stated explicitly; in substance the paper tests that InsightFace suits such systems better than DeepFace.

## Materials and methods

This is an analytical review without an experiment of its own: the paper describes no dataset or shooting conditions. The authors list the stages of recognition — face detection, alignment, feature extraction, comparison with a database — and the quality factors: lighting, viewing angle, resolution, changes in appearance. The frameworks DeepFace and InsightFace (the ArcFace method) are compared on accuracy on the LFW corpus, scalability, GPU support, latency and purpose. The figures come from external sources [3, 6].

## Results

DeepFace, developed in 2014, shows about 97.35 % on LFW (about 97.3 % in the table); the authors note that in practice accuracy may fall. InsightFace reaches 99.8–99.83 % on LFW and about 98 % on the MegaFace corpus, which, in the authors' words, confirms its effectiveness at scales of up to a million faces; it works with embeddings, usually 512-dimensional, and is optimised for GPUs and batch processing. According to Table 1, InsightFace has high scalability, lower latency and is meant for industrial systems; DeepFace has low scalability, higher latency and is meant for prototypes. No numerical latency values are given.

## Authors' conclusions

Neural approaches (ArcFace) improve accuracy over classical methods. The key factor in the choice is not only accuracy but also the scalability of the feature space. The choice of InsightFace is justified for systems with many users.

## Limitations

There are no measurements of the authors' own: accuracies are taken from the literature, and the conditions of the institution — number of users, cameras, lighting — are not specified. The requirements for the system, listed among the tasks, are not formulated. The advantage over classical methods is given without numbers, and latency is described in words, «higher» and «lower». Only two frameworks are considered; the protection of biometric data is not touched on.

## Novelty

The paper does not claim novelty explicitly. Its contribution is a comparison of two frameworks on published figures and a justification of InsightFace.

## Heuristics

- **[explicit]** If a method is chosen for a system with many users — assess not only accuracy but also the scalability of the feature space.
- **[reconstructed]** If a framework is needed for an industrial system rather than a prototype — check GPU and batch-processing support, because DeepFace is described as a wrapper for prototyping.
- **[reconstructed]** If an accuracy figure comes from an open corpus — test it on images from your own institution, because the authors name lighting, viewing angle and resolution as quality factors.

**In one sentence:** On published figures InsightFace with ArcFace is more accurate and scales better than DeepFace (99.8–99.83 % and about 97.35 % on LFW), so the authors choose it for access control, but the paper contains no tests of its own.
