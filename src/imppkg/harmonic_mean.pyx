import cython
import numpy as np

cimport numpy as np


@cython.boundscheck(False)
@cython.wraparound(False)
def harmonic_mean(np.ndarray[np.double_t, ndim=1] nums):
    cdef Py_ssize_t n = nums.shape[0]
    cdef double s = 0.0
    cdef Py_ssize_t i
    for i in range(n):
        s += 1.0 / nums[i]
    return n / s