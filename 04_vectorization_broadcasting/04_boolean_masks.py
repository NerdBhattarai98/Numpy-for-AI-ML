import numpy as np

#boolean - Selects or changes only the values that meet a condition.

a = np.array([5, 10,58,60,15,65,20, 25,16,17,18,33,34,36,37,10,29,30,10,55,56,90])

# print(a[a > 10])                  # select
# a[a > 20] = 0                     # modify in place
# print(a[(a > 5) & (a < 25)])      # combine with & | ~ (never and/or/not)
# print((a > 10).sum())             # count matches (True = 1)


# For a = [10, 25, 5, 40, 15, 60], find values > 20, values < 15, and values between 15 and 50.

print(a[a>20])
print(a[a<15])
print(a[(a>=15)&(a<=20)])
# Replace every value > 50 with 100.

a[a>50] = 100
print(a)
# Count how many values are NOT greater than 20.
a = np.array([5, 15, 20, 25, 30])
count = np.sum(a <= 20)
print(count)