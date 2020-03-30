# Ask the user for a number and determine whether the number is prime or not.
#  (For those who have forgotten, a prime number is a number that has no divisors.).|||| ???? You can (and should!)
#  use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below. ????? ||||
# http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
half = 1/2
prime_list = []
def prime_chk(user_num):
    status = 0
    n = 1
    radical = user_num ** half
    while n <= radical:
        n = n+1
        if user_num % n == 0:
            status = 1
    if status == 1:
        print("your number is NOT prime!\n")
    else:
        print("your number is prime!\n")
try: 
    while True:
        u = int(input("enter a number: "))
        prime_chk(u)
except:
    pass





