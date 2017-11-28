def euler_85():
    return min((abs(2000000 - (((x + 1) * (y + 1)) / 2) * ((x * y) / 2))) for x in range(30, 100) for y in range(x, 100))
