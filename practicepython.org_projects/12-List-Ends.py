# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
#  and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.
# http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
def listchanger():
    user_list1 = []
    print("please enter the members of your first list one by one, \ntype finish when you have entered all the members\n")
    try:
        while True:
            member = int(input("enter a number: "))
            user_list1.append(member)
    except:
        pass
    list2 = [user_list1[0],user_list1[-1]]
    print(list2)
listchanger()

