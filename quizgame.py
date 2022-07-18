print("WELCOME TO MY COMPUTER QUIZ")
Playing=input("Do you want to play?  ")
if Playing.lower() != "yes":
    quit()
print("Ok! let's play :)")
score = 0
answer = input("What does CPU stand for? a. Central processor unit\nb.Center process unit\nc. center processor unit\nd.central processing unit ")
if answer.lower() == "d.central processing unit":
    print("correct!,Geeks")
    score += 1
else:
    print("Incorrect")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("correct!, Geek")
    score += 1
else:
    print("Incorrect,Try again")
answer = input("What does RAM stand for?  ")
if answer.lower() == "random access memory":
    print("correct!, Geek")
    score += 1
else:
   print("Incorrect,Try again")
   answer = input("What does PSU stand for?  ")
if answer == "power supply unit":
    print("correct!, Geek")
    score += 1
else:
    print("Incorrect,Try again")
print("You got " + str(score) + "  questions correct")
print("You got " + str(score/4*100) + "%")