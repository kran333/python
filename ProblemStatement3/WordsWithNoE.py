# Modify the above program to print only the words that have no “e” and
# compute the percentage of the words in the list have no “e.”
wordsList = []
wordsCount = 0
eLetterCount = 0
normalWordCount = 0
totalWordCount = 0
eWordCountPercent = 0
class WordsWithNoE:
    def get_values(self):
        global wordsList
        global wordsCount
        print("Enter the no.of Words : ")
        wordsCount = int(input())
        print("Enter the Words : ")
        for x in range(wordsCount):
            wordsList.append(str(input()))
        return wordsList
    def word_operation(self):
        global eLetterCount
        global normalWordCount
        global totalWordCount
        global eWordCountPercent
        obj = WordsWithNoE()
        operationList = obj.get_values()
        for word in operationList:
           for letter in word:
               if letter == 'e' or letter == 'E':
                   eLetterCount = eLetterCount + 1
                   break
        eWordCountPercent = (eLetterCount/wordsCount)*100
        return eLetterCount,eWordCountPercent
    @staticmethod
    def callingMethod():
        obj = WordsWithNoE()
        print("The Total No.of 'E' lettered word in the Above list and its %'s are :",obj.word_operation())
WordsWithNoE().callingMethod()