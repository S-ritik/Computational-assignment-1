# Q9-To solve system of linear equations by various methods

import numpy as np

truex=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163]) #True solution
a=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]]) #Given matix A
b=np.array([1,2,3,4,5]) #Given matix B
n=len(b)
x0=np.array([0.0,0.0,0.0,0.0,0.0])

#Jacobi method

i=np.identity(n)
d=a*i
r=a-d
x=x0
d_i=np.identity(n)
for i in range(n):
    d_i[i,i]=1/d[i,i]

for i in range(100):
    x=np.dot(d_i,(b-np.dot(r,x)))
    if np.amax(np.absolute(x-truex))<0.01:
        break
print("Using Jacobi method, no. of iterations=",i+1)
print(x)

# Gauss Seidel method

x=x0
for i in range(100):
    for j in range(n):
        d1=b[j]
        for k in range(n):
            if(j!=k):
                d1=d1-(a[j][k]*x[k])
        x[j]=(d1/a[j][j])
    if np.amax(np.absolute(x-truex))<0.01:
        break
print("Using Gauss Seidel method, no. of iterations=",i+1)

print(x)


#Relaxation method

x=np.array([0.0,0.0,0.0,0.0,0.0])
w=1.25
for i in range(100):
    for j in range(n):
        d=b[j]
        for k in range(n):
            if(j!=k):
                d=d-(a[j][k]*x[k])
        x[j]=(w*(d/a[j][j]))+(x[j]*(1-w))
    if np.amax(np.absolute(x-truex))<0.01:
        break
print("Using Relaxation method, no. of iterations=",i+1)
print(x)

# Conjugate gradient method

x=np.array([0.0,0.0,0.0,0.0,0.0])
r0=b-np.dot(a,x)
p=r0
for i in range(100):
    al=(np.dot(r0,r0))/(np.dot(p,np.dot(a,p)))
    x=x+(al*p)
    r1=r0-(al*np.dot(a,p))
    be=(np.dot(r1,r1))/(np.dot(r0,r0))
    p=r1+(be*p)
    r0=r1
    if np.amax(np.absolute(x-truex))<0.01:
        break
print("Using conjugate gradient method, no. of iterations=",i+1)
print(x)


