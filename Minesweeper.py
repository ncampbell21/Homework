#Oct 12
#This is my code for the Minesweeper project. The output is similar to that of Minesweeper. The program takes two argumemts, one being the l and w 
#of the board, and the other being the number of bombs the user wants on the board. A border of 1's is added around the board.
#After this, the board is populated with x bombs placed randomly. Then the function options() is called, which gives the user the option
#to either flag or reveal. If reveal is chosen, the program reveals the spot chosen, and the surrounding numbers if it's a zero. If it's a bomb, 
#game over. If flag is chosen, the given space is flagged. When spaces are revealed, the program checks to see if the # of flags + unrevealed
#spaces is equal to the number of bombs, in which case the user has won.
#Ascii art: https://www.asciiart.eu/, http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
# On my honor, I have neither given nor recieved unauthorized aide. 


import random as r
#for command line
import sys as s 

#store arguments
boardSize = int(s.argv[1])+2
bombs = int(s.argv[2])

flagz = 0
#empty list
board = []

#creates list of 0's
board = [[0] * (boardSize) for size in range(boardSize)]
#gameboard is list of X's
gameboard = [['X'] * (boardSize) for size in range(boardSize)]


#replaces values with bombs
for a in range(bombs):
	#determines random location
	x = r.randrange(1,boardSize-1)
	y = r.randrange(1,boardSize-1)
	#replaces
	board[x][y] = "*"
	for vert in range(-1,2):
		for horiz in range(-1,2):
			if board[x+vert][y+horiz] != "*":
				board[x+vert][y+horiz] +=1

#creates border in the gameboard
gameboard[0] = [1]*boardSize
gameboard[-1] = [1]*boardSize
for j in gameboard:
	j[0] = 1
	j[-1] = 1

#puts same border in solution board
board[0] = [1]*boardSize
board[-1] = [1]*boardSize
for j in board:
	j[0] = 1
	j[-1] = 1
	
# dividing line
print("\n"*40)

#prints gameboard
for row in gameboard:
	print(*row)


#nice formatting stuff
def prettylines():
	print("\n"*15)
	print("-"*120)
	print("\n"*10)

#checks for win
def checkforwin(gameboard,board):
	#numbers of bombs in solution
	bombz = sum(x.count('*') for x in board)
	#number of flags in game board
	flagz = sum(x.count('F') for x in gameboard)
	#number of unrevealed spots in game board
	unrevealed = sum(x.count('X') for x in gameboard)
	#if flags + unrevealed is same as bombs
	if flagz + unrevealed == bombz:
		print('''

                                                                                                                                          
                                                                                                                                          
			YYYYYYY       YYYYYYY                                     WWWWWWWW                           WWWWWWWW                                 !!! 
			Y:::::Y       Y:::::Y                                     W::::::W                           W::::::W                                !!:!!
			Y:::::Y       Y:::::Y                                     W::::::W                           W::::::W                                !:::!
			Y::::::Y     Y::::::Y                                     W::::::W                           W::::::W                                !:::!
			YYY:::::Y   Y:::::YYYooooooooooo   uuuuuu    uuuuuu        W:::::W           WWWWW           W:::::W ooooooooooo   nnnn  nnnnnnnn    !:::!
			   Y:::::Y Y:::::Y oo:::::::::::oo u::::u    u::::u         W:::::W         W:::::W         W:::::Woo:::::::::::oo n:::nn::::::::nn  !:::!
			    Y:::::Y:::::Y o:::::::::::::::ou::::u    u::::u          W:::::W       W:::::::W       W:::::Wo:::::::::::::::on::::::::::::::nn !:::!
			     Y:::::::::Y  o:::::ooooo:::::ou::::u    u::::u           W:::::W     W:::::::::W     W:::::W o:::::ooooo:::::onn:::::::::::::::n!:::!
			      Y:::::::Y   o::::o     o::::ou::::u    u::::u            W:::::W   W:::::W:::::W   W:::::W  o::::o     o::::o  n:::::nnnn:::::n!:::!
			       Y:::::Y    o::::o     o::::ou::::u    u::::u             W:::::W W:::::W W:::::W W:::::W   o::::o     o::::o  n::::n    n::::n!:::!
			       Y:::::Y    o::::o     o::::ou::::u    u::::u              W:::::W:::::W   W:::::W:::::W    o::::o     o::::o  n::::n    n::::n!!:!!
			       Y:::::Y    o::::o     o::::ou:::::uuuu:::::u               W:::::::::W     W:::::::::W     o::::o     o::::o  n::::n    n::::n !!! 
			       Y:::::Y    o:::::ooooo:::::ou:::::::::::::::uu              W:::::::W       W:::::::W      o:::::ooooo:::::o  n::::n    n::::n     
			    YYYY:::::YYYY o:::::::::::::::o u:::::::::::::::u               W:::::W         W:::::W       o:::::::::::::::o  n::::n    n::::n !!! 
			    Y:::::::::::Y  oo:::::::::::oo   uu::::::::uu:::u                W:::W           W:::W         oo:::::::::::oo   n::::n    n::::n!!:!!
			    YYYYYYYYYYYYY    ooooooooooo       uuuuuuuu  uuuu                 WWW             WWW            ooooooooooo     nnnnnn    nnnnnn !!! 
			                                                                                                                                          
			                                                                                                                                          
                                                                                                                                          
                                                                                                                                          
                                                                                                                                          
                                                                                                                                          
                                                                                                                                          

			''')
		quit()
	else:
		#go back
		options()

#if selected bomb
def dead():
	print('''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
									Oof. You hit a bomb!\n\n\n\n\n''')
	print('''
									       . . .                         
									              \|/                          
									            `--+--'                        
									              /|\                          
									             ' | '                         
									               |                           
									               |                           
									           ,--'#`--.                       
									           |#######|                       
									        _.-'#######`-._                    
									     ,-'###############`-.                 
									   ,'#####################`,               
									  /#########################\              
									 |###########################|             
									|#############################|            
									|#############################|            
									|#############################|            
									|#############################|            
									 |###########################|             
									  \#########################/              
									   `.#####################,'               
									     `._###############_,'                 
									        `--..#####..--'



									        GAME OVER :(


		''')
	quit()

#if wants to flag
def flag(revealY,revealX):
	#sets spot to F
	gameboard[revealY][revealX] = "F"
	prettylines()
	#reprints
	for row in gameboard:
		print(*row)
	#check for win
	checkforwin(gameboard, board)

#choose reveal / flag
def options():
	#try this:
	try:
		#asks for input
		action = input("\n\nEnter 'x coordinate' *space* 'y coordinate' to reveal a space.\n\nTo flag a space, enter 'x coordinate' *space* 'y coordinate' *space* 'flag'.\n\n")
		#stores input in list
		action = action.split(" ")
		revealX = int(action[0])
		revealY = int(action[1])
		#if last item = flag
		if action[-1] == "flag":
			#flag function
			flag(revealY,revealX)
		#reveal
		else:
			#tries to reveal bomb
			if board[revealY][revealX] == "*":
				gameboard[revealY][revealX] = board[revealY][revealX]
				dead()
			#tries to revewal number
			elif board[revealY][revealX] != 0 and board[revealY][revealX] != "*":
				gameboard[revealY][revealX] = board[revealY][revealX]
				#reprint
				prettylines()
				for row in gameboard:
					print(*row)
					#win?
				checkforwin(gameboard, board)
				#didn't win --> ask for more input
				options()
			#revealed 0
			else:
				ifZero(revealY, revealX)
	#input invalid stuff
	except ValueError:
		prettylines()
		print("you didn't enter a valid input! Please follow the directions and enter again.")
		prettylines()
		options()

#if tried to reveal 0
def ifZero(revealY, revealX):
	#empty list
	toReveal = []
	#append coords
	toReveal.append([revealY, revealX])
	#while list has stuff
	while len(toReveal)>0: 
		#take out values
		temp = toReveal.pop(0)
		#store values in rx and ry
		rx, ry = temp[0], temp[1]
		#check all around
		for vert in range(-1,2):
			for horiz in range(-1,2):
				#if a spot is a 0 in solution board and not in gameboard
				if board[rx+horiz][ry+vert] == 0 and gameboard[rx+horiz][ry+vert] != 0:
					#append values to the reveal list to be revealed later
					toReveal.append([rx+horiz,ry+vert])
				#set other values equal
				gameboard[rx+horiz][ry+vert] = board[rx+horiz][ry+vert]

	#lines
	prettylines()
	#reprint
	for row in gameboard:
		print(*row)	
	#check for win
	checkforwin(gameboard, board)

#calls options
options()









