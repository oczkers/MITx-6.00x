def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        exp -= 1
        # return base * iterPower(base, exp)
        result = base
        for i in range(exp):
            result *= base
        return result
