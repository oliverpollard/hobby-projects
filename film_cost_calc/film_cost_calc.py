#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:40:24 2017

@author: Oliver
"""

print("Program function: \n\n 1) Calculate film cost per shot \n 2) Compare film economies \n 3) Calculate camera economy \n\n Specify program function (1, 2, 3)")
task0 = int(input(": "))
while task0 != 1 and task0 != 2 and task0 != 3:
    
    print("Program function does not exist.")
    task0 = int(input(": "))

if task0 == 1:
    
    print("Development cost:")
    dev_cost = float(input(": £"))
    print("Price per roll:")
    roll_cost = float(input(": £"))
    print("Exposures per roll:")
    exposures = float(input(": "))

    cost = (dev_cost + roll_cost)/exposures
    
    print("Cost per shot is:", cost)
    
elif task0 == 2:
    
    film_name = ["", ""]
    roll_cost = [0, 0]
    exposures = [0, 0]
    cost_per = [0, 0]
  
    print("Film type 1 name:")
    film_name[0] = input(": ")
    print("Film type 2 name:")
    film_name[1] = input(": ")
    print("Price per roll of", film_name[0],":")
    roll_cost[0] = float(input(": £"))
    print("Price per roll of", film_name[1],":")
    roll_cost[1] = float(input(": £"))
    print("Exposures per roll of", film_name[0],":")
    exposures[0] = float(input(": "))
    print("Exposures per roll of", film_name[1],":")
    exposures[1] = float(input(": "))
    
    if (exposures[0] == exposures[1]) and (roll_cost[0] < roll_cost[1]):
        print("No difference in exposure count therefore", film_name[0],"cheapest.")
    elif (exposures[0] == exposures[1]) and (roll_cost[0] > roll_cost[1]):
        print("No difference in exposure count therefore", film_name[1],"cheapest.")
    else:
        print("Development cost:")
        dev_cost = float(input(": £"))
    
        dev_cost = (roll_cost[1]*exposures[0]-roll_cost[0]*exposures[1])/(exposures[1]-exposures[0])
        
        cost_per[0] = (dev_cost + roll_cost[0])/exposures[0]
        cost_per[1] = (dev_cost + roll_cost[0])/exposures[0]
        
        print("Cost of development", film_name[1],":")
        dev_cost_act = input(": £")
        
        dev_cost = (roll_cost[1]*exposures[0]-roll_cost[0]*exposures[1])/(exposures[1]-exposures[0])
        
        if (cost_per[0] < cost_per[1]) and (dev_cost < dev_cost_act):
            print("It is cheapter to use", film_name[0])
        elif (cost_per[0] < cost_per[1]) and (dev_cost > dev_cost_act):
            print("It is cheapter to use", film_name[1])
        elif (cost_per[0] > cost_per[1]) and (dev_cost < dev_cost_act):
            print("It is cheapter to use", film_name[1])
        elif (cost_per[0] > cost_per[1]) and (dev_cost > dev_cost_act):
            print("It is cheapter to use", film_name[0])
    
    
    
    
elif task0 == 3:
    
    print("Camera cost:")
    camera_cost = float(input(": £"))
    print("Development cost:")
    dev_cost = float(input(": £"))
    print("Price per roll:")
    roll_cost = float(input(": £"))
    print("Exposures per roll:")
    exposures = float(input(": "))
    
    print("Number of shots to analyse: ")
    shots = int(input(": "))

    cost = (dev_cost + roll_cost)/exposures
    
    