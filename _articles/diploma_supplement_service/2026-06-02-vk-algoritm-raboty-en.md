---
title: "From an Excel Sheet to XML: How the Service Builds a Diploma Supplement Step by Step"
project: diploma_supplement_service
platform: VK
type: Educational / hands-on article (algorithm)
date: 2026-06-02
lang: en
authors:
  - Nikita Konkin
  - Claude (Anthropic) — co-author
summary: "A step-by-step explanation of the service pipeline from Excel parsing and validation to final XML generation."
translation_of: 2026-06-02-vk-algoritm-raboty.md
links:
  demo: "https://xn----etb9agicel.xn--p1ai/"
  repo: "https://github.com/nikita-konkin/diploma_supplement_service"
tags: [programming, python, pandas, openpyxl, algorithms, data-processing, learning]
---

🧠 **From an Excel Sheet to XML: How the Service Builds a Diploma Supplement Step by Step**

Last time we looked at the service's architecture from a bird's-eye view — three modules, Docker, different languages. Today we go inside and break down **the algorithm itself**: what exactly happens to the data from the uploaded Excel file to the finished XML. We'll follow the pipeline strictly in order 👇

---

**📥 Step 0. What goes in**

The service needs **two** Excel files:
1. **A grade sheet** — one tab per student (an export from the dean's office).
2. **A list of disciplines** — the reference curriculum (the "mandatory part") that defines the correct order and names of subjects.

The algorithm's job is to overlay the grades from the first file onto the structure of the second and bring everything to a strict format.

---

**🧹 Step 1. Parsing the grade sheet (tab by tab)**

Each tab in the workbook is one student. The algorithm (`process_student_workbook`) walks through the tabs and, for each one:

- takes the **student's name** from the 5th column;
- cleans up the column names and trims the "header" — the actual data starts on the 7th row;
- drops junk rows: `Всего` (Total), `ПГТУ -`, empty subject names;
- **converts hours into credit units**: `credits = hours / 36`;
- normalizes the pass mark: the symbol `V` → `6`.

The output is one shared table `df_stud_scores`: rows are subjects, columns are students.

```python
# hours into credit units
df['часы учр'] = (df['часы учр'].astype(int) / 36).astype(int)
df.rename(columns={"часы учр": "зач ед"}, inplace=True)

# treat the pass mark 'V' as a grade of 6
df['зачет'] = df['зачет'].apply(lambda x: 6 if x == 'V' else x)
```

---

**🏷️ Step 2. Encoding the assessment type right into the row's key**

The key trick of the whole algorithm. Instead of a separate "type" column, the service bakes the assessment type **into the index** of the row by adding a suffix (`parse_rating`):

- pass/exam → `_дисциплина_` (discipline)
- practice → `_практика_` (practice)
- coursework → `_курсовая_` (coursework)

The resulting row key looks like this:

```
Mathematics_discipline_6
   ^subject     ^type   ^credits
```

Why? Throughout the rest of the pipeline, a simple `split('_')` is enough to instantly recover the subject, its type, and its volume — without dragging around extra tables. A simple idea that holds the whole pipeline together.

---

**🔗 Step 3. Matching against the curriculum (the trickiest part)**

The names in the grade sheet and in the curriculum almost never match word for word. So `match_row` is a set of heuristics tried in order:

- **direct match** of the base name;
- **electives** — a name in parentheses `Discipline (module)` → take the part before the parenthesis;
- **dot** — `B1.V.01` → compare by the part before the dot;
- **courseworks** and **electives (facultatives)** — by keywords;
- **prefix groups** like `Discipline * 3` — meaning "the next 3 disciplines belong to this group," and the `count_of_prefix` counter distributes them one by one.

Anything that couldn't be matched is flagged with an empty value. That way the curriculum stays complete and the "holes" are immediately visible to a human.

---

**🚦 Step 4. Highlighting problematic cells**

Before trusting the data, the service highlights anything suspicious (`highlight_problematic_cells`) in two colors:

```python
if cell_value is None or str(cell_value).strip() == '':
    cell.fill = yellow_fill      # 🟡 missing value
elif '!' in str(cell_value) or '?' in str(cell_value):
    cell.fill = red_fill         # 🔴 questionable value
```

🟡 yellow — empty, 🔴 red — contains `!` or `?`. The employee checks only the colored cells, not the entire spreadsheet.

---

**📤 Step 5. Assembling the XML (the "CyberDiploma 3.5.1" format)**

The finale is handled by `DiplomaXMLGenerator`. Here the suffix from Step 2 pays off: we parse the key `subject_type_credits` and place the record into the right XML section:

| Type in the index | XML section |
|-------------------|-------------|
| `дисциплина` (discipline) | `<Дисциплины>` |
| `практика` (practice)     | `<Практики>` |
| `курсовая` (coursework)   | `<Курсовые>` |
| `факультатив` (facultative) | `<Факультативы>` |
| `госэкзамен` (state exam) | `<Госэкзамены>` |

In parallel, the full name is parsed — with careful handling of compound patronymics (`оглы`, `кызы`, `углы`), while the general parameters (qualification, study duration, examination board chair) are taken from the config. The tree is built with `xml.etree.ElementTree` and returned as a ready string.

---

**🧭 The whole pipeline at a glance**

```
2 Excel files
   ↓ parse tabs, clean up, hours→credits
df_stud_scores (subjects × students)
   ↓ encode type into the index  (subject_type_credits)
   ↓ match against the curriculum (match_row heuristics)
df_final
   ↓ highlight problematic cells (🟡/🔴)
   ↓ distribute into sections → ElementTree
XML "CyberDiploma 3.5.1"
```

---

**💡 What's instructive here**

1. **Encoding metadata into the key** (`subject_type_credits`) eliminates extra data structures all along the way.
2. **Fuzzy matching** of the real world is solved not by magic, but by an ordered list of simple heuristics.
3. **Highlight first, then trust** — data validation as a deliberate separate step, not a "fingers crossed."
4. Normalization at the input (hours→credits, `V`→6) makes every subsequent step predictable.

---

**🌍 Try it yourself**

The service is open source under the MIT license — **anyone is welcome to use it**. You can run your own file through it, see the highlighting, and study the algorithm in the code.

🔗 Demo: пгту-ртф.рф (https://xn----etb9agicel.xn--p1ai/)
💻 Source code: https://github.com/nikita-konkin/diploma_supplement_service

Which step should we dig into next time — name matching or XML assembly? Write in the comments 💬

---

✍️ *Authors: Nikita Konkin in co-authorship with Claude (Anthropic).*

#programming #python #pandas #openpyxl #algorithms #data-processing #learning
