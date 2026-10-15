---
title: "ML Playgrounds: A Dark Theme for Streamlit Without a Restart, and a Mistake the Highlighting Found"
project: gd_learn
pair: gd-learn-tema
platform: VK
type: Technical breakdown
date: 2026-10-15
source_from: 3454f68362fdf8bb7a50d824d7b8262b4a267580
source_rev: b8ced41515219b81d5b1751d5618c216d914738f
lang: en
authors:
  - Nikita Konkin
summary: "A theme switch on every page of the site that repaints the Streamlit playgrounds without restarting Python; an explanation of the data on the data-leakage playground, where highlighting the real features exposed a mistake in the documentation; the diabetes features explained; and a speed measurement that reported “×inf faster” because the browser coarsens its clock."
image: /assets/gd_learn/kurs2-theme-preview.png
translation_of: 2026-10-15-tema-i-podsvetka.md
links:
  repo: "https://github.com/nikita-konkin/gd_learn"
  demo: "https://konkin-nikita.ru/gd_learn/topics/"
tags: [programming, python, machine-learning, streamlit, teaching]
---

After the second course's playgrounds — "Foundations of Programming AI Systems in Python" — four changes followed. Two add explanations, one fixes a measurement that gave infinity in the browser, and one concerns the whole site.

## A dark theme without restarting Python

A theme button now sits in the top right corner of the catalogs and the playgrounds. The choice is shared across the site and kept in the browser; until a reader picks one, the system theme applies.

The difficulty was the playgrounds. They run on stlite — Streamlit running in the browser through Pyodide — and Streamlit picks its theme itself, from the system's `prefers-color-scheme` setting. Restarting Python to change the theme is slow: the first load of a page downloads the runtime and takes up to a minute. The answer is to reply to Streamlit's own query: the switch replaces the answer to `prefers-color-scheme` with the reader's choice, and the playground repaints itself.

The templates' colours are now keyed to the `data-theme` attribute rather than to the system theme. Tests check that the switch snippet is on every page and comes before stlite loads. It was checked at 375 pixels too: none of the 13 playgrounds scrolls sideways, and the charts fit the screen.

## Data leakage: what the data are and what got selected

The data-leakage playground shows how selecting features before splitting the sample finds a pattern in pure noise. It used to start straight with numbers. Now a "Data and task" block comes first: what the table is, what is predicted, what the signal is and where exactly the leak happens.

{% include screen.html src="/assets/gd_learn/kurs2-leak-data.webp" wide=true width=1400 height=1000 caption="The “Data and task” block before the first numbers: a table of random noise, random classes, the signal and where the leak happens. The interface is in Russian." alt="The data-leakage page: on the left, sliders for the data, feature selection and validation; on the right, a four-point block — a 300 by 2000 table from a normal distribution, classes 0 and 1, the signal as a shift of the mean in columns #0–#4, and the leak from selecting on the whole table; below, two scores of one model: 0.757 with the leak, 0.510 honestly, a gap of +0.247" %}

The table is 300 rows and 2,000 columns of random numbers, and the classes are assigned at random as well, so the honest answer is known in advance: 0.5. The "strength of the real signal" slider shifts the mean of class 1 in columns #0–#4, and then there is something to predict.

The "What exactly got selected" section now explains its chart. Selection on the whole table picked 20 columns; then it is repeated five times, as in the honest branch — each time on the training part of one fold only. A bar's height is how many folds selected the feature again. The real features are highlighted in colour.

{% include screen.html src="/assets/gd_learn/kurs2-leak-selected-dark.webp" wide=true width=1400 height=1000 caption="“What exactly got selected” in the dark theme: with no signal, one noise feature is still selected in all five folds." alt="Dark theme: a bar chart over the 20 features selected on the whole sample; feature #1181 reaches the dashed line for being selected again in all 5 folds, the rest from 4 down to 0; below the chart, 1 of 20 selected again in all 5 folds, and 0 real features in the data" %}

The highlighting at once found a mistake in the course documentation. It said that at a signal strength of 0.6 five features would reach the top, and that they would be exactly the five columns holding the signal. In fact one of the five is noise, #1181, while the real feature #0 is selected again in only four folds out of five; all five real features reach the top only at 0.8 — and the same #1181 along with them. The documentation has been corrected: a bar's height is a hint, not proof. The same #1181 shows in the screenshot: with zero signal it alone reaches the top — by pure chance.

## Model complexity: what the diabetes features mean

On the model-complexity playground the "Penalty" tab shows how Ridge and Lasso shrink the weights of the ten features of the diabetes dataset. Under the weights chart there is now a "What the features mean" block: what each column measures, the Ridge and Lasso weights at the chosen penalty strength, and how to read the weight of a standardised feature.

{% include screen.html src="/assets/gd_learn/kurs2-fit-features.webp" wide=true width=1400 height=1000 caption="“What the features mean” at alpha = 1.17: Lasso has already zeroed one feature out of ten." alt="A table of ten features — age, sex, body mass index, blood pressure and six blood measurements — with Ridge and Lasso weights at alpha 1.17; the Lasso weight of s2 is zero; below the table, a note about 442 patients and the s1 and s2 pair with a correlation of 0.89; at the bottom, a message that Lasso zeroed 1 feature of 10 and kept 9" %}

What is predicted is how far the disease progressed in the year after the measurements — a number from 25 to 346. The features are standardised before training, so a weight is how much the prediction changes when the feature grows by one standard deviation, and weights of different features can be compared with each other.

Two conclusions in the block are not written as text but computed from the data: which features Lasso keeps longest (here bmi and s5) and which pair nearly repeat each other. That is s1 and s2 — total cholesterol and "bad" cholesterol, with a correlation of 0.89. At the weakest penalty Ridge gives them weights of −43 and +24 — large, of opposite sign and largely cancelling each other out. A penalty shrinks such pairs first.

## A speed measurement and a coarsened clock

On the data-preparation playground the "Vectorisation and memory" tab compares three ways of computing a sum of squares: a Python generator and two ways in NumPy. The measurement runs right in the browser, and for small sizes it showed "0.0 ms" and "×inf faster".

{% include screen.html src="/assets/gd_learn/kurs2-speed.webp" wide=true width=1400 height=1000 caption="The “Vectorisation and memory” tab: times in µs and ms instead of zeros." alt="The data-preparation pipeline page, the vectorisation and memory tab: a sum of squares of 1,000,000 numbers three ways — a Python generator 35 ms, NumPy element-wise 367 µs, NumPy dot product 365 µs — on a logarithmic scale" %}

The cause is the clock. So that timing attacks cannot read memory, browsers coarsen `performance.now()`, and through it the time Python sees: to 0.1 ms in Chrome and to 1 ms in Firefox and Safari. A NumPy sum of ten thousand squares fits within one tick of that clock, and timing a single call gave zero. Now, as in `timeit`, each measurement is a batch of calls lasting at least 20 ms: twenty ticks of the coarsest clock keep the rounding within 5 %. The number of calls is chosen from the series 1, 2, 5, 10, 20, 50…, and the time is shown in µs, ms or s.

## Conclusions

1. The theme of an application that watches `prefers-color-scheme` by itself can be switched by replacing the answer to that query — without a restart and without touching the application's code.
2. An explanation on a chart is also a check: highlighting the real features at once exposed a mistake in text written without it.
3. Conclusions in explanations are better computed from the data than written in: then they cannot drift from the chart at another setting.
4. Timing in a browser has to allow for a coarsened clock: a batch of calls instead of one.

## Availability

The playgrounds open in a browser with nothing to install, and the source code is open.

- Playgrounds: [konkin-nikita.ru/gd_learn/topics](https://konkin-nikita.ru/gd_learn/topics/)
- Source code: [github.com/nikita-konkin/gd_learn](https://github.com/nikita-konkin/gd_learn)
