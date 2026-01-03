# previously computer value was fixed inorder to make it random we will use random module

# "generate a random number out of -1, 0 and 1 in python"  ask this to chatGPT 

import random

computer = random.choice([-1, 0, 1]) # with the help of random module the computer can choose any number randomly.
youstr = input("Enter your choice: ") 
youDict = {"s": 1, "w": -1, "g": 0} 
reversedDict = {1: "Snake", -1: "Water", 0: "Gun"} # make number into Snake, Water or Gun

you = youDict[youstr] 

# By now we have 2 numbers 'you' and 'computer' 

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


'''
hamne 'Random' module ko import kiya cos ham -1, 0, 1 mai se koi bhi ek random number computer se select karva sake
Line 8 mai hamne s, w and g mai se koi bhi ek choice enter kar sake
that choice will be converted into 'you' variable mai {in Line 12} so you ki value ho jaygi -1, 1, 0 mai se {due to Line 9} 
and the reason to write "youDict = {"s": 1, "w": -1, "g": 0}" was we not want to make user type number but letter for better user experience
now we have have 2 number ek computer ka and dusra khud ka {i have mentioned in Line 14} 
we have also make revered Dictionary bhi banai (reversedDict) that will convert number into Snake, Water or Gun 
And to tell that what computer and user has choosen in form of word not numbers we have wrote the code on {Line 16} here 'reversedDict'
dictionary had played a huge role cos it only make number into words(Snake, Water or Gun)

after this it is only combinations of if and elif (rest is easy)

'''




import random as r

random_num = r.randint(1,20)
print("The number to be guessed by you is:- ",random_num)

i = 1
while True:
    print("Number guessed:- ",i)
    if(random_num == i):
        print(f"Hurray the random number has been guessed sucefully and it is {i}")
        break
    i += 1

