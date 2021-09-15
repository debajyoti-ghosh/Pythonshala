# arguments.keyword
def func(a, b, c):
 print(a, b, c)
func(a=1, c=2, b=3) # prints: 1 3 2

# arguments.default.py
def func(a, b=4, c=88):
 print(a, b, c)
func(1) # prints: 1 4 88
func(b=5, a=7, c=9) # prints: 7 5 9
func(42, c=9) # prints: 42 4 9
func(42, 43, 44) # prints: 42, 43, 44



# arguments.default.error.py
def func(a, b=4, c=88):
 print(a, b, c)
func(b=1, c=2, 42) # positional argument after keyword one
