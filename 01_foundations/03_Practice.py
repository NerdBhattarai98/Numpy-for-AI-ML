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

# 15. Create a 1D array [5, 10, 15, 20] with dtype float32. 
# Print its shape, ndim, size, dtype, itemsize and nbytes.

A = np.array([5,10,15,20],dtype = np.float32)
print(A.shape)
print(A.ndim)
print(A.size)
print(A.dtype)
print(A.itemsize)
print(A.nbytes)
# 16. Create a 2D array of shape (3, 4) with values 1 to 12 and dtype int64. 
# Print all six attributes from Q15.

A = np.arange(1,13)
B = A.reshape(3,4)
print(B)

print(B.shape)
print(B.ndim)
print(B.size)
print(B.dtype)
print(B.itemsize)
print(B.nbytes)


# 17Create a 3D array of shape (2, 3, 4) with dtype int32. Print all six attributes.
# Write a function describe(arr) that prints an array's shape, ndim, size, dtype, itemsize and nbytes in a neat format. 
# Test it on your arrays from Q14 to Q16.

A = np.array([[[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]],
               [[13,14,15,16],
                [17,18,19,20],
                [21,22,23,24]]])
print(A)
print(A.shape)
print(A.ndim)
print(A.size)
print(A.dtype)
print(A.itemsize)
print(A.nbytes)


# Verifying formulas with code

# Write code that checks arr.nbytes == arr.size * arr.itemsize 
# for the three arrays from Q14 to Q16.
#  Print True or False for each.

A = np.array([[[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]],
               [[13,14,15,16],
                [17,18,19,20],
                [21,22,23,24]]])

bytes = A.nbytes
size = A.size
itemsize = A.itemsize
total = size * itemsize

if(bytes == total):
    print("Valid Check!")
else:
    print("Invalid Check!")




# Write code that checks arr.size equals the product of all values in arr.shape. (Hint: use np.prod(arr.shape).)

A = np.array([[[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]],
               [[13,14,15,16],
                [17,18,19,20],
                [21,22,23,24]]])

shape = A.shape
total = shape[0] * shape[1]*shape[2]
size = A.size

if(total == size):
    print("Valid Check!")
else:
    print("Invalid Check!")
# Create the same array [1, 2, 3, 4, 5] in int8, int16, int32 and int64.
#  Print the itemsize and nbytes of each in a loop.


B =np.array([1,2,3,4,5],dtype=np.int8)
C =np.array([1,2,3,4,5],dtype=np.int16)
D =np.array([1,2,3,4,5],dtype=np.int32)
E =np.array([1,2,3,4,5],dtype=np.int64)
A = [B,C,D,E]

lenght = len(A)

for i in range (lenght):
    print(f"Item Size of array {i+1}: ",A[i].itemsize)
    print(f"Total Byte Size of array {i+1}: ",A[i].nbytes)

# Data types and astype

# Create A = np.array([1.7, 2.2, 3.9, -4.5]). Convert it to int32 and print the result.
#  Then use np.round(A) first and convert again. Compare the two outputs.

A = np.array([1.7, 2.2, 3.9, -4.5])
B = np.array(A,dtype = np.int32)

C = np.round(A) #Went to the nearest rounded number

print(B) # Just Printed the first digit ignoring the decimal point
print(C)
# Create np.array([0, 1, 2, 0, 5]) and convert it to bool. Then convert the boolean result back to int32.

A=  np.array([0, 1, 2, 0, 5])

B = np.array(A,dtype = np.bool_)
print(B) #Prints value of 0 as false and OTHER as true

C= np.array(B,dtype =np.int32) #converts true as 1 and 0 as false

print(C)
# Create an int32 array of 1,000 elements using np.ones(1000, dtype=np.int32). 
# Convert it to int64 and float32. Print the nbytes before and after each conversion.

A= np.ones(1000, dtype=np.int32)
print(A.nbytes)

A = np.ones(1000, dtype=np.int64)
print(A.nbytes)

A = np.ones(1000, dtype=np.float32)
print(A.nbytes)
# Prove that astype returns a new array and does not modify the original. Print A, B, and A is B. 
# Then change B[0] and check whether A[0] changed.

A = np.array([1,2,3,4,5])
B = A.astype(np.float32)

print("Before Changes:")

print("A(Original Array: )",A)
print("B(Original Array: )",B)

B[0] = 120

print("After Changes:")
print("A: ",A)
print("B: ",B)




# Create np.array(["1", "2", "3"]) and convert it to int32. 
# Then try converting np.array(["1", "a", "3"]) the same way. Use try/except to catch and print the error.

#try/except syntax
# try:
#     # Try some code
# except Exception:
#     # Handle an Exception
# finally:
#     # Do some clean up

import numpy as np

A = np.array(["1","2","3"])
B = A.astype(np.int32)

print(B)

try:
    invalid_array = np.array(["1", "a", "3"])
    C= invalid_array.astype(np.int32)
except ValueError as e:
    print(f"Caught expected error: {e}")

# Create np.zeros((1000, 1000)) with dtype float64, float32 and int8. 
# Print nbytes for each in MB (divide by 10**6).

A = np.zeros((1000,1000))
B = A.astype(np.float64)
C = A.astype(np.float32)
D = A.astype(np.int32)

print(A)

B_MB = B.nbytes/10**6
print(B_MB)

C_MB = C.nbytes/10**6
print(C_MB)

D_MB = D.nbytes/10**6
print(D_MB)

# Write a loop over [np.int8, np.int16, np.int32, np.int64, np.float32, np.float64] 
# that creates np.zeros((100, 100), dtype=...) for each type. Print the dtype name and nbytes. 
# Which type would you pick to save memory?

import numpy as np

A = [np.int8, np.int16, np.int32, np.int64, np.float32, np.float64]

for i in A:
    B = np.zeros((100, 100), dtype=i)

    print(f"Dtype: {i.__name__}")


# __name__
# → gives the name of a class/type

# type(x)
# → gives the type/class of x

# type(x).__name__
# → gives only the clean type name (dunder method)


    print(f"Item size: {B.itemsize} bytes")
    print(f"Total memory: {B.nbytes} bytes")
    print()

A = np.array([1, 2, 3])

type(A)
print(type(A).__name__)

# Create np.array([200], dtype=np.int8) and print the result. 
# Then try np.array([200]).astype(np.int8). What happens and why? 
# (Overflow is a classic dtype trap.)

# A = np.array([200], dtype=np.int8)
# print(A)#Says out of bound

B = np.array([200]).astype(np.int8)
print(B) #OGives [-56 ] as output

# int8 range:
# -128 to 127

# np.array([200], dtype=np.int8)
# → direct conversion
# → out-of-range → OverflowError

# np.array([200]).astype(np.int8)
# → create first in int64, convert later
# → 200 wraps around → -56


# Build a "memory report" script:
# Make a list of 3 arrays (1D, 2D, 3D) with different dtypes.
# For each one, print: dimension name, shape, dtype, size, nbytes.
# At the end, print the total nbytes of all three arrays.


A = np.array([1, 2, 3], dtype=np.int8)          # 1D
B = np.zeros((3, 3), dtype=np.int32)            # 2D
C = np.ones((2, 2, 2), dtype=np.float64)        # 3D

print("Report For 1D Array: ")
print("Dimenstion Name: ",A.ndim)
print("Shape Name: ",A.shape)
print("Data Type: ",A.dtype)
print("Size: ",A.size)
print("Total Memory: ",A.nbytes)
print("\n")
print("\n")

print("Report For 2D Array: ")
print("Dimenstion Name: ",B.ndim)
print("Shape Name: ",B.shape)
print("Data Type: ",B.dtype)
print("Size: ",B.size)
print("Total Memory: ",B.nbytes)

print("\n")
print("\n")

print("Report For 3D Array: ")
print("Dimenstion Name: ",C.ndim)
print("Shape Name: ",C.shape)
print("Data Type: ",C.dtype)
print("Size: ",C.size)
print("Total Memory: ",C.nbytes)

#AI Generated