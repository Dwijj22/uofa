# Set is colleciton of item not in order, Similar to maths but with following three conditions
# 1. The elements in set cannot be duplicate
# 2. Immutable i.e. elements are not modifiable
# 3. No Index, hence no slicing

# Create set, by set keyword or by {}

Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]) # Create by set keyword
Months={"Jan","Feb","Mar"}                            # Create by {}
Dates={21,22,17}                                      # Create by {}

print(Days)
print(Months)
print(Dates)

# Access values in set
for d in Days:
    print(d)

# Add Elements to set
Days.add("Sun")
print(Days)

# Remove Elements to set
Days.discard("Sun")
print(Days)

# Union (Distinct Elements of both sets)

DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
UnionDays = DaysA|DaysB
print(UnionDays)

# Intersection (Common elements of both sets)
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
IntDays = DaysA & DaysB
print(IntDays)

# Difference of Sets (Give a set of containing only first set by removing common elements which is in both first and second sets)
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
DiffDays = DaysA - DaysB # Will print only Mon, Tue
print(DiffDays)

# Compare Sets (Give subset or superset), Will result in True or false
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)