workers_name=input("Enter worker's name:")
task_name=input("Enter activity:")
hours_worked=int(input("Enter worked hours:"))
RATE=30000
wage=int(hours_worked*RATE)
allowance=int(0.05*wage) 
gross_wage=allowance+wage
tax=int(0.05*gross_wage)
net_wage=int(gross_wage-tax)

print(f"wage: {wage}\n allowance:{allowance}\n  gross_wage:{gross_wage}\n tax:{tax}\n net_wage:{net_wage} ")
