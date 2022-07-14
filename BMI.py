print ("THIS IS BMI CALCULATOR")
#this allows user input
weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in m : "))
#BMI calculation
BMI = weight/(height*2)
BMI=round(BMI)
#displays BMI
print(" Your BMI is: ",BMI )