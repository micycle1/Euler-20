"""https://projecteuler.net/problem=587"""

from math import sqrt, asin, pi
from time import time

sectionArea = (1-pi/4)/4 # full area of L section

def integral(x):
    """indefinite integral of cicles line equation (between 0...0.5 on both axes"""
    return (2*x + sqrt(x - x**2) - (2*x*sqrt(x - x**2)) + asin(sqrt(1 - x)))/4

rightInterval = integral(0.5) # cache right interval here

def xIntercept(n):
    """find the x value at which y=x/n intercepts the circle;
        given n, which is degree of the bounding box;
        asymptotically approaches 0.5"""
    return (-sqrt(2) * n**(3/2) + n**2 + n)/(2* (n**2 + 1))

##def getY(x):
##    """plugs x value into equation of circle line, returning the y value"""
##    return 1/2 - sqrt(-(x-1)*x)   

def calculateSectionRatio(n):
    x = xIntercept(n)
    y = x/n # or getY(x)

    curveArea = rightInterval - integral(x)
    triangleArea = x*y*0.5
    concaveArea = curveArea + triangleArea # orange area
    return concaveArea/sectionArea # orange area as proportion of blue area

def calculateSectionRatioOptimised(n):
    x = xIntercept(n)
    curveArea = rightInterval - integral(x)
    triangleArea = x**2/(n*2)
    concaveArea = curveArea + triangleArea # orange area
    return concaveArea/sectionArea # orange area as proportion of blue area

start = time()
targetRatio = 0.00001
n = 1
inc = 1
while calculateSectionRatioOptimised(n) > targetRatio:
    n+=inc
    inc+=1

n-=inc
while calculateSectionRatioOptimised(n) > targetRatio:
    n+=1
print(n, time()-start, 'secs')
