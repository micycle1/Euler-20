def euler_3():
    return max((prime) for prime in set([i for i in range(1, 10000) if all([(i % j) for j in range(2, int(i ** 0.5) + 1)]) and i > 1]) if (600851475143 / prime).is_integer())
