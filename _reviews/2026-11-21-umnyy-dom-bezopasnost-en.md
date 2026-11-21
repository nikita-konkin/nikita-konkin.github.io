---
title: "Security of smart-home systems based on the Internet of Things"
pair: umnyy-dom-bezopasnost
lang: en
date: 2026-11-21
translation_of: 2026-11-21-umnyy-dom-bezopasnost.md
summary: "Information-security threats to Internet-of-Things (IoT) smart-home systems are systematised and classified by the three levels of the architecture. Weak authentication, missing encryption and irregular firmware updates are named the most critical; protection needs a combination of technical and organisational measures."
paper_title: "Security of smart-home systems based on the Internet of Things"
paper_authors: "Sannikov F.B. (supervisor — Konkin N.A.)"
paper_year: 2026
paper_date: "2026"
paper_venue: "Scientific Progress — Creativity of the Young, 2026, no. 1, pp. 764–767"
paper_link: "https://www.elibrary.ru/item.asp?id=93329713"
tags: [internet-of-things, smart-home, information-security, data-protection, authentication]
---

## Problem and relevance

The Internet of Things (IoT) is actively entering everyday life through smart-home systems that join devices and sensors into a single remotely controlled network. The growing number of connected devices increases the potential information-security threats, and the limited computing power of IoT devices does not allow full protection systems, as on a personal computer.

## Aim and hypothesis

The aim is to systematise the current security threats to IoT smart-home systems and analyse protection methods with regard to the devices' limited computing resources. No hypothesis is stated explicitly; in substance a classification of threats by the levels of the IoT architecture is proposed.

## Materials and methods

The smart home is treated as a three-level system: the device level (sensors, actuators, controllers), the network level (Wi-Fi, Zigbee, Z-Wave and MQTT protocols) and the application and cloud-service level. Vulnerabilities are identified for each level: at the device level, weak authentication mechanisms, missing encryption and missing automatic firmware updates; at the network level, man-in-the-middle attacks, DoS attacks and unprotected protocols; at the application level, data leaks through cloud APIs, weak access-right separation and mobile-application vulnerabilities. Protection methods are considered: network segmentation, encryption, multifactor authentication, blockchain, intrusion-detection systems (IDS) and standardisation.

## Results

Network segmentation isolates IoT devices from the main home network, so that compromising a smart socket or a camera does not open access to critical data. IDS are adapted to limited resources by placing sensors on network gateways. Blockchain suits decentralised access control and an event log, but because of its high computational cost its use is limited to experimental systems. The Matter protocol, which includes security requirements at the specification level, and mandatory certification of devices under the IEC 62443 standards are named promising directions.

## The author's conclusions

The author concludes that the most critical vulnerabilities are weak authentication, missing encryption of transmitted and stored data, and irregular firmware updates. Effective protection needs a combination of technical measures (network segmentation, traffic encryption, multifactor authentication) and organisational ones (software updates, replacing default passwords).

## Limitations

The paper is a review and contains no measurements of its own, no experimental data and no quantitative estimates of the effectiveness of the proposed measures. Some statements rely on a single source ("Smart Home with Your Own Hands"), and the practical recommendations for users (network segmentation, software updates, replacing default passwords) are named, but the steps for carrying them out are not described. The link between a specific threat and a specific protection measure is shown at the level of general statements.

## Novelty

The paper does not claim novelty explicitly. In substance it proposes a classification of smart-home security threats by the three levels of the IoT architecture and summarises protection methods with regard to the devices' constraints.

## Heuristics

- **[explicit]** If a smart home contains IoT devices — segment the network, separating them from computers and smartphones, because this way compromising one device does not open access to critical data.
- **[explicit]** If IoT devices are resource-constrained — place intrusion-detection sensors on network gateways, because this removes the load from the end devices.
- **[reconstructed]** If a uniform security level is needed — rely on standards and certification (Matter, IEC 62443), because scattered proprietary solutions hinder universal protection.
- **[reconstructed]** If blockchain is applied to a smart home — account for its computational cost, because on low-power devices it is so far usable only in experiments.

**In one sentence:** Security of an IoT-based smart home requires protecting all three architecture levels — devices, network and applications — and the most critical vulnerabilities are addressed by combining network segmentation, encryption, multifactor authentication and regular firmware updates.
