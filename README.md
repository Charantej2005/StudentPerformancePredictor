# Student Performance Analysis Tool

![Python](https://img.shields.io/badge/Python-3.x-blue)
![NumPy](https://img.shields.io/badge/NumPy-Library-green)
![Pandas](https://img.shields.io/badge/Pandas-Library-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

A modular Python application built using **NumPy** and **Pandas** to analyze student academic performance from CSV datasets. The project follows modular software engineering principles by separating data loading, cleaning, analysis, grading, ranking, and report generation into reusable modules.

---

# Overview

This project demonstrates a complete student performance analysis workflow using Python.

It processes a predefined CSV dataset and performs:

- Data Loading
- Data Cleaning
- Dataset Analysis
- Grade Calculation
- Student Ranking
- CSV Report Generation

---

# Project Goals

- Practice modular Python programming.
- Apply NumPy and Pandas for real-world data analysis.
- Follow software engineering best practices.
- Build a scalable foundation for future versions.

---

# Features

- Load student dataset from CSV
- Remove duplicate records
- Detect missing values
- Fill missing values
- Validate student marks
- Perform dataset analysis
- Generate statistical summaries
- Calculate total marks
- Calculate average marks
- Assign grades automatically
- Generate Pass/Fail status
- Rank students
- Generate CSV reports
- Modular Python architecture

---

# Project Structure

```text
StudentPerformancePredictor/
│
├── data/
│   ├── raw/
│   │   └── students.csv
│   └── processed/
│
├── docs/
│   ├── grading/
│   ├── ranking/
│   └── project_overview.md
│
├── output/
│   ├── logs/
│   └── reports/
│
├── src/
│   ├── __init__.py
│   ├── analysis.py
│   ├── clean_data.py
│   ├── grading.py
│   ├── load_data.py
│   ├── main.py
│   ├── ranking.py
│   ├── report.py
│   └── utils.py
│
├── tests/
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# Technologies Used

- Python 3
- NumPy
- Pandas
- Git
- GitHub

---

# Prerequisites

Before running the project, install:

- Python 3.10 or later
- pip
- Git (optional)

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Charantej2005/StudentPerformancePredictor.git
```

Go to the project directory:

```bash
cd StudentPerformancePredictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run:

```bash
python src/main.py
```

---

# Workflow

```text
Load Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Dataset Analysis
      │
      ▼
Grade Calculation
      │
      ▼
Student Ranking
      │
      ▼
Generate Report
      │
      ▼
Save CSV Report
```

---

# Sample Dataset

Version 1.0 uses a predefined dataset located at:

```text
data/raw/students.csv
```

The dataset contains:

- Student ID
- Name
- Gender
- Class
- Subject Marks
- Attendance

---

# Sample Console Output

```text
========================================
Student Performance Analysis Tool
========================================

Student dataset loaded successfully.

Cleaning Dataset...
✓ Duplicate records removed
✓ Missing values handled
✓ Marks validated

Dataset Analysis...
✓ Dataset information displayed
✓ Statistical summary generated

Grading Students...
✓ Total marks calculated
✓ Average calculated
✓ Grades assigned
✓ Pass/Fail status generated

Ranking Students...
✓ Student ranking generated
✓ Topper identified

Report Generation...
✓ Student report generated
✓ Report saved successfully

Project completed successfully.
```

---

# Output

Running the project generates:

```text
output/
└── reports/
    └── student_report.csv
```

The report contains:

- Student Information
- Total Marks
- Average Marks
- Grade
- Result
- Rank

---

# Project Modules

| Module | Purpose |
|---------|---------|
| load_data.py | Loads the student dataset |
| clean_data.py | Cleans and validates data |
| analysis.py | Performs statistical analysis |
| grading.py | Calculates marks, grades and results |
| ranking.py | Generates rankings |
| report.py | Generates and saves reports |
| utils.py | Helper functions |
| main.py | Controls the project workflow |

---

# Skills Demonstrated

- Python Programming
- Modular Programming
- NumPy
- Pandas
- Data Cleaning
- Data Analysis
- CSV File Handling
- Software Engineering
- Git
- GitHub

---

# Roadmap

## Version 1.0

- CSV dataset support
- Data cleaning
- Dataset analysis
- Grade calculation
- Student ranking
- CSV report generation

## Version 2.0

- User-uploaded CSV datasets
- Excel (.xlsx) support
- Better validation
- Improved error handling
- Save cleaned datasets automatically

## Version 2.1

- Matplotlib visualizations
- Attendance dashboard
- Grade distribution charts

## Version 3.0

- Machine Learning based student performance prediction
- Interactive dashboard
- Multiple dataset support

---

# Author

**Charan Tej N M**

GitHub:
https://github.com/Charantej2005

LinkedIn:
https://www.linkedin.com/in/charan-tej-n-m-6530a11b6

LeetCode:
https://leetcode.com/u/Charan_0302/

---

# License

This project is licensed under the MIT License.

---

If you found this project useful, consider giving it a ⭐ on GitHub.
