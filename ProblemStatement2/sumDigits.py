# Implement a function that meets the specification below. Use a try-except block.
# def sumDigits(s):
#     """Assumes s is a string
#     Returns the sum of the decimal digits in s
#     For example, if s is 'a2b3c' it returns 5"""
String = input("Enter the String : ")
num = []
sum = 0
def sumDigits(s):
    global sum
    char = list(s)
    for i in char:
        try:
            num.append(int(i))
        except Exception as e:
           pass
    print("Numbers in the above string are : ",num)
    for x in num:
        sum = int(sum) + int(x)
    print("Total sum of the digits are : ",sum)

sumDigits(String)