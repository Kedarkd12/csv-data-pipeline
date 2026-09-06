# Employee Data ETL & Validation Pipeline

## Overview

This project is an end-to-end **ETL (Extract, Transform, Load) pipeline** built using Python, Pandas and PostgreSQL.

The pipeline extracts employee data from a CSV file, cleans and validates the data, identifies invalid records and their rejection reasons, generates cleaned and rejected datasets, loads valid records into PostgreSQL, and performs SQL-based analysis.

The project demonstrates a practical data engineering workflow from **raw data ingestion to database loading and analytical reporting**.

---

## ETL Pipeline

```text
Raw CSV
   │
   ▼
Extract
(Pandas)
   │
   ▼
Transform
(Cleaning & Type Conversion)
   │
   ▼
Validate
(Data Quality Checks)
   │
   ├──────────────► Rejected Records
   │                 + Rejection Reasons
   │
   ▼
Cleaned Dataset
   │
   ├──────────────► cleaned.csv
   │
   ▼
PostgreSQL
   │
   ▼
SQL Analysis
   │
   ▼
Analysis Report
```

---

## Features

- Extracts employee data from CSV using Pandas
- Handles missing and blank values
- Converts numeric columns to appropriate data types
- Parses and validates joining dates
- Validates employee IDs, names and departments
- Validates employee age
- Validates employee salary
- Detects duplicate employee IDs
- Records specific rejection reasons for invalid records
- Separates valid and rejected records
- Exports cleaned and rejected CSV files
- Loads valid records into PostgreSQL
- Performs analytical queries using PostgreSQL
- Generates an analysis report from SQL results
- Maintains pipeline logs

---

## Data Validation Rules

| Field | Validation Rule |
|---|---|
| Employee ID | Must be present and unique |
| Employee Name | Must not be empty |
| Department | Must not be empty |
| Age | Must be between 18 and 65 |
| Salary | Must be present and non-negative |
| Joining Date | Must be a valid date in `YYYY-MM-DD` format |

Invalid records are stored separately along with the reason they were rejected.

---

## Project Structure

```text
employee-etl-pipeline/
│
├── data/
│   ├── raw/
│   │   └── employee_records.csv
│   ├── cleaned/
│   │   └── cleaned.csv
│   └── rejected/
│       └── rejected.csv
│
├── logs/
│   └── pipeline.log
│
├── sql/
│   └── analysis.sql
│
├── reports/
│   └── analysis_results.md
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

- **Python 3**
- **Pandas** – data extraction, cleaning and transformation
- **SQLAlchemy** – database connectivity
- **psycopg2** – PostgreSQL connection
- **PostgreSQL** – data storage and SQL analysis
- **SQL** – analytical queries
- **Git & GitHub** – version control

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd employee-etl-pipeline
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Requirements

```text
pandas
SQLAlchemy
psycopg2-binary
```

---

## PostgreSQL Setup

Create a PostgreSQL database for the project.

Example:

```sql
CREATE DATABASE employees;
```

Configure the database connection in `main.py`.

For a real deployment, database credentials should be stored in environment variables rather than directly in the source code.

---

## Running the Pipeline

Place the raw CSV file inside:

```text
data/raw/employee_records.csv
```

Run:

```bash
python main.py
```

The pipeline will:

1. Extract the raw CSV data.
2. Clean blank and invalid values.
3. Convert numeric and date columns.
4. Validate the records.
5. Generate rejection reasons.
6. Separate valid and rejected records.
7. Save the resulting CSV files.
8. Load valid records into PostgreSQL.
9. Log the pipeline execution.

---

## Output Files

### Cleaned Data

```text
data/cleaned/cleaned.csv
```

Contains records that successfully passed all validation rules.

### Rejected Data

```text
data/rejected/rejected.csv
```

Contains invalid records along with their corresponding rejection reasons.

### Pipeline Logs

```text
logs/pipeline.log
```

Contains information about pipeline execution, processing stages and errors.

---

## PostgreSQL Data

Valid employee records are loaded into the PostgreSQL table:

```text
employees
```

The table contains:

```text
employee_id
employee_name
department
age
salary
joining_date
```

---

## SQL Analysis

The loaded PostgreSQL data is analyzed using SQL.

The analysis includes:

1. Average salary by department
2. Top 10 highest-paid employees
3. Salary ranking within each department
4. Employees hired per year
5. Salary comparison by department
6. Employees earning above the overall average salary
7. Top 20% earners in each department
8. Duplicate employee ID detection

The SQL queries are available in:

```text
sql/analysis.sql
```

The results and key observations are documented in:

```text
reports/analysis_results.md
```

---

## Key Data Engineering Concepts Demonstrated

### Extract
- Reading raw CSV data
- Handling source data using Pandas

### Transform
- Handling missing values
- Data type conversion
- Date parsing
- Data cleaning
- Data validation
- Rejection reason generation

### Load
- Writing cleaned and rejected datasets
- Loading validated data into PostgreSQL

### Data Quality
- Missing-value detection
- Range validation
- Duplicate detection
- Invalid date detection
- Record-level rejection tracking

### Analytics
- Aggregations
- Subqueries
- Common Table Expressions
- Window functions
- Ranking
- Department-level analysis

---

## Example Pipeline Result

The pipeline produces two primary datasets:

```text
                    Raw Employee Data
                           │
                           ▼
                    Pandas ETL Pipeline
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
             Valid Records      Invalid Records
                  │                 │
                  ▼                 ▼
           cleaned.csv         rejected.csv
                  │
                  ▼
             PostgreSQL
                  │
                  ▼
             SQL Analysis
                  │
                  ▼
          Analysis Results
```

---

## Project Goal

The goal of this project is to demonstrate how raw, potentially unreliable data can be transformed into **clean, validated and analysis-ready data** through an end-to-end ETL workflow.

The project focuses on practical data engineering skills rather than simply performing individual data analysis tasks.

---

## Future Improvements

Possible future extensions include:

- Automated scheduling using Airflow
- Cloud-based data storage
- Incremental data loading
- Automated data-quality tests
- Unit testing
- Containerization with Docker
- Cloud deployment

---

## Skills Demonstrated

- Python
- Pandas
- ETL Pipelines
- Data Cleaning
- Data Validation
- Data Quality
- PostgreSQL
- SQL
- Window Functions
- Common Table Expressions
- Database Loading
- Logging
- Git & GitHub
- Analytical Reporting

---

## Author

**Kedar Antarkar**

Bachelor of Engineering – Computer Engineering