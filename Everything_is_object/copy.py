# # behaviour in C
# a = [1,2,3]
# b=a   # expection to store value of a into b

# a.append(4) # expection to change a only

# print("a = ",a)
# print("b = ",b)

a = [1,2,3]
b=a.copy()   

a.append(4) 

print("a = ",a)
print("b = ",b)