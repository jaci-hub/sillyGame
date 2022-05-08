import enchant
englishDictionary=enchant.Dict("en_US")

class Player:
    def __init__(this, name, score):
        this.name = name
        this.score = score

sillyArrayScore=['', 'S', 'I', 'L', 'L', 'Y']
#list to store played words
listofPlayedWords=[]
#list of all players
allPlayers=[]
#check if the word built is new
def wordIsNew(buildingWord):
    if buildingWord in listofPlayedWords:
        return False
    else: 
        return True
#function to chack if the word exists
def evaluateWord(buildingWord):
    if wordIsNew(buildingWord)==False:
        return False
    else: 
        return englishDictionary.check(buildingWord)
#check scores
def sillyPlayer(allPlayers):
    for i in range(0, len(allPlayers)):
        if len(allPlayers[i].score)==5:
            return True
    return False
#rules of the game
def gameCheckRules(mychar, buildingWord):
    if mychar!='?' and  mychar!='.' and  mychar[0].isalpha()!=True:
        return False
    elif mychar=='?' and len(buildingWord)==0:
        return False
    elif mychar=='.' and len(buildingWord)<2:
        return False
    elif len(mychar)!=1:
        return False
    return mychar
#get the previous player
def previousPlayer(turn):
    if turn==0:
        turn=len(allPlayers)-1
    else:
        turn-=1
    return turn
        
def main():
    print('*** SILLY GAME ***')
    #ask user for number of players
    numberOfPlayers=input('* Number of players: ')
    while numberOfPlayers.isdigit()==False or int(numberOfPlayers)<2: #if it is one, play with computer!!!
        numberOfPlayers=input('* Number of players: ')
    #create players
    for i in range(0, int(numberOfPlayers)):
        playerName=str(input('* Player '+str(i+1)+' Name: '))
        myplayer=Player(playerName, sillyArrayScore[0])
        allPlayers.append(myplayer)
    #variable that will store the word being built
    buildingWord=''
    #variable that will guide the turns of the players
    turn=0
    #Game starts
    while(sillyPlayer(allPlayers)==False):
        #display the score board
        print('** Score Board **')
        for i in range(0, len(allPlayers)):
            print(allPlayers[i].name+": "+allPlayers[i].score)
        print('-------------------')
        #Words built
        print('* Words built: '+str(len(listofPlayedWords))+' *')
        print('-------------------')
        #display the Word being built
        print('* Word being built *')
        print(buildingWord)
        print('-------------------')
        turn%=len(allPlayers)
        #type char and check the rules of the game
        mychar=str(input(allPlayers[turn].name+': '))
        while gameCheckRules(mychar, buildingWord)==False:
            print('*Invalid! Type a letter.')
            mychar=str(input(allPlayers[turn].name+': '))
        #the char typed is valid and dont violate the rules of the game
        inputChar=mychar
        if inputChar=='?':
            #the other player completes the word
            restOftheWord=str(input('* '+ allPlayers[previousPlayer(turn)].name+', complete the word: '+buildingWord))
            buildingWord+=restOftheWord.upper()
            if evaluateWord(buildingWord) == True:
                print("good!")
                #player that asked for word, gets a silly letter
                allPlayers[turn].score+=sillyArrayScore[len(allPlayers[turn].score)+1]
                #store word, so it cant be played again!
                listofPlayedWords.append(buildingWord)
                #empty the variable
                buildingWord=''
            else: 
                print("bad!")
                #player that completed word, gets a silly letter
                allPlayers[previousPlayer(turn)].score+=sillyArrayScore[len(allPlayers[previousPlayer(turn)].score)+1]
                #empty the variable
                buildingWord=''
        elif inputChar=='.':
            if evaluateWord(buildingWord) == False:
                print("bad!")
                #player that played, gets a silly letter
                allPlayers[turn].score+=sillyArrayScore[len(allPlayers[turn].score)+1]
                #empty the variable
                buildingWord=''
            else: 
                print("good!")
                #store word, so it cant be played again!
                listofPlayedWords.append(buildingWord)
                #empty the variable
                buildingWord=''
        else: 
            #add char to the word being built
            buildingWord+=inputChar.upper()
            turn+=1
    #display loser
    for i in range(0, int(len(allPlayers))):
        if allPlayers[i].score=='SILLY':
            print('* '+allPlayers[i].name+' has lost! *')
main()