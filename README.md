# Employee CSV Data Validation & Cleaning Pipeline

## Overview

This project is a Python-based ETL (Extract, Transform, Load) pipeline that reads employee records from a CSV file, validates the data based on predefined business rules, separates valid and invalid records, and writes them into separate output files.

The project demonstrates fundamental data engineering concepts such as data validation, data cleaning, duplicate detection, and CSV processing using only Python's standard library.

---

## Features

- Read employee data from CSV files.
- Validate employee records.
- Detect missing values.
- Detect duplicate Employee IDs.
- Validate employee age.
- Validate salary values.
- Validate date format.
- Separate valid and invalid records.
- Generate cleaned and rejected CSV files.
- Display a validation summary report.

---

## Validation Rules

The following validations are performed:

- Employee ID cannot be empty.
- Employee ID must be unique.
- Employee Name cannot be empty.
- Department cannot be empty.
- Employee Age must be between 18 and 65.
- Salary must be a positive number.
- Joining Date must follow the required date format(yyyy-mm-dd).

---

## Folder Structure

```
csv-data-pipeline/
│
├── data/
│ ├── raw/
│ │ └── employee_records.csv
│ │
│ ├── cleaned/
│ │ └── cleaned.csv
│ │
│ └── rejected/
│ └── rejected.csv
│
├── logs/
├── reports/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Technologies Used

- Python 3
- csv module
- datetime module
- Git
- GitHub

No external Python libraries were used.

---

## How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project directory

```bash
cd csv-data-pipeline
```

3. Run the project

```bash
python main.py
```

---

## Sample Output

```
Validation Report

Valid Records : 29992
Invalid Records : 8

Missing Employee IDs : 2
Duplicate Employee IDs : 1
Missing Employee Names : 1
Missing Departments : 1
Invalid Ages : 2
Invalid Salaries : 1
Invalid Date Format : 1
```

---

## Output Files

### cleaned.csv

Contains all valid employee records.

### rejected.csv

Contains all records that failed one or more validation rules.

---

## Skills Demonstrated

- Python Programming
- CSV Processing
- Data Validation
- Data Cleaning
- ETL Pipeline Development
- File Handling
- Exception Handling
- Functions
- Dictionaries
- Lists
- Sets
- Git & GitHub

---

## Future Improvements

- Generate validation reports as text files.
- Add logging support.
- Replace CSV processing with Pandas.
- Store processed data in PostgreSQL.
- Add automated unit tests.
- Build an interactive dashboard using Metabase or Apache Superset.

---

## Author

**Kedar Antarkar**

Bachelor of Engineering (Computer Engineering)
