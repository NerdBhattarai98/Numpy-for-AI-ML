import numpy as np

A = np.array([
    [12, 25, 8, 40],
    [5,  30, 15, 45],
    [20, 10, 35, 50],
    [3,  18, 28, 60]
])

# Select every value greater than 25.
print(A[A>25])

# Select values between 10 and 40, inclusive.

print(A[(A >= 10) & (A <= 40)])

# Select rows 0 and 2.
print(A[[0,2]])

# Select columns 1 and 3.
print(A[:,[1,3]])

# Select rows 1 and 3 with columns 0 and 2.

A[np.ix_([0, 2], [1, 3])]

# Select all values greater than 20 OR less than 10.

print(A[(A < 10) | (A > 40)])

#AI Gen Practice Qns
OneD   = np.array([10, 20, 30, 40, 50, 60])
TwoD   = np.arange(1, 17).reshape(4, 4)
ThreeD = np.arange(1, 25).reshape(2, 3, 4)

# Part A: Indexing and slicing
# Print the last element of OneD with a negative index, then the bottom-right element of TwoD with negative indexes.
print(OneD[-2:])
print(TwoD[-1,-1])
# Set r, c = 2, 3 and print TwoD[r, c]. Then use a for i in range(4) loop to print the main diagonal TwoD[i, i].

r = 2
c = 3

print(TwoD[r,c])

for a in range(4):
    print(TwoD[a,a])

    

# Print the four corners of TwoD as a 2x2 array using one slice expression (hint: use a step).
print(TwoD[0:4:3,0:4:3])
# Extract the middle 2x2 block of TwoD, then print it with its rows reversed.

new2by2 = A[1:3,1:3]
print(new2by2)
print(new2by2[::-1])
# Predict, then print the .shape of each: 
# TwoD[1], TwoD[1:2], TwoD[:, 1], TwoD[:, 1:2], ThreeD[0, :, 1]. 
TwoD   = np.arange(1, 17).reshape(4, 4)
print(TwoD)
print(TwoD[1])
print(TwoD[1:2])
print(TwoD[:, 1:2])
print(ThreeD)
print(ThreeD[0, :, 1])
# Explain which ones lose a dimension and why.


# From ThreeD, get the last column of every layer (should be shape (2, 3)) and the first row of the second layer.
print(ThreeD)

print(ThreeD[:,:,-1])
print(ThreeD[1,0])
# Make m = TwoD.copy() and turn it into a checkerboard of zeros: set m[::2, ::2] = 0 and m[1::2, 1::2] = 0. Print it.

m = TwoD.copy()
m[::2, ::2] = 0
m[1::2, 1::2] = 0
print(m)



# Part B: Boolean and fancy indexing
# From ThreeD, select all values that are divisible by 3 and greater than 10.

print(ThreeD[(ThreeD%3 == 0)&(ThreeD > 10)])
# Count how many elements of TwoD are greater than 8 without a loop. (Hint: True counts as 1, so try .sum() on the mask.)
mask = TwoD >= 8
newarr = np.array(TwoD[mask],dtype= bool)
print(newarr)
sum = newarr.sum()
print(sum)
# Select values of OneD that are not between 20 and 40, once with | and once with ~. Check both give the same result.

print(OneD[~(OneD < 20)|(OneD > 40)])
print(OneD[(OneD < 20)|(OneD > 40)])

# Make a copy of TwoD, replace every even number with -1, and confirm with np.array_equal that the original didn't change.

copy = TwoD.copy()
copy[copy%2 == 0] = -1
print(copy)

print(np.equal(copy,TwoD)) 
# np.equal()-compares two arrays element-by-element and returns a boolean array of True and False values.


# Use np.where to build a new array from TwoD where values greater than 10 become 0 and the rest stay unchanged. 
# Is TwoD modified?
# np.where()-np.where() is basically NumPy's instant if-else tool that lets you swap 
# Arguments: (Condition, Value IF True, Value IF False)
# array values or pinpoint their exact index positions based on a condition

newarr = np.where(TwoD>10,0,TwoD) #If trie then 0 if false then value of TwoD only
print(newarr)
print(TwoD)

#No changes to the original array

# Reorder the rows of TwoD as [3, 1, 0, 2] using fancy indexing, then reverse the columns using fancy indexing (not ::-1).

print(TwoD[0])

print(TwoD[[3,1,0,2]])

print(TwoD[[3,1,0,2],::-1])




