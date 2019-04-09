# Write a function called rotate_word() that takes a string and an integer as parameters,
# and that returns a new string that contains the letters from the original string "rotated" by the given amount.
# For example, "cheer" rotated by 7 is "jolly" and "melon" rotated by -10 is "cubed".
# You might want to use the built-in functions ord,
# which converts a character to a numeric code, and chr, which converts numeric codes to characters.
class rotateWordPro:
    def rotateMethod(self,word,rotation):
        li = list(str(word))
        outputString = ''
        for x in li:
            outputString = outputString +chr(ord(x)+rotation)
        print("The Output String is : ",outputString)
    def getData(self):
        word = str(input("Enter the String : "))
        amt = int(input("Enter the Amount of Rotation : "))
        obj = rotateWordPro()
        obj.rotateMethod(word,amt)
rotateWordPro.getData(0)