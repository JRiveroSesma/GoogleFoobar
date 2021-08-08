# -*- coding: utf-8 -*-
"""
@author: Juan Rivero Sesma
"""


def solution(l):

    """
    Count total number lucky triples given in a list. A lucky triple is 
    defined as [li, lj, lk] with i < j < k such that k % j == j % i == 0.
     
    Arguments:
        l -- List to be examined for lucky triples

    Returns:
        Total number of lucky triples contained in l
    """
    
    multiples_counter = [0 for _ in l]
    n_lucky_triples = 0
    
    for i in range(1, len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                multiples_counter[i] += 1
                n_lucky_triples += multiples_counter[j]
    return n_lucky_triples

l1 = [1, 1, 1]
l2 = [1, 2, 3, 4, 5, 6]

print(solution(l1))
print(solution(l2))
