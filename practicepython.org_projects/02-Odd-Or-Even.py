# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?
# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
num = int(input("please enter a number: "))
if num % 2 == 0:
    print("your number is even")
else:
    print("your number is odd")
# Extras:
# 1-If the number is a multiple of 4, print out a different message.

num = int(input("please enter a number: "))
if num % 4 == 0:
    print("your number is made by 4(s)")
elif num % 2 == 0:
    print("your number is even")
else:
    print("your number is odd")


# 2-Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("please enter a number : "))
check = int(input("please enter the number you want to check by: "))
if num % check == 0:
    print("your number is made of %s" % check)
else :
    print("your number is NOT made of %s" % check)