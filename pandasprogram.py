import pandas as pd
# import xlrd
# import openpyxl
df = pd.read_excel("F:\Prabhat\EmployeeData.xlsx")
print(df)
""" Operations on data frame: """

""" Knowing number of rows and column"""
""" shape is the attribute which return tuple"""
print(df.shape)

# Retrieve only rows :
r, c = df.shape
print(r)
# Retrieve only column
print(c)


"""Retrieving Rows from Data Frame"""
"""The method head() gives the first  5 rows and the method tail() returns the last 5 rows, as shown below"""


print(df.head())
print(df.tail())

"""To display only first two rows we need to pass the some values"""

print(df.head(2))

""" Similarly for last two rows we need to pass values in tail function"""

print(df.tail(2))

""" Retrieving a range of rows"""

""" WE can treat dataframe as an object, and retrieve the rows from it using slicing. """
print("fetching rows through slicing")
print(df[1:2])

# Display rows in alternate rows.
print(df[0::2])
# Displaying alternate rows
print(df[::2])

# To Display the rows in reverse order :
print(df[3:4:-1])

"""To Retrieve Column Name"""
""" To retrieve the column names from the data frame, we can use columns attribute as: """

print(df.columns)

""" To retrieve the list of  column data"""

print(df[['EmpID','Ename']])

""" Finding Maximum and Minimum Values"""
"""using max() method we can find the highest values, and with the help of min() method we can find lowest values"""

print(df['Sal'].max())
print(df['Sal'].min())

""""Displaying Statical Information"""
""" We have describe() method that displays very important information like number of values, average, standard deviation, minimum, maximum, 25%, 50% and 75% 
of the total values"""

print(df.describe())

"""" Performing Queries on all rows"""

print([df.Sal>10000000])

# To retrieve the row where salary is maximum, we can write:

print(df[df.Sal == df.Sal.max()])

# To retrieve the rows where Salary is minimum.

print(df[df.Sal == df.Sal.min()])

# To display EmpID, and Name where salary is greater than 10000

print(df[['EmpID','Ename']][df.Sal>10000])


""" Knowing the Index Range"""