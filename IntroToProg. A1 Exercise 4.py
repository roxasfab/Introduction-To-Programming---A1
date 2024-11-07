# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:10:20 2024

@author: roxas
"""

print("Exercise 4")
print("")
#the "print" function allows the data to be printed.

first_question=str(input("What is the capital of France? "))#this segment allows the user to type their answer; user input.
answer="Paris"#the answer to the question.

if first_question.lower()==answer.lower():#this segment accepts the correct answer regardless of the capitalization.
    print("Your answer is CORRECT!")#this segment will appear when the user inputs the correct answer.
    
else:
    print("WRONG. The correct answer is", answer,".")#this segment will appear when the user inputs the wrong answer.
    
capitals = {"Austria" : "Vienna",
           "Belgium" : "Brussels",
           "Czech Republic" : "Prague",
           "Denmark" : "Copenhagen",
           "Finland" : "Helsinki",
           "Germany" : "Berlin",
           "Hungary" : "Budapest",
           "Ireland" : "Dublin",
           "Italy" : "Rome",
           "Portugal" : "Lisbon"}
#dictionary containing ten european countries with their capital cities.

for country in capitals:#this loop will use the dictionary to create aditional ten questions by using each item within the list one by one.
    questions=str(input(f"What is the capital of {{{country}}}? "))#each country in the dictionary will be inserted in the question.

if questions.lower()==capitals[country].lower():#this segment accepts the correct answer regardless of the capitalization.
    print("Your answer is CORRECT!")#this segment will appear when the user inputs the correct answer.
    
else:
    print(f"WRONG. The correct answer is {{{capitals[country]}}}.")#this segment will appear when the user inputs the wrong answer.