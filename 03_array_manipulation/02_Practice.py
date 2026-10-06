# import numpy as np
# A = np.arange(1, 13)                      # 1 to 12
# M = np.array([[1, 2, 3], [4, 5, 6]])
# reshape and -1: Reshape A into (3, 4), then (2, 2, 3), then use -1 to get (4, -1). Print the shape of each. Then try A.reshape(5, -1) in try/except and print the error. Why does it fail?
# flatten vs ravel: Make f = M.flatten() and r = M.ravel(). Set f[0] = 99 and r[1] = 77. Print M, and confirm with np.shares_memory which one touched the original.
# Transpose: Print M.T and M.T.shape. Then, without running it, predict the shape of A.reshape(3, 4).T, then check.
# newaxis vs expand_dims: Make v = np.array([1, 2, 3]). Turn it into a column of shape (3, 1) using np.newaxis, then again with np.expand_dims. Check that both results are equal with np.array_equal.
# squeeze: Create np.zeros((1, 3, 1, 4)). Print its shape after np.squeeze. Then use np.squeeze(x, axis=0) and print that shape. What does axis= change?
# concatenate: Join M with np.array([[7, 8, 9]]) along axis=0. Then try axis=1 in try/except. Why does it fail, and what would you change to make it work?
# stack vs vstack vs hstack: Using a = np.array([1, 2, 3]) and b = np.array([4, 5, 6]), print the result and shape of np.stack((a, b)), np.stack((a, b), axis=1), np.vstack((a, b)) and np.hstack((a, b)). Which two give the same output?
# split vs array_split: Split np.arange(10) into 5 parts with np.split. Then try np.split(np.arange(10), 3) in try/except. Fix it using np.array_split and print the sizes of the parts (hint: [len(p) for p in parts]).
# repeat vs tile: For p = np.array([1, 2, 3]), predict and print np.repeat(p, 2) and np.tile(p, 2). Then use np.repeat(M, 2, axis=0) and np.tile(M, (2, 1)) and describe the difference in one comment.
# flip and a combined challenge: Print np.flip(M), np.flip(M, axis=0) and np.flip(M, axis=1). Then, using only the functions above, turn A into a (3, 4) matrix, flip it left to right, transpose it, and flatten it. Print the final shape and values