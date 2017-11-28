def euler_45():
    return max(2 * h ** 2 - h for h in range(30000) if (1 / 6) * ((48 * h ** 2 - 24 * h + 1) ** 0.5 + 1).is_integer())
