---
title: "Sensor diagnostics of ionospheric short-wave radio lines and network approaches to transmitting received information"
pair: sensornaya-diagnostika-kv
lang: en
date: 2026-11-21
translation_of: 2026-11-21-sensornaya-diagnostika-kv.md
summary: "For a network diagnosing HF radio links, a self-organising network on the AODV protocol with five sites and paths up to 4500 km is simulated in OMNeT++, and a field trial with simultaneous channel diagnostics and data transmission is run on an 80 km link. The simulation confirmed that the routing algorithms and link-layer parameters work, and in the trial a telegraph message was received without errors; the paper gives no final delivery probability or bit error rate."
paper_title: "Sensor diagnostics of ionospheric short-wave radio lines and network approaches to transmitting received information"
paper_authors: "Ivanov D.V., Ivanov V.A., Ryabova N.V., Konkin N.A., Chernov A.A."
paper_year: 2025
paper_date: "2025"
paper_venue: "T-Comm: Telecommunications and Transport, 2025, vol. 19, no. 11, pp. 15–22"
paper_link: "https://www.elibrary.ru/item.asp?id=87280968"
tags: [hf-channel, sensor-diagnostics, ionosphere, sensor-network, routing, simulation]
---

## Problem and relevance

An HF radio channel changes in time with the ionosphere and suffers from in-channel interference, especially concentrated interference. The signal travels by hop modes, the pulses interfere at the receiving antenna, and intermode frequency-time dispersion causes fading. Communication therefore has to be adaptive, and adaptation needs sensor diagnostics of dispersion and interference parameters. Conditions depend on the position of the path, which raises the task of network diagnostics and of passing its results on to users. The paper reduces these questions to the need to develop diagnostics of ionospheric HF channels over many long paths and means of highly reliable transfer of the data obtained over long distances.

## Aim and hypothesis

The aim is to improve methods and means of sensor diagnostics of ionospheric HF radio links and to form network approaches to data transfer that raise the reliability and stability of communication under a changing ionosphere. No hypothesis is stated explicitly; in substance the paper tests that the methodology of wireless sensor networks suits the transfer of diagnostic information over HF links, and that combining channel diagnostics with frequency-time diversity raises the reliability of short-message reception.

## Materials and methods

Topology. The authors compare networks of vertical sounding and of vertical-oblique sounding. The area covered by one station is limited to a radius of 2000 km, the maximum length of a ray reflected from the E layer. In the example of an Australian chirp monitoring network, 8 stations in vertical-oblique mode match 22 vertical-sounding stations in effectiveness. For Russia a zonal hierarchical principle is proposed: 3–4 zones by latitude, with data flowing from zonal centres to a central node.

Simulation. In OMNeT++ with the INET framework a self-organising (ad-hoc) network on the AODV protocol was built from five sites: Moscow (central node), Yoshkar-Ola (regional relay), Cyprus (border node), Dikson and Irkutsk; distances reach 4500 km. The central frequency is 14.1 MHz, the band 3 kHz, the loss model LogNormalShadowing (α = 1.81, σ = 4.1 dB), transmitter power 1.7 to 3.9 kW, receiver sensitivity −106 to −134 dBm. AODV is tuned for HF: a HELLO interval of 45 s, a network diameter of 10 nodes, up to six route-request retries. At the link layer CSMA/CA is used with individual intervals per site (SIFS 25–55 ms, DIFS 70–110 ms, acknowledgement timeout 1500–3500 ms). At the application layer, UDP messages of 40–100 bytes are sent at intervals of 50–250 s.

Field trial. The Yoshkar-Ola – Lake Yalchik link, about 80 km long, September 2023, a USRP N210 platform, GNU Radio, wideband dipoles, an amplifier of up to 10 W. A chirp signal (FMCW-FSK) was used with a frequency sweep rate of 50 kHz/s and a bit rate of 50 bit/s in the 2–10 MHz range; a message of 16 symbols of 8 bits occupied 128 kHz and was repeated 62 times in 160 s. Errors in the matrix of received bits were corrected by the majority principle.

## Results

In 5000 s of simulation more than 370 thousand events were processed, with over ten thousand transmissions and about forty thousand receptions. Caching efficiency was 85.4 % for reception decisions and 66.7 % for interference calculations. A route-request RREQ packet was 52 bytes (83 with MAC and PHY headers), route requests took 376 to 690 ms to propagate, and the mean hop count in the route discovery phase did not exceed one. The central node received up to eight packets and the regional relay up to fifteen, while for Dikson and Irkutsk deliverability fell because of path loss and fading.

In the field trial the telegraph message “test message!!!” was sent and received. The authors write that frequency-time diversity with current channel diagnostics gave error-free transmission of small data volumes in conditions of interference loading of short-range HF channels, while diversity without diagnostics was markedly less effective; there are no numbers for this comparison.

## Authors' conclusions

Methods and means of sensor diagnostics of HF radio channels with parallel highly reliable data transfer have been developed. The sensor-network methodology is justified as the base for routing scenarios, exchange protocols and network management. The simulation confirmed the effectiveness of the modified AODV and the adapted CSMA/CA parameters, revealed limits on range and node sensitivity, and showed the benefit of caching and broadcast of RREQ. The trial showed that a network fragment can be implemented on an 80 km link.

## Limitations

The simulation gives event counters and ranges of values but no final delivery probability or per-node delay, and no comparison with default AODV settings, which the authors cite as standard. The trial describes one link and one message repeated 62 times; the total number of sessions, bit errors and the comparison with diversity without diagnostics are not given. The 80 km link in quasi-zenith propagation and the 4500 km network in the model are linked only by a common idea; there is no joint experiment. Descriptions of the devices and algorithms refer to earlier works [3, 5, 10, 11]. The text does not explain how the model parameters were chosen, for example the communication range “from 1700 to 4500 km”.

## Novelty

The authors write that the scientific novelty rests on the development of original algorithms and software for signal synthesis and digital processing.

## Heuristics

- **[explicit]** If control of the ionosphere over a large territory is needed — build a network of vertical-oblique sounding, because 8 such stations match 22 vertical-sounding stations in effectiveness, and the cost of the network depends on the chosen method.
- **[explicit]** If the territory is large — divide the network into zones by latitude (3–4 for Russia) with zonal centres and one central node.
- **[explicit]** If AODV runs on HF paths — lengthen the service-message intervals (HELLO — 45 s) and raise the number of route-request retries (up to six), because standard settings are meant for mobile and local networks.
- **[explicit]** If a short message has to get through a channel loaded with interference — combine frequency-time diversity with current channel diagnostics and correct errors by the majority principle: without diagnostics effectiveness is markedly lower.
- **[reconstructed]** If network parameters must be checked before field deployment — simulate the network with the losses, interference and delays of real paths and compare routing variants and link-layer parameters.

**In one sentence:** A model of a self-organising five-site HF network on AODV tested routing and link-layer parameters, and a field trial on an 80 km link showed error-free reception of a short message with channel diagnostics combined with frequency-time diversity; the paper gives no numerical reliability figures.
