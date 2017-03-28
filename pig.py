'''
Author: Ian O'Heir
Date: 2/16/2017
Description:
Play's the game pig
'''

# Imports
import math
import sys
import random
def print_scores(player1,player1Score,player2,player2Score):
    '''
    This function prints the scores
    
    Parameters:
    player1:first player's name
    player1Score: first player's score
    player2:second player's name
    player2Score: second player's score
    
    
    Returns: none
    '''
    print("")
    print("--- SCORES\t"+player1+": "+str(player1Score)+"\t"+player2+":",player2Score,"---")
        
def check_for_winner(player,score):
    '''
    This function checks for a winner
    
    Parameters:
    player:The name of a player
    score: the player's score
    
    
    Returns: True or False
    '''
    if (score>=50):
        print("THE WINNER IS: "+player+"!!!!!");
        return True;
    else:
        return False;
        
def roll_again(player):
    '''
    This function checks to see if a player wants to roll again
    
    Parameters:
    player:The name of a player
    
    
    Returns: True or False
    '''
    answer="Y"
    while(answer=="Y" or answer=="y"):
        answer=input("Roll again, "+ player+"? (Y/N) ")
        if(not(answer=="Y") and not(answer=="y") and not(answer=="N") and not(answer=="n")):
            print("I don't understand: \""+answer+"\". Please enter either \"Y\" or \"N\".")
            answer="Y"
        else:
            break
    if (answer=="Y" or answer=="y"):
        return True
    else:
        return False
    
def play_turn(player):
    '''
    This function executes the players turn until they roll a 1 or choose to stop
    
    Parameters:
    player:The name of a player
    
    
    Returns: The function pointsThisTurn, which tells how many points were got this turn
    '''
    print("---------- "+player+"'s turn ----------")
    pointsThisTurn=0
    roll=0
    while(not (roll==1)):
        roll=random.randint(1,6)
        print("\t<<<",player,"rolls a",roll,">>>")
        if (roll==1):
            print("\t!!! PIG! No points earned, sorry "+player+" !!!")
            pointsThisTurn=0
            try:
                input("(enter to continue)")
            except(EOFError):
                break
        else:
            pointsThisTurn+=roll
            print("\tPoints:",pointsThisTurn)
            if(roll_again(player)==False):
               break
                
                
    return pointsThisTurn
        
    

#==========================================================
def main():
    '''
    This function will have two players play a game of pig
    
    
    Returns: none
    '''
    seed=int(input("Enter seed value: "))
    randomSeed=random.seed(seed)
    print("")
    print("")
    print("Pig Dice")
    player1=input("Enter name for player 1: ")
    player2=input("Enter name for player 2: ")
    print("\tHello", player1,"and "+player2+", welcome to Pig Dice!")
    player1Score=0;
    player2Score=0;
    print_scores(player1,player1Score,player2,player2Score)
    didWin=False
    while(didWin==False):
        player1Score+=play_turn(player1)
        print_scores(player1,player1Score,player2,player2Score)
        if(check_for_winner(player1,player1Score)):
            break
        else:
            player2Score+=play_turn(player2)
            print_scores(player1,player1Score,player2,player2Score)
            if(check_for_winner(player2,player2Score)):
                break
            
        
    
        





if __name__ == '__main__':
    main()



