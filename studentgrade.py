

# Instance methods

""" Inside method implementation if we are using Instance variables then such type of methods are called Instance mehtod"""

""" Inside Instance method declaration, we have to pass self variables."""

""" def m1(self) """

""" By using self variables Inside mehtod we can able to access Instance variables"""

""" Within the class we can call Instance method by using self variables and from outside of the class we can
    call  by using object reference."""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def dispaly(self):
        print("Hi", self.name)
        print("Your marks are:", self.marks)

    def grade(self):
        if self.marks >= 60:
            print("you got first division")
        elif self.marks >= 50:
            print("You got 2nd grade")
        elif self.marks >= 35:
            print("You got third grade")
        else:
            print('You are failed')


nuberofcandiate = int(input("Number of candidates"))
for i in range(nuberofcandiate):
    name = input("Enter Name:")
    marks = int(input('Enter Marks'))
    s = Student(name, marks)
    s.dispaly()
    s.grade()
