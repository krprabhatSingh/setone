"""" Setter and Getter Methods: """

""" We can set and get the values of instance variables by using getter and setter method"""

""" Setter Method: """

""" Setter methods can be used to set values to the instance variables. Setter methods also known as mutator methods"""

""" Syntax:"""
""" def setVariable(self,variable):
    self.variable = variable"""

""" Examples:"""
""" def setName(self,name):
    self.name = name"""


""" Getter Method"""
""" Getter methods can be used to get values of the instance variables. Getter methods also known as accessor methods."""

""" def getVariable(self):
    return self.variable"""

""" Examples : """

""" def getName(self):
    return self.name"""


class Student:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

n = int(input('Enter number of students:'))
for i in range(n):
    s = Student()
    name = input("Enter name")
    s.setName(name)
    marks = int(input('Enter Marks:'))
    s.setMarks(marks)

    print('Hi', s.getName())
    print('Your marks are;', s.getMarks())