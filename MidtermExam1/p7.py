def generateTemplates(madLibsForm):
    """
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.
    """
    forms = []
    for word in madLibsForm.split(' '):
        if word == '[ADJ]':
            forms.append('[ADJ]')
        elif word == '[VERB]':
            forms.append('[VERB]')
        elif word == '[NOUN]':
            forms.append('[NOUN]')
    return forms
