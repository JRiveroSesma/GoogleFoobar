# -*- coding: utf-8 -*-
"""
@author: Juan Rivero Sesma
"""


# Recursive solution is very slow compared to the 
# alternative solution based on 4 multiples

def solution_rec(N):
    
    n = int(N)
    steps_n = {1: 0}
    
    def calculate_steps(n):
        
        if n in steps_n:
            return steps_n[n]
        elif n & 1 == 0:
            steps_n[n] = calculate_steps(n >> 1) + 1
        else:
            steps_n[n] = min(calculate_steps(n + 1), calculate_steps(n - 1)) + 1
        
        return steps_n[n]    
        
    return calculate_steps(n)


print('Solution: solution_rec()')
print(f'Solution (1): {solution_rec(str(1))}')
print(f'Solution (2): {solution_rec(str(2))}')
print(f'Solution (3): {solution_rec(str(3))}')
print(f'Solution (5): {solution_rec(str(5))}')
print(f'Solution (6): {solution_rec(str(6))}')
print(f'Solution (9): {solution_rec(str(9))}')
print(f'Solution (21): {solution_rec(str(21))}')
print(f'Solution (167): {solution_rec(str(167))}')
print(f'Solution (28798): {solution_rec(str(28798))}')
print(f'Solution (10**308): {solution_rec(str(10**308))}') # 309 digits long number


print('---------------------------')


def solution(N):
    """
    Reduce a given a positive integer N to 1 using the minimum number of
    steps using the operations defined by:
        
        N / 2 (if number is even only)
        N + 1
        N - 1
    
    Solution:
     The idea is to try to get to the branch of 2**m as fast as possible 
     because dividing by 2 is the fastest way to reduce a number to 1.
     Thus, when the number is even dividing by 2 is the best operation. 
     When the number is odd we have to check in which case we will be able 
     to divide by 2 more consecutive times, that is, in which case N is a 
     multiple of 4.
     By listing even numbers 2-4-6-8-10-... it is easy to notice that we 
     simply get multiples of 4 by skipping one even number starting from 4: 
     4-x-8-x-12-... Therefore, from any odd number it is possible to reach a
     multiple of 4 by either adding or subtracting 1. If we do not reach a
     multiple of 4, we would only reach a multiple of 2 and we would only be 
     able to divide by 2 once instead of two consecutive times.
     
    Arguments:
        N -- Positive integer given as a string to be reduced to 1

    Returns:
        Total number of steps to reduce N to 1
    """
    
    n = int(N)
    steps = 0
    
    while n != 1:
        if n % 2 == 0: # Prioritize //2 for even numbers
            n //= 2
        elif (n + 1) % 4 == 0 and n != 3: # Treat 3 as an edge case
            n += 1
        else:
            n -= 1        
        steps += 1
            
    return steps


print('Solution: solution()')
print(f'Solution (1): {solution(str(1))}')
print(f'Solution (2): {solution(str(2))}')
print(f'Solution (3): {solution(str(3))}')
print(f'Solution (5): {solution(str(5))}')
print(f'Solution (6): {solution(str(6))}')
print(f'Solution (9): {solution(str(9))}')
print(f'Solution (21): {solution(str(21))}')
print(f'Solution (167): {solution(str(167))}')
print(f'Solution (28798): {solution(str(28798))}')
print(f'Solution (10**308): {solution(str(10**308))}') # 309 digits long number


print('---------------------------')


def solution_bin(n):
    n = int(n)
    i = 0
    while n > 1:
        if (n&1) == 0:
            n >>= 1
        elif (n&3) == 1 or n == 3:
            n -= 1
        else:
            n += 1
        i += 1
    return i


print('Solution: solution_bin()')
print(f'Solution (1): {solution_bin(str(1))}')
print(f'Solution (2): {solution_bin(str(2))}')
print(f'Solution (3): {solution_bin(str(3))}')
print(f'Solution (5): {solution_bin(str(5))}')
print(f'Solution (6): {solution_bin(str(6))}')
print(f'Solution (9): {solution_bin(str(9))}')
print(f'Solution (21): {solution_bin(str(21))}')
print(f'Solution (167): {solution_bin(str(167))}')
print(f'Solution (28798): {solution_bin(str(28798))}')
print(f'Solution (10**308): {solution_bin(str(10**308))}') # 309 digits long number
