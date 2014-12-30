def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    iterNum = 1
    gcd = 1
    while(iterNum <= (min(a, b))):
        if((a % iterNum == 0) and (b % iterNum == 0)):
            gcd = iterNum
        iterNum += 1
    return gcd
