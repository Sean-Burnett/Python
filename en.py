import os,sys,random,lotto3

x = random.randrange(1,10)
guess = int(input("Guess a number from 1 to 10.:"))
while (guess!= x):
    if (guess < x):
        print("The answer is higher.")
        guess = int(input("Guess a number from 1-10.:"))
    else:
        print("The answer is lower.")
        guess = int(input("Guess a number from 1-10.:"))

raw_input("You Win")
