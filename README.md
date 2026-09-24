# Employee Data ETL & HR Analytics Dashboard

## Overview

This project is an end-to-end **ETL (Extract, Transform, Load) and analytics pipeline** built using Python, Pandas, PostgreSQL and Power BI.

The pipeline extracts employee data from a CSV file, cleans and validates the records, identifies invalid data and rejection reasons, loads valid records into PostgreSQL, performs analytical SQL queries, and presents the results through an interactive HR Analytics dashboard.

The project demonstrates a practical workflow from **raw data ingestion to data cleaning, database loading, analytical SQL, data modeling and business intelligence reporting**.

---

## Architecture

    Raw CSV
        ↓
    Python / Pandas
        ↓
    Cleaning & Validation
        ↓
    ┌─────────────────────┐
    │                     │
    Valid Records      Rejected Records
        │                     │
        ↓                     ↓
    PostgreSQL           rejected.csv
        │
        ↓
    SQL Analysis
        │
        ↓
    Power BI
        │
        ↓
    HR Analytics Dashboard

---

## Key Features

- Extracts employee data from CSV using Pandas
- Handles missing and blank values
- Converts numeric and date columns
- Validates employee IDs, names, departments, age, salary and joining dates
- Detects duplicate Employee IDs
- Generates record-level rejection reasons
- Separates valid and rejected records
- Exports cleaned and rejected datasets
- Loads valid records into PostgreSQL
- Performs analytical SQL queries
- Uses CTEs, subqueries and window functions
- Builds a star-schema data model in Power BI
- Uses surrogate keys and a date dimension
- Creates DAX measures and KPI cards
- Provides an interactive HR Analytics dashboard
- Maintains pipeline execution logs

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

Invalid records are stored separately along with their corresponding rejection reasons.

---

## Project Structure

    employee-etl-pipeline/
    │
    ├── data/
    │   ├── raw/
    │   ├── cleaned/
    │   └── rejected/
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
    ├── powerbi/
    │   └── HR_Analytics_Dashboard.pbix
    │
    ├── main.py
    ├── requirements.txt
    ├── README.md
    └── .gitignore

---

## Technologies Used

- **Python 3** – ETL pipeline development
- **Pandas** – data extraction, cleaning and transformation
- **PostgreSQL** – database storage and SQL analysis
- **SQLAlchemy** – database connectivity
- **psycopg2** – PostgreSQL connection
- **SQL** – analytical queries
- **Power Query** – data transformation and modeling
- **Power BI** – visualization and dashboard development
- **DAX** – analytical measures and KPIs
- **Git & GitHub** – version control

---

## Installation

Clone the repository:

    git clone <repository-url>
    cd employee-etl-pipeline

Install the required dependencies:

    pip install -r requirements.txt

### Requirements

    pandas
    SQLAlchemy
    psycopg2-binary

---

## PostgreSQL Setup

Create a PostgreSQL database:

    CREATE DATABASE employees;

Configure the database connection in `main.py`.

For production environments, database credentials should be stored using environment variables rather than directly in the source code.

---

## Running the Pipeline

Place the raw dataset inside:

    data/raw/employee_records.csv

Run the pipeline:

    python main.py

The pipeline will:

1. Extract the raw CSV data.
2. Clean blank and invalid values.
3. Convert numeric and date columns.
4. Validate the records.
5. Generate rejection reasons.
6. Separate valid and rejected records.
7. Save the cleaned and rejected datasets.
8. Load valid records into PostgreSQL.
9. Log the pipeline execution.

---

## Output Files

### Cleaned Data

    data/cleaned/cleaned.csv

Contains records that successfully passed all validation rules.

### Rejected Data

    data/rejected/rejected.csv

Contains invalid records along with their corresponding rejection reasons.

### Pipeline Logs

    logs/pipeline.log

Contains information about pipeline execution, processing stages and errors.

---

## PostgreSQL

Valid employee records are loaded into the `employees` table.

The table contains:

    employee_id
    employee_name
    department
    age
    salary
    joining_date

---

## SQL Analysis

The PostgreSQL data is analyzed using SQL queries covering:

- Average salary by department
- Top 10 highest-paid employees
- Salary ranking within departments
- Employees hired per year
- Salary comparison by department
- Employees earning above the overall average salary
- Top 20% earners by department
- Duplicate Employee ID detection

SQL queries are available in:

    sql/analysis.sql

The analysis results and observations are documented in:

    reports/analysis_results.md

---

## Power BI Data Model

The PostgreSQL employee data is modeled in Power BI using a **star-schema approach**.

    dim_employee
         │
         │
    dim_department ── fact_employee ── dim_position
                         │
                         │
                    dim_country
                         │
                         │
                      dim_date

### Dimension Tables

- `dim_employee`
- `dim_department`
- `dim_position`
- `dim_country`
- `dim_date`

### Fact Table

- `fact_employee`

The fact table contains the keys connecting the dimension tables along with employee salary data.

The model uses **surrogate keys** to establish relationships between fact and dimension tables.

A continuous date dimension was created based on the employee joining-date range and includes:

- Date Key
- Full Date
- Day
- Month
- Month Name
- Quarter
- Year

---

## Power BI Dashboard

The project includes an interactive **HR Analytics Dashboard**.

### KPI Cards

- Total Employees
- Average Salary
- Total Salary
- Maximum Salary
- Average Age

### Visualizations

- Employees by Department
- Employees by Position
- Average Salary by Department
- Employee Count Trend
- Employees by Country

### Filters

- Year
- Department
- Position
- Country

The dashboard allows users to interactively explore employee distribution, salary patterns and workforce trends.

---

## Key Data Engineering Concepts Demonstrated

### ETL

- Data extraction
- Data cleaning
- Data transformation
- Data validation
- Database loading

### Data Quality

- Missing-value detection
- Range validation
- Duplicate detection
- Invalid date detection
- Record-level rejection tracking

### Data Modeling

- Fact and dimension tables
- Star schema
- Surrogate keys
- Date dimension
- Fact-to-dimension relationships

### Analytics

- SQL aggregations
- CTEs
- Subqueries
- Window functions
- Ranking
- DAX measures
- Power BI dashboard development

---

## Future Improvements

- Airflow pipeline orchestration
- Incremental data loading
- Automated data-quality testing
- Unit testing
- Docker containerization
- AWS cloud deployment
- Automated Power BI dataset refresh

---

## Skills Demonstrated

Python • Pandas • ETL • Data Cleaning • Data Validation • Data Quality • PostgreSQL • SQL • CTEs • Window Functions • Data Modeling • Star Schema • Surrogate Keys • Power Query • DAX • Power BI • Git & GitHub • Logging • Analytical Reporting

---

## Author

**Kedar Antarkar**

Bachelor of Engineering – Computer Engineering