# -*- coding: utf-8 -*-
"""
Objective: Test distribution of primes

Created on Tue Nov 17 09:30:49 2015

@author: Pramod Mathai
"""
         
from IPython import get_ipython
get_ipython().magic('reset -sf') # clear workspace
import math, numpy as np 
    

def sum_of_primes_Sieve(Number):
# Sieve for computing list of primes    
  in_sieve = np.arange(2,(1+Number)) # sieve the composites out of this list
  factor = 2
  factor_idx = 0
  while factor <= math.ceil(np.sqrt(Number)) : # All composites less than 'Number' must have a 'factor' in this range   
    remove_this  = np.arange(2*factor, (factor*math.floor(Number/factor) + factor), factor) # 'factor' is a prime; we remove its multiples from in_sieve in the next line    
    in_sieve     = sorted(list(set(in_sieve) - set(remove_this))) # More efficient sieving? 
    factor_idx   = factor_idx + 1
    factor       = in_sieve[factor_idx]
      
  sum_exact = np.dot(in_sieve,np.ones(len(in_sieve))) 
  
  print("Based on sieving:")
  print("1. Number of primes <=%d is %d"%(Number, len(in_sieve)))
  print("2. Largest prime <=%d is %d"%(Number, in_sieve[len(in_sieve) - 1]))
  
  return{'exact_sum_primes':sum_exact}       
          
          
def main():   
  print ('')
  print ('This script will use a sieve to find all the primes <= N, a natural number. Sieve takes a few seconds to compute for N = 10^6.') 
  print ('It will display the exact sum of those primes as well as an estimate of that sum that relies on a prime-number-theorem (PNT) based heuristic.')
  N = int(input("Input N (>2) :"))
 
  Sum_Sieve = sum_of_primes_Sieve(N)   
  
  print("3. Exact sum of primes <=%d is %e."%(N, Sum_Sieve['exact_sum_primes']))  
  print("Estimated sum of primes <=%d is %e, using a PNT based heuristic."%(N, pow(N, 2)/(2*np.log(N)))) # Based on PNT based heuristic


main()








