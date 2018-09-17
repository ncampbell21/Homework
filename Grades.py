#September 17
#This is a somewhat simple program. the program takes the argument and rounds it to the nearest tenth if it's a decimal.
#from here, two lists are created. Grades is a list of strings containing grades, and points is a list of lists.
#the program searches the list of lists for numbers that match "num". The element containing "num" is returned and stored in grade_index.
#the string in grades 
#Sources:https://stackoverflow.com/questions/25398259/finding-the-index-of-an-item-in-a-list-of-lists

#import corresponding with the element # in points is printed
import sys as s

#stores arg[1] in num
num = float(s.argv[1])
#rounds num to 10th
num = round(num, 1)
#list of grades
grades = ["F","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"]

#list of list of numbers corresponding to grades
points = [[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],
         [1.0, 1,1, 1.2, 1.3, 1.4],
         [1.5,1.6,1.7,1.8,1.9],
         [2.0,2.1,2.2,2.3,2.4],
         [2.5,2.6,2.7,2.8],
         [2.9,3.0,3.1],
         [3.2,3.3,3.4],
         [3.5,3.6,3.7,3.8],
         [3.9,4.0,4.1],
         [4.2,4.3,4.4],
         [4.5,4.6],
         [4.7,4.8],
         [4.9,5]]

#if number is between 0 and 5 inclusive
if(num>=0 and num<=5):
	#got this snippet of code from: https://stackoverflow.com/questions/25398259/finding-the-index-of-an-item-in-a-list-of-lists
	grade_index = int(([i for i, points in enumerate(points) if num in points][0]))
	#prints element of grades with same position in list as num did in points
	print(grades.pop(grade_index))
#if number isn't between 0 and 5 inclusive
else:
	print("Your number needs to be between or equal to 0 and 5!")




	



