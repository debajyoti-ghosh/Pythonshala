'''The __init()__ method is a special method that automatically
 gets called every time the objects are created.'''

class student:
    def check_pass_fail(self): # whenever we define methods for class we need to
                               # self as a first argument. This self represent the 
                               # object calling it. 
        if self.marks >= 40:
            return True
        else:
            return False
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

# instantiate the student class
student1= student("Rajib", 85)

print(student1.name)
print(student1.marks)




        
