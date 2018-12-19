import random

#EVENS
# ''' Instructions:
#    Work with a partner to complete these tasks. Complete as many as you can. Assume that all variables/lists are declared and initialized (unless you are specifically asked to create/initialize a list); you need only write the code using the variables/lists indicated in the description. Write your solution below the commented description.
# '''
 
# ''' 1. 
#    Create a list of ints, faveNums, that holds 3 integers.
# '''
 

 
 
# ''' 2. 
#    Create a list of Strings, holidays, that holds 14 holidays.  
# # '''
 
holidays = ["Christmas","Veterans day","Easter","Halloween","Diwali","Thanksgiving","Fourth of July","Columbus day",
"Martin Luther King Jr day","Memorial day","Labor day","New years","Boxing day","Valentine's day"]

# ''' 3. 
#    Create a list of characters, grades, that holds 5 letter grades.
# '''
 
 
 
# ''' 4. 
#    Create a list of booleans, funny, the can keep track of whether 18 things are funny or not. 
# '''
 
funny = [True, False, True, True, True, False, False, True, False, True, False, True, False, True, False, False, False, False]
 
 
# ''' 5. 
#    Create a list of doubles, salaries, that holds the salaries of all the employees at a university. The number of employees is stored in the int numEmployees.
# '''
 
 
 
# ''' 6. 
#    A picture's dimensions are stored in integer variables x and y. Create a single list of integers that can store the grayscale value for each pixel in the list.
# '''
 
x = 5
y = 5

pixels = [[12,15,13,14,16]
          [16,19,13,16,34]
          [19,13,35,22,45]
          [16,17,15,14,20]
          [19,13,40,15,67]]

 
 
# ''' 7. 
#    In a class, each student has 0, 1, 2 or 3 siblings. The numbers of students with no siblings is stored in the variable noSiblings, the number of students with one sibling is stored in the variable oneSibling, the number of students with two siblings is stored in the variable twoSiblings, and the number of students with three siblings is stored in the variable threeSiblings. Create a list that holds all the names of the students in the class, as well as the names of all their siblings.
# '''
 
 
 
# ''' 8. 
#    Create a list that holds all the months in the year. (No loop.)
# '''
 
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
 
 
# ''' 9. 
#    Create a list that holds all the days of the week. (No loop.)
# '''
 
 
 
# ''' 10. 
#    Create a list that holds all the possible values for boolean variables. (No loop.)
# '''
 
possibilities = [True, False]
 
# ''' 11. 
#    Create a list that holds the names of all the 3rd form dorms on campus. (No loop.)
# '''
 
 
 
# ''' 12.  
#    Create a list that holds 3 random numbers with values between 0 and 1. (Loop optional.)
# '''
 
numbers = [random.random(),random.random(),random.random()]
 
# ''' 13. 
#    Create a list that will represent a deck of cards. Some example data for cards would be AS (ace of spaces), 5H (5 of hearts), JC (jack of clubs), 9D (9 diamonds). (Loop required.) 
# '''
 
 
 
# ''' 14. 
#    Write a Yahtzee program that simulates the rolling of five dice and prints "Yahtzee" if all five dice are the same; otherwise it should print "Try again."
# '''

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)
dice4 = random.randint(1,6)
dice5 = random.randint(1,6)

result = [dice1, dice2, dice3, dice4, dice5]

if len(set(result) == 1:
   print("Yahtzee")

else:
   print("try again")
 
# ''' 15. 
#    In a list, specials are numbers in a list that have an even number before them, an odd number behind them, and they themselves are divisible by 3. Given a list of ints called numbers, print out the location in the list of the specials, as well as the value in front of them, their value, and the value behind them. For example:
#    position 4: 14, 9, 25
# '''
 
 
 
# ''' 16. 
#    Write a program to search for the "saddle points" in a 5 by 5 list of integers. A saddle point is a cell whose value is greater than or equal to any in its row, and less than or equal to any in its column. There may be more than one saddle point in the list. Print out the coordinates of any saddle points your program finds. Print out "No saddle points" if there are none.
# '''
 
numbers = [[1,2,3,4,5],[6,7,8,9,10],[1,2,3,4,5],[6,7,8,9,10],[15,19,13,17,22]]
points = []

for x in range(5):
   largest = max(numbers[x])
   for y in range(5):

      if x == 0 and largest <= numbers[x][y+1]:
         points.append(x+1)
         points.append(y+1)
         elif x == 4 and largest <= numbers[x][y-1]:
         points.append(x+1)
         points.append(y+1)
      else:
         if largest <= numbers[x][y-1] and largest<=numbers[x][y+1]:
            points.append(x+1)
            points.append(y+1)
print(points)


# ''' 17. 
#    In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal. A chessboard can be represented by an 8 by 8 list. A 1 in the list represents a queen on the corresponding square, and a O in the list represents an unoccupied square. Given the two locations for queens (row1, col1, row2, col2), place the queens in the 2D list, chessboard. Then process the board and indicate whether or not the two queens are positioned so that they attack each other. 
# '''
 
 
 
# ''' 18. 
#    Given a list, write code that will reverse the order of the elements in the list. For example, dog, cat, bunny should become bunny, cat, dog.
# '''
 
animals = ["dog","cat","bunny"]
print(animals[::-1])


 
 
# ''' 19. 
#    Given a list, doorknobs, that holds strings, swap the elements at positions 1 and 3, if possible.
# '''
 
 
 
# ''' 20. 
#    In a list of ints called numbers, find the largest number in the list and place it at the end of the list.
# '''
 
numbers = []

largest = max(numbers)

place = numbers.index(max(numbers))

numbers.pop(place)
numbers.append(largest)
print(numbers)
 
 


# ''' 21. 
#    In a 2D list with dimensions w by h, filled with random numbers from from 1 to 100, replace every odd number with either 2 or 22; 2 if the number was a single digit number, 22 if the number was a 2-digit number. 
# '''
 
 
 
# ''' 22. 
#    In a 2D list with dimensions w by h, holding grayscale values for an image, adjust the colors so the image is inverted. All light portions should be dark, all dark portions should be light. A value of 200 should be 5, a value of 100 should be 155, etc. Remember, there are 256 levels for color, including 0.
# '''
 
 
 

# ''' 23.
#    In a list, shifters, holding ints, shift all elements forward 1 position. For example, position 2 should move to position 1, position 1 to position 0, and position 0 to the end of the list (etc.)
# '''
 
 
 
# ''' 24. 
#    Given an N-by-N grid of elevation values (in meters), a peak is a grid point for which all four neighboring cells are strictly lower. Write a code fragment that counts the number of peaks in a given N-by-N grid.
# '''

size = n
list = []
coords = []
count = 0

for x in range(n+1):
   for y in range{n+1}:
      if x == 0 and y ==0:
         if list[x][y] > list[x][y+1] and list[x][y] > list[x+1][y]:
            count = count + 1
      if x > 0 and x < n and y >0 and y < n:
         if list[x][y] > list[x+1][y] and list[x][y] > list[x-1][y] and list[x][y] > list[x][y+1] and list[x][y] > list[x][y-1]:
            count = count + 1
      if x == n and y ==n:
         if list[x][y] > list[x][y-1] and list[x][y] > list[x-1][y]:
            count = count + 1


         
  
 
# ''' 25. 
#    90% of incoming college students rate themselves as above average. Write some code that, given a list of student rankings (stored in integer list rankings), prints the fraction of values that are strictly above the average value.
# '''
 
 
 
# ''' 26. 
#    Given a 9-by-9 list of integers between 1 and 9, check if it is a valid solution to a Sudoku puzzle: each row, column, and block should contain the 9 integers exactly once.
# '''
 
list = []

for x in range(1,10):
   for y in range(1,10):
    if len(list(set(list[x]))) == 9 and len(list(set(list[x]))) == 9:
      print("wow")





# '''
#     27. Create a list of 100 numbers between 1 and 10 (inclusive), create a new list whose first value is the number of 1s in the original list, whose 2nd value is the number of 2s in the original list, and so on. Average the number of occurences of each number in the list over 100 repetitions. Average the averages. Print the result to the screen.
# '''
 
 
 
# ''' Sources
#    http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html
#    http://introcs.cs.princeton.edu/java/14array/

#ODDS
# # '''

''' Instructions:
   Work with a partner to complete these tasks. Complete as many as you can. Assume that all variables/lists are declared and initialized (unless you are specifically asked to create/initialize a list); you need only write the code using the variables/lists indicated in the description. Write your solution below the commented description.
'''
 
''' 1. 
   Create a list of ints, faveNums, that holds 3 integers.
'''
import random as r
faveNums = []
for i in range(3):
   faveNums += [r.randrange(4353)]
 
''' 2. 
   Create a list of Strings, holidays, that holds 14 holidays.  
'''
 
 
 
''' 3. 
   Create a list of characters, grades, that holds 5 letter grades.
'''
grades = ['A','B','C','D','F']
 
 
''' 4. 
   Create a list of booleans, funny, the can keep track of whether 18 things are funny or not. 
'''
 
 
 
''' 5. 
   Create a list of doubles, salaries, that holds the salaries of all the employees at a university. The number of employees is stored in the int numEmployees.
'''
salaries: list
numEmployees: int
salaries = []

 
''' 6. 
   A picture's dimensions are stored in integer variables x and y. Create a single list of integers that can store the grayscale value for each pixel in the list.
'''
 
 
 
''' 7. 
   In a class, each student has 0, 1, 2 or 3 siblings. The numbers of students with no siblings is stored in the variable noSiblings, the number of students with one sibling is stored in the variable oneSibling, the number of students with two siblings is stored in the variable twoSiblings, and the number of students with three siblings is stored in the variable threeSiblings. Create a list that holds all the names of the students in the class, as well as the names of all their siblings.
'''
noSiblings: int
oneSibling: int
twoSiblings: int
threeSiblings: int
students_withSibs: list

students_withSibs = []
 
''' 8. 
   Create a list that holds all the months in the year. (No loop.)
'''

 
 
''' 9. 
   Create a list that holds all the days of the week. (No loop.)
'''
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
 
 
''' 10. 
   Create a list that holds all the possible values for boolean variables. (No loop.)
'''
 
 
 
''' 11. 
   Create a list that holds the names of all the 3rd form dorms on campus. (No loop.)
'''
third_Dorms = ['Nichols','Squire','Pitman','Memorial']
 
 
''' 12.  
   Create a list that holds 3 random numbers with values between 0 and 1. (Loop optional.)
'''
 
 
 
''' 13. 
   Create a list that will represent a deck of cards. Some example data for cards would be AS (ace of spaces), 5H (5 of hearts), JC (jack of clubs), 9D (9 diamonds). (Loop required.) 
'''
suits = ['A','S','H','D']
rank = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
cards = []

for j in range(len(suits)):
   for i in range(len(rank)):
      card = str(rank[i])+suits[j]
      cards += [str(card)]
 
 
''' 14. 
   Write a Yahtzee program that simulates the rolling of five dice and prints "Yahtzee" if all five dice are the same; otherwise it should print "Try again."
'''
 
 
 
''' 15. 
   In a list, specials are numbers in a list that have an even number before them, an odd number behind them, and they themselves are divisible by 3. Given a list of ints called numbers, print out the location in the list of the specials, as well as the value in front of them, their value, and the value behind them. For example:
   position 4: 14, 9, 25
'''
lis = [2,3,5,45,6,12,9]
for x in range(1,len(lis)-1):
   if lis[x-1]%2 == 0 and lis[x+1]%2==1 and lis[x]%3 ==0:
      print("position "+str(x)+": "+str(lis[x-1])+", "+str(lis[x])+", "+str(lis[x+1]))
 
''' 16. 
   Write a program to search for the "saddle points" in a 5 by 5 list of integers. A saddle point is a cell whose value is greater than or equal to any in its row, and less than or equal to any in its column. There may be more than one saddle point in the list. Print out the coordinates of any saddle points your program finds. Print out "No saddle points" if there are none.
'''
 
 
 
''' 17. 
   In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal. A chessboard can be represented by an 8 by 8 list. A 1 in the list represents a queen on the corresponding square, and a O in the list represents an unoccupied square. Given the two locations for queens (row1, col1, row2, col2), place the queens in the 2D list, chessboard. Then process the board and indicate whether or not the two queens are positioned so that they attack each other. 
'''
chessboard = []
   for a in range(8):
      chessboard += [[0]*8] 

row1: int
col1: int
row2: int
col2: int

chessboard[row1][col1] = 1
chessboard[row2][col2] = 1

attack_imenent = False
if row1 == row2 or col1 == col2:
   attack_imenent = True
elif abs(row1-row2) == abs(col1-col2):
   attack_imenent = True
else: 
   attack_imenent = False

print(attack_imenent)

''' 18. 
   Given a list, write code that will reverse the order of the elements in the list. For example, dog, cat, bunny should become bunny, cat, dog.
'''
 
 
 
''' 19. 
   Given a list, doorknobs, that holds strings, swap the elements at positions 1 and 3, if possible.
'''
one: str
two: str
three:str
four:str
doorknobs = [one,two,three,four]
doorknobs[1],doorknobs[3]= doorknobs[3],doorknobs[1]
 
''' 20. 
   In a list of ints called numbers, find the largest number in the list and place it at the end of the list.
'''
 
 
 
''' 21. 
   In a 2D list with dimensions w by h, filled with random numbers from from 1 to 100, replace every odd number with either 2 or 22; 2 if the number was a single digit number, 22 if the number was a 2-digit number. 
'''
w: int
h: int
import random as r
list_ = []
for x in range(h):
   num = r.randrange(1,101)
   if num%2 != 0:
      if num/10>1:
         num = 22
      else:
         num = 2
   list_ += [[num]*w]



''' 22. 
   In a 2D list with dimensions w by h, holding grayscale values for an image, adjust the colors so the image is inverted. All light portions should be dark, all dark portions should be light. A value of 200 should be 5, a value of 100 should be 155, etc. Remember, there are 256 levels for color, including 0.
'''
 
 
 
''' 23.
   In a list, shifters, holding ints, shift all elements forward 1 position. For example, position 2 should move to position 1, position 1 to position 0, and position 0 to the end of the list (etc.)
'''
shifters = [1,2,3,4,5,6,7]
x = 0
end = shifters[0]
while x<len(shifters)-1:
   shifters[x] = shifters[x+1]
   x+=1
 shifters[len(shifters)-1] = end
''' 24. 
   Given an N-by-N grid of elevation values (in meters), a peak is a grid point for which all four neighboring cells are strictly lower. Write a code fragment that counts the number of peaks in a given N-by-N grid.
'''
 
  
 
''' 25. 
   90% of incoming college students rate themselves as above average. Write some code that, given a list of student rankings (stored in integer list rankings), prints the fraction of values that are strictly above the average value.
'''
rankings= []
average = sum(rankings)/len(rankings)
amt_above = 0
for x in range(len(rankings)):
   if rankings[x] > average:
      amt_above += 1
print(str(amt_above)+"/"+str(len(rankings)))
 
''' 26. 
   Given a 9-by-9 list of integers between 1 and 9, check if it is a valid solution to a Sudoku puzzle: each row, column, and block should contain the 9 integers exactly once.
'''
 
 
 
'''
    27. Create a list of 100 numbers between 1 and 10 (inclusive), create a new list whose first value is the number of 1s in the original list, whose 2nd value is the number of 2s in the original list, and so on. Average the number of occurences of each number in the list over 100 repetitions. Average the averages. Print the result to the screen.
'''
import random as r
def createlist():
   vals = [r.randrange(1,11) for x in range(100)]
   return vals

def averageresult(time_one, time_two, length):
   av_ones = (time_one/length) *100
   av_twos = (time_two/length) *100

   return [av_ones,av_twos]

def get_times(lis):
   lis: list
   times_one = 0
   times_two = 0
   for x in range(len(lis)):
      if str(lis[x]).find('1') == 0:
         times_one += 1
      if str(lis[x]).find('2') == 0:
         times_two += 1
   return [times_one, times_two]

av_of_avs_1 = 0
av_of_avs_2 = 0
for a in range(100):
   val_list = createlist()
   t1,t2 = get_times(val_list)
   av_of_avs_1,av_of_avs_2 = averageresult(t1,t2,100)

print(str(av_of_avs_1)+"%"+" occurence of 1")
print(str(av_of_avs_2)+"%"+" occurence of 2")

 
 
''' Sources
   http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html
   http://introcs.cs.princeton.edu/java/14array/
'''