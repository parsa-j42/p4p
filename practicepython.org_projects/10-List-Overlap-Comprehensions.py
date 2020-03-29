# # This week’s exercise is going to be revisiting an old exercise (see Exercise 5), 
# # except require the solution in a different way.
# # Take two lists, say for example these two:
# # 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# # and write a program that returns a list that contains only the elements that are common between the 
# # lists (without duplicates). Make sure your program works on two lists of different sizes. Write this 
# #  using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).
# # practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

user_list1 = []
user_list2 = []
same = []
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
#------------------------------------------------------
for n in user_list1:
    same.extend([member for member in user_list2 if member == n])
print (same)