list = []
OddNum = []
class largestOdd:
    def getValues(self):
        # global check
        check = 0
        num = 0
        print("Enter the Values")
        for x in range(0,10):
            list.append(int(input()))
        for x in list:
            if x%2 != 0:
                OddNum.append(int(x))
                check = 1
        if check == 1:
                for i in OddNum:
                    if i > num:
                        num = i
                print("Largest Odd Number is : ", num)
        else:
            print("There is no odd Numbers in the List")
            # break

obj = largestOdd()
obj.getValues()