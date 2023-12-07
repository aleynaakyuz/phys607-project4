import h5py
import numpy as np
import random
import math
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


f = h5py.File('./data.hdf', 'r')

print(f.keys())


print(f['data'].keys())

x = f['data/xpos'][:]
y = f['data/ypos'][:]

def func1(x, a, b, c, h, e):
    return a*np.sin(b*x) + h*np.cos(c*x) + e

params, cov = curve_fit(func1, x, y)
a, b, c, h, e = params[0], params[1], params[2], params[3], params[4]
yfit1 = a*np.sin(b*x) + h*np.cos(c*x) + e

errs = (np.diag(cov))**2
print(errs)
plt.plot(x, y, 'bo', label="y-original")
plt.scatter(x, yfit1, label="y=a*np.sin(b*x) + h*np.cos(c*x) + e")
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best', fancybox=True, shadow=True)
plt.grid(True)
plt.show() 

