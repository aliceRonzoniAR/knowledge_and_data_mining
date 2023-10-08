from sympy.logic.boolalg import to_nnf, is_nnf
from sympy.abc import *
from NNF import *
from CNF import *
from dDNNF import *
from sdDNNF import *
from model_counting import *

def maiusc(formula):
    output = ""
    for el in formula:
        if el in ALPHABET.lower():
            output += "~" + el.upper()
        else:
            output += el
    return output

# Definisci la formula logica
#---------------------------------
formula = (A >> B | C) & (C >> ~A)
positive_weights = {"A": 1, "B": 1, "C": 1}
negative_weights = {"A": 1, "B": 1, "C": 1}
#------------------------------------

#------------------------------------
# formula = (A >> B | C) & (C >> D | F)
# positive_weights = {"A": 1, "B": 1, "C": 1, "D": 1, "F": 1}
# negative_weights = {"A": 1, "B": 1, "C": 1, "D": 1, "F": 1}
#--------------------------------------

#--------------------------------------
# formula = (A | B) & (C | D) & (~D | F)
# positive_weights = {"A": 1, "B": 1, "C": 1, "D": 1, "F": 1}
# negative_weights = {"A": 1, "B": 1, "C": 1, "D": 1, "F": 1}
#---------------------------------------

#---------------------------------------
# formula = ((A & B) >> C) & (~B | ~D)
# positive_weights = {"A": 1, "B": 1, "C": 1, "D": 1}
# negative_weights = {"A": 1, "B": 1, "C": 1, "D": 1}
#---------------------------------------

#---------------------------------------
# formula = (A | B) & (~B | C) & (~D | F)
# positive_weights = {"A": 1, "B": 1, "C": 1, "D": 1, "F": 1}
# negative_weights = {"A": 1, "B": 1, "C": 1, "D": 1, "F": 1}
#---------------------------------------

# Chiamata a CNF
cnf_str = CNF(formula)
print("CNF: ", cnf_str)

# Chiamata a dDNNF
dDnnf = to_dDNNF(cnf_str)
dDNNF_str = maiusc(dDnnf)
print("dDNNF: ", dDNNF_str)

# Chiamata a smooth
sdDNNF = smooth(dDnnf)
sdDNNF_str = maiusc(sdDNNF)
print("sd-DNNF: ", sdDNNF_str)

weight = weighted_model(sdDNNF, positive_weights, negative_weights)
print("Weighted Model Counting: ", weight)
