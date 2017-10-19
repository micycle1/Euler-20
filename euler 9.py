def euler_9():
    ab = list(((1000*(a-500)) / (a-1000)) for a in range(1,500) if ((1000*(a-500)) / (a-1000)).is_integer())
    return ab[0]*ab[1]*(1000-sum(ab))
