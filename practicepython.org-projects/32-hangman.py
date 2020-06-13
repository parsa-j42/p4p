# You can start your Python journey anywhere, but to finish this exercise you will have to have finished
#  Parts 1 and 2 or use the solutions (Part 1 and Part 2).

# In this exercise, we will finish building Hangman.
#  In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose
#   the game.

# In Part 1, we loaded a random word list and picked a word from it.
#  In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. In this exercise, we have to put it all together and add logic for handling guesses.

# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

# Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed. If the user guesses a letter they already guessed,
#  don’t penalize them - let them guess again.
# Optional additions:

# When the player wins or loses, let them start a new game.
# Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman.
#  This is challenging - do the other parts of the exercise first!
# Your solution will be a lot cleaner if you make use of functions to help you!
# http://www.practicepython.org/exercise/2017/01/10/32-hangman.html
import random
import os
def dic_sorter():
    user_words = []
    user_letter_nums = (int(input("how many letters do you want your word have?"))+1)
    with open('dic.txt') as dic:
        for line in dic:
            if len(line) == user_letter_nums:
                user_words.append([line.strip()])
    return user_words

def rand_word():
    dic = dic_sorter()
    random_line = random.choice(dic)
    return random_line



def letter_guess(word):
    word = "".join(word)
    word_letters_count = len(word)
    guessed_word = word_letters_count * "_"
    listed_guessed = list(guessed_word)
    listed_word = list(word)
    geusses_number = 0
    wrong_guesses = []
    while "_" in listed_guessed and geusses_number < 6:
        print(listed_guessed)
        print("you have %s wrong guesses remaining!!" % (6-geusses_number))
        player_guess = input("guess a letter : ").lower()
        if player_guess in listed_guessed or player_guess in wrong_guesses:
            print("you guessed this letter before!!!")
        elif not player_guess in listed_word:
            print("wrong guess :(")
            wrong_guesses.append(player_guess)
            geusses_number = geusses_number+1
            
        else:
            for n,i in enumerate(listed_word):
                if(i == player_guess):
                    listed_guessed[n] = listed_word[n]
    print(listed_guessed)
play_again = "Y"
while play_again == "Y":
    os.system('cls')  
    word = rand_word()
    letter_guess(word)
    print(word)
    play_again = input('do you want to play again? (Y/N)').upper()
input()
