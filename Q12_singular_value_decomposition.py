# Q12- Singular Value decomposition of a matrix

import numpy as np
import numpy.linalg as npl

# Function to calculate svd of an input matrix 'a'
# Function f takes matrix 'a' whose singular values to be determined and prints singular values and u and v matrices
def f(a):
    w1,v=npl.eigh(np.dot(np.transpose(a),a))
    v=np.transpose(v)
    v[[0,2],:]=v[[2,0],:]
    print("V=",v) 
    w2,u=npl.eigh(np.dot(a,np.transpose(a)))
    u[:,[1,3]]=u[:,[3,1]]
    u[:,[0,4]]=u[:,[4,0]]
    print("\nU=",u)
    
    print("\nSingular values are ",np.sqrt(w1[2]),np.sqrt(w1[1]),np.sqrt(w1[0]))

a=np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]])

import time
start = time.time()

f(a)

end = time.time()
print(end - start)

print("\nNow using numpy function")

#Using numpy.linalg.svd

import time
start = time.time()

u,s,v=npl.svd(a)
print("\nU=",u,"\nV=",v)
print("\nSingular values are ",s)

end = time.time()
print(end - start)
