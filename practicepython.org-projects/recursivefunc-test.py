def sumer(n,k):
    k = k+n
    if n == 1:
        print(k)
    else:
        return sumer(n-1,k)
x = int(input())
sumer(x,0)
input()