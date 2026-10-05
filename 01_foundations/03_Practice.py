import numpy as np
# Create a 1D array containing 10, 20, 30, 40, 50 using np.arange.
print(np.arange(10,51,10))
# Create a 3x3 array where every element is 5.
print(np.full((3,3),5))
# Create a 4x4 identity matrix in two different ways.
print(np.eye(4))
print(np.identity(4))
# Create a 2x5 array of zeros whose elements are integers, not floats.
print(np.zeros((2,5),dtype=int))


# 5. Make an array A = [1, 2, 3, 4, 5], then make a copy of it.
#  Change the first element of the copy to 100 and print both arrays to 
# show that A didn't change.

A = np.array([1,2,3,4,5])
copy = np.array(A)
copy[0] = 100
print(A)
print(copy)


# 6. Do the same, but this time make the change show up in A as well.

A = np.array([1,2,3,4,5])
copy = np.asarray(A)

copy[0] = 100
print(A)
print(copy)
# 7. Create 5 evenly spaced numbers from 0 to 1, and also get the 
# step size in the same line of code.

arr,step = np.linspace(0,1,5,retstep=True)
print(arr)
print(step)
# 8. Create a 3x4 matrix with 1s on a diagonal shifted one place to the right.
print(np.eye(3, 4, k=1))

# 9. Create a 3x3 matrix with 10, 20, 30 on the main diagonal and zeros everywhere else.
#  Then extract that diagonal back out of the matrix.

A = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(np.diag(A))
# 10. Create an array of all even numbers from 2 to 20 (including 20).

print(np.linspace(2,20,10))
# Tricky
# 11. Create a 5x5 matrix with 1s on the diagonal two places above the main one 
# and on the diagonal two places below it. Hint: you can add two arrays together.

A = np.diag([1,1,1],k=2)
B= np.diag([1,1,1],k=-2)
print(A + B)
# 12. Compare np.arange(0, 1, 0.25) and np.linspace(0, 1, 5). 
# Print both and explain why they have different lengths.

print(np.arange(0,1,0.25))
print(np.linspace(0,1,5))

# 13. Create a 3x3x3 array filled with 7, then print its .shape.
#  It should print (3, 3, 3).

A = np.full(((3,3,3)),7)
print(A)
print(A.shape)

# 14. Create this matrix using only np.diag (you can combine more than one call):

#     [[1 2 0]
#      [3 1 2]
#      [0 3 1]]

A= np.diag([1,1,1])
B = np.array([[0,2,0],[3,0,2],[0,3,0]])
sum = A+ B
print(sum)
# AI GEN Questions

# Create a 1D array [5, 10, 15, 20] with dtype float32. Print its shape, ndim, size, dtype, itemsize and nbytes.
# Create a 2D array of shape (3, 4) with values 1 to 12 and dtype int64. Print all six attributes from Q14.
# Create a 3D array of shape (2, 3, 4) with dtype int32. Print all six attributes.
# Write a function describe(arr) that prints an array's shape, ndim, size, dtype, itemsize and nbytes in a neat format. Test it on your arrays from Q14 to Q16.

# Verifying formulas with code

# Write code that checks arr.nbytes == arr.size * arr.itemsize for the three arrays from Q14 to Q16. Print True or False for each.
# Write code that checks arr.size equals the product of all values in arr.shape. (Hint: use np.prod(arr.shape).)
# Create the same array [1, 2, 3, 4, 5] in int8, int16, int32 and int64. Print the itemsize and nbytes of each in a loop.

# Data types and astype

# Create A = np.array([1.7, 2.2, 3.9, -4.5]). Convert it to int32 and print the result. Then use np.round(A) first and convert again. Compare the two outputs.
# Create np.array([0, 1, 2, 0, 5]) and convert it to bool. Then convert the boolean result back to int32.
# Create an int32 array of 1,000 elements using np.ones(1000, dtype=np.int32). Convert it to int64 and float32. Print the nbytes before and after each conversion.
# Prove that astype returns a new array and does not modify the original. Print A, B, and A is B. Then change B[0] and check whether A[0] changed.
# Create np.array(["1", "2", "3"]) and convert it to int32. Then try converting np.array(["1", "a", "3"]) the same way. Use try/except to catch and print the error.

# Memory experiments

# Create np.zeros((1000, 1000)) with dtype float64, float32 and int8. Print nbytes for each in MB (divide by 10**6).
# Write a loop over [np.int8, np.int16, np.int32, np.int64, np.float32, np.float64] that creates np.zeros((100, 100), dtype=...) for each type. Print the dtype name and nbytes. Which type would you pick to save memory?
# Create np.array([200], dtype=np.int8) and print the result. Then try np.array([200]).astype(np.int8). What happens and why? (Overflow is a classic dtype trap.)

# Mini challenge

# Build a "memory report" script:
# Make a list of 3 arrays (1D, 2D, 3D) with different dtypes.
# For each one, print: dimension name, shape, dtype, size, nbytes.
# At the end, print the total nbytes of all three arrays.

# 1. Fix the bug. This line from your notes crashes. Find the error and fix it so the array becomes 3D, then print shape and ndim.

# python
# A = np.array([1, 2, 3, 4, 5], ndim=3)

# 2. Copy vs view. Create A = np.array([1, 2, 3]). Make B = np.array(A) and C = np.asarray(A). Set B[0] = 99 and C[1] = 77, then print all three arrays. Use np.shares_memory(A, B) and np.shares_memory(A, C) to confirm what you see.

# 3. Hidden dtype. Without passing dtype, create arrays with np.zeros((2, 2)), np.full((2, 2), 9), np.full((2, 2), 9.0), np.eye(2) and np.arange(5). Print the dtype of each and explain why each one is what it is.

# 4. Memory budget. Create np.ones((500, 500)), then the same with dtype=np.float32, then with dtype=np.int8. Print nbytes in MB for each, and check that nbytes == size * itemsize.

# 5. Identity matrix attributes. Create np.eye(4, dtype=np.int32). Print its shape, size, dtype, itemsize and nbytes. Then use astype(np.bool_) on it and print the new nbytes.

# 6. Diagonal round trip. Build a 4x4 matrix with np.diag([10, 20, 30, 40]), then extract its diagonal with np.diag() and check that it equals the original list. Then build np.diag([1, 2, 3], k=-1) and print its shape and size. Why is the shape (4, 4) and not (3, 3)?

# 7. arange vs linspace. Create np.arange(0, 1, 0.1) and np.linspace(0, 1, 10). Print size and dtype for both. Then run np.arange(0, 1, 0.1).size and np.linspace(0, 1, 11).size and compare. Which one lets you control the number of points exactly?

# 8. retstep. Use np.linspace(5, 50, 10, retstep=True) to get the array and the step. Check in code that step == (50 - 5) / (10 - 1). Then change endpoint=False and print the new step.

# 9. Truncation trap. Take np.linspace(-2, 2, 9) and convert it to int32 with astype. Compare the result with np.round(...) converted to int32. Find which values changed and explain why for the negatives.

# 10. Mini challenge: array report. Create a dictionary of five arrays: np.zeros((3, 3), dtype=np.float32), np.full((2, 4), 7, dtype=np.int16), np.eye(3, 4, k=1), np.arange(1, 25).reshape(2, 3, 4) and np.linspace(0, 1, 5). Loop over the dictionary and print, for each array: name, shape, ndim, dtype, size and nbytes. Finish by printing the total nbytes across all five and the name of the array that uses the most memory.
