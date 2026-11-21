---
title: "Estimating the channel capacity gain of a transionospheric radio channel under stochastic error in the experimental estimate of the total electron content of the ionosphere"
pair: vyigrysh-propusknoy-sposobnosti
lang: en
date: 2026-11-21
translation_of: 2026-11-21-vyigrysh-propusknoy-sposobnosti.md
summary: "Stochastic errors of total electron content (TEC) were estimated from 20 reference stations near Yoshkar-Ola, and with them an analytical model gives the capacity gain of a transionospheric channel under adaptive compensation of frequency dispersion. The gain reaches 2.5–7 times and depends on the season and the time of day."
paper_title: "Estimating the channel capacity gain of a transionospheric radio channel under stochastic error in the experimental estimate of the total electron content of the ionosphere"
paper_authors: "Kislitsyn A.A., Ryabova N.V., Konkin N.A."
paper_year: 2020
paper_date: "2020"
paper_venue: "Systems of Synchronization, Generation and Processing of Signals, 2020, vol. 11, no. 4, pp. 12–18"
paper_link: "https://www.elibrary.ru/item.asp?id=44277705"
tags: [ionosphere, transionospheric-channel, TEC, frequency-dispersion, channel-capacity, GNSS]
---

## Problem and relevance

Wideband signals in transionospheric channels are distorted by frequency dispersion. It is compensated with devices matched to the radio channel, and because the medium changes, adaptive compensation is needed. The dispersion parameters are analytically related to total electron content (TEC), but an experimental estimate of the phase contains a random error. It can be reduced by simultaneous measurements from several GNSS receiving stations. Errors in the TEC estimate limit the widening of the channel's coherence band, and the coherence band limits capacity.

## Aim and hypothesis

The aim is to establish experimentally the maximum capacity gain of a transionospheric radio channel when the stochastic error of the TEC estimate is minimised and dispersion is compensated adaptively over a wide band. No hypothesis is stated explicitly; in substance the paper tests that capacity grows even when dispersion is compensated only partly.

## Materials and methods

A hardware-software complex was created: the SmartNet network of reference stations receives GLONASS and GPS signals, and an automated module builds absolute TEC and estimates the stochastic error for each station and for the system as a whole. A majority approach is used: the decision rests on several stations within a correlation radius R, inside which the ionosphere is taken as homogeneous; from the literature the radius is 200–300 km. For N stations the absolute TEC, its mean and its standard deviation are computed.

Capacity is estimated with Shannon's formula C = B·log₂(1 + SNR), which at a low signal-to-noise ratio is about 1.44·B·SNR and at a high one B·log₂ SNR. The analytical model starts from the fact that correcting dispersion with an error below 100 % widens the coherence band; the residual dispersion set by the TEC error limits the band, and the gain depends on the relative TEC error (Eqs 6–9); the gain in the coherence band depends on the relative TEC error with an exponent of −0.5. The estimate is made at a constant SNR.

The experiment used data from 20 reference stations near Yoshkar-Ola. Variations of the mean TEC values: winter 0.3…0.5 TECU, spring 0.15…0.5, summer 0.2…0.55, autumn 0.3…0.6 TECU. The errors are given for night, transition and day time in each season; the observation period is not stated.

## Results

The capacity gain, computed with Eqs (8) and (9) from the relative TEC errors, was 2.5…7 times overall:

- winter: night 2.5–3, transition 3–4, day 4;
- spring: night 3, transition 3.5–7, day 4.5–6;
- summer: night 4–4.5, transition 4–6, day 5–7;
- autumn: night 3.5–4.5, transition 4–4.5, day 4.

The model implies that at a constant SNR capacity grows with the channel band up to values well above its coherence band.

## Authors' conclusions

TEC measurement errors limit the widening of the channel band and its capacity. An approach is proposed for raising the capacity by adaptive dispersion compensation under the stochastic error of the TEC estimate. The gain depends on the season and reaches 2.5–7 times; even compensation with a TEC error below 100 % will improve satellite-communication performance.

## Limitations

The gain is computed by formula from measured TEC errors, not measured on a real channel, although the abstract says “shown experimentally”. The calculation assumes a constant SNR as the band widens; how to ensure this in practice is not discussed. The observation period, the number of days per season and the actual relative TEC errors are not given in the text (they are in Fig. 3). The majority approach is described briefly: the decision rule is not stated; 20 stations are named for the experiment, but it is not said how many were used in each calculation. One area (the vicinity of Yoshkar-Ola). The link between TEC error, residual dispersion and coherence band is taken from the authors' earlier works rather than shown anew.

## Novelty

Not claimed explicitly. The abstract notes the created complex for estimating TEC errors from many receivers and the analytical model of the gain; in substance the paper gives a numerical estimate of the gain by season and time of day.

## Heuristics

- **[explicit]** If the random error of a TEC estimate must be reduced — use simultaneous measurements from several stations within the correlation radius (200–300 km), because the ionosphere is taken as homogeneous inside it.
- **[explicit]** If the signal-to-noise ratio is fixed — raise capacity by widening the band rather than the power, because capacity depends linearly on the band and logarithmically on SNR.
- **[explicit]** If the error in determining TEC is below 100 % — compensating dispersion is still worthwhile, because the coherence band of the channel widens.
- **[reconstructed]** If the potential gain of compensation is being estimated — compute it from the relative TEC error separately by time of day and season, because the gain varies from 2.5 to 7 times.

**In one sentence:** A calculation from the measured TEC errors of 20 stations shows that adaptive dispersion compensation gives a transionospheric channel a capacity gain of 2.5–7 times, depending on the season and time of day.
