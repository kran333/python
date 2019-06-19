# Observe the following function definitions. They Calculate the Factorial as per the Mathematical definition
# 1! = 1 (n + 1)! = (n + 1) * n! Implement factI(n) as an Iterative Implementation & factR(n) as a Recursive Implementation
# def factI(n):
#     """Assumes that n is an int > 0
#     Returns n!
#     Uses Iterative Implementation"""

# def factR(n):
#     """Assumes that n is an int > 0
#     Returns n!
#     Uses Recursive Implementation"""
num = int(input("Enter the Number : "))
def factorialNum(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorialNum(n-1)
print(factorialNum(num))