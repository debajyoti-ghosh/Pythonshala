class student:
    def check_pass_fail(self): # whenever we define methods for class we need to
                               # self as a first argument. This self represent the 
                               # object calling it. 
        if self.marks >= 40:
            return True
        else:
            return False

# instantiate the student class
student1= student()


student1.name = "Rajib"
student1.marks = 85

# call instance methods or access the method of clasd
did_pass = student1.check_pass_fail()
#we have called check_pass_fail method using student1 object, we have called this method without
# passing any arguments, however the method defination has an argument self

# But here the self represnt the student1 object and self.marks refers to the marks attribute of student1
print(student1.name,"has passed the exam - ", did_pass)
        
