# A number, a, is a power of b if it is divisible by b and a/b is a power of b.
# Write a function called is_power that takes parameters a and b and returns True if a is a power of b.
# Note: you will have to think about the base case.
import math
x = int(input("Enter the 'a' value : "))
y = int(input("Enter the 'b' value : "))
def is_power(a,b):
    value = math.pow(a,b)
    value2 = math.pow(b, a / b)
    if value%b == 0 and value2%b == 0:
        return True
    else:
        return False

print(is_power(x,y))