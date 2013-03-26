def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story.
    """
    for adj in listOfAdjs:
        if adj in story:
            story = story.replace(adj, '[ADJ]')
    for verb in listOfVerbs:
        if verb in story:
            story = story.replace(verb, '[VERB]')
    for noun in listOfNouns:
        if noun in story:
            story = story.replace(noun, '[NOUN]')

    return story
