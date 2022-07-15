name = input("Type your name: ")
print("welcome",name, "to choose your adventure")
answer = input("You are at a dead road,please  take left or right.Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You have reached a river.\n Type swim to swim across \n or Type walk to walk around it? ").lower()
    if answer == "SWIM":
        print("You swam across and got eaten by an alligator").lower()
    elif answer == "WALK":
            print("You walked for many miles and run out of energy").lower()
    else: 
        print(" Not a valid option. You lose!")
elif answer == "right":

    answer = input("You've come to a bridge,it looks wobbly,\n doyou want to cross or head back. \n cross or Back").lower()

    if answer == "Cross":
        print("You crossed the bridge and met a stranger do you talk\n or walk away?").lower()
    elif answer == "Head back":
            print("You Head back and lose").lower()
    else: 
        print(" Not a valid option. You lose!")

else:
    print(" Not a valid option. You lose!")
    print("Thank you for trying")

