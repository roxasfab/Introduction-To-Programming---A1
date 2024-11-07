# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:19:57 2024

@author: roxas
"""

def even_or_odd(integer):#defining the EVEN or ODD function.
    
    if (integer%2) == 0:#generates the integer whether it is EVEN or ODD.
        return f"Number {{{integer}}} is an EVEN number."#this segment will appear if the integer is EVEN.
    
    else:
        return f"Number {{{integer}}} is an ODD number."#this segment will appear if the integer is ODD.
    
def main():#calls the EVEN or ODD function.
    
    number_input=int(input("Enter a number: "))
    result=even_or_odd(number_input)
    print(result)
    #engine that prints the result based from the input.
    
if __name__ == "__main__":#declares that the EVEN or ODD function is the main program.
    main()
    