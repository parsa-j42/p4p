# Generate a random number between 1 and 9 (including 1 and 9).
#  Ask the user to guess the number, then tell them whether they guessed too low, too high,
# or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
from random import randint

x = randint(1,9)
esc = 0
while esc != 1:
    guess = int(input("guess a number between 1 and 9: "))
    m = x - guess
    if m == 0:
        print("your guess was exactly right!") 
        print("the number was%s" % x)
        input()
        esc = 1
    elif 1 <= m <= 4:
        print("you are close!") 
    else:
        print("you are really far!")
