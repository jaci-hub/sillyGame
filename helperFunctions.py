import helperVariables
#check if the word built is new
def wordIsNew(aWord):
    if aWord in helperVariables.listofPlayedWords:
        return False
    else: 
        return True
#function to check if the word exists
def evaluateWord(aWord):
    if wordIsNew(aWord)==False:
        return False
    else: 
        return helperVariables.englishDictionary.check(aWord)
#check scores
def sillyPlayer(allPlayers):
    for i in range(0, len(allPlayers)):
        if len(allPlayers[i].score)==5:
            return True
    return False
#rules of the game
def gameCheckRules(mychar, aWord):
    if mychar!='?' and  mychar!='.' and mychar.isalpha()!=True:
        return False
    elif mychar=='?' and len(aWord)==0:
        return False
    elif mychar=='.' and len(aWord)<2:
        return False
    elif len(mychar)!=1:
        return False
    return mychar
#get the previous player
def previousPlayer(turn):
    if turn==0:
        turn=len(helperVariables.allPlayers)-1
    else:
        turn-=1
    return turn