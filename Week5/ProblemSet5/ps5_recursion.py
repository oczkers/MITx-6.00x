# 6.00x Problem Set 5
#
# Part 2 - RECURSION


#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.

    aStr: a string
    returns: a reversed string
    """
    if len(aStr) < 2:
        return aStr
    else:
        return aStr[-1] + reverseString(aStr[1:-1]) + aStr[0]


#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False

    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if len(x) == 0:
        return True
    elif x[0] in word:
        return x_ian(x[1:], word[word.index(x[0]):])
    else:
        return False


#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately.
    """
    def insertNewlinesRec(text, lineLength):
        if len(text) <= lineLength:
            return text
        elif text[lineLength - 1] == ' ':
            return '%s\n%s' % (text[:lineLength], insertNewlinesRec(text[lineLength:], lineLength))
        else:
            return text[0] + insertNewlinesRec(text[1:], lineLength)

    return insertNewlinesRec(text, lineLength)
