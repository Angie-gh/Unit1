# >>>>>>>>>> imports <<<<<<<<<<<
import random
import getpass
import time

# >>>>>>>>>> ai player <<<<<<<<<<<
ai_input = ['rock', 'paper', 'scissors']
# >>>>>>>>>> Options for one or two players <<<<<<<<<<<
possiblePlayers = ['1','2']

# >>>>>>>>>> Response variables <<<<<<<<<<<
playerPrompt = "Input one of the following: rock, paper, scissors: "
invalidEntry = "Sorry, you typed an invalid entry. "
retryPrompt = "Please input your choice again: "
p1win = '\nCongratulations Player1, you won!'
p2win = '\nCongratulations Player2, you won!'
p2Artificalwin = '\nSorry, Player2 won.'

# >>>>>>>>>> Flag to replay the game <<<<<<<<<<<
continueGame = True

# >>>>>>>>>> Continue the game until the user indicates they want to exit <<<<<<<<<<<<
while continueGame:

# >>>>>>>>>> Player-related variables <<<<<<<<<<<
    p1 = True
    p2 = True
    count1 = True

    print('\nTime to play R-O-S-H-A-M-B-O!!!!')

    
    # >>>>>>>>>> Determining if Player 1 will play against the system or with another player <<<<<<<<<<
    playerCount = input("\nHow many players? [1 or 2]: ")

    if playerCount in possiblePlayers:
        count1 = False

    while count1:
        if playerCount not in possiblePlayers:
            print(invalidEntry)
            playerCount = input(retryPrompt)
            if playerCount in possiblePlayers:
                count1 = False

    # >>>>>>>>>> Player 1 <<<<<<<<<<<
    player1 = getpass.getpass(prompt = "\nPlayer 1 - " + playerPrompt)
    # >>>>>>>>>> Making sure that all letters are in lowercase before comparing to the above ai_input list <<<<<<<<<<<
    player1 = player1.lower()
    if player1 in ai_input:
        p1 = False

    while p1:
        if player1 not in ai_input:
            print(invalidEntry)
            player1 = getpass.getpass(prompt = retryPrompt)
            player1 = player1.lower()
            if player1 in ai_input:
                p1 = False

    if playerCount == '1':
        #>>>>>>>>>> The system will randomly choose an entry from the list <<<<<<<<<<< 
        player2  = random.choice(ai_input) 
    else:
        # >>>>>>>>>> Player 2 will be prompted for their input <<<<<<<<<<<
        player2 = getpass.getpass(prompt = "\nPlayer 2 - " + playerPrompt)
        # >>>>>>>>>> Making sure that all letters are in lowercase before comparing to the above ai_input list <<<<<<<<<<<
        player2 = player2.lower()
        if player2 in ai_input:
            p2 = False

        while p2:
            if player2 not in ai_input:
                print(invalidEntry)
                player2 = getpass.getpass(prompt = retryPrompt)
                player2 = player2.lower()
                if player2 in ai_input:
                    p2 = False


    # >>>>>>>>>> Determining the Winner <<<<<<<<<<<
    print ('\nPlayer 1 chose:', player1)
    print ('Player 2 chose:', player2)
    # >>>>>>>>>> Both players chose the same value <<<<<<<<<<<
    if player1 == player2:
        print('\nNo winner, it is a tie :( ')

    elif player1 == ai_input[0] and player2 == ai_input[1]:
        # >>>>>>>>>> Adjust winning response, depending on whether Player2 is a real person or not <<<<<<<<<<
        if playerCount == '1':
             print (p2Artificalwin)
        else:
            print (p2win)

    elif player1 == ai_input[0] and player2 == ai_input[2]:
        print (p1win)

    elif player1 == ai_input[1] and player2 == ai_input[0]:
        print (p1win)

    elif player1 == ai_input[1] and player2 == ai_input[2]:
        # >>>>>>>>>> Adjust winning response, depending on whether Player2 is a real person or not <<<<<<<<<<
        if playerCount == '1':
             print (p2Artificalwin)
        else:
            print (p2win)

    elif player1 == ai_input[2] and player2 == ai_input[0]:
        # >>>>>>>>>> Adjust winning response, depending on whether Player2 is a real person or not <<<<<<<<<<
        if playerCount == '1':
             print (p2Artificalwin)
        else:
            print (p2win)
    
    elif player1 == ai_input[2] and player2 == ai_input[1]:
        print (p1win)
    # >>>>>>>>>> Find out if player(s) want to play again <<<<<<<<<<
    continueyn = input("\nPlay again?: [y/n]: ")
    continueyn = continueyn.lower()
    if continueyn == 'n':
        print ("\n\n")
        print ("              *          ")
        print ("             ***         ")
        print ("            *****          ")
        print ("           *******          ")
        print ("          *********\n          ")
        print ("     Thanks for playing !!!!!\n ")
        print ("          *********          ")
        print ("           *******          ")
        print ("            *****          ")
        print ("             ***         ")
        print ("              *          ")

        time.sleep(5)
        break



