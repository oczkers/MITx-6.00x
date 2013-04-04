import random


def genEven():
    '''
    Generates a random number x, where 0 <= x < 100
    '''
    evens = [i for i in range(0, 100) if i % 2 == 0]
    return random.choice(evens)
