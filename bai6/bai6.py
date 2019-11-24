import numpy as np
#2 vector cho truoc chieu dai cua h nhon hon cua n

h = np.array( [1,0,1] ,dtype= float)
n = np.array([ [1,0,0,1,8,2,]],dtype= float)
x = n.transpose()
print ('\nh[]:',h)
print ('n[]:',n)
# tinh linear convolution

y = np.zeros( (n.shape[1]+h.shape[0] -1 ,n.shape[1] ) )
for i in range(h.shape[0]) :
    for j in range(i+1):
        y[i][j]=h[i-j]
        y[n.shape[1]+h.shape[0]-2 - i][n.shape[1]-i+j-1] = h[h.shape[0]-1-j]

for i in range(h.shape[0],n.shape[1]):
    for j in range(1,n.shape[1]):
        y[i][j] = y[i-1][j-1]
    y[i][0] = y[i-1][n.shape[1]-1]
linear = y.dot(x)
print ('\nLINEAR CONVOLUTION : ')
print (linear.transpose())
print ('\nLINEAR CONVOLUTION TINH TU HAM CO SAN:')
print ('', np.convolve(n[0],h))
# tinh cyclic convolution

a = np.zeros( (n.shape[1],n.shape[1] ) )
a[0][0]= h[0]
for i in range(h.shape[0]-1) :
    a[0][n.shape[1]+1-h.shape[0]+i]= h[h.shape[0]-1-i]
for i in range (1,n.shape[1]):
    for j in range (1,n.shape[1]):
        a[i][j]= a[i-1][j-1]
    a[i][0] = a[i-1][n.shape[1]-1]
cyclic = a.dot(x)
print('\nCYCLIC CONVOLUTION:')
print(cyclic.transpose())

# tinh cyclic tu linear
z= linear.transpose()
cyclic_from_linear = np.zeros((1,n.shape[1]))
for i in range(h.shape[0]-1):
    cyclic_from_linear[0][i]= z[0][i]+z[0][n.shape[1]+i]
for i in range(h.shape[0]-1,n.shape[1]):
    cyclic_from_linear[0][i]=z[0][i]
print('\nCYCLIC FROM LINEAR:')
print(cyclic_from_linear)
