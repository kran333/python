# The built-in function eval takes a string and evaluates it using the Python interpreter. For example:
# >>> eval('1 + 2 * 3')
# 7
# >>> import math
# >>> eval('math.sqrt(5)')
# 2.2360679774997898
# >>> eval('type(math.pi)')
# <type 'float'>
# Write a function called eval_loop that iteratively prompts the user, takes the resulting input and evaluates it using eval,
# and prints the result. It should continue until the user enters 'done',
# and then return the value of the last expression it evaluated.
def eval_loop():
    inval = input("Enter the string :")
    if inval == 'done':
       print("Exit")
    else:
        print(eval(inval))
        eval_loop()

eval_loop()