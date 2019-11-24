import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from matplotlib.colors import LogNorm
#  Đọc file ảnh
image = plt.imread('test.png').astype(float)
plt.figure()
plt.imshow(image)
plt.title('anh goc')

#  Fourier 
img_fft = fftpack.fft2(image)
def plot_spectrum(img_fft):

    plt.imshow(np.abs(img_fft), norm=LogNorm(vmin=5))
    plt.colorbar()

plt.figure()
plot_spectrum(img_fft)
plt.title('Fourier transform')

# khoi phuc
img_new = fftpack.ifft2(img_fft).real
plt.figure()
plt.imshow(img_new, plt.cm.gray)
plt.title('anh khoi phuc')
plt.show()