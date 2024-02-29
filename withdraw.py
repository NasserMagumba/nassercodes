print("1.deposit\n2.withdraw\n3.check balance")
option=int(input("\nEnter option:  "))

balance=0
with_draw_amount=0
deposit_amount=0
if option==1:
    deposit_amount=int(input("\nEnter deposit amount: "))
    if deposit_amount>=5000:
        balance+=deposit_amount
        print(f"balance: {balance}")
    else:
        print("transaction failed")
elif option==2:
    balance=int(input("\nEnter current balance: "))
    with_draw_amount=int(input("\nEnter with draw amount:  "))
    if with_draw_amount<balance:
        balance-=with_draw_amount
        print(f"current balance: {balance}")
    else:
        print("transaction failed")
elif option==3:
    balance=int(input("\nbalance: "))
    print(f"current balance: {balance}")
else:
    print("invalid option")

    


