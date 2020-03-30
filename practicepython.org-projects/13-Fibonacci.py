# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
#  Take this opportunity to think about how you can use functions.
#   Make sure to ask the user to enter the number of numbers in the sequence to generate.
#   (Hint: The Fibonnaci seqence is a
#    sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
#  The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
# http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
def fib():
    z = int(input("how many fib number do you want? "))
    x = 1
    y = 0
    n = 1
    fib_list = [1]
    while n < z:
        y = x+y
        fib_list.append(y)
        x = x+y
        fib_list.append(x)
        n = n+2
    print(fib_list)
fib()
input()

    
