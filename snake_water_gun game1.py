'''
PROJECT 1: SNAKE, WATER, GUN GAME
We all have played snake, water gun game in our childhood. If you haven't, google the
rules of this game and write a python program capable of playing this game with the
user.

we did this project after chapter 8 

'''
'''
1 is for 'snake'
-1 is for 'water'
0 is for 'gun'
'''

computer = -1
youstr = input("Enter your choice: ") # string manga
youDict = {"s": 1, "w": -1, "g": 0} # here dictionary is used to convert the input.
reversedDict = {1: "Snake", -1: "Water", 0: "Gun"} 

you = youDict[youstr] # iss dictionary mai apki choice ki jo value hai {number} usko you variable mai store karo

print(f"you choose {reversedDict[you]}\nComputer chose {reversedDict[computer]}")

if(computer == you):
    print("it's a Draw!")

elif(computer == -1 and you == 1):
    print("You win!")

elif(computer == 1 and you == -1):
    print("You loose!")

elif(computer == 1 and you == 0):
    print("You win!")

elif(computer == 0 and you == 1):
    print("You loose!")

elif(computer == 0 and you == -1):
    print("You win!")

elif(computer == -1 and you == 0):
    print("You loose!")
else:
    print("Something went wrong")

    


def addition(a,b):
    print("performing the addition operation......\n")
    return a+b

def substraction(a,b):
    print("performing the substraction operation......\n")
    return a-b

def multiplication(a,b):
    print("Performing multiplication operation.......\n")
    return a*b

def myMenu():
    print("Main Menu")
    print("1 -> Addition operation")
    print("2 -> Substraction operation")
    print("3 -> Multiplication operation")
    print("4 -> To exit the operation")
    ch = int(input("Please enter your option number:- "))  # Typecasting
    return ch


