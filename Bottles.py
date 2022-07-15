#establishing Variables
one_less_deposit =0.10
one_more_deposit = 0.25

#accepting user inputs
smaller_Containers = int(input("Enter the number of 1L or less containers : "))
larger_Containers = float(input("Enter the number of 1L or more  containers : "))
 
#Calculates the refund amountn based on the user input and variable factors
reFund_Amt =(smaller_Containers*one_less_deposit) + (larger_Containers*one_more_deposit)
#print("The amount to be refunded is", (reFund_Amt,".2f")  
print("The amount to be refunded is",format (reFund_Amt,'.2f'))    