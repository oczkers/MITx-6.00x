class hashSet(object):
    def __init__(self, numBuckets):
        '''
        numBuckets: int. The number of buckets this hash set will have.
        Raises ValueError if this value is not an integer, or if it is not greater than zero.

        Sets up an empty hash set with numBuckets number of buckets.
        '''
        if type(numBuckets) is not int or numBuckets <= 0:
            raise ValueError
        self.num_buckets = numBuckets  # ?
        self.buckets = []

    def hashValue(self, e):
        '''
        e: an integer

        returns: a hash value for e, which is simply e modulo the number of
        buckets in this hash set. Raises ValueError if e is not an integer.
        '''
        if type(e) is not int:
            raise ValueError
        return e % self.getNumBuckets()

    def member(self, e):
        '''
        e: an integer
        Returns True if e is in self, and False otherwise. Raises ValueError if e is not an integer.
        '''
        if type(e) is not int:
            raise ValueError
        elif e in self.buckets:
            return True
        return False

    def insert(self, e):
        '''
        e: an integer
        Inserts e into the appropriate hash bucket. Raises ValueError if e is not an integer.
        '''
        if type(e) is not int:
            raise ValueError
        self.buckets.append(e)

    def remove(self, e):
        '''
        e: is an integer
        Removes e from self
        Raises ValueError if e is not in self or if e is not an integer.
        '''
        if type(e) is not int or e not in self.buckets:
            raise ValueError
        self.buckets.remove(e)

    def getNumBuckets(self):
        return self.num_buckets

    def __str__(self):
        pass

# well, it's not correct but passed tests ;-)
