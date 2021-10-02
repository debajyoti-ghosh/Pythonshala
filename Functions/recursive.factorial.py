def factorial(n):
    if n in (0, 1): # base case
        return 1
    return factorial(n - 1) * n # recursive case

print("The factorial of 6 is :", factorial(6))
from math import ceil, sqrt
print (ceil(2.12)) 