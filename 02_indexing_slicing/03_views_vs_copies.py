#Copy vs View Function
import numpy as np

#copy creates new array(independent data)
#Change in original array wont have change in copied array


#view - Just a refelction or view kind off
#Change in array will change the data in view array

var = np.array([1,2,3,4,5,6,7,8,9,10])

co = var.copy()

var[1] = 40

print("Var:",var)
print("Copy:",co)

x = np.array([10,9,8,7,6,5,4,3,2,1])

vi = x.view()

x[1] = 10

print("x: ",x)
print("View: ",vi)