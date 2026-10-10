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



