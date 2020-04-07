# Write a function that takes an ordered list of numbers
#  (a list where the elements are in order from smallest to largest) and another number. 
#  The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:

# Use binary search
def element_checker(array,element):
    if(len(array)==1): 
        return 0
    else:
        element_checker(array[1:],element)
        status = element == array[0]
        if status:
            return print(status)
user_list = []
print("please enter the members of your first list one by one, \ntype finish when you have entered all the members\n")
try:
    while True:
        member = int(input("enter a number: "))
        user_list.append(member)
except:
    pass

element_to_find = int(input("enter the number you want to check: "))

element_checker(user_list,element_to_find)
input()
