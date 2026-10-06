import numpy as np

OneD = np.array([10, 20, 30, 40, 50])

# 10 ➔ [0] or [-5] (First element)

# 20 ➔ [1] or [-4]

# 30 ➔ [2] or [-3] (Middle element)

# 40 ➔ [3] or [-2]

# 50 ➔ [4] or [-1] (Last element)

TwoD = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# 2D Indexing
# Syntax: array[row, column]

TwoD = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Positive Indexing
# Rows:    0        1        2
# Columns: 0  1  2
#
#          col
#           ↓
# row 0 → [1, 2, 3]
# row 1 → [4, 5, 6]
# row 2 → [7, 8, 9]

# TwoD[row, column]

# Negative Indexing
# Rows:   -3       -2       -1
# Columns: -3  -2  -1
#
#          col
#           ↓
# row -3 → [1, 2, 3]
# row -2 → [4, 5, 6]
# row -1 → [7, 8, 9]

# Positive:
# First row    → row index 0
# Second row   → row index 1
# Third row    → row index 2
#
# First column  → column index 0
# Second column → column index 1
# Third column  → column index 2

# Negative:
# Last row          → row index -1
# Second-last row   → row index -2
# First row         → row index -3
#
# Last column       → column index -1
# Second-last       → column index -2
# First column      → column index -3


ThreeD = np.arange(1, 25).reshape(2, 3, 4) 

#1D indexing
print(OneD[0])
print(OneD[1])
print(OneD[2])
print(OneD[3])
print(OneD[4])

#1D Positive Indexing
print(OneD[0])
print(OneD[4])
print(OneD[1])
print(OneD[2])

#1D Negative Indexing
print(OneD[-1])
print(OneD[-5])
print(OneD[-4])
print(OneD[-3])

#1D Indexing With Variables

# Store an index in a variable and use it
A = OneD[4]
print(A+5)

#  Store different indexes in different variables
A = 1
print(OneD[A])

print("2D Arrays")
# Positive indexing
print(TwoD[0,0])
print(TwoD[0,1])
print(TwoD[1,0])
print(TwoD[1,2])
print(TwoD[2,1])
print(TwoD[2,2])

# Negative indexing
print(TwoD[-1,-1])
print(TwoD[-1,-3])
print(TwoD[-3])
print(TwoD[-2])
print(TwoD[:,-2])
print(TwoD[-1,-1])

# Indexing with variables

#  Store row index in a variable
row = 1
print(TwoD[row])

#  Store column index in a variable
coln = 0
print(TwoD[:,0])

# Change row/column variables and observe
TwoD[0,0] = 5
TwoD[1,1] = 6

print(TwoD)

# 3D Indexing

# 3D Indexing
# Syntax: array[layer, row, column]

# Positive Indexing
# Layer:  0, 1
# Row:    0, 1, 2
# Column: 0, 1, 2, 3
#
# ThreeD[layer, row, column]

# Negative Indexing
# Layer:  -2, -1
# Row:    -3, -2, -1
# Column: -4, -3, -2, -1
#
# -1 → last element in that dimension
#
# ThreeD[layer, row, column]
#
# Positive → starts from 0
# Negative → starts from -1

ThreeD = np.arange(1, 25).reshape(2, 3, 4) 

#Positive Indexing

print(ThreeD[0,0,0])
print(ThreeD[1,2,3])
print(ThreeD[0,1,1])
print(ThreeD[1,2,3])
print(ThreeD[0,1,3])
print(ThreeD[1,2,3])

#Negative Indexing
print(ThreeD[-1,-1,-1])
print(ThreeD[-2])
print(ThreeD[:,-1])
print(ThreeD[:,:,-1])
print(ThreeD[-2,-1,-1])
print(ThreeD[0,-1,2])

# Indexing with variables
layer = 1
print(ThreeD[layer])
row = 2
print(ThreeD[:,row])
coln = 1
print(ThreeD[:,:,coln])
print(ThreeD[layer,row,coln])

#Slicing of Array

# : means “take this range

#Syntax : array[start : stop : step]

#1)Basic Slicing [start : stop]

A = np.array([1,2,3,4,5,6,7,8,9,10])

# Slice from index 2 up to (but excluding) index 6
print(A[2:6]) 

#Slice from beginning but excluding index 4
print(A[:4])

#Slicing from one index number to end
print(A[5:])

#Return Full copy of array
print(A[:])

#2)  array[start:stop:step]

#Starting from 0 till index 8(Excluding) with 2 steps
print(A[0:8:2])

#Print All numbers from beginning to end but step 3
print(A[::3])

#Negative Index #Starts from the last(reverses the array)
print(A[::-1])

#Start at index 7 to index 2 -2 at each step
print(A[7:2:-2]) #[8 6 4]
print(A[7:2:2]) #Returns Empty

#Last Three elements
print(A[-3:])

print(A[-4:-1])

# 2D Slicing

B = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]])

# array[row_slice, column_slice]

#  Select rows

#First Row
print(B[0])

#Second Row
print(B[1])

#Third Row
print(B[2])

#Fourth Row
print(B[3])

#  Select columns
#First Column
print(B[:,0])

#Second Column
print(B[:,1])

#Third Column
print(B[:,2])

#Fourth Column
print(B[:,3])
#  Select a rectangular section
print(B[0:2,0:3])
#  Slice specific rows + columns
print(B[0:2,0:3])
print(B[0:1,1:3])

# array[row_start : row_stop : row_step , col_start : col_stop : col_step]
#  Reverse rows

#First Row
print(B[::-1])
#  Reverse columns
print(B[:,::-1])
#  Step through rows
print(B[::2])
#  Step through columns
print(B[:,::2])

# 3D Slicing

#  array[layer_slice, row_slice, column_slice]
# array[
#     d_start : d_stop : d_step,  # Axis 0: Depth / Layer / Page
#     r_start : r_stop : r_step,  # Axis 1: Rows
#     c_start : c_stop : c_step   # Axis 2: Columns
# ]

A= np.arange(1,31).reshape(2,3,5)
print(A)
#  Select layers

#first Layer
print(A[0])

#Second Layer
print(A[1])

#  Slice rows inside layers
print(A[0,0:1])
#  Slice columns inside layers
print(A[:,:,0])
#  Slice layers + rows + columns together
print(A[0:1,0:2,0:3])

#  Reverse layers
print(A[::-1])
#  Reverse rows
print(A[:,::-1])
#  Reverse columns
print(A[:,:,::-1])

#  Step slicing across dimensions

#Steps Across layers
print(A[::1,:,:])

#Steps Across Rows
print(A[::1,::2,:])

#Steps Across Columns
print(A[:,:,::2])