def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    midPos = len(aStr)/2
    while(char != aStr[midPos]):
        if(midPos == 0):
            return False
        if char < aStr[midPos]:
            return isIn(char, aStr[:midPos])
        if char > aStr[midPos]:
            return isIn(char, aStr[midPos:])
    return True

