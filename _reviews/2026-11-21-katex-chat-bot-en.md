---
title: "Integrating the KaTeX library into a chatbot for rendering mathematical expressions"
pair: katex-chat-bot
lang: en
date: 2026-11-21
translation_of: 2026-11-21-katex-chat-bot.md
summary: "A software module is built that appends an instruction to use KaTeX syntax to the language-model request and converts the formulas to HTML markup on the client side with KaTeX. As a result the chatbot shows mathematical expressions in a form close to traditional mathematical notation instead of a plain string."
paper_title: "Integrating the KaTeX library into a chatbot for rendering mathematical expressions"
paper_authors: "Ermokhin A.A. (supervisor — Konkin N.A.)"
paper_year: 2025
paper_date: "2025"
paper_venue: "Scientific Progress — Creativity of the Young, 2025, no. 1, pp. 30–32"
paper_link: "https://www.elibrary.ru/item.asp?id=83009745"
tags: [chatbot, KaTeX, math-formulas, JavaScript, TypeScript, rendering]
---

## Problem and relevance

The base language models on which chatbots are built do not provide functionality for formatting mathematical expressions, which makes formulas hard to read for educational and scientific use. The KaTeX library solves this by rendering formulas in a familiar form.

## Aim and hypothesis

The aim is to build a software block for analyzing mathematical expressions with KaTeX, for integration into chatbots. The tasks are to integrate KaTeX into a chatbot system and to compare the plain-text format with the KaTeX format when formatting a message. No hypothesis is stated explicitly.

## Materials and methods

KaTeX is a JavaScript library for rendering mathematical expressions; it uses LaTeX syntax and is optimized for the web. The chatbot works as follows: a message is sent to the server, processed and passed to the language model. At the processing stage an instruction "If you mention formulas – use KaTeX syntax" is appended, so the model generates formulas in the "$$ formula $$" format. Before the message is shown on screen, the TypeScript client imports KaTeX: a handler finds the expression in the text and converts it to HTML, wrapping it in span tags of the katex-mathml class.

## Results

With KaTeX applied, the chatbot renders formulas not as a string but in a form close to traditional mathematical notation, which the author calls the LaTeX format. The comparison with the plain-text format showed that the KaTeX format is visually clearer. The paper gives no numerical metrics.

## The author's conclusions

Integrating KaTeX extended the chatbot's functionality and gave a clearer rendering of formulas. The next step is the ability to copy formulas in their original KaTeX form.

## Limitations

The comparison with the plain-text format is qualitative: there are no metrics, such as rendering time or the share of correctly rendered formulas. The language model and the chatbot platform are not described, nor is the handling of inline formulas. The assessment rests on two "before" and "after" images (Figs 1 and 2).

## Novelty

The paper does not claim novelty explicitly. In substance it proposes a way to integrate KaTeX by appending an instruction to the request and converting the formulas to HTML on the client side.

## Heuristics

- **[explicit]** If a language model must produce formulas — append an explicit instruction to use KaTeX syntax to the request, because base models provide no formatting functionality, and the instruction sets the "$$ formula $$" format.
- **[explicit]** If a formula must be shown in a web interface — convert it to HTML on the client and wrap it in a span of the katex-mathml class, because this allows styles to be applied later.
- **[reconstructed]** If a formula format is being assessed — compare the "before" and "after" output on the same message, because the difference shows on an example.

**In one sentence:** Appending an instruction to use KaTeX to the language-model request and converting the formulas to HTML on the client gives a chatbot a clear rendering of mathematical expressions instead of a plain string.
