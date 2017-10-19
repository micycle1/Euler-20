highest = [[0],[0]]

def euler14(N,n,i):
    n = N
    while not n == 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        i += 1

        
    if not N == 1:
        euler14(N - 1,0,0)
    return(N,n,i)

print(euler14(900000,0,0))
