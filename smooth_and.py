from truthTableGenerator import isWellFormed

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def remove_brackets(formula):
    # Eliminates the parenteses at the beginning and at the end but it has to keep sense
    while formula[0] == "(" and formula[-1] == ")" and isWellFormed(formula[1:len(formula) - 1]):
        formula = formula[1:len(formula) - 1]
    return formula


def AND_smooth_or(L, R):
    L = remove_brackets(L)
    R = remove_brackets(R)

    smooth_L = L

    if len(R) == 3:
        smooth_R = R
    else:
        sub = R.split("&", 1)
        smooth_R = AND_smooth_and(sub[0], sub[1])

    for el in L:
        # If element is a literal
        if el in ALPHABET or el in ALPHABET.lower():
            # If element doesn't appear in the right formula
            if el.upper() not in smooth_R and el.lower() not in smooth_R:
                smooth_R += "&(" + el.upper() + "|" + el.lower() + ")"   

    for el in R:
        # If element is a literal
        if el in ALPHABET or el in ALPHABET.lower():
            # If element doesn't appear in the right formula
            if el.upper() not in smooth_L and el.lower() not in smooth_L:
                smooth_L += "&(" + el.upper() + "|" + el.lower() + ")"
    
    return "(" + smooth_L + ")|(" + smooth_R + ")"

def AND_smooth_and(L, R):
    
    L = remove_brackets(L)
    R = remove_brackets(R)

    if "|" in L:
        smooth_L = L.split("|", 1)
        result_L = AND_smooth_or(smooth_L[0], smooth_L[1])
    else:
        result_L = L

    if "|" in R:
        smooth_R = R.split("|", 1)
        result_R = AND_smooth_or(smooth_R[0], smooth_R[1])
    else:
        result_R = R

    return "(" + result_L + ")&(" + result_R + ")"