from sympy.logic.boolalg import to_cnf, is_cnf
from sympy.abc import *

class toString:
    def __init__(self, P):
        self.P = P
    def __str__(self):
        return self.P
    
def CNF(formula): 

    result = is_cnf(formula)
    if result == False:
        cnf = to_cnf(formula)
    else:
        cnf = formula

    cnf_str = toString(str(cnf))
    cnf_str = str(cnf_str)

    return cnf_str