import itertools

def euler_41():
    return max(int("".join(i)) for i in itertools.permutations("1234567") if not (any(int("".join(i)) % x == 0 for x in range(2, int(int("".join(i)) ** 0.5) + 1))))
