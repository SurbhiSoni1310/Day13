from data import List_of_celebs
from art import logo
from time import sleep
import random
import os

print("Welcome to the Higher Lower Game")
print(logo)
print("Rules : ")
print("1. Guess the celebrity having higher/lower Instagram followers than the given celebrity")
print("2. If you answer wrong game ends")
score = 0


def play_game(sample_key):
    global score
    count = List_of_celebs[sample_key]
    print(f"The number of followers of {sample_key} are {count}M")
    del List_of_celebs[sample_key]
    key2 = random.choice(list(List_of_celebs.keys()))
    print(f"Guess if the number of followers of {key2} are Higher/Lower than {sample_key} ? ")
    # print("Secret : "+str(List_of_celebs[key2]))
    print(f"Current Score : {score}")
    choice = input("Type 'h' or 'l' : ").lower()
    if choice == 'h' and count < List_of_celebs[key2]:
        print("Congrats! You got this")
        score += 1
        print(f"Score {score}")
        os.system("cls")
        print(logo)
        play_game(key2)
    elif choice == "l" and count > List_of_celebs[key2]:
        print("Congrats! You got this")
        score += 1
        print(f"Score {score}")
        os.system("cls")
        print(logo)
        play_game(key2)
    else:
        print("You lost :( ")
        print(f"Your score : {score}")
        sleep(10)
        return False


continue_game = True
while continue_game:
    key = random.choice(list(List_of_celebs.keys()))
    continue_game = play_game(key)
