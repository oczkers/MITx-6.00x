def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string

    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) != len(str2):
        return False
    if len(str1) > 0:
        if str1[0] == str2[-1]:
            str1 = str1[1:]
            str2 = str2[:-1]
            return semordnilap(str1, str2)
        else:
            return False
    else:
        return True
