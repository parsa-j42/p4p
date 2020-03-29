# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python
# that takes this list a and makes a new list that has only the even elements of this list in it.
# http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
user_list1 = []
evens=[]
print("please enter the members of your first list one by one, \ntype finish when you have entered all the members\n")
try:
    while True:
        member = int(input("enter a number: "))
        user_list1.append(member)
except:
    pass

evens = [num for num in user_list1 if (num % 2) == 0]
print(evens)
input()