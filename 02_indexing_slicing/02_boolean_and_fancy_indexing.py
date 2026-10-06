import numpy as np

OneD = np.array([10, 20, 30, 40, 50, 60])
TwoD = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
ThreeD = np.arange(1, 25).reshape(2, 3, 4)

#Condition on Array

#1D array
print(OneD>30)

# Print a Boolean array showing which elements of OneD are less than 40
print(OneD<40)

#2D Array
print(TwoD<5)

#3D Array
print(ThreeD<5)

# 2. Comparison operators

#  ==
print(OneD == 40)

# >, <,
#  >=, # <=,
print(TwoD>=5)
#  !=

print(ThreeD != 5)

#3. Boolean masks
# A Boolean mask is an array of True and False values used to select elements.

mask = (OneD > 30)
print(OneD[mask]) #Gives only true values

mask = (TwoD%2 == 0)
print(TwoD[mask])

# Create a mask for elements greater than or equal to 40, then use it to select the matching values.

mask = OneD >= 40
print(OneD[mask])

# 4. Filtering data- To Filter the data present in array(Masking but indirect)

print(OneD[OneD > 35])
print(TwoD[TwoD%2 != 0])
print(ThreeD[ThreeD%2 ==0])

# 5. Multiple conditions — AND (&)
# Both conditions must be true. Put parentheses around each condition.

print(OneD[(OneD >= 20) & (OneD <= 40)])

# Select values from OneD that are greater than 10 AND less than 50.
print(OneD[(OneD>10)&(OneD<50)])

print(TwoD[(TwoD%2 != 0) & (TwoD > 5)])

# 6. Multiple conditions — OR (|)
print(OneD[(OneD < 20) | (OneD > 50)])

# NOT (~)
# Reverses the Boolean mask: True becomes False, and vice versa.

mask = OneD < 35
print(OneD[~mask])

# Create a mask for values equal to 30, then use ~ to select all values that are not 30.

mask = (TwoD == 4) #4 Bahek Sabai aaucha
print(TwoD[~mask])

# 8. Boolean indexing on 2D arrays
print(TwoD[TwoD > 10])

# Select all values in TwoD that are less than or equal to 6.
print(TwoD[TwoD <= 6])

# 9. Boolean filtering with multiple conditions on 2D arrays

print(TwoD[(TwoD >= 5) & (TwoD <= 10)])

# Select all values in TwoD that are greater than 8 OR less than 4.
print(TwoD[(TwoD > 8) | (TwoD < 4)])

# Boolean indexing on 3D arrays
print(ThreeD[ThreeD > 20])
# Select all values in ThreeD that are less than 5 OR greater than 20.

print(ThreeD[(ThreeD < 5)|(ThreeD > 20)])

# Fancy Indexing
# Fancy indexing means selecting elements using lists or arrays of indices.

# 11. Select multiple 1D indices

# OneD[ [0, 2, 4] ]
# │    └───────────► 2. The List: A Python list of specific index positions you want
# └────────────────► 1. The Indexing Tool: Tells NumPy "pull out these positions"
print(OneD[[0, 2, 4]])

# Select the elements at indices 1, 3, and 5.
print(OneD[[1,3,5]])

# 12. Select indices in any order
print(OneD[[3,4,1,5,4]])

# Select elements at indices 5, 0, and 2, in that order.
print(OneD[[5,0,2]])

# 13. Select the same index multiple times
print(OneD[[2, 2, 0]])

# Select indices 1, 1, 4, and 1.
print(OneD[[1,1,4,4,1,1]])

# 14. Select multiple rows
# The first index list chooses rows; : keeps every column.

print(TwoD[[0,2],:])

# Select rows 1 and 3 from TwoD, including all columns.
print(TwoD[[1,3],:])

# 15. Select multiple columns
# The : keeps every row; the index list chooses columns.
print(TwoD[:,[0,2]])

# Select columns 1 and 3 from TwoD, including all rows.
print(TwoD[:,[1,3]])

# 16. Combine row and column selection
# np.ix_() creates a combination of the chosen rows and columns.

print(TwoD[np.ix_([0, 2], [1, 3])])

# Select rows 1 and 3 and columns 0 and 2 together using np.ix_().

print(TwoD[np.ix_([1,3],[0,2])])

# 17. Fancy indexing combined with slicing
print(TwoD[[0, 2], 1:4])

# Select rows 1 and 3, but only columns from index 0 up to (excluding) index 2.
print(TwoD[[1,3],0:2])

# TwoD[slice][fancy]- This is for if you want to row index and row slice OR COLUMN slice and column index(both not possible)

print(TwoD[0:2, [1, 3]])
# 18. Fancy indexing on a 3D array

print(ThreeD[[0, 1], 0, 0])

# Select row 1, column 2 from both layers of ThreeD.
print(ThreeD[[0, 1], 1, 2])

# 19. Fancy indexing combined with Boolean indexing
selected = OneD[[0, 2, 4]]
print(selected[selected > 20])

# First select indices 1, 2, 3, and 5 from OneD. From those selected values, print only the ones greater than 30.
selected = OneD[[1,2,3,5]]
print(selected[selected > 30])

i = type(selected)
print(i.__name__)