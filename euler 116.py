import math

def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)

s = 0
tiles = 50

for length in [2, 3, 4]:
    i = 1
    while tiles - (length * i) > 0:
        s += nCr(tiles - (length * i) + i, i)
        i += 1

print(int(s) + 1)


