import random

cards= ["Diamond","Spad","Heart","Clubs"]

ranks= [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

def find_ran():

    c=random.choices(cards)
    r=random.choices(ranks)

    return(f"The {r} of {c} card picked")
print(find_ran())
