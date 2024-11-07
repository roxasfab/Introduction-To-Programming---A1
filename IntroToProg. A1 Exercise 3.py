# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:26:43 2024

@author: roxas
"""

print("Exercise 3")
print("")
#the "print" function allows the data to be printed.

#create a variable for each component of the user input.
name = str(input("Enter your full name: "))
#this will allow the user the input their name.
hometown = str(input("Enter your hometown: "))
#this will allow the user the input their hometown.

while True: #while condition creates infinite loop as long as the statement is true.
    age = input("Enter your age (Numbers only): ")
    
    if age.isdigit(): #this segment checks if the input from user is valid.
        age=int(age)
        break
    
    else: #this segment will tell the user that their input is not valid.
        print("Invalid input. Please type using numbers only.")
        continue
 
#this segment will store the user's personal information in a dictionary.
user_input={'Name' : name,
            'Hometown' : hometown,
            'Age' : age}

#this segment prints the user's personal information in a single line.
print("Name: ", user_input['Name'], "Hometown: ", user_input['Hometown'], "Age: ", user_input['Age'])