number1 = 5
string1 = "Hello! Test type()"
list1 = [1,2,3]
dic1 = {'a': 2, 'b':5}
def my_function():
    pass

list_all = [number1,string1, list1, dic1, my_function]
print(list_all)
print(*[type(x) for x in list_all],sep='\n')
