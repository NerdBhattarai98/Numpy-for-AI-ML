import numpy as np

OneD = np.array([1,2,3],dtype=float)
TwoD = np.array([[1,2,3],[4,5,6]],dtype=np.float64)
ThreeD = np.array([[[1,2,3],[4,5,6]]],dtype=np.int32)

print("1D Array: ",OneD)
print("2D Array: ",TwoD)
print("3D Array: ",ThreeD)

#.shape - gives the dimension of the array

print(OneD.shape) #(Rows,)
print(TwoD.shape) #(Rows,Columns) 
print(ThreeD.shape) #(Layers,Rows,Columns)

#ndim - gives the dimesntion of Array

print(OneD.ndim)
print(TwoD.ndim)
print(ThreeD.ndim)

#size - total number of elements in an array
print(OneD.size) 
print(TwoD.size) #(2,3) dimension ko 2*3=6
print(ThreeD.size)#(1,2,3) dimension ko 1*2*3=6

# .dtype - What type of data is stored in array

print(OneD.dtype)
print(TwoD.dtype)
print(ThreeD.dtype)

#.itemsize - How many bites does one element uses

print(OneD.itemsize)
print(TwoD.itemsize) #float64 -> 8 Byte
print(ThreeD.itemsize) #int 32 -> 4 byte


#.nbytes
# Total memory consumed by the array's elements.
# nbytes = size × itemsize

print(OneD.nbytes) 
print(TwoD.nbytes)
print(ThreeD.nbytes)

#DataTypes
A = np.array([1, 2, 3], dtype=np.int32)

B = np.array([1, 2, 3], dtype=np.int64)

C = np.array([1, 2, 3], dtype=np.float32)

D = np.array([1, 2, 3], dtype=np.float64)

E = np.array([True, False, True], dtype=np.bool_)

print(A.dtype)
print(B.dtype)
print(C.dtype)
print(D.dtype)
print(E.dtype)

# .astype() - To convert the datatype of an array
A = np.array([1, 2, 3])

B = A.astype(np.float64)

print(A)
print(A.dtype)

print(B)
print(B.dtype)

# Integer → Float
A = np.array([1, 2, 3, 4])

B = A.astype(np.float64)

print(B)
print(B.dtype)

# Float → Integer
A = np.array([1.2, 2.8, 3.9])

B = A.astype(np.int32)

print(B)#Gives only first digit not a mathematical output

# Dtype is memory
A = np.array([1, 2, 3, 4], dtype=np.int32)

B = np.array([1, 2, 3, 4], dtype=np.int64)

print(A.itemsize)
print(B.itemsize)

print(A.nbytes)
print(B.nbytes)

# int32  → 4 bytes/element
# int64  → 8 bytes/element