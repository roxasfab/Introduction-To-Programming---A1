# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:19:38 2024

@author: roxas
"""

print ("Exercise 6")
print("")
#the "print" function allows the data to be printed.

correct_password=12345
#password format for this exercise.
attempt_limit=5
#additional five attempts for every wrong password input.

while True:#this loop will allow attempts in case of invalid input. 
    user_input=int(input("Please enter password: "))
    #this segment allows the user to enter the password; user input.
    attempt_limit-=1
    #reduces the total attempt limit by one attempt.
    if user_input==correct_password:#the console will tell the user that their input is valid when the input is equal to the data inside the variable.
        print("Logged in successfully.")#appears if the answer is valid.
        break#loop ends as the valid answer is entered.
    
    elif attempt_limit>0:#the console will tell the user that their input is invalid.
        print("Incorrect password. Please try again.")#appears if the answer is invalid.
        
    else:
        print("Attempt limit reached. Try again after 24 hours.")#appears if the attempt limit is reached.
        break#loop ends as the attempt limit is reached.