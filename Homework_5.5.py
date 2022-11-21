#potrebno u istom folderu imati game.py, score.py, score_list.json

from game import play_game
from score import get_score_list

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit?: ")

    if selection == "A":
        play_game()
    elif selection == "B":
        get_score_list()
    else:
        break

print("The end")