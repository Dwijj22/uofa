# Array within array are called two dimensional (2-D array), array elements are accessed by two indcies compared to 1-D array
# Consider days temperatures measured at certian interval of time of day as below representated as arry as follows

""" 
Day 1 - 11 12 5 2 
Day 2 - 15 6 10 
Day 3 - 10 8 12 5 
Day 4 - 12 15 8 6  
"""

from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

#Print first Row
print ( T[0] )

#Print first Row second element
print ( [T[0][1]] )

# To Print entire array
for r in T:                 # For row r in T(2-D array)
    for c in r:             # For column c in row r
        print (c, end = " ") # Seperate the elements of array with space i.e. end = " "
    print ()                # To print the next row in next line this is equivalent to print /n in the previous print



# Inserting value to Array
T.insert(2, [0,5,11,13,6])
for r in T:
   for c in r:
      print(c,end = " ")
   print()
   
# update value to Array
T[2] = [11,9]
T[0][3] = 7
for r in T:
   for c in r:
      print(c,end = " ")
   print()

# Deleting value in array
del T[3]

for r in T:
   for c in r:
      print(c,end = " ")
   print()
   