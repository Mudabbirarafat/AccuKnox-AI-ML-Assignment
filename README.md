# AccuKnox AI/ML Assignment

This repository contains my solutions for the AccuKnox AI/ML assignment.  
The assignment focuses on API integration, data storage using SQLite, basic data processing, visualization, and conceptual understanding of AI/ML systems.

---

## Problem Statement 1

### 1. API Data Retrieval and Storage
- A public REST API is used to fetch JSON data.
- Since a dedicated books API was not provided, a stable public mock API was used.
- Relevant fields from the API response are mapped to a book-like schema.
- The data is stored in a local SQLite database and displayed using a SELECT query.

**Assumptions:**
- The API does not directly provide book metadata.
- Author names and publication years are synthetically generated for demonstration purposes.

File:
- `api_to_sqlite.py`

---

### 2. Data Processing and Visualization
- Data is fetched from a public API.
- The API does not include test scores.
- A deterministic synthetic score is derived for each record purely for demonstration.
- The average score is calculated.
- A bar chart is generated using matplotlib.

**Assumptions:**
- Test scores are derived from existing attributes in a consistent manner.
- The goal is to demonstrate data processing and visualization, not score accuracy.

File:
- `score_visualization.py`

---

### 3. CSV Data Import to SQLite
- A CSV file containing user information is read using Python’s csv module.
- Records are inserted into a SQLite database using parameterized queries.
- Inserted data is verified using a SELECT query.

File:
- `csv_to_sqlite.py`
- `users.csv`

---

## Problem Statement 2
Responses for conceptual questions related to AI, ML, LLMs, chatbot architecture, and vector databases are provided separately.

File:
- `theory_answers.txt`

---

## Run Instructions

```bash
pip install requests matplotlib
python api_to_sqlite.py
python score_visualization.py
python csv_to_sqlite.py
Notes
SQLite is used for simplicity and local execution.

All assumptions are explicitly documented as allowed by the assignment.

The focus is on correctness, clarity, and explainability.

yaml
Copy code

---

Github - https://github.com/Mudabbirarafat

- Most complex Python project:
https://github.com/Mudabbirarafat/django-file-upload-access-control

- Most complex database project:
https://github.com/Mudabbirarafat/django-file-upload-access-control