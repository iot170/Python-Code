from array import *
vals = array('i', [5, 8, 7, 6, 5, 4])
#
# # PRINT THE ALL LIST ONE BY ONE
# for i in vals:
#     print(i)
# PRINT REVERSE LIST
# vals.reverse()

# PRINT BY INDEX NUMBER
# print(vals [0])

# PRINT ADDRESSES AND SIZE
# print(vals.buffer_info())

# PRINT LIST USING LENGTH FUNCTION
# for i in range(len(vals)):
#     print(i)

# ALSO WORK WITH CHAR

#  from array import *
#  vals = array('u', ['a', 'b', 'c', 'd'])
#
# # PRINT THE ALL LIST ONE BY ONE
# for i in vals:
#     print(i)

# Print new array using old array values|

# vals = array('i', [2, 4, 5, 6])
# New array
# newArr = array(vals.typecode, (a for a in vals))

# Also print the square of the old list
# newArr = array(vals.typecode, (a*a for a in vals))

# PRINT THE ALL LIST ONE BY ONE
# for i in newArr:
#     print(i)

# Using while loop
i = 0
while i<len(vals):
    print(vals[i])
    i+=1

