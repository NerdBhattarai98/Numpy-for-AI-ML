import numpy as np

A = np.array([1, 2, 3, 4, 5, 6])
B = np.array([7, 8, 9, 10, 11, 12])

TwoD = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

C = np.array([
    [1, 2],
    [3, 4]
])

D = np.array([
    [5, 6],
    [7, 8]
])

#reshape() - Changes the shape of array without altering its data
print(A.reshape(2,3)) 
print(A.reshape(1,6))
print(A.reshape(6,1))

# print(A.reshape(4,2)) #Not enough as 6 elements only but reshape has 4*2=8

# -1 in reshape() - it calculates the desired dimenstion for you

print(A.reshape(2,-1))

print(A.reshape(3,-1))

print(A.reshape(-1,3))

# -flatten() - Converts any array to 1D array

print(TwoD.flatten())

E = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print(E)
print(E.flatten())


#-ravel-Converts any array to 1D array
E = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print(E)
print(E.ravel())

#flatten vs ravel
# flatten - returns a copy (Change in original array not shown)
# ravel - return a view (Change in orginal array shown)

# .T - Transposes(row to column,column to row)
E = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print(E)
print(E.T)

#transpose - Same as .T

print(np.transpose(E))

#newaxis - np.newaxis(Adds a dimension)
#np.newaxis always inserts a fresh dimension of size 1, while : keeps the array's original length right where it is
A = np.array([1,2,3,4,5])
print(A.shape)

B = A[:,np.newaxis,np.newaxis,np.newaxis]

print(B)
print(B.shape)

A = np.array([1,2,3,4,5,6,7])
print(A)

B = A[np.newaxis,:]

C = A[:,np.newaxis]
print(B.shape)
print(B)
print(C.shape)
print(C)

#expand_dims()


A = np.array([1, 2, 3])

B = np.expand_dims(A, axis=0)
C = np.expand_dims(A,axis =1)

print(B)
print(B.shape)
print(C)
print(C.shape)

# squeeze()

A= np.array([[1],[2],[3]])
print(A.shape)
B = np.squeeze(A)
print(B)

A = np.array([[1,2,3]])
print(A.shape)
B = np.squeeze(A)
print(B)
print(B.shape)

# concatenate() - Join arrays along an exising axis
A =np.array([[10,20,30]])
B = np.array([[40,50,60]])

print(np.concatenate((A,B),axis=0)) #Down the rows
print(np.concatenate((A,B),axis=1)) #Acorss the column

# stack() - Join Arrays by creating a new dimenstions

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print(np.stack((A,B))) #New Dimension as in 2D bhayo yo

A = np.array([10,20,30])
B = np.array([40,50,60])

print(np.stack((A,B)).shape)

# vstack() - one row above another

A = np.array([10,20,30])
B = np.array([40,50,60])

print(np.vstack((A,B)))

#hstack - stack horizontally

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print(np.hstack((A, B))) #Horizontally Stack Two 1D arrays


# split()- Splits an array into equal parts

A = np.array([1,2,3,4,5,6,7,8,9,10])

print(np.split(A,5))

B = np.array([10, 20, 30, 40, 50, 60])
print(np.split(B,2))

# array_split()

# Similar to split(), but can handle unequal divisions.
A = np.array([1,2,3,4,5,6,7,8,9,10])
print(np.array_split(A,4))

A = np.array([1,2,3,4,5,6,7])
print(np.array_split(A,3))

# repeat()

# Repeats individual elements.

A = np.array([1,2,3,4,5])
print(np.repeat(A,5))

B = np.array([10,20,30])
print(np.repeat(B,3)) 

# tile() - Repeats whole array in a pattern

A = np.array([0,1])

print(np.tile(A,5))

#repeat vs tile
#repeat first repeats the individual element before moving to the next one
#tile repeats the array pattern

B = np.array([5,10])

print(np.tile(B,4))

# 20. flip() - Reversecs and array

A = np.array([1, 2, 3, 4, 5])

print(np.flip(A))

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.flip(A))

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(np.flip(A))