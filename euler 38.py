def euler_38():
    return max(int("%s%s" % (i,i*2)) for i in range(1000,9999) if sorted([int(x) for x in str(i)] + [int(x) for x in str(2*i)]) == [1,2,3,4,5,6,7,8,9])



