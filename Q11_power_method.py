# Q11- To find dominant eigenvalue and eigenvector of matrix using power method

import numpy as np
import numpy.linalg as npl

a=np.array([[2,-1,0],[-1,2,-1],[0,-1,2]]) #Given matrix
x=np.array([[2],[1],[1]]) #test eigen vector
y=np.array([[1,0,1]]) #test transpose vector

testeigen=np.dot(np.dot(a,x),y)[0][0]/np.dot(x,y)[0][0] #Test eigenvalue
error=1
i=1 #to keep track of iternation

while(error>=0.01):
    x=np.dot(a,x)
    egn=np.dot(np.dot(a,x),y)[0][0]/np.dot(x,y)[0][0]  #Iterative Eigenvalue
    error=(egn-testeigen)/testeigen
    testeigen=egn
    i=i+1

print("Eigenvalue is",egn,"\nEigenvector is ",x)
