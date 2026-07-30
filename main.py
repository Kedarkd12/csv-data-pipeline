import csv
import datetime

def load_data():
    employees=[]

    with open("data/raw/employee_records.csv") as file:
        reader=csv.DictReader(file)
        for row in reader:
            employees.append(row)
    return employees

def validate_data(records):
    invalid_records=[]
    valid_records=[]
    seen_ids=set()
    missing_employee_id=0
    duplicate_employee_id=0
    missing_employee_name=0
    missing_employee_department=0
    invalid_age=0
    invalid_salary=0
    invalid_date=0
    for record in records:
        if record["Employee_ID"] not in seen_ids:
            seen_ids.add(record["Employee_ID"])
            duplicate_eid=False
        else:
            duplicate_employee_id+=1
            duplicate_eid = True
        eid = validate_id(record)
        if eid == False:
            missing_employee_id+=1
        name = validate_name(record)
        if name == False:
            missing_employee_name+=1
        dept = validate_department(record)
        if dept == False:
            missing_employee_department+=1
        age = validate_age(record)
        if age == False:
            invalid_age+=1
        salary = validate_salary(record)
        if salary == False:
            invalid_salary+=1
        date = validate_date(record)
        if date == False:
            invalid_date+=1
        if not duplicate_eid and eid and name and dept and age and salary and date == True:
            valid_records.append(record)
        else:
            invalid_records.append(record)
    return valid_records,invalid_records,missing_employee_id,missing_employee_name,missing_employee_department,invalid_age,invalid_salary,invalid_date,duplicate_employee_id

def validate_id(record):
    valid = True
    e_id = record["Employee_ID"].strip()
    if e_id == "":
        valid = False
    return valid

def validate_name(record):
    valid = True
    if record["Employee_Name"].strip() == "":
        valid = False
    return valid

def validate_department(record):
    valid = True
    if record["Department"].strip() == "":
        valid = False
    return valid

def validate_age(record):
    valid = True
    if record["Age"].strip() != "":
        try:
            age = int(record["Age"])
            if not 18 < age < 70:
                valid = False
        except ValueError:
            valid = False
    else:
        valid = False
    return valid

def validate_salary(record):
    valid = True
    if record["Salary"].strip() != "":
        try:
            salary = float(record["Salary"])
            if salary <= 0:
                valid = False
        except ValueError:
            valid = False
    else:
        valid = False
    return valid

def validate_date(record):
    valid = True
    if record["Joining_Date"].strip() != "":
        try:
            join_date = datetime.date.fromisoformat(record["Joining_Date"])
        except ValueError:
            valid = False
    else:
        valid = False
    return valid

def seperate_records(records):
    pass

def write_cleaned_csv(correct):
    with open("data/cleaned/cleaned.csv","w",newline="") as file:
        writer = csv.DictWriter(file,fieldnames=["Employee_ID","Employee_Name","Age","Country","Department","Position","Salary","Joining_Date"])
        writer.writeheader()
        for row in correct:
            writer.writerow(row)

def write_rejected_csv(incorrect):
    with open("data/rejected/rejected.csv","w",newline="") as file:
            writer = csv.DictWriter(file,fieldnames=["Employee_ID","Employee_Name","Age","Country","Department","Position","Salary","Joining_Date"])
            writer.writeheader()
            for row in incorrect:
                writer.writerow(row)

def invalid_data_report(data):
    print("Validation report")
    print("------------------")
    print("Valid Records:",len(data[0]))
    print("Invalid Records:",len(data[1]))
    print("Missing Employee IDs:",data[2])
    print("Missing Employee Name:",data[3])
    print("Missing Employee Department:",data[4])
    print("Invalid Age:",data[5])
    print("Invalid Salary:",data[6])
    print("Invalid Date Format:",data[7])
    print("Duplicate Employee IDs",data[8])

def main():
    records=load_data()
    data = validate_data(records)
    correct_data = data[0]
    incorrect_data = data[1]
    invalid_data_report(data)
    write_cleaned_csv(correct_data)
    write_rejected_csv(incorrect_data)

"""#debugging
    print(len(records))
    for employee in records[:5]:
        print(employee, end="\n\n")
"""

if __name__=="__main__":
    main()