# DRY :- don't repeat yourself

import random
win_num=random.randint(1,100)
guess=1
number=int(input("enter a number between 1 to 100:-"))
game_over=False

while not game_over:
    if number==win_num:
        print(f"you win !! and you guess this number in {guess} times")
        game_over=True
    else:
        if number<win_num:
            print("too low")
        else:
            print("too high")

        guess+=1                                         #not repeat
        number=int(input("guess again:- " ))             #not repeat