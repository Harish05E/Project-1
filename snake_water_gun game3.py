
import random

computer = random.choice([-1, 0, 1]) # with the help of random module the computer can choose any number randomly.
youstr = input("Enter your choice: ") 
youDict = {"s": 1, "w": -1, "g": 0} 
reversedDict = {1: "Snake", -1: "Water", 0: "Gun"} # make number into Snake, Water or Gun

you = youDict[youstr] 

# By now we have 2 numbers 'you' and 'computer' 

print(f"you choose {reversedDict[you]}\nComputer chose {reversedDict[computer]}")



# understanding Patterns  {comuter - you}
'''
elif(computer == -1 and you == 1): (computer - you) == -2
    print("You win!")

elif(computer == -1 and you == 0):(computer - you) ==  -1
    print("You loose!")

elif(computer == 1 and you == -1): (computer - you) ==  2
    print("You loose!")

elif(computer == 1 and you == 0): (computer - you) == 1
    print("You win!")

elif(computer == 0 and you == -1):(computer - you) == 1
    print("You win!")

elif(computer == 0 and you == 1):(computer - you) == -1
    print("You loose!")                '''

'''
we are loosing when "-1" and "2" is occuring baki cases mai "1" ya "-2" mai ham jit rahe hai so ham simple se usse replace kar sakte hai lets do it. 
'''

if((computer - you) == -1 or (computer - you) == 2):  # matlab itni sari jo lines hai upar usse hai iss ek line mai replace kar sakte hai. 
    print("You loose!")
else:
    print("You win!")   # But drawback is it's not readable only you know the logic 

# code is a little bit wrong but in this page that's not our moto it is to understand to build logic and to make code length as small as possible
