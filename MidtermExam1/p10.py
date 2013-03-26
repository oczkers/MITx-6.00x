def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)


def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    numbers = (5, 8, 24)

    step = 1
    while True:
        results = [sum(i) == n for i in combinations_with_replacement(numbers, step) if sum(i) <= n]
        if True in results:
            return True
        elif len(results) == 0:
            return False
        step += 1
