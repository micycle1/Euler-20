def euler25():
    fibo = [1, 1]
    
    while not len(str(fibo[-1])) == 1000:
        fibo.append(fibo[-1] + fibo[-2]) 
        
    return len(fibo)