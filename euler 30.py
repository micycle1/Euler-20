def euler_30():
    return sum(i for i in range(2, 200000) if sum((int(letter) ** 5) for letter in str(i)) == i)
