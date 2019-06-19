# In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter "e."
# Since "e" is the most common letter in English, that’s not easy to do. In fact,
# it is difficult to construct a solitary thought without using that most common symbol.
# It is slow going at first, but with caution and hours of training you can gradually gain facility.
# All right, I’ll stop now.
# Write a function called has_no_e that returns True if the given word doesn’t have the letter "e" in it.
class NoLetterE:
    global inputstr
    global count
    def __init__(self,inputString):
        global inputstr
        inputstr = inputString
    def has_no_e(self):
        global inputstr
        global count
        count = 0
        strList = list(inputstr)
        for x in strList:
            if str(x) == 'e' or str(x) == 'E':
                count = count + 1
        if count > 0:
            return True
        else:
            return False
    def verifyMethod(self):
        obj = NoLetterE("DEvelopment")
        result = obj.has_no_e()
        if result == True:
            print("Input String has Letter 'E'")
        elif result == False:
            print("Input String DOES NOT Contain letter 'E' or 'e'")
        else:
            print("Inavalid")
NoLetterE.verifyMethod(0)