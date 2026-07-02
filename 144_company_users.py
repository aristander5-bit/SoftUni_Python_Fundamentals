companies = {}

while True:
    line = input()
    if line == "End":
        break

    data = line.split(" -> ")
    company_name = data[0]
    employee_id = data[1]

    if company_name not in companies:
        companies[company_name] = []
    if  employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

for company_name, employees in companies.items():
    print(company_name)

    for emp in employees:
        print(f"-- {emp}")