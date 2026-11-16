---
title: "IonoReview: Labelling Ionograms by the Measurement, Not the Picture"
project: ionoreview
pair: ionoreview-intro
platform: VK
type: Technical breakdown
date: 2026-11-16
source_rev: f063dc58b8f7beb49c569089c0fac234267edc77
lang: en
authors:
  - Nikita Konkin
summary: "A desktop editor for labelling ionograms and reviewing the labels. Each frame comes with a power matrix in dB and axes in MHz and km, so mask boundaries, contrast and automatic labelling all work in physical units. DBSCAN or K-means pre-labelling proposes candidates, but an expert sets and accepts the mode; only accepted records are exported. The Windows build needs no Python, and a project is created from a folder of H5 files with one menu command."
image: /assets/ionoreview/preview.png
translation_of: 2026-11-16-ionorazmetka.md
links:
  repo: "https://github.com/nikita-konkin/ionoreview"
tags: [ionosphere, ionograms, data-labelling, machine-learning, python, tkinter]
---

To train a model to find layers and modes on an ionogram you need labelled ionograms, and labelling turns out to be the slowest part of the work. The usual tools, LabelMe, CVAT and Label Studio, work with a picture: to them a polygon is an outline over the pixels of a PNG. For an ionogram that is not enough. An operator who sets a 1F or 2F label needs to see the trace's real frequency and range, not pixel numbers, and to bring up a faint trace from the measured power rather than from an image that has already been coloured.

IonoReview (ИоноРазметка in Russian) labels the measurement itself. In the first week of November the editor went from its first version to v0.3.0, gaining expert acceptance, blind reviews, a user manual with screenshots of every window, and project creation straight from H5 files.

## The measurement beside the picture

Besides the PNG, each frame of a set carries an NPZ file: a power matrix in dB and physical axes, frequency in MHz and virtual range in km. A pixel of the working PNG matches an element of the matrix, and the PNG carries no labels or plot margins. Everything else follows from this.

- The axes, the cursor readout, the range window and the outline of every mask are in MHz and km.
- The dB scale sliders and colour schemes redraw the ionogram from the measured power, so a faint trace can be brought up without losing detail.
- Automatic labelling looks for clusters among points above a threshold in dB, with links set in MHz and km. The settings carry over between frames of different sizes.
- A mask's position in MHz and km, its power and its area in MHz·km are computed straight from the NPZ, ready as features for a mode classifier.
- The manifest keeps checksums of the source measurement, the PNG and the NPZ, and the history keeps every saved version of the labels. It can be shown that a set of labels belongs to this very measurement.

{% include screen.html src="/assets/ionoreview/editor-en.webp" wide=true width=1520 height=1000 caption="The main window on the demonstration set: an accepted ionogram of the NIC1 — Yoshkar-Ola path with 1E, 1F and Interference masks. The axes are in MHz and km of virtual range." alt="The IonoReview window: on the left a list of five ionograms marked Accepted, an expert field, details of frame T031 on the NIC1 → Yoshkar-Ola path from 23 August 2026, 496 × 418 pixels, a list of objects and the buttons Accept and next, Needs changes, next and Ambiguous, next; along the top the modes Select / vertices, Polygon, Zoom area and Multi-select, range fields of 2480–3314 km and an Auto-label button; in the centre an ionogram from 7 to 31.8 MHz with blue 1F outlines round two converging rays, orange 1E outlines low down and dashed Interference outlines on the left; at the bottom the dB scale, opacity, the Modes colour scheme and the paths to the PNG and JSON" %}

The labels are `Signal`, `1E`, `1F`, `2F`, `3F`, `E`, `Es` and `Interference`. `Signal` means a useful signal whose mode is not established. Separate pieces of one mode share a group number but remain separate outlines. A polygon must cover the visible band of the echo: it must not fill the gap between branches or extend a trace where it cannot be seen. An empty result is accepted only with an explicit "No useful signal" mark. The labelling rules, with examples, are built into the program.

## Clusters are not modes yet

Pre-labelling works in two ways. DBSCAN groups dense patches of points above the threshold and separates the noise, finding the number of groups by itself. With K-means the user sets the number of groups, and isolated points are dropped first. For numeric ionograms the threshold is set in dB and the links in MHz and km, and the search can be limited to the visible area.

{% include screen.html src="/assets/ionoreview/cluster-dialog.webp" width=620 height=550 max=460 caption="The cluster search settings, in the Russian interface: a 43 dB threshold and links of 0.15 MHz in frequency and 25 km in range." alt="The signal cluster search window in Russian: the method Auto (DBSCAN), a threshold of 43 dB, a frequency link of 0.15 MHz, a range link of 25 km, 4 DBSCAN neighbours for a dense point, at least 12 points per cluster, a minimum band of 0.25 MHz, and Visible area only ticked; a note says that candidates are shown in orange, existing masks are kept, the user assigns the 1F, 2F and E labels, and the calculation does not depend on the colour scale sliders" %}

Candidates first appear in a preview. They can be selected, added, rejected, corrected and given a common class, but the preview itself changes no labels and never reaches the export. The program warns plainly that the number of clusters is not the number of modes: touching traces may merge into one cluster, faint ones may be lost, and interference may form groups of its own. Clustering finds similar patches of signal; the physical mode is established by the expert.

{% include screen.html src="/assets/ionoreview/candidates.webp" wide=true width=1520 height=1000 caption="DBSCAN candidates over an ionogram, in the Russian interface: 10 clusters, 18 polygons, 1,816 points and 16 noise points. This is not labelling yet: the expert assigns the classes." alt="The IonoReview window in Russian with frame T023: over an ionogram from 7 to 31.8 MHz and 2478 to 3170 km, candidate outlines in several colours — pink round the main 1F trace, teal and yellow round the 1E segments low down, purple and green on the high ray, orange on faint patches; beside the buttons a note reads 10 clusters, 18 polygons, and at the bottom DBSCAN: 1816 points, noise 16, candidates are not labels yet" %}

## Acceptance instead of saving

Every record goes through expert review and gets a status: pending, accepted, needs changes, or ambiguous. Editing an accepted record returns it to pending. Records are saved atomically, earlier versions stay in the history, and a revision check stops a second window from silently overwriting someone else's changes.

The export takes accepted records only: the PNG, a LabelMe-format JSON with review and provenance fields, the NPZ, and the manifest. A proposal from a model or an algorithm is imported as preliminary labelling and needs review too: a proposal by itself means nothing.

For a blind review a set can switch the hints off with the `assistance_disabled` flag in its manifest. Such a set has no automatic labelling and no import of other labels, while manual editing and acceptance remain. The expert then labels independently, and the result can be compared fairly with a model.

## From an archive to a set

A new project is created from the File → Create project from H5 menu: the program scans a folder of H5 files and LFS recordings, subfolders included, writes PNGs and NPZ files with physical axes into a separate project folder, and opens it. The sources are not changed, existing projects are not overwritten, and unsuitable files, such as an H5 holding detections but no ionogram, are skipped with an explanation in the manifest. Preparation can be stopped after the current file.

For a large archive there are separate commands that resume after a stop: an inventory of the archive, reading and hashing the files from cloud storage, building the sets, and checking the result. Unreadable files go into a report instead of stopping the work. A library of several sets opens through a shared catalogue; the library in the manual's screenshot holds 63 sets and 17,958 images.

## The Windows build

The editor is written in Python with Tkinter. For every version tag, GitHub Actions builds a portable archive for Windows 10/11: unpack it and run `IonoReview.exe`, no Python needed. Before release the built exe runs a self-test, and in v0.3.0 the self-test also checks the H5 loader, which now ships in the build. User ionograms, labels and model weights are not part of the archive.

## An experimental track: a vision model

Apart from the editor, in the Python project, sits an experimental track for fine-tuning the Qwen3.5-2B vision-language model with QLoRA. The vision encoder is frozen, and the LoRA projections of the text decoder are trained. Only accepted records go into training; before training the set is frozen as a snapshot with a fingerprint, and the `train`, `validation` and `test` parts are split by observation rather than by fragments of one ionogram.

Quality is measured by semantic IoU and Dice on the full original images. The documentation notes that these are not instance AP, and that by themselves they do not confirm the physical interpretation of the modes. The model's proposals return to the editor as preliminary labels through the LabelMe import, with no automatic acceptance. For blind sets the model is loaded once and does not read the set's manual labels.

## Conclusions

1. Labelling an ionogram in physical units, MHz, km and dB, makes mask boundaries, contrast and automatic labelling carry over between frames of different sizes.
2. A cluster is a hypothesis about the signal, not a mode: the expert sets the classes, and only what is accepted is exported.
3. A blind mode without hints is needed to compare a model with independent expert labels rather than with its own corrected proposals.
4. Checksums and a version history tie every mask to a specific measurement.

## Availability

- Source code and the user manual: [github.com/nikita-konkin/ionoreview](https://github.com/nikita-konkin/ionoreview)
- The Windows build: [latest release](https://github.com/nikita-konkin/ionoreview/releases/latest)
