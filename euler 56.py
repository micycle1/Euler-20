def euler_56():
    return max((sum(list(map(int, str(a ** b))))) for a in range(100) for b in range(100))
