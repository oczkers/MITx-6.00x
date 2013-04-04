import random


def deterministicNumber():
    '''
    Deterministically generates an even number between 9 and 21
    '''
    return 10  # ;-)


def stochasticNumber():
    '''
    Stochastically generates a uniformly distributed even number between 9 and 21
    '''
    evens = [i for i in range(9, 22) if i % 2 == 0]
    return random.choice(evens)
