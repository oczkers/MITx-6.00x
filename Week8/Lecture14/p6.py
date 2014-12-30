import random


def choose():
    bucket = [0, 1, 2, 3, 4, 5]
    r = 0
    g = 0

    for draw in range(3):
        i = random.choice(bucket)
        bucket.remove(i)
        if i % 2 == 0:
            r += 1
        else:
            g += 1

        if g > 0 and r > 0:
            return False
    return True


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    fraction = 0
    for i in range(numTrials):
        if choose():
            fraction += 1
    return float(fraction) / numTrials
