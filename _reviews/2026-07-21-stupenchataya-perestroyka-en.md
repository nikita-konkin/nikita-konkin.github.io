---
title: "Step adjustment of the operating frequency for a panoramic SDR ionosonde"
pair: stupenchataya-perestroyka
lang: en
date: 2026-07-21
translation_of: 2026-07-21-stupenchataya-perestroyka.md
summary: "The only paper in the set about an instrument rather than a medium: a mechanism for stepping the operating frequency across 0–30 MHz in a panoramic SDR ionosonde on USRP, where a sample counter tags the stream and a tag handler shifts the frequency by a user-defined step."
paper_title: "Step adjustment of the operating frequency for a panoramic SDR ionosonde"
paper_authors: "Konkin N.A. (supervisor — Ryabova N.V.)"
paper_year: 2019
paper_date: "2019"
paper_link: "https://www.elibrary.ru/item.asp?id=41467774"
tags: [SDR, GNU-Radio, USRP, ionosonde, panoramic-sounding, instrumentation]
---

## Summary

Against the rest of the set this paper stands apart twice over: Konkin is the sole author, and the subject is not the ionosphere but the instrument that measures it. The task is to give a panoramic SDR ionosonde on the USRP platform the ability to step its operating frequency across 0–30 MHz, in such a way that both the step and the moment of adjustment are set by the user during the sounding session itself.

The mechanism is described at the level of GNU Radio blocks, and that is the text's principal merit. A sinusoidal signal generator serves as the source of the operating frequency; a Tags strobe block counts a specified number of samples from the start of the stream and tags it; a tag sink block, written as a Python block, detects the tag with the key "strobe" and sends a pmt message to a Frequency sweeper block, which shifts the frequency by the step set through a QT GUI Range element. The sample count before the next shift can be changed dynamically. Figure 2 shows the frequency stepping on the receiving and transmitting sides at once.

It is a complete description of a working subsystem — and at the same time a text without a single measurement in it.

## Strengths

- **The mechanism is described reproducibly.** Specific blocks, the tag key, the message type and the implementation approach for the handlers are all named. From a description at this level the flowgraph can be rebuilt without access to the sources.
- **Dynamism is stated as a requirement, not a side effect.** Both the step and the sample count before switching change during the session. For panoramic sounding, where conditions shift faster than a sweep across the band takes, this is a substantive property.
- **There is evidence it works.** Figure 2 shows the stepping from both ends — receiving and transmitting — rather than only as commanded in software.
- **A clear boundary of contribution.** The work is explicitly positioned as an extension of the ionosonde from [1], and what has been added is stated plainly.

## What to keep in mind

- **Not a single quantitative characteristic.** The natural parameters of a stepping mechanism — settling time, the spread of the switching instant relative to the nominated sample, the behaviour of phase across the boundary between steps — are absent. Without them "the stepping works" describes the presence of a function, not its fitness.
- **Binding to samples rather than to time is not discussed.** For stream processing this is a sensible choice, but the correspondence between samples and time depends on the sample rate, and what happens when that changes does not follow from the text.
- **What it gives the instrument is not shown.** The text stops at the point where the frequency steps. How this affects the ionogram, the time to sweep the band, or the quality of the measurement is not assessed.
- **Figures carry the load with minimal captions.** From Figure 2 neither the step, nor the range, nor the duration of the particular run can be recovered.
- **No version information.** The flowgraph in the screenshot is tied to a specific GNU Radio release and a specific USRP model; without them reproduction grows harder the more time passes.

## Suggestions

- Give the frequency settling time and the spread of the switching instant relative to the nominated sample — two numbers that turn a description into a measurement.
- State whether phase continuity is preserved across the boundary between steps, and whether it matters for the processing that follows.
- Show an end-to-end result: an ionogram obtained in this mode next to one from the previous mode.
- Name the GNU Radio version and the USRP model.

## Heuristic

- A mechanism described down to blocks, keys and message types is reproducible; one described down to intent is not. The difference in length between the two is small.
- Every switch has a switching time. Until it is measured there is nothing to say about the subsystem's fitness, even if it plainly works.
- A paper about one subsystem benefits from a single end-to-end measurement showing what changed at the output of the whole instrument.
- A screenshot of a development environment ages with its version; a release number in the text extends the life of the description.
