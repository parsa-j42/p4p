# Given a .txt file that has a list of a bunch of names, 
# count how many of each name there are in the file,
#  and print out the results to the screen. 
# http://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
read_file = open('22-read-from-file.txt', 'r')
current_line = read_file.readline()
dareth = 0
luke = 0
lea = 0
other_names = 0
while current_line:
    if current_line == "Darth\n" or current_line == 'Darth':
        dareth += 1
    elif current_line == "Luke\n" or current_line == "Luke":
        luke += 1
    elif current_line == "Lea\n" or cur"Lea":
        lea += 1
    else:
        other_names += 1
    current_line = read_file.readline()
print("luke = ",str(luke),"\nDareth = ",str(dareth),"\nlea = ",str(lea),"\nothername = ", str(other_names))
input()