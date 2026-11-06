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

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import os

def getExercise(fileName):
    data = readData(fileName)
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
    return exercise

def initFile(fileName):
    if not os.path.exists(fileName):
        with open(fileName, 'w') as file:
            file.write("Date,Exercise,Weight,Reps,Score\n")

def plotData(fileName, exercise, a):
    data = readData(fileName)
    dates = []
    scores = []
    for i, row_exercise in enumerate(data[:, 1]):
        if row_exercise == exercise:
            dates.append(datetime.strptime(data[i,0], '%m/%d/%Y'))
            scores.append(data[i, a])   
    plt.figure()
    plt.plot(dates, scores, marker='o', color='blue')
    plt.title(f'Progress of {exercise}')
    plt.xlabel("Date")
    if a == 2:
        plt.xlabel("Weight")
    if a == 4:
        plt.ylabel("Score")
    plt.grid()
    plt.show()
    print(f'\nData for {exercise} Successfully plotted.\n\n')

def writeData(fileName):
    print("\n=-=-=- Enter New Lift -=-=-=\n")
    date = input("Enter date (MM/DD/YYYY): ").strip()
    while True:
        exercise = getExercise(fileName)
        weight = int(input("Enter weight used (lbs): "))
        reps = int(input("Enter reps performed: "))
        a = input(f'Save this Exercise: {reps} reps of {exercise} at {weight} lbs on the date {date} (y/n): ')
        if a == 'y':
            score = weight * np.log(reps+2)
            break
        else: 
            continue
    with open(fileName, 'a') as file:
        file.write(f"{date},{exercise},{weight},{reps},{score}\n")
      
    print(f"\nSuccessfully saved {exercise}: {weight} lbs x {reps} reps!\n")
    
def readData(fileName):
    data = np.genfromtxt(fileName, delimiter=',', dtype=str)
    if data.ndim == 1 and data.size > 0:
        data = data.reshape(1, -1)
    return data

def viewRecords(fileName, exercise):
    data = readData(fileName)
    weightMax = int(0)
    scoreMax = int(0)
    scoreMaxRep = 0
    scoreMaxWeight = 0
    total = 0
    for i, row_exercise in enumerate(data[:, 1]):
        if row_exercise == exercise:
            weight = int(float(data[i,2]))
            reps = int(float(data[i,3]))
            total = total + weight * reps
            if int(float(data[i,2])) > weightMax:
                weightMax = int(float(data[i,2]))
            if int(float(data[i,4])) > scoreMax:
                scoreMax = int(float(data[i,4]))
                scoreMaxRep = int(float(data[i,3]))
                scoreMaxWeight = int(float(data[i,2]))
    print(f'\n\nYour Most Impressive Lift by Weight of {exercise} is {weightMax}lbs')
    print(f'\n\nYour Most Impressive Set overall of {exercise} is {scoreMaxRep} rep(s) of {scoreMaxWeight}lbs')
    print(f'\n\nYou have lifted a Total of {total}lbs')
    print('\n\n')
        
            
