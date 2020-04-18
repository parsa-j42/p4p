# As you may have guessed, we are trying to build up to a full tic-tac-toe board. 
# However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe,
#  not worrying about how the moves were made.

# If a game of Tic Tac Toe is represented as a list of lists, like so:

# game = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space, 
# 
# and a 2 means that player 2 put their token in that space.

# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe
#  game board, tell me whether anyone has won, and tell me which player won, if any.
#  A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.
#  Don’t worry about the case where TWO people have won - assume that in every board there 
#will only be one winner.

# Here are some more examples to work with:

# winner_is_2 = [[2, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]

# winner_is_1 = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]

# winner_is_also_1 = [[0, 1, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]

# no_winner = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 2]]

# also_no_winner = [[1, 2, 0], 
# 	[2, 1, 0],
# 	[2, 1, 0]] 0 4 8 , 2 4 6 
# http://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html
def winner_checker(game):
    row_1, row_2, row_3 = game[0], game[1], game[2]
    father_list = game[0] + game[1] + game[2]
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
        print("no winner")
winner_checker([[1, 2, 0],[2, 1, 0],[2, 1, 0]])
input()