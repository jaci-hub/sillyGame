import helperVariables
def gameWinner():
    #display the score board
    print('** Score Board **')
    for i in range(0, len(helperVariables.allPlayers)):
        print(helperVariables.allPlayers[i].name+": "+helperVariables.allPlayers[i].score)
    print('-------------------')
    for i in range(0, int(len(helperVariables.allPlayers))):
        if helperVariables.allPlayers[i].score!='SILLY':
            print('* '+helperVariables.allPlayers[i].name+' wins! *')