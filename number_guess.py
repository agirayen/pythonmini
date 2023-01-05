import random
n=random.randrange(1,10)

guess=int(input("Enter your guess  "))


while n!= guess:

    if guess<n:
        print("You guessed low")
        guess=int(input("Enter again "))
    elif guess>n:
        print("You guessed high")
        guess=int(input("Enter again "))
    else:
        break
print("right guess")    
        
                  

          
