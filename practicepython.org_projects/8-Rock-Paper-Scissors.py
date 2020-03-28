# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
#  and ask if the players want to start a new game)
# Remember the rules:
#     Rock(0) beats scissors(1)
#     Scissors(1) beats paper(2)
#     Paper(2) beats rock(0)
# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
import os
esc = 0
while esc != 1:
    pl1 = int(input("type 0 for Rock, 1 for Scissors and 2 for Paper\n : "))
    x = os.system("cls")
    pl2 = int(input("type 0 for Rock, 1 for Scissors and 2 for Paper\n : "))
    x = os.system("cls")
    if (pl1 - pl2) == -1 or 2:
        print("player 1 WON")
    else:
        print("player 2 WON")
    esc = int(input("type 0 if you want to play again and type 1 if you want to exit: "))
    x = os.system("cls")


