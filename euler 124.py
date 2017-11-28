from numpy import prod

def rad(n):
     factors = set()
     d = 2
     step = 1
     while d * d <= n:
          while n > 1:
               while n % d == 0:
                    factors.add(d)
                    n = n / d
               d += step
               step = 2
     return prod(list(factors))

dico = {}

for i in range(1, 10):
     dico[i] = rad(i)

dico1 = sorted(dico, key=dico.get)

print(dico1)  # [i+1, 10001]
