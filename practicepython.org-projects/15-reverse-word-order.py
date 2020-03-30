# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string:
# My name is Michele
# Then I would see the string:
# Michele is name My
# shown back to me.
# http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
def sent_reverser():
    user_sent = input("write a sentence and press enter: ")
    listed_sent = user_sent.split()
    listed_sent = listed_sent[::-1]
    reversed_sent = " ".join(listed_sent)
    print(reversed_sent)
sent_reverser()
input()