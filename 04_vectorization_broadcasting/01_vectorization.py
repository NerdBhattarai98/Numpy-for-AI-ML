import numpy as np
import time

# 1. Vectorization - Performs entire operation on Numpy Array Without using any for loops

arr = np.array([1, 2, 3, 4, 5])
result = arr * 2
print(result)

A = np.arange(1000000)
print(A)

start = time.perf_counter()
v = []

for value in A:

    v.append(value * 5)

loop_time = time.perf_counter() - start

start = time.perf_counter()

numpy_result = A * 5

numpy_time = time.perf_counter() - start


print(loop_time)
print(numpy_time)

# 0.2005740000000742 for loop it was 0.2s
# 0.0024335999999038904 for numpy it was 0.002s

# 2. Vectorized Expressions - Allows to perform mathematical calculations on entire array

x = np.array([1, 2, 3, 4, 5])

result = x ** 2 + 2 * x + 5

print(result)

# Calculate: x³ + 2x² - 5x + 10

result = x**3 + 2 * x ** 2 - 5 * x + 10
print(result)

# 1. Square every value
result = x**2
print(result)
# 2. Multiply every value by 10
result = x*10
print(result)
# 3. Add 100 to every value
result = x+100
print(result)
# 5. Normalize an array -To level the playing field between different units or ranges. Imagine you're analyzing houses with Age (ranging 0 to 100 years) and Price (ranging $100,000 to $1,000,000). If you feed those raw numbers to an algorithm, Price will completely bully and overpower Age just because its numbers are bigger. Normalizing squishes both features down to a 0–1 scale so they contribute equally.

result = (x-np.min(x))/(np.max(x)-np.min(x))
print(result)