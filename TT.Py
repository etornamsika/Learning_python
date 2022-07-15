tax_rate = 0.05
tip_rate = 0.18


#accept input from user
cost_0f_meal=float(input("Enter cost of meal:  "))

#MyVariables
tax_Amount = cost_0f_meal * tax_rate
tipped_Amount = cost_0f_meal *tip_rate
Grand_Total= (cost_0f_meal +tax_Amount)- tipped_Amount
print(" The tax Amount  is: ", tax_Amount)
print(" The tipped Amount is: ",tipped_Amount)
print(" The sum total is: ",Grand_Total format( ),'.2f')

