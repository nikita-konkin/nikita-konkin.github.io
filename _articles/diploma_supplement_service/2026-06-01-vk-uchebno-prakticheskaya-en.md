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

🎓 **How ​​to Build a Document Automation Service from Three Languages: A Practical Analysis**

Hello! Today, we'll use a real-world project to explore how modern "polyglot" services work—when different parts of a system are written in different languages ​​but still function as a unified whole. As an example, we'll use our diploma application automation service. This will be useful for those learning backend, microservices, and Docker. Let's get started 👇

---

**📌 Task**

We have a routine task: take an Excel file with courses, hours, and grades, check it for errors, and export it to a strict XML format. Doing it manually is time-consuming and easy to make mistakes. So, let's automate it.

We've broken the task down into two scenarios:
- Build a **pivot table** and highlight problematic cells;
- Generate an **XML document** using a template.

---

**🧩 Architecture: Why Three Modules Instead of One**

The main idea of ​​this lesson: you don't have to write everything in one application. We've divided the system into three independent services:

🔹 **java-api** — the "front door." It accepts HTTP requests and decides where to send the task. It's written in the lightweight **Takes** framework (not the heavy Spring framework—minimalism is enough for a gateway).

🔹 **python-engine** — the brains behind the spreadsheets. **FastAPI + pandas + openpyxl**: reads Excel, finds inconsistencies, and colorizes problematic cells.

🔹 **python-xml-engine** — an XML generator based on a template, also in FastAPI.

Why is this? 👉 Each module can be modified and restarted separately. Python is strong in data processing (pandas!), Java in its robust API layer. We take the best from each language.

---

**🔍 Practical snippet: how to highlight an error in Excel**

The most visual example is the cell validation logic. We use `openpyxl` to loop through the file and highlight anything suspicious (empty values, `!` and `?` characters) in red:

```python
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

fill = PatternFill(start_color="FFC7CE",
end_color="FFC7CE",
fill_type="solid")

for row in ws.iter_rows():
for cell in row:
if cell.value in (None, "", "!", "?"):
cell.fill = fill # highlighted the problem
```

Simple, but this saves hours of manual verification. The employee doesn't look at the entire file, but only at the red cells ✅

---

**🐳 Docker: Launch with a Single Command**

Three services = three potential headaches with environment setup. The solution is Docker Compose. All modules are described in `docker-compose.yml`, communicate within the same network, and everything is launched like this:

```sh
docker-compose up --build
```

Neither "it works on my computer" nor manually installing Java and Python. This is an important skill: **packaging a project so that it runs on the first try for anyone.**

---

**💡 What to take away from this analysis**

1. It's useful to break down a large task into independent services.
2. You can mix languages ​​– choose the right tool for the task.
3. `pandas` + `openpyxl` – a powerful combination for working with Excel.
4. Docker Compose turns a "zoo of technologies" into a single, runnable project.

---

**🌍 The service is open to everyone**

The project is completely open source, licensed under the MIT license—**anyone can use it**, without registration or restrictions. You can try out the live demo, deploy it yourself, or disassemble the code for learning purposes.

🔗 Demo: pgtu-rtf.rf (https://xn----etb9agicel.xn--p1ai/)
💻 Source code: https://github.com/nikita-konkin/diploma_supplement_service

Have you ever tried building projects from multiple languages? Share in the comments 💬

---

✍️ *Article author: Nikita Konkin, co-authored with Claude (Anthropic).*

#programming #backend #python #java #docker #microservices #fastapi #training
