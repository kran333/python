string = "bbace"
dict = {}
li = list(string)
count = 0
setData = set(li)
sortList = list(setData)
sortList.sort()
print(sortList)
for x in sortList:
    count = li.count(x)
    dict[x] = count
print(dict)
while dict.values() != 0:
    for x,y in dict.items():
        if y > 0:
            print(x,end="")
            dict[x] = y - 1
        else:
            continue
    print()