---
title: "Developing a hardware-software system for automatic satellite antenna orientation based on telemetry analysis"
pair: orientatsiya-antenny
lang: en
date: 2026-11-21
translation_of: 2026-11-21-orientatsiya-antenny.md
summary: "A hardware-software system is built on an Arduino UNO R3 with a u-blox NEO-M8N GNSS receiver and a 28BYJ-48 stepper motor, which orients a satellite antenna automatically using the HDOP parameter. In the experiments the average time to establish the optimal position was 1.6–4.2 minutes; HDOP dropped from 3.2 to 1.8 (by 43.75 %) and positioning errors fell by 40 %."
paper_title: "Developing a hardware-software system for automatic satellite antenna orientation based on telemetry analysis"
paper_authors: "Marsyukov N.S. (supervisor — Konkin N.A.)"
paper_year: 2025
paper_date: "2025"
paper_venue: "Scientific Progress — Creativity of the Young, 2025, no. 1, pp. 503–505"
paper_link: "https://www.elibrary.ru/item.asp?id=83009913"
tags: [satellite-antenna, GNSS, HDOP, Arduino, telemetry, positioning]
---

## Problem and relevance

Accurate positioning of satellite antennas matters for reliable communication on moving objects and in difficult terrain. Manual tuning is ineffective in dynamic scenarios, so automation based on telemetry reduces signal loss and raises transmission reliability.

## Aim and hypothesis

The aim is to develop a hardware-software system for the automatic orientation of a satellite antenna toward the optimal signal reception, based on the analysis of telemetry data. No hypothesis is stated explicitly.

## Materials and methods

The system is built on an Arduino UNO R3 microcontroller; satellite signals are received by a multi-system u-blox NEO-M8N GNSS receiver (GPS, GLONASS, Galileo, BeiDou), which sends data in NMEA 0183 format (GPGGA messages with coordinates and time, GPGSA messages with the HDOP parameter). HDOP reflects the influence of satellite geometry on accuracy: values below 1 are ideal, above 3 a critical error. Control follows five steps: initialization (the antenna at 0°, the 28BYJ-48 motor calibrated over ±180°); continuous reading of HDOP, with a search for a position triggered when a threshold is exceeded (the paper gives HDOP > 3.0 as an example); a rotation by a fixed angle of 15° through the ULN2003 driver with a pause of 5–10 seconds; storing the HDOP for each angle and picking the angle with the minimum HDOP after a ±180° cycle; background monitoring with a repeated search when the signal degrades. The program is written in C++.

## Results

The average time to establish the optimal position is 1.6–4.2 minutes at a step of 15°, pauses of 5–10 s and an analysis of 12–24 positions. The HDOP drops from 3.2 to 1.8 (by 43.75 %), and the positioning errors fall by 40 %. The author takes this as confirmation of the system's ability to stabilize the signal in dynamic conditions.

## The author's conclusions

The system adapts the antenna's orientation in real time, reducing the influence of interference. The prospects are machine-learning algorithms to cut the reaction time to 15–30 s and multi-channel GNSS receivers.

## Limitations

The experimental conditions (the object, its speed, the environment) are not described; it is unclear how the positioning errors were measured and how the ranges of 1.6–4.2 minutes and 12–24 positions were obtained. The drop in HDOP and errors is given without statistics (number of runs, spread). There is no comparison with the manual tuning to which the introduction appeals.

## Novelty

The paper does not claim novelty explicitly. In substance it proposes an autonomous antenna-orientation loop that uses HDOP as both a trigger and the metric for choosing a position.

## Heuristics

- **[explicit]** If an antenna must be oriented automatically — use HDOP as both the threshold and the metric, because a low HDOP corresponds to good satellite geometry and accurate positioning.
- **[explicit]** If the antenna is turned by an angle — hold a pause of 5–10 seconds before re-measuring, because the signal needs time to stabilize.
- **[reconstructed]** If an optimal angle is sought — store the HDOP for each position and pick the minimum after a full cycle, because this selects the angle with the minimum HDOP among all those checked.

**In one sentence:** The Arduino UNO R3 system finds the optimal position of a satellite antenna using the HDOP parameter in 1.6–4.2 minutes on average, lowering the HDOP from 3.2 to 1.8 and the positioning errors by 40 %.
