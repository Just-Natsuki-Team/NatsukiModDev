#...It's crap text what more do you want from me?

#This defines a single function that generates garbage text of a given character length
init python:
    import random

    nonunicode = "blah"

    def craptext(length):
        output = ""
        for x in range(length):
            output += random.choice(nonunicode)
        return output
