print("\n\t\t\t====Weekly Pay====\t\t\t\n")
print("""
1.Managers
2.Hourly workers
3.Commission workers
4.Piece workers                 """)

pay_code=int(input("\nEnter Pay Code:"))
overtime_pay=0
wage=0
commission=0


if pay_code==1:
    wage=20000

elif pay_code==2:
    hours_worked=int(input("Enter Hours Worked:"))
    if hours_worked <=40:
        wage=hours_worked * 300

    elif hours_worked > 40:
        wage=hours_worked * 300
        overtime_pay=int(1.5 * 300) + wage
        
    else:
        print("invalid")

elif pay_code==3:
    gloss_weekly_sales=int(input("Enter Gloss Weekly Sales:"))
    commission=0.057 * gloss_weekly_sales
    wage=int(250 + commission)


elif pay_code==4:
    number_of_items=int(input("Enter Number of Items:"))
    wage=int(200 * number_of_items)

else:
    print("invalid")   

print(f"\nWage:{wage}\n\nOvertime Pay:{overtime_pay}\n")

    

    
    



        

    












   




    
    
        

    
    



