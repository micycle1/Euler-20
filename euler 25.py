def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    else:
        return fibo(n-1) + fibo(n-2)


print(fibo(17))
i = 0
while not len(str(fibo(i))) == 1000:
    i+=1
