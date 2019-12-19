import numpy as np
import scipy
from scipy import linalg
a=np.matrix('1 2 3;4 5 6;7 8 9')
b=np.matrix('8 6 3;9 5 1;7 4 2')
c=np.asarray([5,8,6])
d=np.asarray([4,9,7])
# Array operations using numpy
print "1st array: ",c
print "2nd array: ",d
#append
print "Appending two arrays: ",np.append(c,d)
#length
print "length of c: ",np.size(c)
print "length of d: ",np.size(d)
# Matrix operations
print"1st matrix:\n",a
print"2nd matrix:\n",b
#addition
print "Addition of two matrices:\n",np.add(a,b)
#subtraction
e=a-b
print "Subtraction of matrices:\n",e
#multiplication
f=a*b
print "multiplication of two matrices:\n",f
#determinant
print "det of a:\n",np.linalg.det(a)
print "det of b:\n",np.linalg.det(b)
#transpose
print "Transpose of a:\n",np.transpose(a)
print "Transpose of b:\n",np.transpose(b)
#inverse
print "inverse of a:\n",np.linalg.inv(a)
print "inverse of b:\n",np.linalg.inv(b)
#eigen values
print "eigen matrix of a:\n",np.linalg.eig(a)
print "eigen matrix of b:\n",np.linalg.eig(b)
#exponential
print "exponential of a:\n",np.exp(a)
print "exponential of b:\n",np.exp(b)
#rank
print "Rank of a:\n",np.linalg.matrix_rank(a)
print "Rank of b:\n",np.linalg.matrix_rank(b)
#Square root
print "Square root of a:\n",np.sqrt(a)
print "Square root of b:\n",np.sqrt(b)