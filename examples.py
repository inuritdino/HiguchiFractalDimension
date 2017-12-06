#!/usr/bin/python3

"""
Some basic examples of HFD usage.
Note: extra dependency: Matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from hfd import hfd, curve_length, lin_fit_hfd

def apply_hfd(x,name=None):
    print("##################")
    print("#### "+str(name))
    print("##################")
    ## HFD optimized
    print("*** HFD optimized")
    t = time.time()
    print("\tHFD=",hfd(x,opt=True))
    print("\ttiming:",time.time() - t)
    ## HFD, not optimized
    print("*** HFD non-optimized")
    t = time.time()
    print("\tHFD=",hfd(x,opt=False))
    print("\ttiming:",time.time() - t)
    ##
    print("*** step-by-step (not-optimized)")
    t = time.time()
    k, L = curve_length(x,opt=False)
    HFD = lin_fit_hfd(np.log2(k),np.log2(L),log=False)
    print("\tHFD=",HFD)
    print("\ttiming:",time.time()-t)
    plt.plot(np.log2(k),np.log2(L),'.')
    plt.annotate("HFD = "+str(HFD),(0.05,0.1),xycoords='axes fraction')
    plt.xlabel('Log interval')
    plt.ylabel('Log curve length')
    if name:
        plt.title(name)

    return HFD;

### Higuchi original data: random Gaussian increments = Brownian
N = 2**16
z = np.random.randn(N+1000)
x = np.empty(N,dtype=np.float)
for i in range(N):
    x[i] = np.sum(z[:(i+1000)])

plt.subplot(221)
apply_hfd(x,"Brownian")

### Gaussian
N = 2**11
x = np.random.randn(N)

plt.subplot(222)
apply_hfd(x,"Gaussian")

### Pink noise
N = 2**17
x = np.loadtxt('pink.txt')

plt.subplot(223)
apply_hfd(x,"Pink")

### Heart data
x = np.loadtxt('heart.txt')
x = x[x<180]

plt.subplot(224)
apply_hfd(x,"Heart: inter-beat intervals")
plt.show()
