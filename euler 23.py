import math

def euler_23():
    abundant_numbers = [i for i in range(20162) if factor(i) > i]
    numbers = set([(i) for i in range(20162)])

    for x in range(len(abundant_numbers)):
        for y in range(x,len(abundant_numbers)):
            if abundant_numbers[x] + abundant_numbers[y] in numbers:
                numbers.remove(abundant_numbers[x]+abundant_numbers[y])

    return sum(numbers)

def factor(n):
    factors1 = []
    factors2 = []
    for i in range(1,math.ceil(n ** 0.5)+1):
        if (n/i).is_integer():
            if not (n/i) in factors1:
                factors1.append(i)

    for item in factors1:
        if not int(n/item) in factors1:
            factors2.append(int(n/item))
        
    factors2.reverse()
    
    factors1 += factors2[:-1]
    return(sum(factors1))



