---
title: "Step adjustment of the operating frequency for a panoramic SDR ionosonde"
pair: stupenchataya-perestroyka
lang: en
date: 2026-07-21
translation_of: 2026-07-21-stupenchataya-perestroyka.md
summary: "An algorithm and a working GNU Radio flowgraph for stepping the operating frequency of a panoramic SDR ionosonde across 0–30 MHz on the USRP platform: a sample count tags the stream, and detecting the tag triggers the frequency shift."
paper_title: "Step adjustment of the operating frequency for a panoramic SDR ionosonde"
paper_authors: "Konkin N.A. (supervisor — Ryabova N.V.)"
paper_year: 2019
paper_date: "2019"
paper_link: "https://www.elibrary.ru/item.asp?id=41467774"
tags: [SDR, GNU-Radio, USRP, ionosonde, panoramic-sounding, instrumentation]
---

## Problem and relevance

Ionospheric sounding can be carried out with panoramic and channel ionosondes. The work extends panoramic sounding functionality on the USRP (Universal Software Radio Peripheral) platform using GNU Radio software. No justification of significance beyond this engineering task is given in the paper.

## Aim and hypothesis

To describe the algorithm and present a working flowgraph for stepping the operating frequency of a panoramic SDR ionosonde. No hypothesis is stated: the work is an engineering one and makes no testable claim about the medium.

## Materials and methods

The flowgraph is assembled in GNU Radio on the USRP platform. Adjustment covers the range 0 to 30 MHz. A sinusoidal signal generator, Signal source, acts as the source of operating frequencies.

A Tags strobe block counts a specified number of samples from the start of the working stream and determines the moment of adjustment. A tag sink block, written as a Python block, detects the tag with the key "strobe", indicating that the specified number of samples has passed. Once detected, a pmt (polymorphic types) message is delivered to the Frequency sweeper block, also written as a Python block, which cyclically shifts the frequency across 0–30 MHz on the signal from tag sink, with a step set in a QT GUI Range element. The number of samples before the next shift and the step are defined by the user and can be changed dynamically during a sounding session.

## Results

A working GNU Radio flowgraph is given (Fig. 1) along with frequency-stepping plots on the receiving and transmitting sides together with the Samples and Freq step controls (Fig. 2). Quantitative characteristics of the adjustment — settling time, the spread of the switching instant relative to the nominated sample, phase behaviour across the boundary between steps — are not stated in the paper. The effect on the ionogram and on the time to sweep the band is not assessed.

## Authors' conclusions

The engineering side of the panoramic SDR ionosonde has been advanced by introducing stepwise adjustment of the operating frequency across 0 to 30 MHz on the USRP platform with GNU Radio software. The frequency shift is possible dynamically during a sounding session, with the step and the timing defined by the user.

## Limitations

Operation is shown by plots but not measured: the text contains no numerical characteristics of the adjustment. The GNU Radio version and the USRP model are not stated, although the flowgraph shown is tied to a specific release of the environment.

## Novelty

Claimed as an extension of the ionosonde functionality from [1]: stepwise frequency adjustment with user control over the step and the moment of switching, including during a session.

## Heuristics

- **[stated]** If a parameter must change during stream processing — then tie the moment of change to the number of samples passed, because a sample counter is synchronous with the stream itself whereas an external timer is not.
- **[stated]** If the step and the adjustment interval may need to differ during a session — then expose them as interface controls, because that allows the mode to change without restarting the session.
- **[reconstructed]** If an event in one block of the graph must trigger an action in another — then carry it as a tag with a named key and a message, because this decouples detection from execution.
- **[reconstructed]** If the environment's stock blocks are insufficient — then add what is missing as separate scripted blocks, because the rest of the graph then stays unchanged.
- **[reconstructed]** If the fact of adjustment is being verified — then inspect the receiving and transmitting plots together, because agreement distinguishes a real frequency shift from a command in the control program.

**In one sentence:** Stepwise 0–30 MHz frequency adjustment for a panoramic SDR ionosonde on USRP, where a sample count delivered as a tag triggers a shift by a user-defined step.
