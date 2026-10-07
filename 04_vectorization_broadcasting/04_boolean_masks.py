import numpy as np

#boolean - Selects or changes only the values that meet a condition.

a = np.array([5, 10, 15, 20, 25])

print(a[a > 10])                  # select
a[a > 20] = 0                     # modify in place
print(a[(a > 5) & (a < 25)])      # combine with & | ~ (never and/or/not)
print((a > 10).sum())             # count matches (True = 1)
