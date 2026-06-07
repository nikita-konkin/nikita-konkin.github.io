---
title: "From an Excel Sheet to XML: How the Service Builds a Diploma Supplement Step by Step"
project: diploma_supplement_service
pair: diploma-algoritm-raboty
platform: VK
type: Technical breakdown (algorithm)
date: 2026-06-02
lang: en
authors:
  - Nikita Konkin
summary: "A step-by-step explanation of the service pipeline from Excel parsing and validation to final XML generation."
translation_of: 2026-06-02-vk-algoritm-raboty.md
links:
  demo: "https://xn----etb9agicel.xn--p1ai/"
  repo: "https://github.com/nikita-konkin/diploma_supplement_service"
tags: [programming, python, pandas, openpyxl, algorithms, data-processing]
---

The previous breakdown looked at the service architecture as a whole — three modules, separation by language, deployment via Docker. This one examines the processing algorithm itself: what happens to the data on its way from an uploaded Excel file to the final XML. The account follows the order of the pipeline.

## Step 0. The input

The service requires two Excel files:

1. **A grade sheet** — one worksheet per student (an export from the dean's office).
2. **A subject list** — the reference curriculum (the "mandatory part") that defines the correct order and naming of subjects.

The algorithm's task is to map the grades from the first file onto the structure of the second and bring the result into a strict format.

## Step 1. Parsing the grade sheet by worksheet

Each worksheet corresponds to one student. The `process_student_workbook` function iterates over the worksheets and, for each one:

- takes the student's name from the fifth column;
- cleans up the column names and cuts off the header — the real data starts at the seventh row;
- discards service rows: `Всего` (Total), `ПГТУ -`, and empty subject names;
- converts hours to credit units using `credits = hours / 36`;
- normalizes the pass mark: the symbol `V` is interpreted as a grade of `6`.

The output is a single `df_stud_scores` table where rows are subjects and columns are students.

```python
# hours to credit units
df['часы учр'] = (df['часы учр'].astype(int) / 36).astype(int)
df.rename(columns={"часы учр": "зач ед"}, inplace=True)

# a 'V' pass mark is treated as a grade of 6
df['зачет'] = df['зачет'].apply(lambda x: 6 if x == 'V' else x)
```

## Step 2. Encoding the assessment type into the row name

This is the algorithm's key technique. Instead of a separate "type" column, the service writes the assessment type directly into the row index by appending a suffix (the `parse_rating` function):

- a pass or exam → `_дисциплина_` (subject)
- practical training → `_практика_` (practice)
- a coursework → `_курсовая_` (coursework)

The resulting row key looks like this:

```
Mathematics_subject_6
   ^subject    ^type  ^credits
```

From there, a single `split('_')` is enough to determine the subject, its type, and its volume anywhere in the pipeline, without consulting additional tables. It is a simple decision that holds the whole pipeline together.

## Step 3. Matching against the curriculum

The names in the grade sheet and in the curriculum almost never match verbatim, so `match_row` is a set of heuristics applied in order:

- a direct match of the base name;
- electives of the form `Subject (module)` — the part before the parenthesis is used;
- dotted codes such as `Б1.В.01` — compared by the part before the dot;
- courseworks and electives — matched by keywords;
- prefix groups of the form `Subject * 3` — meaning that three subjects of this group follow; the `count_of_prefix` counter distributes them in turn.

Anything that cannot be matched is marked with an empty value. This keeps the curriculum complete and makes the gaps immediately visible to the reviewer.

## Step 4. Highlighting problematic cells

Before the data is trusted, the service marks suspicious values (`highlight_problematic_cells`) in two colors:

```python
if cell_value is None or str(cell_value).strip() == '':
    cell.fill = yellow_fill      # missing value
elif '!' in str(cell_value) or '?' in str(cell_value):
    cell.fill = red_fill         # disputed value
```

Yellow marks an empty cell, red a value containing `!` or `?`. The reviewer works only with the highlighted cells rather than the entire table.

## Step 5. Building the XML in the "CyberDiploma 3.5.1" format

The final stage is handled by `DiplomaXMLGenerator`. Here the suffix from step 2 comes into play: the `subject_type_credits` key is parsed, and the record is placed into the correct XML section.

| Type in the index | XML section |
|-------------------|-------------|
| `дисциплина` (subject)     | `<Дисциплины>` |
| `практика` (practice)      | `<Практики>` |
| `курсовая` (coursework)    | `<Курсовые>` |
| `факультатив` (elective)   | `<Факультативы>` |
| `госэкзамен` (state exam)  | `<Госэкзамены>` |

In parallel, the full name is parsed with careful handling of compound patronymics (`оглы`, `кызы`, `углы`), while general parameters — qualification, duration of study, the chair of the examination board — are taken from configuration. The document tree is assembled with `xml.etree.ElementTree` and returned as a finished string.

## The pipeline at a glance

```
2 Excel files
   ↓ parse worksheets, clean, hours → credits
df_stud_scores (subjects × students)
   ↓ encode the type into the index (subject_type_credits)
   ↓ match against the curriculum (match_row heuristics)
df_final
   ↓ highlight problematic cells
   ↓ distribute into sections → ElementTree
"CyberDiploma 3.5.1" XML
```

## Takeaways

1. Encoding metadata into the row key (`subject_type_credits`) removes the need for extra data structures along the whole processing path.
2. Fuzzy name matching is solved not by "magic" but by an ordered list of simple heuristics.
3. Highlighting before trusting the data is a deliberate, separate validation step.
4. Normalization at the input (hours → credits, `V` → 6) makes the subsequent steps predictable.

## Availability

The project is open source under the MIT license. You can run your own file, see the highlighting, and study the algorithm in the source code.

- Demo: [пгту-ртф.рф](https://xn----etb9agicel.xn--p1ai/)
- Source code: [github.com/nikita-konkin/diploma_supplement_service](https://github.com/nikita-konkin/diploma_supplement_service)
