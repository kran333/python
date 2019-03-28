s = "1.58,1.36,1.54,1.85,1.654"
list = []
num = []
sum = float(0.0)
class addDecimal:
    def addMethod(self):
        for x in s:
            if x != ",":
                list.append(x)
            else:
                str = ''.join(list)
                num.append(float(str))
                list.clear()
        print(num)
        for x in num:
           global sum
           sum = float(x) + sum
        print("Sum is :",sum)
object = addDecimal()
object.addMethod()