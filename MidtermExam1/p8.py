def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    if madTemplate == '[ADJ]':
        valid = listOfAdjs
    elif madTemplate == '[VERB]':
        valid = listOfVerbs
    elif madTemplate == '[NOUN]':
        valid = listOfNouns

    return userWord in valid
