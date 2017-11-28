def euler_5():
    return min((i) for i in range(2520, 300000000, 2520) if all((i % x == 0) for x in [11, 12, 13, 14, 15, 16, 17, 18, 19]))
