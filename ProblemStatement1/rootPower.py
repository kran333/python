import math
root = 0
pwd = 0
userInput = 0
failCount = 0
sucessCount = 0
class rootPower:
    def getValues(self):
        global userInput
        userInput = int(input("Enter the Number : "))
    def operations(self):
        global root
        global pwd
        global userInput
        global failCount
        global sucessCount
        object.getValues()
        for x in range(2,6):
            res = int(math.pow(userInput,1/x))
            # print(res)
            if math.pow(res,x) == userInput:
                print("Root number :",res,"Power Number :",x)
                sucessCount = sucessCount + 1
                object.operations()
                # break
            else:
               failCount = failCount + 1
        if failCount != 0 and sucessCount == 0:
            print("Not perfect Number")
            object.operations()

object = rootPower()
object.operations()