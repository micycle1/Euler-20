def euler_29():
    return len(set([a ** b for a in range(2, 101) for b in range(100)]))
