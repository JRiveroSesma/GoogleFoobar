# -*- coding: utf-8 -*-
"""
@author: Juan Rivero Sesma
"""


def solution(s):
    """
    Compute number of salutes given a string representing 
    the walking sense of employees in a corridor.
    
    Arguments:
        s -- String representing employees walking sense
        
        
    Returns: 
        Total numbers of salutes
    """
    
    s.replace('-','') # '-' are not needed to solve the problem
    
    encounters = 0
    # Pick a position starting from the left
    for position, sense in enumerate(s):
        if sense == '>':
            # If employee going right, count employees at his right going left
            encounters += s[position:].count('<') 
    
    return encounters * 2
        

string1 = ">----<"
string2 = "<<>><"
string3 = ">----<"

print(solution(string1))
print(solution(string2))
print(solution(string3))
