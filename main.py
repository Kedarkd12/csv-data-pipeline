import csv
import datetime

def load_data():
    employees=[]

    with open("data/raw/employee_records.csv") as file:
        reader=csv.DictReader(file)
        for row in reader:
            employees.append(row)
    return employees

def validate_id(records):
    colleague=set()
    missing_employee_id=0
    duplicate_employee_id=0
    for record in records:
        e_id = record["Employee_ID"].strip()
        if e_id == "":
            missing_employee_id+=1
        else:
            if e_id not in colleague:
                colleague.add(e_id)
            else:
                duplicate_employee_id+=1
    return missing_employee_id,duplicate_employee_id

def validate_name(records):
    missing_employee_name=0
    for record in records:
        if record["Employee_Name"].strip() == "":
            missing_employee_name+=1
    return missing_employee_name

def validate_department(records):
    missing_employee_department=0
    for record in records:
        if record["Department"].strip() == "":
            missing_employee_department+=1
    return missing_employee_department

def validate_age(records):
    invalid_age=0
    for record in records:
        if record["Age"].strip() != "":
            try:
                age = int(record["Age"])
                if not 18 < age < 70:
                    invalid_age+=1
            except ValueError:
                invalid_age+=1
        else:
            invalid_age+=1
    return invalid_age

def validate_salary(records):
    invalid_salary=0
    for record in records:
        if record["Salary"].strip() != "":
            try:
                salary = float(record["Salary"])
                if salary <= 0:
                    invalid_salary+=1
            except ValueError:
                invalid_salary+=1
        else:
            invalid_salary+=1
    return invalid_salary

def validate_date(records):
    invalid_date=0
    for record in records:
        if record["Joining_Date"].strip() != "":
            try:
                join_date = datetime.date.fromisoformat(record["Joining_Date"])
            except ValueError:
                invalid_date+=1
        else:
            invalid_date+=1
    return invalid_date

def seperate_records(records):
    pass

def write_cleaned_csv(records):
    pass

def write_rejected_csv(records):
    pass

def invalid_data_report(data):
    print("Validation report")
    print("------------------")
    print("Missing Employee IDs:",validate_id(data)[0])
    print("Missing Employee Name:",validate_name(data))
    print("Missing Employee Department:",validate_department(data))
    print("Invalid Age:",validate_age(data))
    print("Invalid Salary:",validate_salary(data))
    print("Invalid Date Format:",validate_date(data))
    print("Duplicate Employee IDs",validate_id(data)[1])

def main():
    records=load_data()
    invalid_data_report(records)

"""#debugging
    print(len(records))
    for employee in records[:5]:
        print(employee, end="\n\n")
"""

if __name__=="__main__":
    main()