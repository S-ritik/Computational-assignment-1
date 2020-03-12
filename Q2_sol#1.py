"""
This is code of question 2 in which we have to solve the given system
of linear equations using numpy function
"""
import numpy as np
import numpy.linalg as npl

# For solving Ax=B, first to input A
A=np.array([[1,0.67,0.33],[0.45,1.0,0.55],[0.67,0.33,1]])

# Now creating B
B=np.array([2,2,2])

# to solve by using solve function
x=npl.solve(A,B)
print(x)
