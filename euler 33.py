for y in range(1, 99):  # bottom
    for x in range(1, y):  # top
        if len(str(x)) == 2 and len(str(y)) == 2:
            if x / y == int(str(x)[-2]) / int(str(y)[-2]) and not str(y)[1] is "0" and not  str(y)[1] == str(y)[0]:
                print(x, y)
