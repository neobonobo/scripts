f=open("salaries.txt","r")

employees={}

for line in f:
    entry=line.strip().split(",")
    employee=entry[0]
    salary=entry[1]
    currency=entry[2]
    employees[employee]=salary +" "+currency
    print(employee+":"+salary+" "+currency)
f.close
print(employees)

