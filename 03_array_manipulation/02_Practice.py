import numpy as np
A = np.arange(1, 13)                      # 1 to 12
M = np.array([[1, 2, 3], [4, 5, 6]])



# reshape and -1: Reshape A into (3, 4), then (2, 2, 3), then use -1 to get (4, -1). 
# Print the shape of each. Then try A.reshape(5, -1) in try/except and print the error. Why does it fail?

B = A.reshape(2,2,3)
print(B)
print(A.reshape((4,-1)))
# flatten vs ravel: Make f = M.flatten() and r = M.ravel(). Set f[0] = 99 and r[1] = 77.
#  Print M, and confirm with np.shares_memory which one touched the original.

f = M.flatten()
r = M.ravel()

f[0] = 99
r[1]=77 #ravel is a view

print(M)

print(np.shares_memory(f,M))

print(np.shares_memory(r,M))
# Transpose: Print M.T and M.T.shape. Then, without running it, predict the shape of A.reshape(3, 4).T, then check.

print(M.T)
print(M.T.shape)

matrix = A.reshape(3, 4)
print("Original shape:", matrix.shape)

print("Transposed Shape:",matrix.T.shape)


# newaxis vs expand_dims: Make v = np.array([1, 2, 3]). Turn it into a column of shape (3, 1) using np.newaxis, 
# then again with np.expand_dims. Check that both results are equal with np.array_equal.

v = np.array([1, 2, 3])
A = v[:,np.newaxis]
print(A.shape)

B=np.expand_dims(v,axis=1)
print(B.shape)

print(np.array_equal(A,B))

# squeeze: Create np.zeros((1, 3, 1, 4)). Print its shape after np.squeeze. Then use np.squeeze(x, axis=0) and print that shape. 
# What does axis= change?

# squeeze and axis: with no axis,
# squeeze removes every size-1 dimension, so (1,3,1,4) becomes (3,4).
# With axis=0 it removes only that one, giving (3,1,4), which is why you saw 3 dimensions.
# If the axis you name isn't size 1, you get an error.

print("Squeeze")

A= np.zeros((1,3,1,4))
print(A)
print(np.squeeze(A))
print(np.squeeze(A,axis =0 ))

print("Squeeze")
#Thw Dimesntion changes due to axis = 0 why but Like when axis = 0 it gived 3 dimn but in normal ome it is 2 dimn
# concatenate: Join M with np.array([[7, 8, 9]]) along axis=0. 
# Then try axis=1 in try/except. Why does it fail, and what would you change to make it work?

C = np.array([[7, 8, 9]])
new = np.concatenate((M,C),axis=0)
print(new)

try:
    new = np.concatenate((M,C),axis=1)
    print(new)
except:
    print("Error")

# stack vs vstack vs hstack: 
# Using a = np.array([1, 2, 3]) and b = np.array([4, 5, 6]), 
# print the result and shape of np.stack((a, b)), np.stack((a, b), axis=1), np.vstack((a, b)) and np.hstack((a, b)). 
# Which two give the same output?

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.vstack((a,b)))
print(np.stack((a,b)))
print(np.hstack((a,b)))
#vstack and stack gives the same output

# split vs array_split: Split np.arange(10) into 5 parts with np.split. 
# Then try np.split(np.arange(10), 3) in try/except. Fix it using np.array_split and print the sizes of the parts 
# (hint: [len(p) for p in parts]).

A = np.arange(10)

try:
    print(np.split(A,3))
    print("Use try block of code")
except:
    print(np.array_split(A,3))
    A = np.array_split(A,3)
    print("Used Except Block of code")
    sizes = [len(p) for p in A]
    print(sizes)

    

# repeat vs tile: For p = np.array([1, 2, 3]), predict and print np.repeat(p, 2) and np.tile(p, 2).
#  Then use np.repeat(M, 2, axis=0) and np.tile(M, (2, 1)) and describe the difference in one comment.

p = np.array([1, 2, 3])
print(np.repeat(p,2))
print(np.tile(p,2))

print(np.repeat(M,2,axis = 0))
print(np.tile(M, (2, 1)))
#repeat first repeats the rows before moving to another row but tile just dublicates the matrix in exact order
# flip and a combined challenge: Print np.flip(M), np.flip(M, axis=0) and np.flip(M, axis=1). 
# Then, using only the functions above, turn A into a (3, 4) matrix, flip it left to right, transpose it, and flatten it. 
# Print the final shape and values

print("-----------------------")
print(M)
print(np.flip(M)) #Every element in reverse order
print(np.flip(M, axis=0)) #Just goes up
print(np.flip(M, axis=1)) #Mirror Flip