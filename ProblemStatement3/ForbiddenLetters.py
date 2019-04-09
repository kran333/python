# Write a function named avoids that takes a word and a string of forbidden letters,
# and that returns True if the word doesn’t use any of the forbidden letters.
froLetters = ['a','e','i','o','u']
inputWords = ''
class ForbiddenLetters:
    def verificationMethod(self):
        global froLetters
        global inputWords
        inputWords = input("Enter the Word with the mentioned Letters 'a','e','i','o','u' : ")
        for var in froLetters:
            if var == inputWords:
                return True
            else:
                return False
    @staticmethod
    def callingFunction():
        obj = ForbiddenLetters
        print(obj.verificationMethod(0))
ForbiddenLetters.callingFunction()