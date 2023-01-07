# Matrix is special case of 2-D Array where each data element of strictly same size. So every matrix is 2-D Array but not vice-versa

from numpy import * 
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,20,18],
   ['Sun',13,15,19,16]])
m = reshape(a,(7,5))
print(m)

# Accessing Elements of Array
print (a[1])        # Access Entire Row
print (a[1][2])     # Access particular Element in Row 1

# Appending Row
a_r = append (a, [['Avg',12,15,13,11]],0)  # We have to specify axis value i.e. 0 for ROW and 1 for Column
print(a_r)

# Adding Column
m_c = insert(a,[5],[[1],[2],[3],[4],[5],[6],[7]],1) # We have to specify axis value 1 here since column
print(a_r)
print(m_c)

# Delete ROW here Deleteing row 2 we know the index starts from 0 hence given value 1
d_r = delete(a,[1],0)
print(d_r)

# Delete Column 
d_c = delete(a,[3],1)
print(d_c)

# Update row
a[3] = ['Thu',0,0,0,0]
print (a)




