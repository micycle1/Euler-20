import math

def euler_21():
    return sum(list(i for i in range(10000) if i == factor(factor(i)) and not i == factor(i)))

def factor(n):
    factors1 = []
    factors2 = []
    for i in range(1, math.ceil(n ** 0.5) + 1):
        if (n / i).is_integer():
            factors1.append(i)

    for item in factors1:
        factors2.append(int(n / item))
        
    factors2.reverse()
    
    factors1 += factors2[:-1]
    return(sum(factors1))



