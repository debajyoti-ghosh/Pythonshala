# """ Returns prime numbers till N, included"""
from math import sqrt, ceil
def prime_num (n) :
    list_prime = []    
    if n < 2:
        print("Prime number starts from 2.")
    for candidate in range (2,n+1):
        is_prime = True
        root = ceil(sqrt(candidate))
        for prime in list_prime:
            if prime > root:
                break
            elif candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            list_prime.append(candidate)
    return list_prime

print("Prime number till 11 is: ",prime_num (11))



# # primes.py
# from math import sqrt, ceil
# def get_primes(n):
#     """Calculate a list of primes up to n (included). """
#     primelist = []
#     for candidate in range(2, n + 1):
#         is_prime = True
#         root = ceil(sqrt(candidate)) # division limit
#         for prime in primelist: # we try only the primes
#             if prime > root: # no need to check any further
#                 break
#             if candidate % prime == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primelist.append(candidate)
#     return primelist
       
# print("Prime number till 8 is: ",get_primes (8))