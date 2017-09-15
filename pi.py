import math

def pi():
    n = int(input("Enter the value for n: "))
    result = 0
    sign = 1
    for denom in range(1, 2*n, 2):
        result = result +sign * 4/denom
        sign = -sign
    print("Approximation of pi is", result)
    print("Difference from pi is", math.pi - result)
    pi()

pi()
    


