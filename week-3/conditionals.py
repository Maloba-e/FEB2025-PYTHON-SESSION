#conditional statements- help us make decisions
#basic conditionals
#if statement
#if ... else statement
#if..elif..else statement

##if statement - only one expectation
temperature = 30
if temperature <= 30 :
    print("it is cold")
    
##if...elif..else
marks = float(input("Enter your average score:"))
if marks >=70 :
    print(f'Your score is {marks}\nYou have passed')
elif marks >= 60:
    print(f'Your score is {marks}\nYou have passed')
elif marks >=50:
    print(f'Your score is {marks}\nYou have passed')
else:
    print(f'Your score is {marks}\nYou have failed')