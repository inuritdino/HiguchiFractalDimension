# Higuchi Fractal Dimension (HFD)

Following:
T. Higuchi, Approach to an Irregular Time Series on the
Basis of the Fractal Theory, Physica D, 1988; 31: 277-283.

### Requirements

- Python3
- NumPy
- C compiler (for the optimized version)

### Compilation (optional)

To compile the C library (assume the compiler name is `gcc`):

```bash
gcc -shared hfd.c -o libhfd.so -lm -fPIC
```

Keep the name for the output library `libhfd.so`: Python wrapper looks for this name.

### Python module

In python, assuming the package is in the Python's path and called `HiguchiFractalDimension`:

```python
import HiguchiFractalDimension
```

The module contains several functions:

- `hfd` calculates HFD of a 1D series
- `curve_length` caculates a paired array (k,Lk), i.e. interval "times" and the curve length.
- `lin_fit_hfd` calculates linear fitting from (k,Lk) data and returns HFD.


### Examples

```python
import numpy as np
import HiguchiFractalDimension as hfd

x = np.random.randn(10000)
y = np.empty(9900)
for i in range(x.size-100):
	y[i] = np.sum(x[:(i+100)])
	
## Note x is a Guassian noise, y is the original Brownian data used in Higuchi, Physica D, 1988.

hfd.hfd(x) # ~ 2.00
hfd.hfd(y) # ~ 1.50
```
