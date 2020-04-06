def array_sum(array):
    if len(array) != 0:
        return array[0] + array_sum(array[1:])
x = [1,5,2,100,3]
print(array_sum(x))
input()