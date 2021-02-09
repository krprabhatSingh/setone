"""" Types of method : """

""" Inside Python class 3 types of method are allowed"""

""" 1. Instance Methods """
""" 2. Class Methods """
""" 3. Static Methods """

""" Instance Method """

""" Inside method implementation if we are using instance variables then such type of methods are called instance methods """
""" Inside instance method declaration, we have to pass self variable. """

""" def m1(self): """

""" By using self variable inside method we can able to access instance variables. """

""" Within the class we can call instance method by using self variable and from outside of the class we can call by
    using object reference."""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print('Hi', self.name)
        print('Your marks are :', self.marks)
    def grade(self):
        if self.marks>=60:
            print('you got first grade')
        elif self.marks >= 50:
            print('You got second grade')
        elif self.marks >= 35:
            print("you got third grade")
        else:
            print("you are failed")

n = int(input("Enter number of students:"))
for i in range(n):
    name = input("Enter Name:")
    marks = int(input("Enter Marks:"))
    s = Student(name, marks)
    s.display()
    s.grade()
    print()



"""" Setter and Getter Methods:"""

""" We can set and get the values of instance variables by using getter and setter methods."""

""" Setter Method"""

""" setter methods can be used to set values to the instance variables. Setter methods also known as mutator methods"""

"""syntax:"""

def setVariable(self,variable):
    self.variable = variable

""" Getter Method"""
""" Getter method can be used to get values of the instance variables. Getter method also known as accessor methods"""

""" Syntax : """
""" def getVariable(self):
         return self.variable"""

class Student:
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks

n = int(input("Enter number of students"))
for i in range(n):
    s = Student()
    name = input("Enter Name:")
    s.setName(name)
    marks = int(input('Enter Marks:'))
    s.setMarks(marks)

    print('Hi',s.getName())
    print('Your Marks are:', s.getMarks())
    print()



""" 2. Class Methods """


""" Inside method implementation if we are using only class variables(static variables), then such type 
    of methods we should declare as class method"""

""" We can declare class method explicitly by using @classmethod decorator."""
""" For class method we should provide cls variable at the time of declaration"""

""" We can call classmethod by using classname or object reference variable."""

"""Example"""

class Animal:
    legs = 4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs...'.format(name, cls.legs))
Animal.walk('Dog')
Animal.walk('Cat')


""" Example """

class Test:
    count = 0
    def __init__(self):
        Test.count = Test.count + 1
    @classmethod
    def noOfObjects(cls):
        print("The number of objects created for test class:", cls.count)


t1 = Test()
t2 = Test()
Test.noOfObjects()
t3 = Test()
t4 = Test()
t5 = Test()
Test.noOfObjects()