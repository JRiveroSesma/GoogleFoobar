# -*- coding: utf-8 -*-
"""
@author: Juan Rivero Sesma
"""


def solution(l):
    """
    Sort a list of versions.
    
    Arguments:
        l -- Unsorted list of versions
           
    Returns: 
        Sorted list of versions
    """
    
    # Use Python list sort with secondary and third key to sort in case of draw
    return sorted(l, key = lambda version:[int(i) for i in version.split('.')])
        

l1 = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
l2 = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
print(solution(l1))
print(solution(l2))
