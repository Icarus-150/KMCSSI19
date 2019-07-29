
def pluralize(word,num):

    if num > 1:
        if word [-3:]== "ife" :
            return( word[:-3] + "ives")
        elif word[-2:] == "sh" or word[-2:] == "ch" :
            return( word + "es")
        elif word[-2:] == "us":
            return(word[:-2] + "i")
        elif word[-2:] == "ay" or word[-2:] == "oy" or word[-2:] == "ey" or word[-2:] == "uy":
            return(word + "s")
        elif word[-2:] == "y ":
            return(word[:-2] + "ies")
        else:
            return(word +"s")
    else:
        return[word]

print(pluralize(raw_input("enter word:   "),(raw_input("enter number:  "))))
