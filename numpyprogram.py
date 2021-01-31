# A python program to accept two matrices and find their products :

import sys
from numpy import *

# accept number of rows and cols of fist matrix into r1, c1
r1, c1 = [int(a) for a in input("First matrix rows, cols:").split()]

# Accept number of rows and columns of 2nd matrix r2, c2

r2, c2 = [int(a) for a in input("Enter matrix rows, cols:").split()]

# Test the condition if c1!= r2 then multiplication is not possible
if c1!= r2:
    print('Multiplication is not possible')
    sys.exit()  # Terminate the program

# Accept first matrix elemetns as a stirng into str1
str1 = input('Enter first matrix elements: 555555555555555555555555555555555555555555555555\n')

# Convert str1 into a matrix whith size r1*c1

x = reshape(matrix(str1), (r1, c1))

# Accept second matrix elemtns as a string into str2
str2 = input("Enter 2nd elemetns as string:55555555555555555555555555555555555" \)