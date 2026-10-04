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

