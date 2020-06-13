# Implement a function that takes as input three variables,
#  and returns the largest of the three. Do this without using the Python max() function!
# The goal of this exercise is to think about some internals that Python
#  normally takes care of for us. All you need is some variables and if statements!
# http://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html
num_1 = int(input("enter ur first num: "))
num_2 = int(input("enter ur second num: "))
num_3 = int(input("enter ur third num: "))
if num_1 < num_2:
    bigger_num = num_2
else:
    bigger_num = num_1
if num_3 > bigger_num:
    bigger_num = num_3
print("the biggest number is " + str(bigger_num))
input()