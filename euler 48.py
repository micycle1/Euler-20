def euler_48():
    return int(str(sum((i ** i) for i in range(1000)) - 1)[-10:])
