stringList = []
strName= ""
class lengthMethod:
    def getString(self):
        print("Enter the String :")
        name = str(input())
        return name
    def displayMethod(self):
        strName = obj.getString()
        strLen = len(strName)
        for i in strName:
            ind = strName.index(i)
            if ind == strLen-1:
                for x in range(0,10):
                    stringList.append("")
                stringList.append(i)
            else:
                stringList.append(i)
        print(stringList)
obj = lengthMethod()
obj.displayMethod()