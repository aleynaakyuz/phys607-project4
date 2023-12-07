"""
This is an excercise for curve fitting tuttorial.

We are going to fit a function to the data that we
used in the class in 10/31

You need to plot the fitted function onto the data 
and print the errors.
"""

import h5py
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


f = h5py.File('./data.hdf', 'r')

print(f.keys())

print(f['data'].keys())

x = f['data/xpos'][:]
y = f['data/ypos'][:]

plt.scatter(x, y)
plt.show()

#def model():

    # function that you guess
    #return 

#params, cov = curve_fit()


