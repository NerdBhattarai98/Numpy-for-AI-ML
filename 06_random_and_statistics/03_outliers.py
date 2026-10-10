# A. What is an outlier?
# An outlier is a value that lies unusually far from the rest of a dataset.

import numpy as np

marks = np.array([1,6,9,12,55,59,70, 72, 75, 78, 80, 82, 500])

q1,q2,q3 = np.percentile(marks,[25,50,75])

InQuRa = q3 - q1

upper_limit =  q3 + 1.5*InQuRa
lower_limit =  q1 - 1.5*InQuRa

# Method 1: Remove outliers
print(lower_limit , upper_limit)
# 62.25 92.25 Anything above and below this is outlier so 500 is outlier
mask = (marks < lower_limit) | (marks > upper_limit)

print(mask)
print(marks[~mask])

#Method 2 : np.clip

print(np.clip(marks,lower_limit,upper_limit))

# Method 3: Replace outliers with NaN

print(np.where(mask,np.nan,marks))