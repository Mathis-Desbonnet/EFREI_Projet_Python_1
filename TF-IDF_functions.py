def occurrenceOfWords(text : str, word : str):
    """
    Returns the number of occurrences of a word in a text.
    """
    words = text.split()
    counter = 0
    for i in words:
        if i == word:
            counter += 1
    return counter

def TFCalculator(text : str):
    """
    Returns the term frequency of each word in a text.
    """
    words = text.split()
    words = list(set(words))
    TF = {}
    for word in words:
        TF[word] = occurrenceOfWords(text, word)
    return TF

print(TFCalculator(open("./cleaned/Nomination_Chirac1.txt", "r").read()))