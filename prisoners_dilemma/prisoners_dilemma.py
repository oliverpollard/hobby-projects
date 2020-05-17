#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:34:12 2018

@author: Oliver
"""
import numpy as np
import pylab as pl

def play(p1_moves, p2_moves):
    
    n = len(p1_moves) - 1
    p1_next_move = 0
    p2_next_move = 0
    
    #player 1 - tit-for-tat
    if p2_moves[n] == 0:
        p1_next_move = 0
    elif p2_moves[n] == 1:
        p1_next_move = 1
        
    #player 2 - your strategy
    if len(p1_moves) == 1:
        if p1_moves[n] == 0:
            p2_next_move = 0
        elif p1_moves[n] == 1:
            p2_next_move = 1
            
    elif len(p1_moves) > 1:
        if p1_moves[n-1] == 1 and p1_moves[n] == 1:
            p2_next_move = 0
        elif p1_moves[n-1] == 0 and p1_moves[n] == 1:
            p2_next_move = 1
        elif p1_moves[n-1] == 1 and p1_moves[n] == 0:
            p2_next_move = 0
        elif p1_moves[n-1] == 0 and p1_moves[n] == 0:
            p2_next_move = 1
    
        
    return p1_next_move, p2_next_move


"""
Moves
    0 - cooperate
    1 - defect
"""

N = 100

p1_moves = np.ones((1,1))
p2_moves = np.ones((1,1))
score = np.zeros((2,N))

#inital moves
p1_moves[0] = 0
p1_moves[0] = 1

n = 1
while n < N:
    
    next_move = play(p1_moves, p2_moves)
    p1_moves = np.append(p1_moves, next_move[0])
    p2_moves = np.append(p2_moves, next_move[1])

    if p1_moves[n] == 0 and p2_moves[n] == 0:
        score[0, n] = score[0, n-1] + 3
        score[1, n] = score[1, n-1] + 3
    elif p1_moves[n] == 1 and p2_moves[n] == 1:
        score[0, n] = score[0, n-1] + 1
        score[1, n] = score[1, n-1] + 1
    elif p1_moves[n] == 0 and p2_moves[n] == 1:
        score[0, n] = score[0, n-1] + 0
        score[1, n] = score[1, n-1] + 5
    elif p1_moves[n] == 1 and p2_moves[n] == 0:
        score[0, n] = score[0, n-1] + 5
        score[1, n] = score[1, n-1] + 0
    
    n = n + 1

moves = np.linspace(0, N, num=N)
    
pl.figure(1)
pl.plot(moves, score[0])
pl.plot(moves, score[1])
pl.legend(["player 1","player 2"])
pl.show()

print("Player 1 score:", score[0,n-1])
print("Player 2 score:", score[1,n-1])