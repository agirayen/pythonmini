import time
import random
name=input("What is your name? ")
print("Hello "+name ," It is time to play")
time.sleep(1)
print("Start guessing...\n")
time.sleep(0.5)

words=['python','travel','market','square','publish','confirm']
word=random.choice(words)
guesses=''
turns=5

while turns>0:
    failed=0

    for char in word:
        if char in guesses:
            print(char,end="")
        else:
            print("_",end="")
            failed=failed+1
    if failed == 0:
        print("\n you won")
        break

    guess = input("\n guess a character: ")
    guesses=guesses+guess
    if guess not in word:
        turns=turns-1
        print("\n wrong")
        print("\n you have",+turns,"more guesses")

        if turns == 0:
            print("\n you lose")
        
            
