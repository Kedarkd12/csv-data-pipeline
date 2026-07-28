import csv

def load_data():
    employees=[]

    with open("data/raw/employee_records.csv") as file:
        reader=csv.DictReader(file)
        for row in reader:
            employees.append(row)
    return employees

def validate_data(records):
    missing_employee_id=0
    missing_employee_name=0
    missing_employee_department=0
    for record in records:
        if record["Employee_ID"].strip() == "":
            missing_employee_id+=1
        if record["Employee_Name"].strip() == "":
            missing_employee_name+=1
        if record["Department"].strip() == "":
            missing_employee_department+=1
    print("Validation report")
    print("------------------")
    print("missing_employee_id",missing_employee_id)
    print("missing_employee_name",missing_employee_name)
    print("missing_employee_department",missing_employee_department)

def main():
    records=load_data()
    validate_data(records)

"""#debugging
    print(len(records))
    for employee in records[:5]:
        print(employee, end="\n\n")
"""

if __name__=="__main__":
    main()