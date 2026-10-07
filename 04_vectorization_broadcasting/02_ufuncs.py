import numpy as np

#np.add() - add array elements by elements

A = np.array([1,2,3,4,5])
B = np.array([5,4,3,2,1])

print(np.add(A,B))

# np.multiply() - MULTIPLIES ELEMENT BY ELEMENT

A = np.array([1,2,3,4,5])
B = np.array([5,4,3,2,1])

print(np.multiply(A,B))

# np.sqrt() - Square root of each element
print(np.sqrt(A))

# np.exp()- calculates e^x(Eulers Number raised to power)

print(np.exp(A))

# np.log() - log values of every element

print(np.log(A))

# Operators - Performs Element-Wise operation

A = np.array([1,2,3,4,5])

print(A + 5)
print(A - 5)
print(A * 2)
print(A / 2)
print(A ** 2)
print(A % 3)

