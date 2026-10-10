import numpy as np

marks = np.array([80, 90, np.nan, 70, 100])

print(marks)
print(marks.mean())

#When you run regular marks.mean(), NumPy just throws its hands up and prints nan because that one missing value poisons the whole batch.

#NumPy converts the array to floating-point numbers because np.nan is a floating-point value.

# 1. Detect missing values
a = np.array([10, np.nan, 30, np.nan, 50])

print(np.isnan(a))
print(np.isnan(a).sum())

np.isnan(a) 

# checks every element.
# Missing values produce True.
# .sum() counts the True values because True behaves like 1 and False like 0 in this calculation.

# Note : Don't use equality to detect missing values. Use np.isnan().

# 2. Calculate statistics while ignoring missing values

a = np.array([10, 20, np.nan, 40])

print(a.mean())
print(np.nanmean(a)) #Ignores the nan value and calculates like 10+20+40 divide by 3 kind of

print(a.sum())
print(np.nansum(a)) #Simple 10+20+40

# Normal function	Ignores NaN?
# np.mean(a):No
# np.sum(a)	No
# np.std(a)	No
# np.max(a)	No
# np.min(a)	No
# np.nanmean(a)	Yes
# np.nansum(a)	Yes
# np.nanstd(a)	Yes
# np.nanmax(a)	Yes
# np.nanmin(a)	Yes

#only the ones using nan function would ignore nan not others

# 3. Remove missing values

a = np.array([10, np.nan, 30, 40, np.nan])

clean = a[np.isnan(a)]
print(clean)

clean = a[~np.isnan(a)] #Prints only clean values
print(clean)

# 4. Fill missing values with a fixed number

fill = np.where(np.isnan(a),0,a)

print(fill)

# C. The important part: 2D arrays and column means

X = np.array([
    [10, 100],
    [20, np.nan],
    [np.nan, 300],
    [40, 400]
])

print(np.isnan(X).sum(axis=0)) #along the rows
print(np.isnan(X).sum(axis=1)) #along the columns
print(np.nanmean(X, axis = 0))
print(np.nanmean(X, axis = 1))

clean = X[~np.isnan(X)]
print(clean)

fill = np.where(np.isnan(X),0,X)
print(fill)

#To Drop Rows containing nan

clean_X = X[~np.isnan(X).any(axis=1)]

# clean_X = X[~np.isnan(X).any(axis=0)] #Why this wont work
# Here’s why it's breaking: axis=0 checks down the columns, which spits out a boolean mask of length 2 (one for each column).'
# ' But X has 4 rows, so NumPy throws a shape mismatch error because a 2-element mask doesn't match a 4-row array.
# If your goal is to drop rows that contain any NaNs, you need to check across the rows using axis=1 instead:

print(clean_X)



X = np.array([
    [10, 100],
    [20, 200],
    [30, 300]
])

print(X.shape)                          # (3, 2)
print(np.mean(X, axis=0).shape)         # (2,) -> dimension got deleted!
print(np.mean(X, axis=0, keepdims=True).shape) # (1, 2) -> dimension is preserved!

# keepdims=True preserves the reduced dimensions as axes of size one, maintaining the input array's dimensionality to ensure compatibility for mathematical broadcasting.
