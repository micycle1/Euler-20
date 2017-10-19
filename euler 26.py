import decimal,re
decimal.getcontext().prec = 1000

def longestrepeating(strg):
    regex = re.compile(r"(?=(.+)\1)")
    matches = regex.findall(strg)
    if matches:
        return int(len(max(matches, key=len)))
maxi = 0
for n in range(1,1001):
    print(longestrepeating(str(decimal.Decimal(1)/decimal.Decimal(n))),n)

