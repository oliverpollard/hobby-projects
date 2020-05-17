#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 15:21:57 2018

@author: Oliver
"""

import numpy as np
import pylab as pl
import random

N = 100
data = np.zeros((N,N,1))
p_growth = 0.2
p_death = 0
n_growth = 1
t_time = 8

#random initalisation
population = 5
count = 0
while count < population:
    rand_x = int(random.uniform(0,N-1))
    rand_y = int(random.uniform(0,N-1))
    if data[rand_x,rand_y,0] == 0:
        data[rand_x,rand_y,0] = 1
        count = count + 1

time = 0
while time < t_time:
    x_count = 0
    while x_count < N:
        y_count = 0
        while y_count < N:
            if data[x_count, y_count, 0] == 1:
                if (data[x_count-1, y_count-1, 0] == 0) or (data[x_count-1, y_count, 0] == 0) or (data[x_count-1, y_count+1, 0] == 0) or (data[x_count, y_count-1, 0] == 0) or (data[x_count, y_count+1, 0] == 0) or (data[x_count+1, y_count-1, 0] == 0) or (data[x_count+1, y_count, 0] == 0) or (data[x_count+1, y_count+1, 0] == 0):
                    
                    if random.uniform(0,1) < p_growth:
                        
                        growth_count = 0
                        while growth_count < n_growth:
                            print("hello")
                            x_rand = int(random.uniform(x_count-1, x_count+1))
                            y_rand = int(random.uniform(y_count-1, y_count+1))
                            if (0 <= x_rand <= N-1) and (0 <= y_rand <= N-1):
                                if data[x_rand, y_rand, 0] == 0:
                                    data[x_rand, y_rand, 0] = 1
                                    
                                    growth_count = growth_count + 1
                                    population = population + 1
                    
            if random.uniform(0,1) < p_death:
                data[x_count, y_count, 0] = 0
                population = population - 1
                
            y_count = y_count + 1
        x_count = x_count + 1
    
    time = time + 1
 
#plotting
x_plot = np.array([])
y_plot = np.array([])
x_count = 0
while x_count < N:
    y_count = 0
    while y_count < N:
        if data[x_count, y_count, 0] == 1:
            x_plot = np.append(x_plot, x_count)
            y_plot = np.append(y_plot, y_count)
        y_count = y_count + 1
    x_count = x_count + 1

pl.plot(x_plot, y_plot, '.')
pl.xlim(0,N)
pl.ylim(0,N)
pl.show()

print(population)
    