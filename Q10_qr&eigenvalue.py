# Q10- qr decomposition

import numpy as np
import numpy.linalg as npl

# given matrix A
A=np.array([[5,-2],[-2,8]])
q,r=npl.qr(A)
print("QR decomposition of given matrix is \nQ=",r,"\nR=",r)

#For calculating eigenvalues using qr decomposition
for i in range(0,10):
    q,r=npl.qr(A)
    A=r*q
print("Eigen values of A using qr decomposition are ",A[0][0],A[1][1])

#For eigenvalues using eigh function
w,v=npl.eigh(A)
print("Eigenvalues of A using numpy.linalg.eigh are ",w[0],w[1])
