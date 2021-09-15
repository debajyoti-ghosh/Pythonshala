def minimum(*n):
    # print(type(n)) # n is a tuple
    if n: # explained after the code
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)
minimum(1, 3, -7, 9) # n = (1, 3, -7, 9) - prints: -7
minimum() # n = () - prints: nothing



'''Have you noticed how we checked whether n wasn't empty with a
simple if n:? This is because collection objects evaluate to True
when non-empty, and otherwise False in Python. This is true for
tuples, sets, lists, dictionaries, and so on.
One other thing to note is that we may want to throw an error when
we call the function with no arguments, instead of silently doing
nothing. In this context, we're not concerned about making this
function robust, but in understanding variable positional
arguments.'''


####Let's make another example to show you two things that, in my experience, are
# confusing to those who are new to this

def func(*args):
    print(args)
values = (1, 3, -7, 9)
func(values) # equivalent to: func((1, 3, -7, 9))
func(*values) # equivalent to: func(1, 3, -7, 9)
def func(a,b,c):
    print(a,b,c)
func(1,3,9)
