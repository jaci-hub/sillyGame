import random #to help the computer play a random word, when it has to start a new word
import helperFunctions

def computerNextChar(buildingWord):
    if len(buildingWord)==0:
        return random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 
    else:
        allWords=open("C:\\Users\\Jacin\\OneDrive\\Documents\\Programming\\jaciProject\\sillyGame\\allEnglishWords.txt")
        # go through all words in the dictionary
        for myword in allWords:
            if len(myword)>len(buildingWord):
                count=0
                #remove the new line char at the end of myword
                myword=myword.replace("\n", "")
                # check if the word in the dictionary starts the same as the word being built
                for i in range(0, len(buildingWord)):
                    if myword[i].upper()==buildingWord[i]:
                        count+=1
                # if the words starts the same and it hasnt been played yet
                if count==len(buildingWord) and helperFunctions.wordIsNew(myword.upper())==True:
                    if len(myword)==len(buildingWord):
                        allWords.close()
                        return '.', myword.upper()
                    else:
                        allWords.close()
                        return myword[len(buildingWord)].upper(), myword.upper()
        allWords.close()
        return '?', 
     
if __name__=='__main__':
    buildingWord=str(input('* Enter a letter or word: ')).upper()
    while buildingWord.isalpha()!=True:
        buildingWord=str(input('* Enter a letter or word: ')).upper()
    print(computerNextChar(buildingWord))