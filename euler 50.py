def sieve(n):
    if n <= 2:
        return []
    sieve = list(range(3, n, 2))
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [el for el in sieve if el]

def euler_58():
    primes = sieve(1000000)
    primes_sum = [2]

    for i in range(0,len(primes)):
        if primes_sum[-1]+primes[i] < 1000000:
            primes_sum.append(primes_sum[-1]+primes[i])
        else:
            break
        
    primes = set(primes)

    for j in reversed(primes_sum):
        for k in primes_sum:
            if j-k in primes:
                return j-k

