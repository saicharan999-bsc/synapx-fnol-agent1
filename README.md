# Autonomous Insurance Claims Processing Agent

## Overview
This project implements a lightweight agent for processing FNOL (First Notice of Loss) documents.
The agent extracts key claim information, validates mandatory fields, and routes claims to the
appropriate workflow based on predefined business rules.

The solution focuses on clarity, robustness, and explainability rather than heavy AI models.

---

## Features
- Supports FNOL documents in TXT and PDF formats
- Extracts structured fields from unstructured text
- Identifies missing mandatory fields
- Routes claims using deterministic rule-based logic
- Provides a clear explanation for each routing decision
- Outputs results in a clean JSON format

---

## Project Structure
synapx-fnol-agent/
│
├── src/
│ ├── extractor.py # Extracts text and fields from FNOL documents
│ ├── validator.py # Checks for missing mandatory fields
│ ├── router.py # Applies routing rules
│ ├── main.py # Entry point / pipeline orchestration
│
├── input_docs/ # Sample FNOL documents
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md


---

## How to Run

### 1. Install dependencies

pip install -r requirements.txt

2. Run with default sample
python src/main.py

3. Run with a specific FNOL document
python src/main.py input_docs/fnol_fraud.txt
python src/main.py input_docs/fnol_injury.txt

Output Format
{
  "extractedFields": {},
  "missingFields": [],
  "recommendedRoute": "",
  "reasoning": ""
}
