---
title: "How to Build a Document Automation Service from Three Languages: A Practical Breakdown"
project: diploma_supplement_service
platform: VK
type: Educational / hands-on article
date: 2026-06-01
lang: en
authors:
  - Nikita Konkin
  - Claude (Anthropic) — co-author
summary: "A practical look at a polyglot service architecture for Excel validation, XML generation, and Docker-based deployment."
translation_of: 2026-06-01-vk-uchebno-prakticheskaya.md
links:
  demo: "https://xn----etb9agicel.xn--p1ai/"
  repo: "https://github.com/nikita-konkin/diploma_supplement_service"
tags: [programming, backend, python, java, docker, microservices, fastapi, learning]
---

🎓 **How to Build a Document Automation Service from Three Languages: A Practical Breakdown**

Hi! Today we'll use a real project to look at how modern "polyglot" services are built — where different parts of the system are written in different languages yet work together as a single whole. As an example, we'll take our service that automates diploma supplements. This will be useful for anyone learning backend development, microservices, and Docker. Let's go 👇

---

**📌 The problem**

There's a routine task: take an Excel file with subjects, hours, and grades, check it for errors, and export it into a strict machine-readable XML format. Doing it by hand is slow and error-prone. So let's automate it.

We split the task into two scenarios:
- build a **pivot table** and highlight problematic cells;
- generate an **XML document** from a template.

---

**🧩 Architecture: why three modules instead of one**

The main takeaway of this lesson: you don't have to write everything in a single application. We split the system into three independent services:

🔹 **java-api** — the "front door." It accepts HTTP requests and decides where to route the task. Built on the lightweight **Takes** framework (not heavy Spring — a minimalist approach is plenty for a gateway).

🔹 **python-engine** — the brain for tables. **FastAPI + pandas + openpyxl**: it reads the Excel file, looks for inconsistencies, and fills the "sick" cells with color.

🔹 **python-xml-engine** — an XML generator that works from a template, also on FastAPI.

Why this way? 👉 Each module can be developed and restarted independently. Python is strong at data processing (pandas!), Java at a reliable API layer. We take the best of each language.

---

**🔍 Hands-on snippet: how to highlight an error in Excel**

The most illustrative part is the cell-validation logic. Using `openpyxl`, we walk through the file and fill anything suspicious (empty values, the `!` and `?` symbols) with red:

```python
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

fill = PatternFill(start_color="FFC7CE",
                   end_color="FFC7CE",
                   fill_type="solid")

for row in ws.iter_rows():
    for cell in row:
        if cell.value in (None, "", "!", "?"):
            cell.fill = fill   # flagged a problem
```

Simple, but this is exactly what saves a person hours of manual checking. The employee looks only at the red cells, not the whole file ✅

---

**🐳 Docker: launch with a single command**

Three services = three potential headaches with environment setup. The solution is Docker Compose. All modules are described in `docker-compose.yml`, communicate inside one network, and everything spins up like this:

```sh
docker-compose up --build
```

No "works on my machine," no manual installation of Java and Python. This is an important skill: **packaging a project so it runs for anyone on the first try.**

---

**💡 What to take away from this breakdown**

1. A big task is best split into independent services.
2. Languages can be mixed — pick the right tool for the job.
3. `pandas` + `openpyxl` is a powerful combo for working with Excel.
4. Docker Compose turns a "zoo of technologies" into one runnable project.

---

**🌍 The service is open to everyone**

The project is fully open source under the MIT license — **anyone is welcome to use it**, with no registration or restrictions. You can try the live demo, deploy it yourself, or take the code apart for learning.

🔗 Demo: пгту-ртф.рф (https://xn----etb9agicel.xn--p1ai/)
💻 Source code: https://github.com/nikita-konkin/diploma_supplement_service

Have you tried building projects from several languages? Share in the comments 💬

---

✍️ *Authors: Nikita Konkin in co-authorship with Claude (Anthropic).*

#programming #backend #python #java #docker #microservices #fastapi #learning
