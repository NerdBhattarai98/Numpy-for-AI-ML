import numpy as np

# scale each feature to mean 0 and std 1, and turn scores into probabilities.
# Standardization → make features comparable.

X = np.array([
    [10, 100],
    [20, 200],
    [30, 300],
    [40, 400]
], dtype=float)

mean = X.mean(axis=0, keepdims=True) 
std  = X.std(axis=0, keepdims=True)
Z = (X - mean) / std
print(Z)

#Exercise

import numpy as np

X = np.array([
    [50, 1, 20, 30000],
    [80, 2, 15, 45000],
    [120, 3, 10, 60000],
    [150, 3, 7, 80000],
    [200, 4, 3, 120000],
], dtype=float)

# Column 0 → House Size (m²)
# Column 1 → Bedrooms
# Column 2 → Age (years)
# Column 3 → Income

mean = X.mean(axis = 0,keepdims=True)
std = X.std(axis = 0,keepdims=True)

Z = (X - mean)/std
print(Z)

#                  Size     Bedrooms     Age      Income
# House 1        -1.33      -1.57      +1.51     -1.18
# House 2        -0.76      -0.59      +0.67     -0.70
# House 3         0.00      +0.39      -0.17     -0.22
# House 4        +0.57      +0.39      -0.67     +0.42
# House 5        +1.52      +1.37      -1.34     +1.70

# after standardization, each COLUMN as a whole has mean 0 and standard deviation 1.
