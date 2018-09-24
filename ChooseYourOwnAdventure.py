#Nico Campbell
#On my honor, I have neither given nor recieved unauthorized aide.
#Sep 24 2018
#Description: This is a simple choose your own adventure style game. It features ascii art and some fun illustrations to make it more engaging, too!
#I wish that this game turned out a bit more in-depth and lasted longer, but I spent a lot of the time focusing on quality over quantity and trying to
#perfect the ascii art and making sure there were absolutely no ways to break this game. I ended up using the try/except thing to display
#a message when someone tries to quit, because I didn't really have any errors pop up every so I made my own... Hope you enjoy! 
#Sources:
#https://www.asciiart.eu/
#http://science.ascii.uk/
#http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20



#import sys
import sys


#define greeting function
def greeting():
	print("\n\n\n\n") #add some lines
	print("=" * 362) #nice dividing line
	print(r'''  

		.----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.   
		| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  
		| |     ______   | || |  ____  ____  | || |     ____     | || |      __      | || |  _________   | || |  _________   | |  
		| |   .' ___  |  | || | |_   ||   _| | || |   .'    `.   | || |     /  \     | || | |  _   _  |  | || | |_   ___  |  | |  
		| |  / .'   \_|  | || |   | |__| |   | || |  /  .--.  \  | || |    / /\ \    | || | |_/ | | \_|  | || |   | |_  \_|  | |  
		| |  | |         | || |   |  __  |   | || |  | |    | |  | || |   / ____ \   | || |     | |      | || |   |  _|  _   | |  
		| |  \ `.___.'\  | || |  _| |  | |_  | || |  \  `--'  /  | || | _/ /    \ \_ | || |    _| |_     | || |  _| |___/ |  | |  
		| |   `._____.'  | || | |____||____| | || |   `.____.'   | || ||____|  |____|| || |   |_____|    | || | |_________|  | |  
		| |              | || |              | || |              | || |              | || |              | || |              | |  
		| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  
		 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   			
	
		 							  ____||____
									 ///////////\			
									///////////  \
									|    _    |  |
									|[] | | []|[]|
									|   | |   |  |			
	
 
					.----------------.  .----------------.  .----------------.  .----------------. 
					| .--------------. || .--------------. || .--------------. || .--------------. |		
					| |   _____      | || |     _____    | || |  _________   | || |  _________   | |
					| |  |_   _|     | || |    |_   _|   | || | |_   ___  |  | || | |_   ___  |  | |		
					| |    | |       | || |      | |     | || |   | |_  \_|  | || |   | |_  \_|  | |
					| |    | |   _   | || |      | |     | || |   |  _|      | || |   |  _|  _   | |		
					| |   _| |__/ |  | || |     _| |_    | || |  _| |_       | || |  _| |___/ |  | |
					| |  |________|  | || |    |_____|   | || | |_____|      | || | |_________|  | |		
					| |              | || |              | || |              | || |              | |
					| '--------------' || '--------------' || '--------------' || '--------------' |
					 '----------------'  '----------------'  '----------------'  '----------------' 
	
						Hey! Welcome to Choate Life®, the ONLY realistic Choate simulation!


	''')
	
	while True: #forever loop
		answer1 = input('''



									     Type 'let's go!' to start!\n\n\n\n\n''') #input is stored in answer1
		try: #try this:
			if answer1.lower() == "let's go!": 
				morning()#morning function
				break#break loop
			else:#this means that the user didn't put it what we asked them to
				print("You didn't input the right response! Try again please.")
		except KeyboardInterrupt:#if someone quits (control + C, etc)
			print("Goodbye! See you next time!")
			sys.exit()#exit program
#define morning function
def morning():
	print("=_=" * 60) #dividing line
	print(r'''

          .
									           .
									           |
									     '.  _..._  .'
									       .'     '.
									  '-. /         \ .-'
									 _ _  ; L I F E ;  _ _
									      \         /
									   .-' '._   _.' '-.
									      .   ```   .
									     '     |     '
									           '
            '
    ''')
	while True: #while loop
		answer2 = input('''

								Good morning! It's 6 am on Monday, and the sun is shining.
					It's bright outside and you feel sleep deprived, as you stayed up working last night.


						 You have two tests today. Do you want some coffee? Type 'yes' or 'no'\n\n\n\n\n''')#input is stored in answer2
		try:# try this:
			if answer2.lower() == "yes": #if input is yes
				coffee() #coffee function
				break #break loop
			elif answer2.lower() == "no": #if input is no
				nocoffee() #nocoffee function
				break #break loop
			else: #user input isn't one of the options
				print("You didn't input the right thing! Try again please.")
				morning()#restart function
		except KeyboardInterrupt: #someone tries to quit
			print("Bye! Sorry that you're leaving...") 
			sys.exit()#quits program
#defining function
def nocoffee(): 
	print("|-\-/-"*60) #dividing line
	print('''

							Good job avoiding caffeine dependency. Woo!
						First block is approaching and you have a Chemistry test!
				You breeze through the test until you reach one last question that really stumps you:''')
	print('''


						    __________________	  __________________
						.-/|                  \ /                  |\-.
						||||                                       ||||
						||||            Is gasoline a...           ||||
						||||                                       ||||
						||||             a) element                ||||
						||||             b) compound               ||||
						||||             c) mixture                ||||
						||||                                       ||||
						||||                                       ||||
						||||                                       ||||
						||||                                       ||||
						||||__________________ 	 __________________||||
						||/===================\|/===================\||
						`--------------------~___~-------------------'' ''')

	while True: #while loop
		answer3 = input('''


							 Type 'a', 'b', or 'c' to give your answer!\n\n\n''') #stores input in answer3
		try: #try this:
			if answer3.lower() == "c": #does answer = c?
				correct() #correct function
				break# break loop
			elif answer3.lower() =="a" or "b": #does answer = a or b?
				incorrect()#incorrect function
				break#break loop
			else:# input doesn't match answers
				print("You didn't input any of the options! Try again.")
				nocoffee()#restart function
		except KeyboardInterrupt: #someone tries to quit
			print("Ok. Bye!")
			sys.exit()#exit program
#defining coffee function
def coffee():
	print(r"//\\"*45) #divding line 
	print("\n\n\n\n\n\n")
	print('''

					         {
					      {   }
					       }_{ __{
					    .-{   }   }-.
					   (   }     {   )
					   |`-.._____..-'|
					   |             ;--.
					   |            (__  \
					   |             | )  )
					   |             |/  /
					   |             /  /   
					   |            (  /
					   \             |
					    `-.._____..-' ''')


	print("\n\n\n\n\n\n")
	while True: # while loop
		answer4 = input('''

					You drank your coffee! However, you've developed a caffeine addiction. 
					You abandon your life at Choate to become a Starbucks barista :((((
						This is the end of your journey at Choate :( Sorry! 




									Type ':(' to restart, or anything else to exit.\n\n\n''') # input is stored in answer4
		try: #try this:
			if answer4 == ":(": #does answer4 = ;(?
				greeting()#restart
				break#break loop
			else:#input doesn't match
				sys.exit()#exit program
		except KeyboardInterrupt:#someone tries to quit
			print("Such a sad ending :(. Bye!")
			sys.exit()#exit program
#defining correct function
def correct():
	print("<>"*90) #dividing line
	print("\n\n\n\n")
	print('''

								__
								     ||
								    ====
								    |  |__
								    |  |-.\
								    |__|  \\
								     ||   ||
								   ======__|
								  ________||__
								 /____________\''')


													
				''')
	while True:#while loop
		answer5 = input('''

								Wow! You really are a science whiz. Good job! 
					You do an -amazing- job on this test, and become inspired to apply to SRP! Go you. 
				You are filling out your application, and need to decide whether you want to apply to the quantitative or biology section. 

								Enter 'quantitative' or 'biology' to decide! \n\n\n\n''')#input is stored in answer5
		try:#try this:
			if answer5.lower() == "biology": #does answer = biology?
				biology()#biology function
				break#break loop
			elif answer5.lower() == "quantitative": #does answer = quant?
				quantitative()#quant function
				break #break loop
			else:# input doesn't match answers
				print("\n\nYour answer doesn't work! Enter a valid answer now.\n\n")
		except KeyboardInterrupt:#someone tries to quit
			print("Goodbye, friend! Sorry I wasn't entertaining enough :(")
			sys.exit()#exit program
#defining incorrect function
def incorrect():
	print("[]"*90) #dividing line
	print(''' \n\n\n

				     .-""""""-.
				   .'          '.
				  /   O      O   \
				 :           `    :
				 |                |   
				 :    .------.    :
				  \  '        '  /
				   '.          .'
				     '-......-'  \n\n\n''')

	while True:# while loop
		answer6 = input('''



							What a disaster!!! You did horribly on the test and your ego is CRUSHED. 
										Choate is rough :(. It's time to re-evaluate your life.
						You leave the Choate lifestyle and become a monk at a monestary in rural Kazakhstan... Nice.

								If you want to play again, type ':)'. To leave, type anything else.\n\n''') #input stored in answer6
		try:#try this
			if answer6 ==":)": #does input = :)?
				greeting()#start from beginning
				break#break loop
			else:#input doesn't match answers
				sys.exit()#exit program
		except KeyboardInterrupt:#someone tries to quit
			print("Peace out!")
			sys.exit()#exit program
#defining bio function
def biology():
	print("::"*90)
	print('''

				6098)o%:::%o(860
				098)o%:::%o(8609
				 6o%:%o(86098)
				  (86098)o
				6098)o%::%o9
				098)o%::::::%o9
				 6o%::::::%o(860
				    6o%::%o(8609
				      o(86098)
				  (86098)o%:%o9
				6098)o%:::%o(860
				098)o%:::%o(8609
				 6o%:%o(86098)
				  (86098)o
				6098)o%::%o9
				098)o%::::::%o9
				 6o%::::::%o(860
				    6o%::%o(8609
				      o(86098)
				  (86098)o%:%o9
				6098)o%:::%o(860
				098)o%:::%o(8609
				 6o%:%o(86098)
				  (86098)o
				6098)o%::%o9
				098)o%::::::%o9
				 6o%::::::%o(860
				    6o%::%o(8609
				      o(86098)
				  (86098)o%:%o9
				6098)o%:::%o(860
				098)o%:::%o(8609
				 6o%:%o(86098)
				  (86098)o
				6098)o%::%o9
				098)o%::::::%o9
				 6o%::::::%o(860
				    6o%::%o(8609
				      o(86098)
				  (86098)o%:%o9
				6098)o%:::%o(860




		''')
	while True: #while loop
		answer7 = input('''

									Wow! You love researching biology and become a slighlty antisocial scientist with your own lab! 
							Although you never win a Nobel Prize, you are satisfied with studying amoebas for the rest of your life. Cool!



													Type ':)' to restart the game! Type anything else to exit the game.\n\n\n''')# input is stored in answer7
		try:#try this:
			if answer7 == ":)": #does anser7 = :)?
				greeting()#start from beginning
				break#break loop
			else:#input doesn't match answers
				print("Goodbye!")
				sys.exit()#exit program
		except KeyboardInterrupt:#someone tries to quit
			print("Goodbye! It's been fun.")
			sys.exit()#quit program
#defining quant function
def quantitative():
	print("++"*90) #dividing line
	print(r'''




		    .-.                                                               .-.
		   /   \           .-.                                 .-.           /   \
		  /     \         /   \       .-.     _     .-.       /   \         /     \
		-/-------\-------/-----\-----/---\---/-\---/---\-----/-----\-------/-------\--
		          \     /       \   /     `-'   `-'     \   /       \     /
		           \   /         `-'                     `-'         \   /
		            `-'                                               `-'


	


		''')
	while True:#while loop
		answer8 = input('''

									Wow! So you became a famous physicist. Choate did you well. 
								However, you still get flashbacks of all that work you did during those four years...



										Type ':)' to replay the game, or type anything else to quit!\n\n\n''')#input is stoed in answer8
		try:#try this:
			if answer8 == ":)":#does answer8 = :)?
				greeting()#restart
				break#break loop
			else:#input doesn't match answers
				print("Thanks!")
				sys.exit()#exit program
		except KeyboardInterrupt:#someone tries to quit
			print("It's been real. Bye!")
			sys.exit()#exit program




greeting() #calls greeting function










