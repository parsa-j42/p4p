# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
#  One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
# (If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes,
#  happy numbers are a real thing in mathematics - you can look it up on Wikipedia. 
#  The explanation is easier with an example,
# which I will describe below.)
# http://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
def overlapper():
    read_primenum_file = open('23-prime-numbers.txt', 'r')
    read_happynum_file = open('23-happy-numbers.txt', 'r')
    current_primenum = read_primenum_file.readline()
    stripped_prime = current_primenum.rstrip("\n")
    current_happynum = read_happynum_file.readline()
    stripped_happy = current_happynum.rstrip("\n")
    overlap_list = []
    while stripped_prime != "997":
        current_primenum = read_primenum_file.readline()
        stripped_prime = current_primenum.rstrip("\n")
        while stripped_happy != "1000" and int(stripped_happy) <= int(stripped_prime):
            if stripped_prime == stripped_happy:
                overlap_list.append(stripped_happy)
                current_primenum = read_primenum_file.readline()
                stripped_prime = current_primenum.rstrip("\n")
                read_happynum_file.seek(0)
            current_happynum = read_happynum_file.readline()
            stripped_happy = current_happynum.rstrip("\n")

        
    print(overlap_list)
overlapper()
input()