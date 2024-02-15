employee_name=input("Enter employee name: ")
hours_worked=int(input("Enter hours worked: "))
RATE=30000
wage=int(hours_worked*RATE)
if wage >=500000:
    print("you are eligible to pay tax")
    tax=0.1*wage
else:
    print("you arenot eligible for paying tax ")
    tax=0
net_wage=wage-tax
print(f"netwage: {net_wage}")
print(f"wage: {wage}")
