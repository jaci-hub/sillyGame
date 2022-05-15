import classPlayer
import helperVariables
import helperFunctions
import computersMove

#MEDIUM LEVEL COMPUTER
def gameWithMediumLevelComputer():
    #create player: user
    playerName=str(input('* Player Name: '))
    myplayer=classPlayer.Player(playerName, helperVariables.sillyArrayScore[0])
    helperVariables.allPlayers.append(myplayer)
    #create player: computer
    myplayer=classPlayer.Player('Computer', helperVariables.sillyArrayScore[0])
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
            #the computer completes the word
            buildingWord=computersMove.computerNextChar(buildingWord)[1]
            #when the word is valid or the word is type in full so the computer only needs to add "." 
            if helperFunctions.evaluateWord(buildingWord) == True or computersMove.computerNextChar(buildingWord)[0]=='.': 
                print("* Computer completed: "+ buildingWord)
                #player that asked for word, gets a silly letter
                helperVariables.allPlayers[turn].score+=helperVariables.sillyArrayScore[len(helperVariables.allPlayers[turn].score)+1]
                #store word, so it cant be played again!
                helperVariables.listofPlayedWords.append(buildingWord)
                #empty the variable
                buildingWord=computersMove.computerNextChar('')[0]
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
            #computer adds char
            if computersMove.computerNextChar(buildingWord)[0].isalpha():
                buildingWord+=computersMove.computerNextChar(buildingWord)[0]
                turn+=1
            elif computersMove.computerNextChar(buildingWord)[0]=='?':
                print('* Computer played "?"')
                #the user player completes the word
                restOftheWord=str(input('* '+ helperVariables.allPlayers[helperFunctions.previousPlayer(turn)].name+', complete the word: '+buildingWord))
                buildingWord+=restOftheWord.upper()
                if helperFunctions.evaluateWord(buildingWord) == True:
                    print("* Valid!")
                    #Computer gets a silly letter
                    helperVariables.allPlayers[turn].score+=helperVariables.sillyArrayScore[len(helperVariables.allPlayers[turn].score)+1]
                    #store word, so it cant be played again!
                    helperVariables.listofPlayedWords.append(buildingWord)
                    #computer plays
                    buildingWord=computersMove.computerNextChar('')[0]
                    turn+=1
                else: 
                    print("* Invalid!")
                    #user player gets a silly letter
                    helperVariables.allPlayers[helperFunctions.previousPlayer(turn)].score+=helperVariables.sillyArrayScore[len(helperVariables.allPlayers[helperFunctions.previousPlayer(turn)].score)+1]
                    #computer plays
                    buildingWord=computersMove.computerNextChar('')[0]
                    turn+=1
            elif computersMove.computerNextChar(buildingWord)[0]=='.':
                #store word, so it cant be played again!
                helperVariables.listofPlayedWords.append(buildingWord)
                #empty the variable
                buildingWord=computersMove.computerNextChar('')[0]
                print('* Computer played "."')
                turn+=1

if __name__=='__main__':
    gameWithMediumLevelComputer()