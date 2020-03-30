# Write a password generator in Python. Be creative with how you generate passwords
#  - strong passwords have a mix of lowercase letters, uppercase letters, numbers, 
#  and symbols. The passwords should be random, generating a new password every time the
#   user asks for a new password. Include your run-time code in a main method.
# http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
from random import randint
lower_words = list(map(chr, range(97, 123)))
upper_words = list(map(chr, range(65, 91)))
symbols = list("!@#$%^&*()_+-=")
numbers = list(range(0,9))
def generate_password(level):
    n = 0
    while n != 2:
        n = n+1
        rand1 = randint(0,25)
        rand2 = randint(0,25)
        rand3 = randint(0,13)
        rand4 = int(0,9)
    if level == 5:
        password = [lower_words[rand1] + upper_words[rand2] + symbols[rand3] , numbers[rand4]]
        print(password)
    if level == 4:
        password = []




