# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
CURRENT_YEAR = 2020
user_name = input("enter your name : ")
user_age = int(input("enter your age : "))
# years left to 100 years 
remained_years = 100 - user_age
remained_years = CURRENT_YEAR + remained_years
print (user_name + " you will turn to 100 years old in %s" % remained_years)
input()