# This exercise is Part 4 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 3.

# In 3 previous exercises, we built up a few components needed to build a Tic Tac Toe game in Python:

# Draw the Tic Tac Toe game board
# Checking whether a game board has a winner
# Handle a player move from user input
# The next step is to put all these three components together to make a two-player Tic Tac Toe game! Your challenge in this exercise is to use the functions from those previous exercises all together in the same program to make a two-player game that you can play with a friend. There are a lot of choices you will have to make when completing this exercise, so you can go as far or as little as you want with it.

# Here are a few things to keep in mind:

# You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
# If there are no more moves left, don’t ask for the next player’s move!
# As a bonus, you can ask the players if they want to play again and keep a running tally of who won more - Player 1 or Player 2.
# http://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html
def board_drawer(player,game_list):
    game_list = ["" if x==0 else "X" if x==2 else "O" if x==1 else x for x in game_list]
    print(game_list)
    print(" ---" * 3)  
    print("| ",game_list[0],"| ",game_list[1],"| ",game_list[2],"|")
    print(" ---" * 3)  
    print("| ",game_list[3],"| ",game_list[4],"| ",game_list[5],"|")
    print(" ---" * 3)  
    print("| ",game_list[6],"| ",game_list[7],"| ",game_list[8],"|")
    print(" ---" * 3)  
#----------------------------------
def move_convertor(player,game_list):
    user_move = input("player %s turn: type ur selection with \" row,column \" format: " % player)
    user_move = user_move.split(",")
    if int(user_move[0]) == 2:
        move = int(user_move[1]) - 1 + 3
    elif int(user_move[0]) == 3:
        move = int(user_move[1]) - 1 + 6 
    else:
        move = int(user_move[1]) - 1
    game_list[move] = int(player)
    board_drawer(p_shape,game_list)
#----------------------------------
def winner_checker(game):
    row_1, row_2, row_3 = game[0], game[1], game[2]
    father_list = game
    x = 0
    status = 0
    while x<6 :
        if father_list[x] == father_list[x+1] == father_list[x+2] :
            status = 1
            winner = father_list[x]
        x = x+3
    x = 0
    if status != 1:
        while x<3 :
            if father_list[x] == father_list[x+3] == father_list[x+6]:
                status = 1
                winner = father_list[x]
            x = x+1
    x = 0
    if status != 1:
        if (father_list[0] == father_list[4] == father_list[8]) or (father_list[2] == father_list[4] == father_list[6]):
            status = 1
            winner = father_list[4]
    if status == 1 and winner != 0:
        print("winner is player %s" % winner)
    else:
        return 0
#----------------------------------

game_list = [0,0,0,0,0,0,0,0,0]
z = 0
print("player 1 in O and player 2 is X")
while winner_checker(game_list) == 0 and 0 in game_list:
    z = z+1
    if z % 2 == 0:
        player = 2
        p_shape = "X"
    else:
        player = 1
        p_shape = "O"
    move_convertor(player,game_list)

input()