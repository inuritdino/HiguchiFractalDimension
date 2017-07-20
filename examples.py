#!/usr/bin/python3

"""
Some basic examples of HFD usage.
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from hfd import hfd, curve_length, lin_fit_hfd
import tretsa

def apply_hfd(x,name=None):
    ## HFD optimized
    print("*** HFD optimized")
    t = time.time()
    print("\tHFD=",-hfd(x,opt=True))
    print("\ttiming:",time.time() - t)
    ## HFD, not optimized
    print("*** HFD non-optimized")
    t = time.time()
    print("\tHFD=",-hfd(x,opt=False))
    print("\ttiming:",time.time() - t)
    ##
    print("*** step-by-step (not-optimized)")
    t = time.time()
    k, L = curve_length(x,opt=False)
    HFD = -lin_fit_hfd(np.log2(k),np.log2(L),log=False)
    print("\tHFD=",HFD)
    print("\ttiming:",time.time()-t)
    plt.plot(np.log2(k),np.log2(L),'.')
    plt.annotate("HFD = "+str(HFD),(0.05,0.1),xycoords='axes fraction')
    plt.xlabel('Log interval')
    plt.ylabel('Log curve length')
    if name:
        plt.title(name)

    return HFD;

def apply_dfa(x,name=None):
    print("*** DFA")
    t = time.time()
    f,l = tretsa.DFA(x,return_logarithms=True)
    print("\tDFA time:",time.time() - t)
    alpha = np.polyfit(l,f,deg=1)[0]
    print("\talpha(DFA) =",alpha)
    plt.plot(l,f,'.')
    plt.annotate("alpha = "+str(alpha),(0.05,0.9),xycoords='axes fraction')
    plt.xlabel('Log length')
    plt.ylabel('Log fluctuation')
    if name:
        plt.title(name)

    return alpha;

### Higuchi original data: random Gaussian increments = Brownian
N = 2**16
z = np.random.randn(N+1000)
x = np.empty(N,dtype=np.float)
for i in range(N):
    x[i] = np.sum(z[:(i+1000)])

plt.subplot(421)
apply_dfa(x,"Brownian")
plt.subplot(422)
apply_hfd(x,"Brownian")

### Gaussian
N = 2**11
x = np.random.randn(N)

plt.subplot(423)
apply_dfa(x,"Gaussian")
plt.subplot(424)
apply_hfd(x,"Gaussian")

### Pink noise
N = 2**17
x = tretsa.util.generate_data_with_scaling(1.0,N=N)

plt.subplot(425)
apply_dfa(x,"Pink")
plt.subplot(426)
apply_hfd(x,"Pink")

### Heart data
x = np.loadtxt('test.txt')
x = x[x<180]
# plt.plot(x)

plt.subplot(427)
apply_dfa(x,"Heart")
plt.subplot(428)
apply_hfd(x,"Heart")
plt.show()
