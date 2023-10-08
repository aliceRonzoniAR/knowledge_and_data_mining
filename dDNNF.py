from truthTableGenerator import isWellFormed
from shannon_upper import *
from shannon_lower import *
from shannon_equal import *

def shannon(dictionary):
    output = ""
    for key, value in dictionary.items():
        #If the value is a tuple
        if len(value) == 2 and type(value) == tuple:
            # If the key in the tuple is equal for both formulas
            if key in value[0] and key in value[1]:
                if key.isupper():
                    output += shannon_equal(key, value, "u")
                else:
                    output += shannon_equal(key, value, "l")
            else:
                output += "("
                for val in value:
                    lit = val.split("|")
                    if key.isupper():
                        output += shannon_upper(key, lit)    
                    else:
                        # Key è minuscola
                        output += shannon_lower(key, lit)
                output = output[:-1]
                output += ")&"
        # If there are only 2 literals
        elif len(value) == 3:
            par = 0
            lit = value.split("|")
            lit.remove(key)
            if key.isupper():
                output += "(" + key + "|(" + key.lower() + "&"
            elif key.islower():
                output += "(" + key + "|(" + key.upper() + "&"
            par += 2
            output += value[0]
            output += ")" * par
            output += "&"
        else:
            # If it is not a tuple and has more than two literals
            literals = value.split("|")
            literals.remove(key)
            if key.isupper():
                output += "(" + key + "|(" + key.lower() + "&"
            elif key.islower():
                output += "(" + key + "|(" + key.upper() + "&"
            for i in range(len(literals) - 1):
                if literals[i].isupper():
                    output += "(" + literals[i] + "|(" + literals[i].lower() + "&"
                elif literals[i].islower():
                    output += "(" + literals[i] + "|(" + literals[i].upper() + "&"
            par += 2
            output += literals[-1]
            output += ")" * par
            output += "|"
    return output[:-1]

def to_dDNNF(input):
    # ELiminate white spaces
    input = input.replace(" ", "")
    d = {}
    # Alphabet
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    new_input = input
    # In this for we replace the negation of a literal with its lower value
    for i in reversed(range(len(input))):
        # If it is a literal
        if input[i] in ALPHABET:
            # Check if it is negated
            if input[i - 1] == "~":
                literal = input[i].lower()
                toRemove = input[i - 1] + input[i] 
                # Replace substitues every occurence in the formula
                new_input = new_input.replace(toRemove, literal)
    
    # Split the formula according to the value of & (the in put is in CNF so we are safe that & is only external to parentesis)
    v = new_input.split("&")
    
    for i in range(len(v)):
        #Eliminate parentesis
        while v[i][0] == "(" and v[i][-1] == ")" and isWellFormed(v[i][1:len(v[i]) - 1]):
            v[i] = v[i][1:len(v[i]) - 1]
    c = v.copy()

    # Loop on formulas 
    for i in range(len(v)):
        if v[i] not in c:
            #Se non compare in c, vuol dire che l'ho già considerato e quindi posso passare avanti
            continue
        break_flag = False
        equal = False
        # Divide the literals
        lit = v[i].split("|")
        # Consider every literal
        for j in range(len(lit)):
            # Compare all the other literals
            for k in range(i+1, len(v)):
                # If the first literal is positive
                if lit[j].isupper():
                    # Check if the negation of the first literal appear in the other formulas
                    if lit[j].lower() in v[k]:
                        break_flag = True
                        # Build dictionary: 'literal' : ('formula1', 'formula2')
                        d[lit[j]] = (v[i], v[k])
                        # Remove the literal from the formulas
                        c.remove(v[i])
                        c.remove(v[k])
                        break
                # If the first literal is negative
                else:
                    # Check if the negation (positive) of the first literal appear in the other formulas
                    if lit[j].upper() in v[k]:
                        break_flag = True
                        # Build dictionary: 'literal' : ('formula1', 'formula2')
                        d[lit[j]] = (v[i], v[k])
                        # Remove the literal from the formulas
                        c.remove(v[i])
                        c.remove(v[k])
                        break
                # Controllo se il letterale compare uguale nelle altre formule
                if lit[j] in v[k]:
                    equal = True
                    key = lit[j]
                    value = v[k]
                
            if break_flag:
                break
            # Se sto considerando l'ultimo elemento della disjunction vuol dire che prima non e' mai stato inserito
            elif j == len(lit) - 1:
                # COntrollo se compariva uguale nelle altre formule
                if equal:
                    # Se compariva uguale inserisco le formule nel dizionario
                    d[key] = (v[i], value)
                    # Remove the literal from the formulas
                    c.remove(v[i])
                    c.remove(value)
                else:
                    # Se la formula ha tutti letterali diversi la inserisco nel dizionario
                    d[lit[j]] = v[i]
    return shannon(d)