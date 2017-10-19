import math;

def euler_20():
    return sum(int(digit) for digit in str(math.factorial(100)))
