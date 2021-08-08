# -*- coding: utf-8 -*-
"""
@author: Juan Rivero Sesma
"""


def solution(M, F):
    """
    Computes number of cycles to generate M, F bombs from a unit of each one.
    Reverse engineering approach: 
        Given starting (M,F)=(5,3) M>F -> (2,3), F>M -> (2,1), M>F -> (1,1) 
        3 cycles in total (number of arrows)
    
    Arguments:
        M -- Number of Mach bombs
        F -- Number of Facula bombs
           
    Returns: 
        Total number of cycles to generate M and F bombs respectively
    """

    a = int(M)
    b = int(F)
    
    cycles = 0 # Total number of cycles
    while a >= 1:
        if a < b:
            a, b = b, a # Exchange a, b values to divide greater by smaller
        new_cycles = a // b
        a -= new_cycles * b
        cycles += new_cycles
    
    return 'impossible' if (a, b) != (0, 1) else str(cycles - 1)
  
print(solution('4', '7'))
print(solution('2', '1'))      
# print(solution('1', '1'))
# print(solution('1', '2'))
# print(solution('3', '6'))
# print(solution('3', '9'))
