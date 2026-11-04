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
import matplotlib as plt
import numpy as np
from datetime import datetime

#---------------------------------------------------
#  Inputs
#---------------------------------------------------

def plotData(exercise):
    data = readData()
    dates = []
    scores = []
    
    for i, row_exercise in enumerate(data[:, 1]):
        if row_exercise == exercise:
            dates.append(datetime.strptime(data[i,0], '%m/%d/%Y'))
            scores.append(data[i, 4])   
    plt.figure()
    plt.plot(dates, scores, marker='o', color='blue')
    plt.title(f'Score Progress of {exercise}')
    plt.xlabel("Date")
    plt.ylabel('Score')
    plt.grid()
    plt.show()

def writeData():
    data = readData()
    while True:
        print("\n=-=-=- Enter New Lift -=-=-=\n")
        date = input("Enter date (MM/DD/YYYY): ").strip()
        while True:
            exercise = input("Enter Exercise Name: ").strip().upper()
            if exercise in np.char.upper(data[:, 1]):
                break
            else:
                a = input(f'Exercise {exercise} not found, create new? (y/n): ').strip().lower()
                if a == 'y':
                    break
                else:
                    continue
                weight = int(input("Enter weight used (lbs): "))
                reps = int(input("Enter reps performed: "))
        a = input(f'Save this Exercise: {reps} reps of {exercise} at {weight} lbs on the date {date} (y/n)')
        if a == 'y':
            score = weight * np.log(reps+8)
            break
        else: 
            continue
    with open(fileName, 'a') as file:
        file.write(f"{date},{exercise},{weight},{reps},{score}\n")
      
    print(f"\nSuccessfully saved {exercise}: {weight} lbs x {reps} reps!")
        
def readData():
    data = np.genfromtxt(fileName, delimiter=',', dtype=str)
    if data.ndim == 1 and data.size > 0:
        data = data.reshape(1, -1)
    return data

#---------------------------------------------------
#  Computations
#---------------------------------------------------

writeData()

#---------------------------------------------------
#  Outputs
#---------------------------------------------------
