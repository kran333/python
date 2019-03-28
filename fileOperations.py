# try:
#     f = open("doc.txt",'w')
#     f.write("Hello World...\n")
#     f.write("Welcome to Kubes World\n")
# finally:
#     f.close()
try:
    f = open("doc.txt", 'w')
    for i in range(1,6):
        for j in range(0,i):
            print("*", end = "")
            f.write("*")
        print()
        f.write("\n")
finally:
    f.close()