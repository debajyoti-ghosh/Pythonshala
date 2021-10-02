class student:
    pass        # as class without any attribute or method are not allowed so pass statement is added.

student1= student() # object,named student1 of class, named student is created
student2 = student() # another instant or object of the same class

student1.name = "Rajib" # attributs added to the object, though not a proper way 
student1.marks = 85 # to add attributes to the objects, usually we want to put attributes inside the class,
# so that all the objects created from the class have these attributes by default
# similarly we also put methods inside the class, so the all the objects can access them

print(student1.name)
print(student1.marks)