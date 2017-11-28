def euler_63():
    return sum(((len(str(x ** i)) == i) for x in range(1, 10) for i in range(1, 25)))
