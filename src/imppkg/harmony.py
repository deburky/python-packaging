import contextlib
import sys

import numpy as np
from termcolor import cprint

from imppkg.harmonic_mean import harmonic_mean


def main():
    result = 0.0
    try:
        nums = [float(num) for num in sys.argv[1:]]
    except ValueError:
        nums = []
    nums = np.array(nums, dtype=np.float64)  # Convert to NumPy array
    with contextlib.suppress(ZeroDivisionError):
        result = harmonic_mean(nums)
    cprint(str(result), "grey", "on_cyan", attrs=["bold"])
