---
title: "Classification of solar flares with ResNet-50: analysis of training components and comparison with baselines"
pair: solnechnye-vspyshki-resnet
lang: en
date: 2026-11-21
translation_of: 2026-11-21-solnechnye-vspyshki-resnet.md
summary: "A dataset of 357 multichannel SDO/AIA images of five classes (quiet Sun and flares B, C, M, X) is built from the NASA VSO archive and used to train a ResNet-50 convolutional network. A TSS of 0.58 is reached at ROC-AUC 0.87; class weights contribute most (TSS falls by 0.16 without them), while a spatial-attention block only hurts on the small dataset."
paper_title: "Classification of solar flares with ResNet-50: analysis of training components and comparison with baselines"
paper_authors: "Korotkova N.A. (supervisor — Konkin N.A.)"
paper_year: 2026
paper_date: "2026"
paper_venue: "Scientific Progress — Creativity of the Young, 2026, no. 1, pp. 722–725"
paper_link: "https://www.elibrary.ru/item.asp?id=93329699"
tags: [solar-flares, ResNet-50, SDO-AIA, machine-learning, image-classification, Grad-CAM]
---

## Problem and relevance

Solar flares of classes M and X disrupt radio communication, cause failures of GPS/GLONASS navigation systems and damage on-board electronics. The Solar Dynamics Observatory (SDO) provides continuous multichannel images of the solar atmosphere, which opens the way to using convolutional neural networks to classify flare activity.

## Aim and hypothesis

The aim is to develop an algorithm for classifying solar flares based on ResNet-50, with an analysis of the training components and interpretation of the predictions by the Grad-CAM method. No hypothesis is stated explicitly. The paper compares baselines directly and removes training components one by one to assess their effect on quality; the author explains the network's advantage over scalar statistics by its extraction of spatial features of active regions.

## Materials and methods

Images of active solar regions were obtained through the NASA VSO archive in three wavelengths — 1600 Å, 304 Å and 171 Å — combined into 224×224-pixel RGB images. The dataset holds 357 samples of five classes: quiet — 163, M — 103, C — 67, B — 14, X — 10. The 70 % / 15 % / 15 % split was made by active region, so that all images of one region fall into only one split. The imbalance is compensated by a weighted CrossEntropy loss and weighted batch sampling. The base is a ResNet-50 pretrained on ImageNet, with a head FC 512→128→5 with LayerNorm and GELU. Training is two-phase: the encoder is frozen (3 epochs), then fine-tuned with WarmupCosine and early stopping (patience = 10). The threshold τ that separates the M/X class from the rest was chosen on the validation split by sweeping from 0.05 to 0.95 and fixed at the maximum TSS. The main metric is TSS = POD − FAR = TP/(TP+FN) − FP/(FP+TN); ROC-AUC, PR-AUC and Brier Score were computed in addition.

## Results

The convolutional network reached TSS = 0.58, ROC-AUC = 0.87 and Recall(M+X) = 0.78 at threshold τ = 0.65. Baselines: the majority-class classifier gives TSS = 0, logistic regression on pixel statistics gives TSS = 0.74 but is unstable across repeated runs, and XGBoost gives TSS = 0.06. The final value over 5 training runs is TSS = 0.58 ± 0.03. On the test split the model finds 7 of the 9 possible M and X flares, with 8 false alarms out of 41 quiet events.

Component analysis: the class weights (quiet — 0.2; B — 0.3; C — 0.4; M — 1.5; X — 4.0) are critical — removing them lowers TSS by 0.160. A spatial-attention block tends to overfit on the small dataset: removing it raises TSS by 0.149 with Recall growing to 1.000. MixUp augmentation lowers TSS by 0.011, label smoothing improves TSS by 0.038. For correct predictions Grad-CAM concentrates on the structures of active regions, while for missed flares (FN) the activation is diffuse; reliability is confirmed by a label-permutation test (TSS ≈ 0).

## The author's conclusions

The author concludes that an algorithm for classifying solar flares based on ResNet-50 has been developed with TSS = 0.58 ± 0.03; the class weights are the key component under imbalance, whereas a spatial-attention block lowers quality on small samples, and Grad-CAM confirms the physical soundness of the model's features.

## Limitations

The dataset is small (357 samples, with only 14 and 10 images in classes B and X), which limits the robustness of the conclusions and makes some baselines unstable. Most false alarms fall on C-class flares near the M threshold, but there is no quantitative breakdown of this boundary. The threshold τ and the metrics were obtained on one active-region split; the TSS spread is assessed only over training runs, not over different splits.

## Novelty

The paper does not claim novelty explicitly. In substance it proposes a ResNet-50-based procedure for classifying solar flares, with an analysis of the contribution of individual training components and Grad-CAM interpretation.

## Heuristics

- **[explicit]** If the classes in a dataset are strongly imbalanced — use a weighted loss and weighted batch sampling, because without an explicit penalty the model ignores the rare M and X classes.
- **[explicit]** If a split is built from images of one active region — put all images of that region into only one split, because otherwise data leakage occurs.
- **[explicit]** If the dataset is small — do not add a spatial-attention block, because it tends to overfit.
- **[reconstructed]** If a threshold uses a metric with an extremum — tune the threshold only on the validation split, because otherwise the test quality estimate will be inflated.
- **[reconstructed]** If interpretability is checked — add a label-permutation test, because it separates meaningful features from chance correlations.

**In one sentence:** ResNet-50 on 357 multichannel SDO/AIA images classifies solar flares with TSS 0.58 ± 0.03 and ROC-AUC 0.87, with class weights as the main contributor, while a spatial-attention block worsens quality on the small dataset.
