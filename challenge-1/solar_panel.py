# -*- coding: utf-8 -*-
"""
@author: Juan Rivero Sesma
"""


import math


def solution(area):
    """
    Compute list of the areas of the largest squares
    that can be obtained from a given total area.
    
    Arguments:
    area -- total input area of solar panels
    
    Returns:
    squares -- list containing the largest squares
    """
    
    squares = []
    remaining_area = area
    while remaining_area > 0:
        # Calculate largest square fitting the remaining area
        # Note: Python 2.7.4 math.floor returns type float
        side_len = int(math.floor(math.sqrt(remaining_area)))
        squares.append(side_len * side_len)
        remaining_area -= squares[-1]
    
    return squares
