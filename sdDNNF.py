from truthTableGenerator import isWellFormed
from smooth_and import *
from smooth_or import *

def smooth(formula):
    # Eliminates the parenteses at the beginning and at the end but it has to keep sense
    while formula[0] == "(" and formula[-1] == ")" and isWellFormed(formula[1:len(formula) - 1]):
        formula = formula[1:len(formula) - 1]
    
    # Check if there is and & or and | at level 0
    bracketLevel = 0
    for i in reversed(range(len(formula))):
        if formula[i] == "(":
            bracketLevel += 1
        if formula[i] == ")":
            bracketLevel -= 1
        if formula[i] == "&" and bracketLevel == 0:
            L = formula[: i]
            R = formula[i+1 :]
            result_and = AND_smooth_and(L, R)
            return result_and
        elif formula[i] == "|" and bracketLevel == 0:
            L = formula[: i]
            R = formula[i+1 :]
            result_or = OR_smooth_or(L, R)
            return result_or