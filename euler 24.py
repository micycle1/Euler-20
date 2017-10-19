import itertools

def euler_24():
    i = 1
    for p in itertools.permutations("0123456789"):
        if i == 10 ** 6:
            return int("".join(str(x) for x in p))
        i += 1
