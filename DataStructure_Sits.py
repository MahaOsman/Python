# create an empty set
x = set()
# adding elements to a set

x.add(3)
x.add(2)
x.add(4)
x.add(1)
print(x)

# what happens when adding a duplicated value
x.add(1)
x.add(3)
# notice that no matter adding a duplicate nothing changes and won't be added again
print(x)

# removing a value from a set
x.remove(3)
print(x)

# displaying the length of a set
print(f"The set has {len(x)} elements")
