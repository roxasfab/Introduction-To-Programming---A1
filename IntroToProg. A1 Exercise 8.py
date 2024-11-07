# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:47:42 2024

@author: roxas
"""

print ("Exercise 7")
print("")
#the "print" function allows the data to be printed.

names=["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]
#dictionary containing strings of different names which can appear on the search engine.

name_search=str(input("Please enter a name: "))
#this segment allows the user to enter the name of their choice; user input.

if name_search in names:
    print("The name", name_search, "is on the list.")
    #this segment will appear to tell the user that their input is valid.
    
else:
    print("The name", name_search, "is not on the list.")
    #this segment will appear to tell the user that their input is invalid.