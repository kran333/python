try:
    f1 = open("readFile.txt","w")
    f1.write("Welcome to Kubes World \n")
    f1.write("Hello World \n")
    f1.write("Good Bye \n")
    f1.write("Good Morning")

finally:
    f1.close()


try:
    f2 = open("readFile.txt", "r")
    for x in f2:
        print(x)
finally:
    f2.close()