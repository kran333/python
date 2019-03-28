string = input("Enter the Name :")
n = int(input("Enter the no.of Times :"))
try:
    f = open("Namefile.xls",'w')
    for x in range(1,n):
        f.write(str(x))
        f.write(". ")
        f.write(string)
        f.write("\n")
finally:
    f.close()