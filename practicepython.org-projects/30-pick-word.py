# http://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
# In this exercise, the task is to write a
#  function that picks a random word from a list of words from the SOWPODS dictionary.
#  Download this file and save it in the same directory as your Python code. This file is
#   Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments.
#  Each line in the file contains a single word.
import random
def rand_word():
    dic_lines = open('SOWPODS.txt').read().splitlines()
    random_line = random.choice(dic_lines)
    return random_line
word = rand_word()
print(word)