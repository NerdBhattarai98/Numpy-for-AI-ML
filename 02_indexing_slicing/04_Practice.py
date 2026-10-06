import numpy as np

A = np.array([
    [12, 25, 8, 40],
    [5,  30, 15, 45],
    [20, 10, 35, 50],
    [3,  18, 28, 60]
])

# Select every value greater than 25.
print(A[A>25])

# Select values between 10 and 40, inclusive.

print(A[(A >= 10) & (A <= 40)])

# Select rows 0 and 2.
print(A[[0,2]])

# Select columns 1 and 3.
print(A[:,[1,3]])

# Select rows 1 and 3 with columns 0 and 2.

A[np.ix_([0, 2], [1, 3])]

# Select all values greater than 20 OR less than 10.

print(A[(A < 10) | (A > 40)])

#AI Gen Practice Qns
OneD   = np.array([10, 20, 30, 40, 50, 60])
TwoD   = np.arange(1, 17).reshape(4, 4)
ThreeD = np.arange(1, 25).reshape(2, 3, 4)

# Part A: Indexing and slicing
# Print the last element of OneD with a negative index, then the bottom-right element of TwoD with negative indexes.
print(OneD[-2:])
print(TwoD[-1,-1])
# Set r, c = 2, 3 and print TwoD[r, c]. Then use a for i in range(4) loop to print the main diagonal TwoD[i, i].

# Print the four corners of TwoD as a 2x2 array using one slice expression (hint: use a step).
# Extract the middle 2x2 block of TwoD, then print it with its rows reversed.
# Predict, then print the .shape of each: TwoD[1], TwoD[1:2], TwoD[:, 1], TwoD[:, 1:2], ThreeD[0, :, 1]. Explain which ones lose a dimension and why.
# From ThreeD, get the last column of every layer (should be shape (2, 3)) and the first row of the second layer.
# Make m = TwoD.copy() and turn it into a checkerboard of zeros: set m[::2, ::2] = 0 and m[1::2, 1::2] = 0. Print it.




# Part B: Boolean and fancy indexing
# From ThreeD, select all values that are divisible by 3 and greater than 10.
# Count how many elements of TwoD are greater than 8 without a loop. (Hint: True counts as 1, so try .sum() on the mask.)
# Select values of OneD that are not between 20 and 40, once with | and once with ~. Check both give the same result.
# Make a copy of TwoD, replace every even number with -1, and confirm with np.array_equal that the original didn't change.
# Use np.where to build a new array from TwoD where values greater than 10 become 0 and the rest stay unchanged. Is TwoD modified?
# Reorder the rows of TwoD as [3, 1, 0, 2] using fancy indexing, then reverse the columns using fancy indexing (not ::-1).
# Print the main diagonal of TwoD using TwoD[[0,1,2,3], [0,1,2,3]], then print the anti-diagonal the same way.
# Pick rows 0 and 3 and columns 0 and 3 in two ways: TwoD[np.ix_([0,3],[0,3])] and TwoD[[0,3],[0,3]]. Print both and explain why the results differ in shape.
# Break it on purpose. Wrap each line in try/except and print the error message:
# python
# OneD[OneD > 20 & OneD < 50]
# OneD[(OneD > 20) and (OneD < 50)]
# OneD[10]



# Part C: Views and copies
# Using your x and vi example, add checks for np.shares_memory(x, vi), vi.base is x and co.base is None (where co = x.copy()). Print all three.
# Create a = np.arange(10) and these:
# python
# b = a[2:6];  c = a[[2,3,4,5]];  d = a[a > 4]
# e = a.view(); f = a.copy();     g = a

# Predict which of them share memory with a, then print a small table of name and np.shares_memory(a, ...) in a loop.

# A view is a separate array object over the same data. Prove it:
# python
# x = np.arange(10)
# v = x.view()
# v.shape = (2, 5)

# Print x.shape (does it change?), then set v[0, 0] = 99 and print x[0]. What does this tell you about shape vs data?

# Make m = TwoD.copy(). Run row = m[0]; row[:] = 0, then col = m[:, 1]; col *= 100. Predict the final m, then check.
# Writing vs reading with fancy indexing. Using m = TwoD.copy():
# m[[0, 1]] = -1. Does m change?
# r = m[[2, 3]]; r[:] = 5. Does m change?

# Explain the difference in one comment.

# The chained-indexing trap. Predict which one changes m, then test:
# python
# m = TwoD.copy()
# m[[0, 1]][0, 0] = 999    # A
# m[0:2][0, 0]   = 999     # B

# (Hint: one of these writes into a temporary copy.)

# Write two functions:
# zero_first_bad(arr) sets arr[0] = 0 directly.
# zero_first_safe(arr) does the same on a copy and returns it.

# Call both on a fresh array and print the original after each call.

# Memory check: big = np.arange(1_000_000). Create vw = big[::2] and cp = big[::2].copy(). Print vw.base is big and cp.base is None, then explain which one used new memory.
# Bonus: test m.flatten() against m.ravel() with np.shares_memory. Which one is a copy and which is (usually) a view?
# Mini challenge
# Build a "safe cleaner":
# python
# marks = np.array([[78, 85, -1],
#                   [90, -1, 88],
#                   [55, 70, 95],
#                   [34, 66, 72]])   # -1 = absent
# Make a cleaned copy where every -1 becomes 0.
# Using only indexing, print the marks of students 0 and 2 (fancy), the last two subjects of every student (slice) and every mark above 80 (boolean).
# Count how many marks are above 80 in each subject. (Hint: mask.sum(axis=0).)
# Finish with a check, np.array_equal, that proves the original marks still contains the -1 values.