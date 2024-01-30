"""
Filename: A1.py
Author: Joshua Nichols
Last Modified: 1/22/2024
"""
from itertools import count
def prime_gen():
    """
    This generator function will generate an infinite number of primes
    """

    
    yield 2
    prime_cache = []
    n = 3
    while True:
        is_prime = True
        for p in prime_cache:
            if n % p == 0:
                is_prime = False
                break
            if p > int(n ** 0.5 + 1):
                break
        if is_prime:
            prime_cache.append(n)
            yield n
        n += 2

   



i = 1
for x in prime_gen():   #prints the millionth prime number generated
    if i == 1_000:
        print(x)
        print(i)
        break
    i += 1
    

                
            
        

