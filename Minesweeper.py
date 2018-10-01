#Oct 1
#Although I didn't fully finish the HW, I did have to spend a lot of time thinking about this. The program accepts two command-line arugments
#and saves them. Then it creates a list of 0's with the dimension of the first number entered. Afer this, there is a loop that
#generates two random numbers, finds the 0 in the board with teh coordinates of these two numbers, and replaces them with a *
#the program prints the final result by printing each row "unpackaged" from the brackets


#import random
import random as r
#for command line
import sys as s 


boardSize = int(s.argv[1])
bombs = int(s.argv[2])

#empty list
board = []

#creates list of 0's
board = [[0] * boardSize for _ in range(boardSize)]

#replaces values with bombs
for bombs in board:
	#determines random location
	x = r.randrange(boardSize)
	y = r.randrange(boardSize)
	#replaces
	board[x][y] = "*"

#prints
for r in board:
    print(*row)


