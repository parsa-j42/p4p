def fib(num):
    x = 0
    print("start fib ", num)
    #fib(3) = fib(2) + fib(1)
    #fib(4) = fib(3) + fib(2)
    #fib(n) = fib(n-1) + fib(n-2)
    if num == 1 or num == 2:
        x = 1
    else:
        #print("start fib", num,"||",num-1)
        x1 = fib(num-1)
        #print("start fib", num,"||",num-2)
        x2 = fib(num-2)
        x = x1 + x2
    print("finish fib ", num)
    return x

print(fib(5))
