import numpy as np

X = np.array([
    [45,  80,  7],
    [50,  np.nan, 8],
    [np.nan, 70,  6],
    [60,  90,  9],
    [65,  85,  np.nan],
    [70,  95,  8],
    [75,  80,  7],
    [80,  85,  100]
], dtype=float)

print(X.shape)
print(X.dtype)

nanvalue = np.isnan(X).sum()
print(nanvalue)

colnnan = np.isnan(X).any(axis = 0).sum()
print(colnnan)

rownan = np.isnan(X).any(axis = 1).sum()
print(rownan)

colnmean = np.nanmean(X,axis = 0,keepdims=True)
print(colnmean)

# X.mean() doesn't give a useful result here. Wont Give a valid result as one nan value is not calculatable so it gives nan for 
# each and every one of them

filled_X = np.where(np.isnan(X),colnmean,X)
print(np.mean(filled_X,axis = 0,keepdims= True))
print(filled_X.shape )

#Claude

a = np.array([4, np.nan, 8, np.nan, 12, 16])

X = np.array([
    [5.0,    200, 1],
    [7.0, np.nan, 2],
    [np.nan, 180, 2],
    [9.0,    220, np.nan],
    [6.0, np.nan, 3],
])

# Easy

# How many NaNs are in a?
print(np.isnan(a).sum())
# What does a.mean() return? What does np.nanmean(a) return?a.mean() reutrns nan where as np.nanmean(a) returns actual mean excluding nan
# Remove the NaNs from a.
print(a[~np.isnan(a)])

# Predict
# 4. What is the shape of np.isnan(X).sum(axis=0)? Of np.isnan(X).sum(axis=1)?
# np.isnan(X).sum(axis=0)? is (1 , 3)
# np.isnan(X).sum(axis=1)?is (5,1)
# 5. What does np.nan == np.nan give, and why can’t you use == to find NaNs?
# np.nan == np.nan doesn’t raise an error. It quietly returns False. 
# That’s what makes it dangerous: a == np.nan is False everywhere, so it never finds anything.
# 6. What shape does X[~np.isnan(X).any(axis=1)] have? How many rows survive?
#it will be (1,3) and only one row will survive


# Harder
# 7. Fill each column of X with its own median. Confirm no NaNs remain.

colnmed = np.nanmedian(X,axis=0)
print(colnmed)

fill = np.where(np.isnan(X),colnmed,X)
print(fill)
# 8. Which column has the most missing values? Find it with one line of code (hint: argmax).

counts = np.isnan(X).sum(axis=0)
print(counts)
print(np.argmax(counts))

#Statistics

scores = np.array([55, 60, 62, 65, 68, 70, 72, 75, 78, 400])
grades = np.array(["B", "A", "C", "B", "A", "B", "D", "B", "C", "A"])

data = np.array([
    [1, 10, 5],
    [2, 20, 3],
    [3, 30, 8],
    [4, 40, 1],
    [5, 50, 6],
])

# Easy

# Mean and median of scores. Which is larger, and why?

me = np.mean(scores)
print(me)

medi = np.median(scores)
print(medi)
# Q1, Q2, Q3, and IQR of scores.
q1,q2,q3 = np.percentile(scores,[25,50,75])
print(q1)
print(q2)
print(q3)
InQuRa = q3 - q1
print(InQuRa)
# Count each grade with np.unique. Which grade is most common?
value , count = np.unique(grades,return_counts=True)
print(value,count)
print(np.max(count))

# Predict
# 4. Without running it: in data, what is the correlation between column 0 and column 1? Check it.
# Yes Correlated
# 5. What shape does np.corrcoef(data, rowvar=False) have? What would the shape be without rowvar=False?
# all the columns * all columns so my guess is 3*3
# 6. If you remove the 400, will the mean change a lot or a little? What about the median?
# Mean will change much but median wont

# Harder
# 7. Print the correlation matrix rounded to 2 decimals. Which off-diagonal pair is weakest?

print(np.round(np.corrcoef(data, rowvar=False), 2))

# [[1. 1. 0.]
#  [1. 1. 0.]
#  [0. 0. 1.]]
#column 1 and 3
#column 2 and 3
# 8. Compute the mean of each column of data with keepdims=True. What shape do you get, and why would you want it?

print(np.mean(data,keepdims=True,axis = 0))
# (3,1) shape and it is valid because 3 colmns 3 different values


prices = np.array([120, 135, 128, 140, 132, 125, 138, 900, 130, 5])

# Easy

# Compute Q1, Q3, IQR, and both bounds.
sorted_prices = np.sort(prices)

Q1,Q2,Q3 = np.percentile(sorted_prices,[25,50,75])
InQuRa = Q3 - Q1
print(InQuRa)

upper = Q3 + InQuRa * 1.5
lower = Q1 - InQuRa * 1.5
print(InQuRa)
print(lower,upper)
# Build the outlier mask and print the outliers.
mask = (sorted_prices < lower) | (sorted_prices > upper)
print(sorted_prices[~mask])
# Remove the outliers and print the cleaned array.

# Predict
# 4. How many outliers will there be? Think about both ends before running.
#2
# 5. What does np.clip(prices, lower, upper) do to 900 and 5?
# the lower will be 108.5 and upper will be 154.5 like values of 5 and 900 respectively
# 6. Does the mean go up or down after removing the outliers? The median?
#Mean will go down because 900 is removed but median will slighly change as 2 elements are removed

# Harder
# 7. Replace outliers with NaN, then compute np.nanmean and np.nanmedian. Compare with removing them.

print(np.where(mask,np.nan,sorted_prices))
# 8. Write ~(prices >= lower) & (prices <= upper) and compare its output with the correct mask. Which one is wrong, and why?
#Only 900 will be printed as it is the only one which satisfies the condition
print(sorted_prices[ ~(prices >= lower) & (prices <= upper)])
