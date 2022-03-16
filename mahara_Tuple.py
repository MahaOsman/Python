"""

First Note when declaring Tuples it's known whith ,

"""
tuple_one = 1, 2, 3, 4
tuple_two = (2, 4, 5, 7)
print(type(tuple_one))
print(type(tuple_two))

# summing 2 tuples
new_tuple = tuple_one+tuple_two
# note that you can have a duplicated value
print(new_tuple)

# display a value with index
print(tuple_one[1])
# adding a new value
# tuple_one[4] = 10
tuple_one = 1, 2, 3, 5, 10
print(tuple_one)
"""
you can't it's a type error 
the only way to update a tuple is to update the whole tuple
"""
