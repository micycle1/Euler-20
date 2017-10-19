def euler_4():
    return max( (a*b,a,b)  for a in range(1000) for b in range(1000) if str(a*b) == str(a*b)[::-1])
