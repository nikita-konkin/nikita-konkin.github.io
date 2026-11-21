---
title: "A web system for remote control of an ionospheric sounding complex"
pair: veb-upravlenie-zondirovaniem
lang: en
date: 2026-11-21
translation_of: 2026-11-21-veb-upravlenie-zondirovaniem.md
summary: "A comparative analysis of technologies for a web system that remotely controls an ionospheric sounding complex is carried out, and the choice of the Django, Jinja2 and Docker stack is justified. An initial prototype is developed; the authors write that it can be integrated with the DIDBase Station list and then state that this integration gives it a list of 131 ionospheric sounding stations."
paper_title: "A web system for remote control of an ionospheric sounding complex"
paper_authors: "Mukhamedzyanov R.R., Titov D.N. (supervisor — Konkin N.A.)"
paper_year: 2026
paper_date: "2026"
paper_venue: "Scientific Progress — Creativity of the Young, 2026, no. 1, pp. 740–742"
paper_link: "https://www.elibrary.ru/item.asp?id=93329705"
tags: [ionospheric-sounding, ionosonde, web-system, Django, Docker, SCADA]
---

## Problem and relevance

Modern tasks of industrial automation and scientific research call for effective systems for remotely controlling measurement equipment. Existing solutions, including SCADA systems and proprietary software, are not flexible enough for unique installations such as ionospheric sounders. The development of web technologies opens the way to building reliable and easily integrated control systems.

## Aim and hypothesis

The aim is to analyse technological solutions and design the architecture of a web system for remote control of an ionospheric sounding complex based on Django, justifying the choice of the stack and developing an initial prototype. No hypothesis is stated explicitly.

## Materials and methods

A comparative analysis of SCADA systems and the Django, Flask and FastAPI frameworks was carried out by the criteria of built-in authentication and an administration interface, object-relational mapping (ORM), suitability for rapid development and the entry threshold. The architecture is built on Django and Jinja2 modules: Django is the base platform, Jinja2 provides server-side generation of dynamic HTML pages, and Docker containerisation provides portability, isolation and scaling. The prototype interacts with a configuration and scheduling database and, according to the paper, can be integrated with the DIDBase Station list, a digital ionogram database.

## Results

The analysis showed that only Django provides built-in authentication mechanisms, a ready administration interface and an ORM, whereas Flask and FastAPI lack them and need third-party libraries or independent implementation. An initial prototype of a web interface was developed with selection of the configuration of an oblique-sounding ionosonde; the paper first says the prototype “can be integrated” with the DIDBase Station list and then states that, thanks to this integration, it supports an up-to-date list of 131 ionospheric sounding stations. Django and the database run in Docker containers, orchestrated with Docker Compose.

## Authors' conclusions

The authors conclude that the choice of the Django, Jinja2 and Docker stack is justified and that the initial prototype confirmed the workability of the proposed architecture. For further industrial adoption they recommend phased deployment, monitoring of operation and backup of configurations.

## Limitations

The prototype is at an early stage: no quantitative figures for the system's performance, reliability or security are given, and testing of control of real equipment on an installation is not described: the authors only write that parameters from the database control the equipment. The framework comparison relies on qualitative criteria without measurements. Integration with the DIDBase Station list is described as possible and immediately used as the basis for the list of 131 stations; its details and verification result are not disclosed.

## Novelty

The paper does not claim novelty explicitly. In substance it proposes a modular architecture for a web control system for an ionosonde on the Django, Jinja2 and Docker stack with possible integration into the DIDBase Station list.

## Heuristics

- **[explicit]** If a web system must control a unique installation — choose a framework with built-in authentication, an administration interface and an ORM (Django), because this speeds up development and covers basic security requirements.
- **[reconstructed]** If a system must move between environments — package the components in Docker containers with Compose orchestration, because this standardises the environment and simplifies deployment.
- **[reconstructed]** If an up-to-date list of stations is needed — connect to an existing database (DIDBase) rather than maintaining a private list, because the external base already holds a list of 131 stations.

**In one sentence:** For remote control of an ionospheric sounding complex the Django, Jinja2 and Docker stack is justified, and the initial prototype, according to the authors, supports a list of 131 ionospheric sounding stations when integrated with the DIDBase Station list.
