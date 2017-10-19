def euler_36():
    return sum(x for x in range(10**6) if (str(x) == str(x)[::-1]) and (str(bin(x))[2:] == str(bin(x))[2:][::-1]))



