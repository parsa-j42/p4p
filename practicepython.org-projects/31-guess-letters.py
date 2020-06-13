# http://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html
# Let’s continue building Hangman. In the game of Hangman,
#  a clue word is given by the program that the player has to guess, letter by letter.
#   The player guesses one letter at a time until the entire word has been guessed.
#    (In the actual game, the player can only guess 6 letters incorrectly before losing).
# Let’s say the word the player has to guess is “EVAPORATE”. 
# For this exercise, write the logic that asks a player to guess
#  a letter and displays letters in the clue word that were guessed correctly.
#   For now, let the player guess an infinite number of times until they get the entire word.
#    As a bonus, keep track of the letters the player guessed and display a different message if the player
#     tries to guess that letter again. Remember to stop the game when all the letters have been guessed correctly!
#      Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining
#       - we will deal with those in a future exercise.

# An example interaction can look like this:

# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...
# And so on, until the player gets the word.
#--------------------------------------------------------------------------------
import random
def rand_word():
    dic_lines = open('SOWPODS.txt').read().splitlines()
    random_line = random.choice(dic_lines)
    return random_line

def letter_guess(word):
    word_letters_count = len(word)
    guessed_word = word_letters_count * "_"
    listed_guessed = list(guessed_word)
    listed_word = list(word)
    n = 0
    while "_" in listed_guessed :
        print(listed_guessed)
        player_guess = input("guess a letter : ").upper()
        n = n+1
        if player_guess in listed_guessed:
            print("you guessed this letter before!!!")
        elif not player_guess in listed_word:
            print("wrong guess :(")
        else:
            #listed_guessed[listed_word.index(player_guess)] = player_guess
            for n,i in enumerate(listed_word):
                if(i == player_guess):
                    listed_guessed[n] = listed_word[n]
    print(listed_guessed)
word = rand_word()
print(word)
letter_guess(word)
input()
