---
title: "ML Playgrounds: A Second Course, a Catalog by Topic and Numbers That Depend on the Library Version"
project: gd_learn
pair: gd-learn-kurs2
platform: VK
type: Technical breakdown
date: 2026-10-12
source_from: 3c47636f2b71d97ff80e15ec09b35350a0fb52ef
source_rev: 3454f68362fdf8bb7a50d824d7b8262b4a267580
lang: en
authors:
  - Nikita Konkin
summary: "The playgrounds of a master's machine learning course have been joined by six playgrounds of a bachelor's course on programming AI systems in Python, and the site has become one catalog by topic. What each playground shows, why the tests check properties rather than the lectures' numbers, and what testing on several Python versions had to say about that."
image: /assets/gd_learn/kurs2-preview.png
translation_of: 2026-10-12-ploshchadki-vtorogo-kursa.md
links:
  repo: "https://github.com/nikita-konkin/gd_learn"
  demo: "https://konkin-nikita.ru/gd_learn/topics/"
tags: [programming, python, machine-learning, streamlit, teaching]
---

In the [previous breakdown]({% link _articles/gd_learn/2026-09-29-playgroundy-kursa-en.md %}) the playgrounds repeated the labs of one course — Machine Learning Fundamentals in a linguistics master's programme. Now they have been joined by six playgrounds of a second, bachelor's course: Foundations of Programming AI Systems in Python. The site has turned from a set of apps into one resource: 13 pages of two courses arranged under six topics.

{% include screen.html src="/assets/gd_learn/kurs2-topics.webp" wide=true width=1400 height=1000 caption="The catalog by topic: the playgrounds of both courses on one page, under shared headings — tasks and models, data, evaluation and others." alt="The «Площадки по машинному обучению» page: a short description of the site and cards of both courses' playgrounds grouped by topic" %}

## Six playgrounds

Each playground follows one of the lab modules and makes visible one mistake that is easy to miss in a notebook.

- **Data preparation pipeline.** The order of the cleaning steps is part of the result. A median computed after removing outliers fills the gaps with −48.65. A mean computed before removing them gives −332.43 — below the physical limit of −120 dBm. Filling in adds a new error to the table instead of fixing the old one.
- **Data leakage.** The features are pure noise; the honest answer is 0.5. Selecting features before splitting the sample gives a score of 0.757, selecting inside each cross-validation fold gives 0.510. Of 2,000 features, 108 pass p < 0.05, while chance gives about a hundred; not one survives the Bonferroni correction.
- **Metric and imbalance.** A model that always answers "no failure" is right 97.9% of the time and finds no failures at all. If missing a failure costs ten times more than a false alarm, the cheapest threshold is 0.834. The threshold changes the model's decision, the cost of an error only the assessment of that decision — two different knobs.
- **Model complexity.** A degree-17 polynomial is off by 0.023 on the training points and by 13.2 on new ones, 23 times worse than answering "the mean".
- **A neural network in NumPy** with a backward pass you can break on purpose. A network with the ReLU derivative forgotten still trains to 0.887 against 0.947 — from outside it looks like unlucky data. A gradient check catches the error, but not on every weight: six weights of the second layer do not depend on the ReLU derivative, and checking one of them would miss it.
- **Task graph and failures.** Retries, skips and an unchecked publication show up in the run log. Without the edge "evaluation → publication", the pipeline ships a model that was never evaluated.

<div class="screens screens-wide">
{% include screen.html src="/assets/gd_learn/kurs2-data.webp" wide=true width=1400 height=1000 caption="Data preparation: the order of the cleaning steps, and list-versus-array memory measured right in the browser." alt="The data preparation playground: the «Как пользоваться» (how to use) block and a table of six network node readings with statuses" %}
{% include screen.html src="/assets/gd_learn/kurs2-leak.webp" wide=true width=1400 height=1000 caption="Data leakage: 0.757 with the leak against 0.510 honestly — on data where there is nothing to predict." alt="The data leakage playground: scores of 0.757 with the leak and 0.510 honestly, a gap of +0.247 and a bar chart by cross-validation fold" %}
{% include screen.html src="/assets/gd_learn/kurs2-metric.webp" wide=true width=1400 height=1000 caption="Metric and imbalance: 97.9% correct answers and zero failures found." alt="The metric and imbalance playground: 97.9% accuracy, 0 failures found, recall 0.000" %}
{% include screen.html src="/assets/gd_learn/kurs2-fit.webp" wide=true width=1400 height=1000 caption="Model complexity: the training error falls, the error on new points soars." alt="The model complexity playground: an error of 0.023 in training, 13.2 on new points and a plot of the degree-17 polynomial" %}
{% include screen.html src="/assets/gd_learn/kurs2-nn.webp" wide=true width=1400 height=1000 caption="A NumPy network: the backward pass can be broken, and the error then caught by a gradient check." alt="The NumPy network playground: loss before and after training, an accuracy of 0.947, a learning curve and a decision boundary" %}
{% include screen.html src="/assets/gd_learn/kurs2-dag.webp" wide=true width=1400 height=1000 caption="The task graph: a training failure, retries, and what of it reaches the log." alt="The task graph and failures playground: 7 of 7 done, 0 skipped, 9 attempts, and a graph of six tasks" %}
</div>

The playgrounds load heavy dependencies only when they cannot do without them. Every extra Python wheel lengthens the first load in the browser, so the model scores for "Metric" and the data for "Neural network" are computed in advance, and these pages do not need scikit-learn.

## Numbers that depend on the version

The first version of the playgrounds repeated the lectures' numbers to the last digit, as the first course's playgrounds do. In repeating them, it rechecked the lectures too. The leakage lecture compared asymmetric pipelines: the leaky branch without scaling, the honest one with it. That did not change the conclusion, but a comparison should differ only in what is being discussed. The regularisation lecture printed only the degenerate case of Lasso, with all ten features zeroed — that is giving up on the model, not selecting features. What was found was fixed in the course materials, not fitted in the playgrounds.

Then the tests ran in CI for the first time, on a clean Linux and fresh packages — until then they had been run on one machine with older versions. Three discrepancies turned up:

- **scikit-learn 1.9** started dropping small singular values in linear regression. For a degree-17 polynomial this acts as regularisation: the training error became 0.043 instead of 0.023, and the "explosion" between the points, which is what the tab exists for, disappeared. Now the playground solves the least-squares problem itself and behaves the same with any version;
- **NumPy 2** computes sine and cosine differently from 1.x in the last bit, and the stored "two moons" data matched its recomputation only to 2·10⁻¹⁶;
- **the memory ratio of a list to an array** is 4.5. The lecture rounded it to a whole number, and the result depended on the Python version: "5 times" on 3.12, where `sys.getsizeof(0)` is 28, and "4 times" on 3.10, where it is 24.

After this, the link between playgrounds and lectures was loosened to a shared topic: exact agreement of numbers turned out to be fragile and demanded editing lectures for the sake of playgrounds. The tests now check what a playground claims, as a property: leakage inflates the score, the honest score is close to 0.5, the training error falls as the model gets more flexible, a broken backward pass is caught by a gradient check. There is also a rule of "one knob — one cause": no control may change two things at once. A slider that drives both data generation and the sample split is exactly the mistake after which no conclusion can be drawn from the experiment.

## "How to use"

The latest change concerns all thirteen pages. Each now opens with a short, expanded block: what the page is for, three steps worth trying, and the main thing to notice. The steps name the real controls, and every number in them was read off the page in the browser, not taken from the lecture. A test keeps each block to two to four steps and ninety words. The long explanation for those who have not heard the lecture stays below, collapsed.

Rereading the pages found errors too. Two claims in the long explanations turned out to be wrong and were corrected. Two hints with LaTeX were written as ordinary Python strings, so `\alpha` and `\varepsilon` reached the page as control characters — a bell and a vertical tab. And the gradient-descent playground at step size 1 reported "Converged in 1 iteration" with the error frozen at its initial 43.95: batch descent jumped over the minimum and landed at the same height every time, so the loss stopped changing. Now convergence also requires the weights to have stopped moving, and a run that ends where it started says whether its step overshoots or crawls.

## Conclusions

1. A playground that repeats a lecture's numbers checks the lecture along the way. What it finds is worth fixing at the source, not fitting in the copy.
2. Exact agreement of numbers depends on library and platform versions. Testing on several versions in CI showed this before the students did.
3. A teaching claim is more reliably checked as a property: "leakage inflates the score" survives a scikit-learn update, "0.023" does not.
4. If an experiment's conclusion rests on a library's behaviour, that behaviour is better pinned down by one's own code: a polynomial solved by its own least squares overfits with any version.
5. A short instruction on every page is code worth checking too: its numbers were read in the browser, and its length is limited by a test.

## Availability

The playgrounds of both courses are open and run in the browser with nothing to install: Python runs on the student's side through stlite. The source code is open under the MIT licence.

- Catalog by topic: [konkin-nikita.ru/gd_learn/topics](https://konkin-nikita.ru/gd_learn/topics/)
- Playgrounds of the second course: [konkin-nikita.ru/gd_learn/ml-practice](https://konkin-nikita.ru/gd_learn/ml-practice/)
- Source code: [github.com/nikita-konkin/gd_learn](https://github.com/nikita-konkin/gd_learn)
