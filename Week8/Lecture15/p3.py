from math import sqrt


def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if not L:
        return float('NaN')

    n = len(L)
    u = 0
    for i in L:
        u += len(i)
    u = float(u) / n

    return sqrt(float(sum([(len(t) - u) ** 2 for t in L])) / n)
