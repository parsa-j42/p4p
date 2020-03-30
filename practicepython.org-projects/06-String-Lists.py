# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
# http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

word = input("enter a word , i\'ll check if it\'s plaindrome or not: ")
reverse = word[::-1]
if reverse == word:
    print("your word is palindrome!!")
else:
    print("your word is NOT palindrome!!")