# Tuturial Point DS in Python
# Array operation can be
# CRUD, plus traverse thru all elements

# 1. READ Traverse and Print all elements
from array import *
newArray = array('i', [10,20,30,40,50]) # where i is type code which means signed integer of 2 bytes
for x in newArray:
    print (x)
    
# 2. READ and Print particular element of Array i.e. R(Read) in CRUD
print (newArray[1])

# 3. INSERT / CREATE a element at position 2
newArray.insert(2,80)
print ('Inserting New Element')
for x in newArray:
    print (x)
    
# 4. UPDATE a element
print ('Updating Element')
newArray[3] = 100 # Update the array at position 3 with value 100
for x in newArray:
    print (x)
    
# 5. Remove DELETE the element from the Array
print ('Remove element')
newArray.remove(40) # Removes 40 from Array
for x in newArray:
    print (x)
    
    
    
    



