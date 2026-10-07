import numpy as np

# np.where- is a vectorized if/else.Array lai if/esle wala kaam garcha

x = np.array([-3, -1, 0, 2, 5])

print(np.where(x > 0, x, 0)) #If value is lesser than 0 then print 0 and if it is greater than 0 then print the value itslef

x = np.array([-5, -1, 0, 1, 2, 3, 4, 10])

# np.clip() - limits the value to a range

print(np.clip(x, 0, 3))

# Below 0 → becomes 0
# Between 0 and 3 → stays the same
# Above 3 → becomes 3

# Exercise
# Given temperature = [10, 25, 30, 15, 35], return "Hot" if >= 25, else "Cold".

temp = np.array([10, 25, 30, 15, 35])

print(np.where(temp >= 25,"Hot","Cold"))
# Clip [-10, 20, 50, 80, 120] to 0 to 100.

array = np.array([-10, 20, 50, 80, 120])

print(np.clip(array,0,100))
# Write relu(x) with np.where, then again with np.maximum(0, x).

print(np.where(array<0,0,25))
print(np.maximum(0,array))
# max(0, -3) → 0
# max(0, -1) → 0
# max(0,  2) → 2
# max(0,  5) → 5