word = input("Please enter your word that you want to use the duplicate encoder for")

def duplicate_encode(word):
    word = word.lower()
    letterlist = list(word)
    output = ""
    for i in range (0, len(letterlist)):
        if letterlist.count(letterlist[i]) == 1:
            output += "("
        else:
            output += ")"
    return output


print(duplicate_encode(word))
