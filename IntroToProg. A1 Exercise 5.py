# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 18:20:45 2024

@author: roxas
"""

print ("Exercise 5")
print("")
#the "print" function allows the data to be printed.

calendar={1 : 31,
          2 : "__",
          3 : 31,
          4 : 30,
          5 : 31,
          6 : 30,
          7 : 31,
          8 : 31,
          9 : 30,
          10 : 31,
          11 : 30,
          12 : 31}
#dictionary containing the months of a year in numerical form with their corresponding days.

m=int(input("Please enter a month number: "))#this segment allows the user to type a month number; user input.

if m in calendar:
    print("There are", calendar[m], "days for this month.")
    #this segment shows the corresponding answer based from the entered input.
else:
    print("Invalid. Please enter a correct month number (1-12 only).")
    #this segment tells the user that the entered input is invalid.
    
if m==2 in calendar:#this segment will verify whether the month of February falls under leap year or not.
    leap_year=int(input("Please enter the year: "))
    
    if(leap_year%400==0) or (leap_year%100!=0) and (leap_year%4==0):#this segment locates the leap year.
        print("There are 29 days for this month (leap year).")
        
    else:
        print("There are 28 days for this month.")#this segment will appear if the entered input is not a leap year.
