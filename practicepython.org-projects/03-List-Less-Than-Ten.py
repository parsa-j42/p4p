# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# and write a program that prints out all the elements of the list that are less than 10.
# http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

user_list = list(input("enter a list that includes only numbers: "))
for i in user_list:
    if i == (" " or "," or "[" or "]"):
        user_list.remove(i)
for i in range(0, len(user_list)): 
    user_list[i] = int(user_list[i]) 
    if user_list[i] < 10 :
        print(user_list[i])

# Extras:
#1- Instead of printing the elements one by one,
#  make a new list that has all the elements less than 5 from this list in it and print out this new list.
less=[]
user_list = list(input("enter a list that includes only numbers: "))
for i in user_list:
    if i == (" " or "," or "[" or "]"):
        user_list.remove(i)
for i in range(0, len(user_list)): 
    user_list[i] = int(user_list[i]) 
    if user_list[i] < 10 :
        less.append(user_list[i])
    print (less)

#2-Write this in one line of Python.

user_list = list(input("enter a list that includes only numbers: "))
for i in user_list:
    if i == (" " or "," or "[" or "]"):
        user_list.remove(i)
for i in range(0, len(user_list)): 
    user_list[i] = int(user_list[i]) 
    if user_list[i] < 10 :
        print(user_list[i], end = ",")

#3-Ask the user for a number and return a list that contains only elements from 
# the original list a that are smaller than that number given by the user.
less=[]
user_list = list(input("enter a list that includes only numbers: "))
user_check = int(input("enter a number which you want the list members be less than that: "))
for i in user_list:
    if i == (" " or "," or "[" or "]"):
        user_list.remove(i)
for i in range(0, len(user_list)): 
    user_list[i] = int(user_list[i]) 
    if user_list[i] < user_check :
        less.append(user_list[i])
    print (less)
