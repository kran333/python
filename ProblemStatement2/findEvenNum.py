# Implement a function that satisfies the specification. Use a try-except block.
# def findAnEven(l):
# 	"""Assumes l is a list of integers
# 	Returns the first even number in l
# 	Raises ValueError if l does not contain an even number"""
list = [10,15,13,14,17,19,20,22]
evenList = []
oddList = []
def findAnEven(li):
    global evenList
    for i in li:
        if i%2 == 0:
            evenList.append(i)
        else:
            oddList.append(i)
    print(evenList)

findAnEven(list)