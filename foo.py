# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 18:32:46 2022

@author: lenovo
"""

def is_divisible_by_k(x, k):
    '''
    Checks whether x is divisible by k.
    '''
    #bug: instead of assert, return should be used
    return(x%k == 0) 
'''
Store all the integers that are multiples of 2 or 5 or 7 that are lower 
or equal to 1000 (excluding doubles)
'''
#bug: tuple is immutable, x should be a list
x = []
for i in range(1000):
    #bug: an 'or' operator should be used, in the arguments of is_divisible_by_k, i should be used, as that is the variable used in the for
    #bug: the parentheses were wrongly placed
    if (is_divisible_by_k(i, 2) |         is_divisible_by_k(i, 3) |
is_divisible_by_k(i, 7)):
        #bug: x.append(i) should have been indented
        x.append(i)

'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower 
or equal to 1000 (excluding doubles)
'''
print(sum(x))