#Task Description: Project<4>
#File: <Project4_main.py>
# Date: <11/01/2026>
# Team Pair:  <9B>
# Authors: 
# <Kieran Baker>
#     <bake1212>
# 
# Team: <Number>
#
# ELECTRONIC SIGNATURE
# <Kieran Baker>
# 
# The electronic signatures above indicate that the program
# submitted for evaluation is the combined effort of all
# team members and that each member of the team was an
# equal participant in its creation. In addition, each
# member of the team has a general understanding of
# all aspects of the program development and execution.
#
#  Version 1.0    Original    November 2026
# 
# Gym tracker                                     EXPAND ON DESCRIPTION
#

fileName = 'gymLog.csv'

from Project_4_Functions import initFile, plotData, writeData, readData

def toNum(a):
    if ( a == '1' or a == '2' or a == '3' or a == '4' ):
        a = int(a)
    elif ( a == 'four' ):
        a = int(4)
    elif ( a == 'three' ):
        a = int(3)
    elif ( a == 'two' ):
        a = int(2)
    elif ( a == 'one' ):
        a = int(1)
    else:
        a = -100
    return a

def main():
    while True:    
        file = input("Enter csv File name: ")
        isTrue = input(f"\nUse file {file}? (y/n): ")
        if isTrue == 'y':
            break
        else:
            print("\n\n")
            continue
    while True:
        initFile(file)
        print("+=-=-=-=-=-=-=-=-=-=-=-=-=-=+\n")
        print("|                           |\n")
        print("|     Gym Logger 67000      |\n")
        print("|                           |\n")
        print("+=-=-=-=-=-=-=-=-=-=-=-=-=-=+\n")
        print("|                           |\n")
        print("|  Type 1:   Log Exercise   |\n")
        print("|  Type 2:    Plot Data     |\n")
        print("|  Type 3:   View Records   |\n")
        print("|                           |\n")
        print("|  Type 4:   Quit Program   |\n")
        print("|                           |\n")
        print("+=-=-=-=-=-=-=-=-=-=-=-=-=-=+\n")
        a = str(input().strip().lower())
        a = toNum(a)
        if a == -100:
            print("\n\n  Invalid Input, Try Again \n\n")
            continue
        if a == 1:
            writeData(file)
        
            
            
            
        if a == 4:
            break
        
main()
    
        
    