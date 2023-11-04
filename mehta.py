#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#
def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        if divisor != n:
            yield divisor
        
def solve(n):
    #Get all posible proper divisors (you don't want remainders when divided)
    l = list(divisorGenerator(n))
    z = 0 #Stupid flag
    
    #Check if each divisor is an even perfect square
    for i in l:
        if i%2==0 and math.sqrt(i).is_integer():
            z+=1
            
    if z != 0:        
        ll = len(l)
        g = math.gcd(z, ll)
        z = int(z/g)
        ll = int(ll/g)
        return f"{z}/{ll}" 
    else: 
        return "0"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
