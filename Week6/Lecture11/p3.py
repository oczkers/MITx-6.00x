def genPrimes():
    allp = []
    for i in range(2, 999999):
        if all((i % p) != 0 for p in allp):
            allp.append(i)
            yield i
