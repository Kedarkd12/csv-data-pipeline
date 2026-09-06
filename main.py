import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import os
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

conn_string = os.getenv("DATABASE_URL")
engine = create_engine(conn_string)

def load_data():
    logger.info("Reading employee_records.csv")
    employees = pd.read_csv("data/raw/employee_records.csv")
    logger.info("Extracted %d records", len(employees))
    employees = employees.replace(r"^\s*$", pd.NA, regex=True)
    employees["Salary"]=pd.to_numeric(employees["Salary"],errors="coerce")
    employees["Age"]=pd.to_numeric(employees["Age"],errors="coerce")
    logger.info("Data cleaning and type conversion completed")
    return employees

def duplicate_data(data):
    print("Duplicate Employee ID:",data["Employee_ID"].duplicated().sum())

def missing_data(data):
    print("Missing Employee ID:",data["Employee_ID"].isna().sum())
    print("Missing Employee Name:",data["Employee_Name"].isna().sum())
    print("Missing Employee Department:",data["Department"].isna().sum())
    data["Joining_Date"]=pd.to_datetime(data["Joining_Date"],format="%Y-%m-%d",errors="coerce")
    print("Invalid or Missing Joining Date:",data["Joining_Date"].isna().sum())


def invalid_data(data):
    data["Age"]=data["Age"].apply(lambda x:pd.NA if x<18 or x>65 else x)
    print("Invalid or Missing Age:",data["Age"].isna().sum())
    data["Salary"]=data["Salary"].astype(float)
    data["Salary"]=data["Salary"].apply(lambda x:pd.NA if x<0 else x)
    print("Invalid or Missing salaries:",data["Salary"].isna().sum())

def write_data(data):
    invalid = data[data.isna().any(axis=1) | data["Employee_ID"].duplicated(keep="first")]
    valid = data[~(data.isna().any(axis=1) | data["Employee_ID"].duplicated(keep="first"))]
    logger.info("Valid records: %d", len(valid))
    logger.info("Rejected records: %d", len(invalid))
    invalid.to_csv("data/rejected/rejected.csv",index=False)
    logger.info("Rejected CSV written successfully")
    valid=valid.drop(columns=["Rejection_Reason"])
    valid.columns=valid.columns.str.lower()
    valid.to_csv("data/cleaned/cleaned.csv",index=False)
    logger.info("Cleaned CSV written successfully")
    valid.to_sql("employees",engine,if_exists="replace",index=False)
    logger.info("Data Loaded to PostgreSQL successfully")
    print("Valid Records:",len(valid))
    print("Invalid Records:",len(invalid))
    print("Data Loaded to PostgreSQL successfully.")

def reports(data):
    data["Rejection_Reason"]=""
    data.loc[data["Employee_ID"].isna(),"Rejection_Reason"]+="Missing Employee ID ; " 
    data.loc[data["Employee_Name"].isna(),"Rejection_Reason"]+="Missing Employee Name ; "
    data.loc[data["Department"].isna(),"Rejection_Reason"]+="Missing Employee Department ; "
    data.loc[data["Age"].isna(),"Rejection_Reason"]+="Missing Employee Age ; "
    data.loc[data["Age"]<18,"Rejection_Reason"]+="Invalid Age:Too Young ; "
    data.loc[data["Age"]>65,"Rejection_Reason"]+="Invalid Age:Too Old ; "
    data.loc[data["Salary"].isna(),"Rejection_Reason"]+="Missing Employee Salary ; "
    data.loc[data["Salary"]<0,"Rejection_Reason"]+="Invalid Employee Salary ; "
    data.loc[data["Joining_Date"].isna(),"Rejection_Reason"]+="Missing/Invalid Joining Date ; "
    data.loc[data["Employee_ID"].duplicated(keep="first"),"Rejection_Reason"]+="Duplicate Employee ID ; "
    return data["Rejection_Reason"]

def main():
    logger.info("========== ETL PIPELINE STARTED ==========")
    data=load_data()
    missing_data(data)
    reports(data)
    invalid_data(data)
    duplicate_data(data)
    write_data(data)
    logger.info("========== ETL PIPELINE COMPLETED ==========")

"""#debugging
    print(employees.head(5))
    employees.info()
    print(employees.shape)
    print(employees.describe())
"""

if __name__=="__main__":
    main()