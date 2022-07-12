def after_first(text, marker):

    indFirst = text.index(marker)
    return text[indFirst+len(marker):]

def before_first(text, marker):
    return text[:text.index(marker)]

def scoop(text, starter, ender):
    
    cutOne = after_first(text, starter)
    cutTwo = before_first(cutOne, ender)
    return cutTwo