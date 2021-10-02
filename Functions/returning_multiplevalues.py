def add_product (a,b):
    # print("The addition of ",a," and ",b," is: ",a+b)
    return a+b,a*b

c = add_product(2,3)
print("The addition is: ",c[0])
print("The product is: ",c[1])