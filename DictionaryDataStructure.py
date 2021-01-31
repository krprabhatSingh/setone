""" Dictionary"""

""" We can use lit , tuple and set to represet a group of individual objects as a single entity"""

"""if we want to represent a group of objects as key- value pairs then we should go for dictionary."""

""" Duplicate keys are not allowed but values can be duplicated"""
""" Hetrogeneous objects are allowed for both key and values"""
""" Insertion order is not preserved"""
""""Dictionary are mutalble"""
"""Diconaries are dynamic"""
""" indexing and slicing concepts are not included"""

# create a dictionary
d = {} or d = dict{}

d[100] = "name"
d[200] = "Address"
print(d)

or

d = {100:'name', 200:'Address'}

# Access data from the dictionary :
print(d[100])
print(d[200])

""" update dictionaries"""

d = {100:"Prabhat", 200:"Rohan", 300:"Piyush"}
print(d)
d[100] = "Kunal"
print(d)
# Delete element from dictionary
del d[100]
print(d)
# To remove all entries from the dictionaries
d.clear()
# to delete total dictionary
del d
print(d) # NameError , d is not defined

"""Function in dictioary"""

""" dict() : to create an empyt dictionary"""
d = dict()