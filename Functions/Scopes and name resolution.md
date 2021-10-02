Let's start with a very simple example:
# scoping.level.1.py
    def my_function():
        test = 1 # this is defined in the local scope of the function
        print('my_function:', test)
    test = 0 # this is defined in the global scope
    my_function()
    print('global:', test)
I have defined the test name in two different places in the previous example. It is
actually in two different scopes. One is the global scope (test = 0), and the other is
the local scope of the my_function function (test = 1). If you execute the code,
you'll see this:
# C:\Users\Papai\Documents\git\Pythonshala> python scoping.level.1.py
    my_function: 1
    global: 0
It's clear that test = 1 shadows the test = 0 assignment in my_function. In the
global context, test is still 0, as you can see from the output of the program, but we
define the test name again in the function body, and we set it to point to an integer
of value 1. Both the two test names therefore exist, one in the global scope, pointing
to an int object with a value of 0, the other in the my_function scope, pointing to an
int object with a value of 1. Let's comment out the line with test = 1. Python
searches for the test name in the next enclosing namespace (recall the LEGB rule:
local, enclosing, global, built-in described in Chapter 1, A Gentle Introduction to
Python) and, in this case, we will see the value 0 printed twice. Try it in your code.
Now, let's raise the stakes here and level up:
# scoping.level.2.py
    def outer():
        test = 1 # outer scope
        def inner():
            test = 2 # inner scope
            print('inner:', test)
        inner()
        print('outer:', test)
    test = 0 # global scope
    outer()
    print('global:', test)