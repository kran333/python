# The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.
# One way to find the GCD of two numbers is based on the observation that if r is the remainder when a is divided by b,
# then gcd(a, b) = gcd(b, r). As a base case, we can use gcd(a, 0) = a.
# Write a function called gcd that takes parameters a and b and returns their greatest common divisor.

#------------Method1-------------
# import math
# print(math.gcd(60,42))

#------------Method2--------------
small = 0
num = []
def gcdMethod(x,y):
    if x < y:
        if x == 0:
            return y
        small = x
    else:
        if y == 0:
            return x
        small = y
    try:
        for i in range(1,small):
            if x%i == 0 and y%i == 0:
                num.append(i)
    except Exception as e:
        print(e)
    return num
print("the list of factors are : ",gcdMethod(56,8))