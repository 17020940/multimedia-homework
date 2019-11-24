
import numpy as np

import matplotlib.pyplot as plt

# cac thong so cho truoc 
f= 5 # tan so
fs =80000  # tan solay mau
N = 5 # so chu ki ve
A = 2 # bien do
n= 10 # 1 gia tri nguyen

# Get x values of the sine wave

x = np.arange(0,N/f,1/fs)
i = 0 
y = A*np.sin(2*np.pi*f*x)
z = 0
while (i< 2*n +1) :
    z+= A/( (2*i+1)*(2*i+1) ) * np.sin( 2 * (2*i+1) * np.pi * f * x )
    i+=1
# Hinh 1
plt.subplot(2,1,1)
plt.plot(x, y, '-', lw=2)
plt.title('Figure 1')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')

#Hinh 2 
plt.subplot(2,1,2)
plt.plot(x, z, '-', lw=2)
plt.title('Figure 2')
plt.xlabel('Time')
plt.ylabel('Amplitude ')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')

plt.tight_layout()
plt.savefig('bai1')
plt.close()