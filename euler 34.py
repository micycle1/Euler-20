import math

def euler_34():
    return sum(n for n in range(3,200000) if n == sum( math.factorial(int(letter)) for letter in str(n)))



