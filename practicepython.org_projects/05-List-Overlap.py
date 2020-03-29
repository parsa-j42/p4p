# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only
#  the elements that are common between the lists (without duplicates).
#  Make sure your program works on two lists of different sizes.
#  http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
from random import randint
#-------------------------inputs--------------------------
user_list1 = []
user_list2 = []
print("please enter the members of your first list one by one, \ntype finish when you have entered all the members\n")
try:
    while True:
        member = int(input("enter a number: "))
        user_list1.append(member)
except:
    pass
print("please enter the members of your second list one by one, \ntype finish when you have entered all the members\n")
try:
    while True:
        member = int(input("enter a number: "))
        user_list2.append(member)
except:
    pass
#---------------------------proccess-----------------------------
overlaped_list = []
for i in user_list1:
    for n in user_list2:
        if n == i:
            if i not in overlaped_list: 
                overlaped_list.append(i)
#--------------------------outputs-------------------------------------
print(overlaped_list)
#=======================extras=========================================
#1:
l = 0
rand_list1 = []
rand_list2 = []
while l < randint(1,100):
    rand_list1.append(randint(1,100))
    l = l+1
l = 0
while l < randint(1,100):
    rand_list2.append(randint(1,100))
    l = l+1
overlaped_list2 = []
for i in rand_list1:
    for n in rand_list2:
        if n == i:
            if i not in overlaped_list2: 
                overlaped_list2.append(i)
print(overlaped_list2)
input()
#2: 
#??????????