---
title: "Comparing STT/TTS technologies for transcribing audio files"
pair: stt-tts-transkribirovanie
lang: en
date: 2026-11-21
translation_of: 2026-11-21-stt-tts-transkribirovanie.md
summary: "The offline libraries Vosk and MultilingualTTS are compared with the cloud service Yandex SpeechKit in accuracy, speed and safety of speech-to-text and text-to-speech conversion. The cloud service gave a WER of 21.62 % and a recognition accuracy of 78.38 % and completed the task in a third of the total time of the offline solution, which however processes data locally."
paper_title: "Comparing STT/TTS technologies for transcribing audio files"
paper_authors: "Korotkova N.A., Ermokhin A.A. (supervisor — Konkin N.A.)"
paper_year: 2025
paper_date: "2025"
paper_venue: "Scientific Progress — Creativity of the Young, 2025, no. 1, pp. 41–43"
paper_link: "https://www.elibrary.ru/item.asp?id=83009749"
tags: [speech-recognition, speech-synthesis, STT, TTS, Vosk, Yandex-SpeechKit]
---

## Problem and relevance

Speech-to-text (STT) and text-to-speech (TTS) technologies are widely used, and there are two approaches: offline libraries for confidential tasks and cloud services with high-quality synthesis. Their strengths and weaknesses in accuracy, speed and safety need to be understood.

## Aim and hypothesis

The aim is to compare the effectiveness of offline and cloud solutions for STT and TTS on the example of the libraries Vosk and MultilingualTTS and the service Yandex SpeechKit. No hypothesis is stated explicitly.

## Materials and methods

Vosk is based on the hybrid Kaldi architecture: the audio is converted to WAV at 16 kHz with mono sound, after which noise reduction is applied; recognition is done by the pretrained model vosk-model-small-ru-0.22 in a streaming way, in chunks of 4000 frames. For speech synthesis, MultilingualTTS on Silero models is used: numbers are turned into words, special symbols are removed, “ё” is replaced with “е”, and long texts are split into chunks of up to 800 characters for the Tacotron-2 and FastSpeech models; the result is saved as WAV or OGG via ffmpeg. The cloud Yandex SpeechKit uses neural algorithms with emotional coloring and noise reduction.

## Results

The cloud service Yandex had a Word Error Rate (WER) of 21.62 %, the offline library 31.58 %; the recognition accuracy was 78.38 % and 68.42 % respectively. The total task time of the cloud service was 3.09 seconds, three times faster than the offline library (9.04 seconds), but the local solution spends an extra 5.71 seconds on model initialization. After startup the offline library generates audio slightly faster: 23.88 characters per second, versus 19.83 for the cloud server. Safety is the advantage of the offline solutions: data are processed locally without being sent to the network, while cloud servers are potentially vulnerable when handling confidential information.

## Authors' conclusions

The cloud service Yandex is more accurate and on the whole faster; the offline solutions win in safety and in generation speed after startup. The choice depends on the requirements for accuracy, speed, safety and functionality.

## Limitations

The measurement setup (the test audio files, their number, duration and noise conditions) is not described. The speed comparison includes model initialization only for the offline solution, which complicates the comparison. The claim that cloud servers are vulnerable is general and is not backed by specific data.

## Novelty

The paper does not claim novelty explicitly. In substance it brings offline and cloud solutions together in a single comparison of accuracy, speed and safety on specific tools.

## Heuristics

- **[explicit]** If the data are confidential — choose an offline library, because it processes data locally and does not send them to the network.
- **[explicit]** If synthesis with emotional coloring and noise reduction is needed — use a cloud service, because it relies on neural algorithms.
- **[reconstructed]** If speed is compared — account for offline model initialization separately, because it adds 5.71 seconds before generation starts.

**In one sentence:** The cloud Yandex SpeechKit recognizes more accurately (WER 21.62 % and accuracy 78.38 %) and completes the task in a third of the total time of the offline solution, while the offline libraries Vosk and MultilingualTTS win in safety and in generation speed after startup.
