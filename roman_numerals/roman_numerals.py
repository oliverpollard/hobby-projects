#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:09:39 2020

@author: oliver
"""

import numpy as np

def numbers_conv(numbers):
    
    numbers_string = str(numbers)[::-1]
    print("Arabic Number:", numbers)
    
    number_breakdown = np.zeros((len(numbers_string)))
    
    c = 0
    while c < len(number_breakdown):
        number_breakdown[c] = int(numbers_string[c])*10**c
        c = c + 1
    print(number_breakdown)
    print(numbers_string)
    output = 1
    return output

def numerals_conv(numerals):

    num_dict = {"I": 1,"V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sub_dict = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

    print("Roman Numeral:", numerals)

    numbers = np.zeros((length))
    
    c = 0
    while c < length - 1:
        pair = numerals[c] + numerals[c+1]
        if pair in sub_dict:
            numbers[c] = -num_dict[numerals[c]]
            numbers[c+1] = num_dict[numerals[c+1]]
            c = c + 2
        else:
            c = c + 1
    
    
    c = 0
    while c < length:
        if numbers[c] == 0:
            numbers[c] = num_dict[numerals[c]]
        c = c + 1
    
    output = int(sum(numbers))
    return output


value = input().upper()
length = len(value)

if value.isdigit():
    print(numbers_conv(value))
else:
    """
    c = 0
    while c < length:
        if numerals[c] in num_dict:
            if c == length-1:
                valid_input = 1
            else:
                continue
        else:
            print("Invalid input")
            break
        c = c + 1
    """
    print(numerals_conv(value))

