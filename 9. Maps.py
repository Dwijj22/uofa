# Maps are also called ChainMap, which chains multiple dictionary as one unit, It contains key:value pair-
# -without duplicate keys, part of collections

import collections
dict1 = {'day1':'Mon', 'day2':'Tue'}
dict2 = {'day3':'Wed', 'day1':'Thu'}

resDict = collections.ChainMap(dict1, dict2)

# Print full ChainMap
print (resDict)

# Print Keys
print (list(resDict.keys()))

# Print Values
print (list(resDict.values()))

# Print all values of Maps
print('Elements')

for key , value in resDict.items():
    print(key,value)
    
# Updating Map
# When the element of the dictionary is updated, the result is instantly updated in the result 
# -of the ChainMap. In the below example we see that the new updated value reflects in the result -
# -without explicitly applying the ChainMap method again.

# Example
import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day4': 'Thu'}

res = collections.ChainMap(dict1, dict2)
print(res.maps,'\n')

dict2['day4'] = 'Fri'
print(res.maps,'\n')
