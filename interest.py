#Establishing variables
int_per_annum =0.04
int_in_2years=int_per_annum*2
int_in_3years=int_in_2years*3

#accepting input from user
deposited_Amt=float(input("Enter amount deposited:  "))
number_of_years =input("Enter the number years you are saving:   ") 
#calculating
total_amount_1 = int_per_annum+deposited_Amt

total_amount_2 = int_in_2years+deposited_Amt

total_amount_3 = int_in_3years+deposited_Amt

#displaying result
print("your total balance is: ",format(total_amount_1,'.2f'))
print("your total balance is: ",format (total_amount_2,'2f'))
print("your total balance is: ",format(total_amount_3,'.2f'))
  