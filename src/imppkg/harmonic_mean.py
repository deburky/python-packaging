def harmonic_mean(nums):
    """
    Pure Python implementation of harmonic mean.
    Args:
        nums (list or iterable of numbers): The numbers to calculate the harmonic mean of.
    Returns:
        float: The harmonic mean of the numbers.
    """
    n = len(nums)
    if n == 0:
        raise ValueError("harmonic_mean requires at least one data point")
    return n / sum(1 / num for num in nums)
