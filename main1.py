## This file is used to import the formula and the weights to calculate the truth table

from truthTableGenerator import *

# Definisci la formula logica
#---------------------------------
formula = "(A > B | C) & (C > ~A)"
positive_weights = {"A": 1, "B": 1, "C": 1}
negative_weights = {"A": 1, "B": 1, "C": 1}
#------------------------------------

#------------------------------------
# formula = "(A > B | C) & (C > D | F)"
# positive_weights = {"A": 1, "B": 1, "C": 1, "D": 1, "F": 1}
# negative_weights = {"A": 1, "B": 1, "C": 1, "D": 1, "F": 1}
#--------------------------------------

#--------------------------------------
# formula = "(A | B) & (C | D) & (~D | F)"
# positive_weights = {"A": 1, "B": 1, "C": 1, "D": 1, "F": 1}
# negative_weights = {"A": 1, "B": 1, "C": 1, "D": 1, "F": 1}
#---------------------------------------

#---------------------------------------
# formula = "((A & B) > C) & (~B | ~D)"
# positive_weights = {"A": 1, "B": 1, "C": 1, "D": 1}
# negative_weights = {"A": 1, "B": 1, "C": 1, "D": 1}
#---------------------------------------

#---------------------------------------
# formula = "(A | B) & (~B | C) & (~D | F)"
# positive_weights = {"A": 1, "B": 1, "C": 1, "D": 1, "F": 1}
# negative_weights = {"A": 1, "B": 1, "C": 1, "D": 1, "F": 1}
#---------------------------------------

# Result obtained by the truth table
writeTruthTable(formula, positive_weights, negative_weights)