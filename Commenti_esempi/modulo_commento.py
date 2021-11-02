def average(a, b) -> float:
    """
    Return the average value (arithmetic mean) of two numbers.

    Parameters
    ----------
    a : numeric
        A number to average.
    b : numeric
        Another number to average.

    Returns
    -------
    result : float
        The average of a and b, computed using ``0.5 * (a + b)``.

    Example
    -------
    >>> average(5, 10)
    7.5
    """
    return (a + b) * 0.5