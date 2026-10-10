import numpy as np

# Mean, median, standard deviation, minimum and maximum 
import numpy as np

scores = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(scores)) #Mean is the average
print("Median:", np.median(scores)) # Median is exact middle np.sort(arr) must be sorted before finding the values
print("Standard deviation:", np.std(scores))
print("Minimum:", np.min(scores))
print("Maximum:", np.max(scores))

# Symmetric Data: A balanced bell curve where the mean, median, and mode are all chilling dead in the center.

# Positively Skewed: The bulk of the data is bunched on the left with a long tail stretching right, 
# which drags the mean higher than the median. Mean > Median.

# Negatively Skewed: The bulk of the data is bunched on the right with a long tail stretching left, 
# which drags the mean lower than the median. Mean < Median

# exactly half the office makes more than $50k, and half makes less

normal = np.array([10, 20, 30, 40, 50])
extreme = np.array([10, 20, 30, 40, 500])

print(np.mean(normal))
print(np.median(normal))

print(np.mean(extreme))
print(np.median(extreme))

# Median is often a useful measure of a typical value when a dataset contains extreme values. 
# It is less sensitive to outliers than the mean.

# In a company of nine employees earning $50,000 and one executive earning $950,000,
# the mean salary of $140,000 is skewed upward by the outlier, 
# whereas the median salary of $50,000 accurately reflects typical earnings.

# B. Statistics by column

X = np.array([
    [10, 100],
    [20, 200],
    [30, 300]
])

print(np.mean(X,axis= 0)) #Along the column
print(np.mean(X,axis= 1)) #Along the rows

# C. Percentiles and quartiles

a = np.array([10, 20, 30, 40, 50, 60, 70])

print(np.percentile(a, [25, 50, 75]))

#Quartiles = Divides the dataset into 4 equal parts

#50th Percentile Q2 or Median The Middle of Data
#25th Percentile or Q1 is the Median of values below Q2(Median)
#75th Percentile Q3 is the Median of values above Q2(Median)

#IQR(InterQuartile Range)

# The interquartile range (IQR) measures the statistical dispersion of the 
# middle 50 percent of a dataset by calculating the difference between the third and first quartiles.

# The IQR is simply the window that covers the two middle quarters—throwing away
# the bottom 25% (the crazy low values) and the top 25% (the crazy high values).

q1, median, q3 = np.percentile(a, [25, 50, 75])

iqr = q3 - q1

print("Q1:", q1)
print("Median:", median)
print("Q3:", q3)
print("IQR:", iqr)

# # If we get IQR as 30,It means the middle 50% of your dataset spans a width of 30 units
# By definition, the IQR spans from the 25th percentile (Q_1) to the 75th percentile
#  (Q_3). Since 75% - 25% = 50%, it literally captures the exact middle 50% of your dataset.
# If you have 50 students total, that means right around 25 of them—that core middle chunk—scored between 50 and 80 marks. 

#Cheatcode

# Imagine you line up all your data from smallest to largest:

# Chop off the bottom 25% (the lowest, weirdly small values).

# Chop off the top 25% (the highest, crazy outlier values).

# What’s left in the middle is your core squad—the middle 50% of your data. 
# The IQR is simply the distance (or gap) between the start of that middle group and the end of it.

# D. Count unique values



grades = np.array(["A", "B", "A", "C", "B", "A"])

values, counts = np.unique(grades, return_counts=True)

print(values , counts)

# E. Correlation matrix

X = np.array([
    [1, 20],
    [2, 40],
    [3, 60],
    [4, 80]
])

corr = np.corrcoef(X, rowvar=False)
print(corr)

# Why rowvar=False matters
# By default, np.corrcoef() treats rows as variables. But ML datasets usually have rows as samples and columns as features.

# Understand the matrix
# - Diagonal values are 1: each variable is perfectly correlated with itself.
# - Off-diagonal values describe the relationship between different columns.


# - Correlation near +1: strong positive linear relationship.Same Direction in sync
# - Correlation near -1: strong negative linear relationship.Different Direction
# - Correlation near 0: little or no linear relationship. No Relation of columns at all

X = np.array([
    [1, 50],
    [2, 20],
    [3, 80],
    [4, 30],
    [5, 60]
])

corr = np.corrcoef(X, rowvar=False)

print(corr)

# [[1.         0.19867985]
#  [0.19867985 1.        ]]

# 1.0 on the diagonal: each column is perfectly correlated with itself.
# 0.1 off the diagonal: the two columns have almost no linear correlation.

# Column 1	Column 2
# Column 1	1.0	0.8
# Column 2	0.8	1.0

# Row 1, Column 1 = 1.0: Column 1 compared with itself. Always 1.
# Row 2, Column 2 = 1.0: Column 2 compared with itself. Always 1.
# Row 1, Column 2 = 0.8: Correlation between Column 1 and Column 2.
# Row 2, Column 1 = 0.8: Correlation between Column 2 and Column 1.