from truthTableGenerator import isWellFormed

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def remove_brackets(formula):
    # Eliminates the parenteses at the beginning and at the end but it has to keep sense
    while formula[0] == "(" and formula[-1] == ")" and isWellFormed(formula[1:len(formula) - 1]):
        formula = formula[1:len(formula) - 1]
    return formula

def OR_smooth_and(L, R):
    L = remove_brackets(L)
    R = remove_brackets(R)

    if "|" in L:
        sub = L.split("|", 1)
        smooth_L = OR_smooth_or(sub[0], sub[1])
    else:
        smooth_L = L

    if "|" in R:
        sub = R.split("|", 1)
        smooth_R = OR_smooth_or(sub[0], sub[1])
    else:
        smooth_R = R

    return smooth_L + "&(" + smooth_R + ")"
        

def OR_smooth_or(L, R):
    L = remove_brackets(L)
    R = remove_brackets(R)

    if "|" in L:
        bracketLevel = 0
        for i in reversed(range(len(R))):
            if L[i] == "(":
                bracketLevel += 1
            if L[i] == ")":
                bracketLevel -= 1
            if L[i] == "&" and bracketLevel == 0:
                sub0 = L[: i]
                sub1 = L[i+1 :]
                break
        smooth_L = OR_smooth_and(sub0, sub1)
    else:
        smooth_L = L

    if "|" in R:
        bracketLevel = 0
        for i in reversed(range(len(R))):
            if R[i] == "(":
                bracketLevel += 1
            if R[i] == ")":
                bracketLevel -= 1
            if R[i] == "&" and bracketLevel == 0:
                sub0 = R[: i]
                sub1 = R[i+1 :]
                break
        smooth_R = OR_smooth_and(sub0, sub1)
    else:
        smooth_R = R

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