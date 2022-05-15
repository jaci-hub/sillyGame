import playWithComputer
import playWithPlayers
import displayWinner
import helperVariables
     
def main():
    #intro notice about the game
    print('*'*15+ ' ABOUT THE GAME '+ '*'*15)
    print('- It is NOT case sensitive')
    print('- Words CANNOT be played twice')
    print('- Accronyms/abbreviations are valid')
    print('   e.g. CEO- Chief Executive Officer')
    print('   e.g. MN- Minnesota')
    print('   e.g. CG- Computer Graphics')
    print('   e.g. AAA- Automobile Association of America')
    print('- Not all words might be recognized!')
    print('   - We are working to improve that.')
    print('*'*45)
    input('* Press "ENTER" to continue...')
    
    print('*** SILLY GAME ***')
    print('1- Play with Computer (MEDIUM LEVEL)') #level medium because the txt file that backs it up doesnt contain all the words, for example, capitals of countries!
    print('2- Multiplayer game')
    print('3- Quit')
    choice=input('* Enter an option above: ')
    while choice.isdigit()==False or int(choice)<1 or int(choice)>3:
        choice=input('* Enter an option above: ')
    
    #Keep the game on till user quits
    while int(choice)!=3:
        #game with computer
        if int(choice)==1:
            playWithComputer.gameWithMediumLevelComputer()
            #display loser
            displayWinner.gameWinner()
        elif int(choice)==2:
            #ask user for number of players
            numberOfPlayers=input('* Number of players (5 max): ')
            while numberOfPlayers.isdigit()==False or int(numberOfPlayers)<2 or int(numberOfPlayers)>5:
                print('* Invalid!')
                numberOfPlayers=input('* Number of players (5 max): ')
            #game with players
            playWithPlayers.gameWithPlayers(numberOfPlayers)
            #display loser
            displayWinner.gameWinner()
        
        print('-'*20) #leave a line between winner display and new menu
        
        #reinitialize variables
        helperVariables.listofPlayedWords=[]
        helperVariables.allPlayers=[]
        
        #repeat the menu
        print('*** SILLY GAME ***')
        print('1- Play with Computer (MEDIUM LEVEL)') #level medium because the txt file that backs it up doesnt contain all the words, for example, capitals of countries!
        print('2- Multiplayer game')
        print('3- Quit')
        choice=input('* Enter an option above: ')
        while choice.isdigit()==False or int(choice)<1 or int(choice)>3:
            choice=input('* Enter an option above: ')
    print('* Bye!')
main()