# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?
# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
num = int(input("please enter a number: "))
if num % 2 == 0:
    print("your number is even")
else:
    print("your number is odd")
    
