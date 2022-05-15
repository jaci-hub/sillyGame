import classPlayer
import helperVariables
import helperFunctions

def gameWithPlayers(numberOfPlayers):
    #create players
    for i in range(0, int(numberOfPlayers)):
        playerName=str(input('* Player '+str(i+1)+' Name: '))
        myplayer=classPlayer.Player(playerName, helperVariables.sillyArrayScore[0])
        helperVariables.allPlayers.append(myplayer)
    #variable that will store the word being built
    buildingWord=''
    #variable that will guide the turns of the players
    turn=0
    #Game starts
    while(helperFunctions.sillyPlayer(helperVariables.allPlayers)==False):
        #display the score board
        print('** Score Board **')
        for i in range(0, len(helperVariables.allPlayers)):
            print(helperVariables.allPlayers[i].name+": "+helperVariables.allPlayers[i].score)
        print('-------------------')
        #Words built
        print('* Words built: '+str(len(helperVariables.listofPlayedWords))+' *')
        print('-------------------')
        #display the Word being built
        print('* Word being built *')
        print(buildingWord)
        print('-------------------')
        turn%=len(helperVariables.allPlayers)
        #type char and check the rules of the game
        mychar=str(input(helperVariables.allPlayers[turn].name+': '))
        while helperFunctions.gameCheckRules(mychar, buildingWord)==False:
            print('* Invalid!')
            mychar=str(input(helperVariables.allPlayers[turn].name+': '))
        #the char typed is valid and dont violate the rules of the game
        inputChar=mychar
        if inputChar=='?':
            #the other player completes the word
            print('* '+ helperVariables.allPlayers[helperFunctions.previousPlayer(turn)].name+', complete the word *')
            restOftheWord=str(input(buildingWord))
            buildingWord+=restOftheWord.upper()
            if helperFunctions.evaluateWord(buildingWord) == True:
                print("* Valid!")
                #player that asked for word, gets a silly letter
                helperVariables.allPlayers[turn].score+=helperVariables.sillyArrayScore[len(helperVariables.allPlayers[turn].score)+1]
                #store word, so it cant be played again!
                helperVariables.listofPlayedWords.append(buildingWord)
                #empty the variable
                buildingWord=''
            else: 
                print("* Invalid!")
                #player that completed word, gets a silly letter
                helperVariables.allPlayers[helperFunctions.previousPlayer(turn)].score+=helperVariables.sillyArrayScore[len(helperVariables.allPlayers[helperFunctions.previousPlayer(turn)].score)+1]
                #empty the variable
                buildingWord=''
        elif inputChar=='.':
            if helperFunctions.evaluateWord(buildingWord) == False:
                print("* Invalid!")
                #player that played, gets a silly letter
                helperVariables.allPlayers[turn].score+=helperVariables.sillyArrayScore[len(helperVariables.allPlayers[turn].score)+1]
                #empty the variable
                buildingWord=''
            else: 
                print("* Valid!")
                #store word, so it cant be played again!
                helperVariables.listofPlayedWords.append(buildingWord)
                #empty the variable
                buildingWord=''
        else: 
            #add char to the word being built
            buildingWord+=inputChar.upper()
            turn+=1
if __name__=='__main__':
    #ask user for number of players
    numberOfPlayers=input('* Number of players: ')
    while numberOfPlayers.isdigit()==False or int(numberOfPlayers)<1:
        numberOfPlayers=input('* Number of players: ')
    gameWithPlayers(numberOfPlayers)