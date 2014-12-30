def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    tup_len = len(aTup)
    if tup_len == 0:
        return ()
    tup_new = [aTup[0]]
    n = 2
    while n < tup_len:
        tup_new.append(aTup[n])
        n += 2
    return tuple(tup_new)
