"""Class"""
""""In python every thing is an object."""
"""To create objects we required some Model or Plan or Blue print, which is nothing but class"""
"""We can write a class to represent properties(attributes) and actions (behaviour) of object"""

""" Properties can be represented by variables"""
""" Actions can be represented by method"""
""" So class is a template which contain variables and method"""

""" Define a class"""
# class className:

"""" There are three types of variables are allowed"""
""" 1. Instance Variable(Object Level Variables)"""
""" 2. Static Variables(Class Level Variables)"""
""" 3. Local Variables(Method Level Variables)"""

"""VARIOUS TYPES OF ALLOWED METHODS"""

""""1. Instance Methods"""
""" 2. Class Methods"""
""" 3. Static Methods"""

# Reference variables :
"""The variable which can be used to refer object is called reference variable"""
"""By using reference variable, we can access properties and methods of object"""

class Student:

    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def talk(self):
        print("My name is", self.name)
        print("My Rollno is:", self.rollno)
        print("My Marks are:", self.marks)

s1 = Student("Prabhat",100,80)
s1.talk()


"""" Self variable :"""

""" self is the default variable which is always pointing to current object(like this keyword in Java)"""
""" By using self we can access instance variables and instance methods of objects"""

"""" *** self should be first parameter inside constructor  def __init__(self)"""
"""" *** self should be first parameter inside instance methods"""

""" Constructor"""
""" Per object constructor will be executed only once. """
""" Constructor can take atleast one argument(atleast self)"""


"""" Variables :"""
"""" 1. Instance Variables: """
""" If the value of a variable is vary from object to object, then such type of variable are called instance variables """

""" For every object a separate copy of instance variable will be created"""


""" Where we can declare Instance variables:"""
""" 1. Inside Constructor by using self variable"""
""" 2. Inside Instance Method by using self variable"""
""" 3. Outside of the class by using object reference variable"""


"""" 1. Inside Constructor by using self variable:"""

""" We can declare instance variables inside a constructor by using self keyword."""
""" Once we creates object, automatically these variables will be added to the object"""

class Employee:
    def __init__(self):
        self.eno = 100
        self.ename = 'Prabhat'
        self.esal = 10000
e = Employee()
print(e.__dict__)


""" 2  Inside Instance Method by using self variable : """
""" We can also declare instance variables inside instance method by using self variable."""
""" If any instance variable declared inside instance method, that instance variable will be added once we call that method"""

class Test:

    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        self.c=30

t = Test()
t.m1()
print(t.__dict__)

""" 3. Outside of the class by using object reference variable : """

""" we can also add instance variables outside of a class to a particular object"""

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c=30

t=Test()
t.m1()
t.d=40
print(t.__dict__)


""" How to access Instance variables :"""
""" we can access instance variables with in the class by using self variable and outside of the class by using object
    reference"""

class Test:
    def __init__(self):
        self.a=10
        self.b=20

    def display(self):
        print(self.a)
        print(self.b)

t=Test()
t.display()
print(t.a,t.b)



"""Note""" """ Delete instance variables from the object"""

""" The instance variables which are deleted from one object, will not be deleted from other objects"""

class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40

t1=Test()
t2=Test()
del t1.a
print(t1.__dict__)
print(t2.__dict__)

""" If we change the values of instance variables of one object then those changes won't be reflected"""
""" to the remaining objects,because for every object we have separate copy of instance variables are available."""

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

t1=Test()
t1.a = 888
t1.b = 999
t2 = Test()
print('t1:', t1.a, t1.b)


""" Static variables:"""

"""if the value of a variable is not varied from object to object, such type of variables we have to declare with
in  the class directly but outside method. Such type of variables are called static variables."""

""" for total class only one copy of static variable will be created and shared by all objects of that class"""

class Test:
    x=10
    def __init__(self):
        self.y

t1=Test()
t2=Test()
print('t1:', t1.x, t1.y)
print('t2:', t2.x, t2.y)
Test.x = 888
t1.y = 999
print('t1:', t1.x, t1.y)
print('t2:', t2.x, t2.y)


""" Various places to declare static variables:"""

""" 1. In general we can declare within the class directly but from outside of any method"""
""" 2. Inside constructor by using class name"""
""" 3. Inside instance method by using class name"""
""" 4. Inside classmethod by using either class name or cls variable"""
""" 5. Inside static method by using class name"""


class Test:
    a = 10
    def __init__(self):
        Test.b = 20
    def m1(self):
        Test.c = 30
    @classmethod
    def m2(cls):
        cls.d1 = 40
        Test.d2 = 400
    @staticmethod
    def m3():
        Test.e = 50
print(Test.__dict__)
t = Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)
Test.f = 60
print(Test.__dict__)


"""" HOW TO ACCESS static variables:"""

""" 1. Inside constructor: by using either self or classname"""
""" 2. Inside instance method : by using either self or classname"""
"""3.  Inside class method: by using either cls variable or classname"""
""" 4. Inside static method : by using classname"""
""" 5. From outside of class: by using either object reference or classname"""


class Test:
    a = 10
    def __init__(self):
        print(self.a)
        print(Test.a)
    def m1(self):
        print(self.a)
        print(Test.a)
    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)
    @staticmethod
    def m3():
        print(Test.a)


t = Test()
print(Test.a)
print(t.a)
t.m1()
t.m2()
t.m3()