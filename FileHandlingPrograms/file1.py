import re
space = re.compile(r"\s+")
inputFile = open("sample2.txt","r")
outputFile = open("csv.txt","w")
list = []
while (True):
        record = inputFile.read(16)
        if not record: break
        print(record)
        temp = record
        list.append(temp.split(" "))
        values = space.split(record)
        outputFile.write('"'+','.join(values)+'"\n')
outputFile.close()