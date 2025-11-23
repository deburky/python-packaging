# test/test_harmonic_mean.py
import numpy as np

from imppkg.harmonic_mean import harmonic_mean as py_harmonic_mean

try:
    from imppkg.harmonic_mean import harmonic_mean as cy_harmonic_mean
except ImportError:
    from imppkg.harmonic_mean import harmonic_mean as cy_harmonic_mean

NUM_RUNS = 500


def test_harmonic_mean():
    """Test correctness of Python and Cython implementations."""
    data = np.array([1, 2, 4], dtype=np.float64)
    expected = 3 / (1 + 1 / 2 + 1 / 4)
    assert abs(py_harmonic_mean(data) - expected) < 1e-9
    assert abs(cy_harmonic_mean(data) - expected) < 1e-9


def time_harmonic_mean():
    """Time the performance of Python vs Cython implementations."""
    import timeit
    import random

    data = [random.uniform(1, 100) for _ in range(10**6)]
    py_time = timeit.timeit(lambda: py_harmonic_mean(data), number=NUM_RUNS)
    cy_time = timeit.timeit(lambda: cy_harmonic_mean(data), number=NUM_RUNS)
    print(f"Python harmonic_mean: {py_time:.4f} seconds ({NUM_RUNS} runs)")
    print(f"Cython harmonic_mean: {cy_time:.4f} seconds ({NUM_RUNS} runs)")


if __name__ == "__main__":
    test_harmonic_mean()
    print("All tests passed.")
    time_harmonic_mean()
