# Write a password generator in Python. Be creative with how you generate passwords
#  - strong passwords have a mix of lowercase letters, uppercase letters, numbers, 
#  and symbols. The passwords should be random, generating a new password every time the
#   user asks for a new password. Include your run-time code in a main method.
# http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
from random import randint,shuffle
lower_words = list(map(chr, range(97, 123)))
upper_words = list(map(chr, range(65, 91)))
symbols = list("!@#$%^&*()_+-=")
numbers = list(range(0,9))
def generate_password():
    password = ""
    print("Hey, I will help you to make your safe personal password!")
    lower_words_quantity = int(input("tell me how many lower-words should your password have?: "))
    upper_words_quantity = int(input("tell me how many upper-words should your password have?"))
    symbols_quantity = int(input("tell me how many symbols should your password have?"))
    numbers_quantity = int(input("tell me how many numbers should your password have?"))
    n = 0
    while n <= lower_words_quantity:
        n = n+1
        random = randint(0,25)
        password = password + lower_words[random]
    n = 0
    while n <= upper_words_quantity:
        n = n+1
        random = randint(0,25)
        password = password + upper_words[random]
    n = 0
    while n <= symbols_quantity:
        n = n+1
        random = randint(0,13)
        password = password + symbols[random]
    n = 0
    while n <= numbers_quantity:
        n = n+1
        random = randint(0,9)
        password = password + str(numbers[random])
    listed_pass = list(password)
    shuffle(listed_pass)
    shuffled_pass = "".join(listed_pass)
    print(shuffled_pass)

generate_password()
input()


    


        
    



