# Alphabet
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def weighted_model(formula, positive, negative):
    weight = ""
    for el in formula:
        if el in ALPHABET:
            weight += str(positive.get(el))
        elif el in ALPHABET.lower():
            weight += str(negative.get(el.upper()))
        elif el == "&":
            weight += "*"
        elif el == "|":
            weight += "+"
        else:
            weight += el
    return eval(weight)
