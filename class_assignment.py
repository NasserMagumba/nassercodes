
cost_price=int(input("Enter cost price: \n "))
transport_cost=int(input("Enter transport cost: \n"))


selling_price=int(cost_price+0.05*cost_price)+(0.02*transport_cost)

profit_margin=int(selling_price-cost_price)

print(f"selling price: {selling_price}\n profitmargin: {profit_margin}")
