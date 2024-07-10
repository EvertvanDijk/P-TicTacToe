#import os
from os import system, name
from random import randint
import numpy as np

# cls() to work on win and 'nix platforms
def cls():
    lambda: system('cls' if name =='nt' else 'clear')


# enter initial values for board
board_layout = [" "," "," "," "," "," "," "," "," "]
winner = ""


def draw_board(a,b,c,d,e,f,g,h,i):
# create the board according to values presented.
    cls()
    print("---- ---- ---")
    print("| "+a+" | "+b+" | "+c+" |")
    print("---- ---- ---")
    print("| "+d+" | "+e+" | "+f+" |")
    print("---- ---- ---")
    print("| "+g+" | "+h+" | "+i+" |")
    print("---- ---- ---")

#def test_for_win
def check_for_win(player, position):
    if position == "-1":
        cls()
        print("Thanks for playing, bye")
        exit()
    if board_layout[int(position)-1] == " ":
        board_layout[int(position)-1] = player
    draw_board(board_layout[0], board_layout[1], board_layout[2], board_layout[3], board_layout[4], board_layout[5], board_layout[6], board_layout[7], board_layout[8])

# Test all possible winning combinations

# lots of if else statements here, use numpy
    #
    # #

#print("last turn by "+player)
    if player == "X":
        computers_turn()
    else:
        play_the_game()

#computers turn
def computers_turn():
    x = randint (1,9)
    #print(x)
    check_for_win("O", x)


#play the game
def play_the_game():
    x = input("Choose a position: ")
    check_for_win("X", x)
    
draw_board(" "," "," "," "," "," "," "," "," ")

while winner != "winner" :
    x = input("Choose a position: ")
    check_for_win("X", x)
    #play_the_game(x)
