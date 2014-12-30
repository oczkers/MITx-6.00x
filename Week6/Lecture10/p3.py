def isPrime(n):
    if type(n) != int:
        raise TypeError
    elif n == 0:
        raise ValueError

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
