# Dictionary are Key:value type of array e.g family[elderSon]='dwij' here elderSon is key and dwij is value for e.g family = {'father':'ravi', 'elderSon': 'dwij', 'mother':'prathima', 'youngerSon';'samvid'}

# In Dictionary Key cannot be duplicate e.g. if have two keys with same name then last key value will be considered.

family = {'father':'ravi', 'elderSon': 'dwij', 'mother':'prathima', 'youngerSon':'samvid'}



print(family['elderSon'])
print(family['mother'])

#Add to Dictionary
family['grandfather'] = 'Nagaraj' 

#Update a Dictionary  
family['father'] = 'Ravikumar Nagaraja' 

print (family['grandfather'])

#Delete a Dictionary
del family['grandfather']

#Duplicate Key i.e. Name which has value Zara and also Manni, hence the code below will print Manni, which is last key;value pair from Left to right
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print (dict['Name'])


#Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys but something like ['key'] is not allowed.

#Example
#An example is as follows −

#!/usr/bin/python

dict = {['Name']: 'Zara', 'Age': 7}
print( dict['Name'])
#Output
#When the above code is executed, it produces the following result −

#Traceback (most recent call last):
#   File "test.py", line 3, in <module>
#      dict = {['Name']: 'Zara', 'Age': 7};
#TypeError: list objects are unhashable



