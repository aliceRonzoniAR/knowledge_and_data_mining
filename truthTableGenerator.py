# This function controls if the formula is well formed.
# It checks if for every '(' there is the corrisponding ')'
#
# INPUT: P is a proposition
# OUTPUT: True if the proposition is well formed, False if is not

def isWellFormed(P):
    bracketLevel = 0
    for p in P:
        if p == "(":
            bracketLevel += 1
        elif p == ")":
            # If there is only a close ')' without any '(' stop running and return False
            if bracketLevel == 0:
                return False
            # There was an opening '(' and now also a close one so we reduce the number
            bracketLevel -= 1
    return bracketLevel == 0

#######################################################################################
#
#   In this section there are function to determine the truth values returned by the logical connectives
#
# INPUT: P, Q are propositions
#        truthValues is a dictionary that contains the value (True or False) for each variable
#
# OUTPUT: depends on the result returned by function parseProposition
#         parseProposition returns the truth value of a proposition
#######################################################################################

def negation(P, truthValues):
    return not parseProposition(P, truthValues)
 
def conjunction(P, Q, truthValues):
    return parseProposition(P, truthValues) and parseProposition(Q, truthValues)

def disjunction(P, Q, truthValues):
    return parseProposition(P, truthValues) or parseProposition(Q, truthValues)

# A -> B == ~A | B
def implication(P, Q, truthValues):
    return (not parseProposition(P, truthValues)) or parseProposition(Q, truthValues)

def equivalence(P, Q, truthValues):
    return parseProposition(P, truthValues) == parseProposition(Q, truthValues)

########################################################################################
#
#   END SECTION
#
########################################################################################



# This function return the truth value of a singular literal or of a proposition

def parseProposition(P, truthValues):
    P = P.replace(" ", "")

    if not isWellFormed(P):
        return "Error"

    # Eliminates the parenteses at the beginning and at the end but it has to keep sense
    while P[0] == "(" and P[-1] == ")" and isWellFormed(P[1:len(P) - 1]):
        P = P[1:len(P) - 1]

    if len(P) == 1:
        return truthValues[P]
    
    # At this point we have to evaluate the proposition respecting the priority
    # To do that we check in reverse order of priority.
    # Since we are dealing with recursive calls we want that the first to be evaluated is 
    # the one with higher priority, so the last in the recursive call.

    # Table of priority
    #
    #   Symbol  | Priority
    #      ~    |    1
    #      &    |    2
    #      |    |    3
    #      >    |    4
    #      =    |    5

    # Checks if at level0 there is an equivalence (=)
    bracketLevel = 0
    for i in reversed(range(len(P))):
        if P[i] == "(":
            bracketLevel += 1
        if P[i] == ")":
            bracketLevel -= 1
        if P[i] == "=" and bracketLevel == 0:
            return equivalence(P[0:i], P[i + 1:], truthValues)
        
    # Checks if at level0 there is an implication (>)
    bracketLevel = 0
    for i in reversed(range(len(P))):
        if P[i] == "(":
            bracketLevel += 1
        if P[i] == ")":
            bracketLevel -= 1
        if P[i] == ">" and bracketLevel == 0:
            return implication(P[0:i], P[i + 1:], truthValues)

    # Checks if at level0 there is a disjunction (|)
    bracketLevel = 0
    for i in reversed(range(len(P))):
        if P[i] == "(":
            bracketLevel += 1
        if P[i] == ")":
            bracketLevel -= 1
        if P[i] == "|" and bracketLevel == 0:
            return disjunction(P[0:i], P[i + 1:], truthValues)

    # Checks if at level0 there is a conjunction (&)
    bracketLevel = 0
    for i in reversed(range(len(P))):
        if P[i] == "(":
            bracketLevel += 1
        if P[i] == ")":
            bracketLevel -= 1
        if P[i] == "&" and bracketLevel == 0:
            return conjunction(P[0:i], P[i + 1:], truthValues)

    # Checks if at level0 there is a negation (~)
    bracketLevel = 0
    for i in reversed(range(len(P))):
        if P[i] == "(":
            bracketLevel += 1
        if P[i] == ")":
            bracketLevel -= 1
        if P[i] == "~" and bracketLevel == 0:
            return negation(P[i + 1:], truthValues)

def writeTruthTable(P, positive_weights, negative_weights):

    # Total weight is the sum of the weights of True evaluation of the proposition
    total_weight = 0

    # Select the variables that are present in the formula and assign them the value True
    truthValues = {}
    for i in range(len(P)):
        if P[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            truthValues[P[i]] = True

    # Print the head of the table
    for statement in list(truthValues.keys()):
        print(statement, end=" | ")
    print("\tw(I)\t| ", P)


    # Print truth table for the first row (all TRUE)
    for truthValue in list(truthValues.values()):
        print("T", end=" | ")
    
    # Print weight and first result for the first row (all TRUE)
    # Weight is given by the product of the single elements
    weight = 1
    for key, value in truthValues.items():
        if value == True:
            weight *= positive_weights.get(key)
        else:
            weight *= negative_weights.get(key)        

    # Print the evaluation of the proposition for the first raw
    print("\t", weight, end="\t| ")
    if parseProposition(P, truthValues):
        # If it's T keep track of the weight
        total_weight += weight
        print("T")
    else:
        print("F")

    # j is the index, we start from the last element
    j = len(truthValues.values()) - 1
    # Keep running the while cicle until every literal has been evaluated FALSE
    while True in truthValues.values():
        # Select the key of the j-element in the dictionary truthValues
        key = list(truthValues.keys())[j]
        # Negation of its value
        truthValues[key] = not truthValues[key]

        # if truthValues[key] == FALSE => TRUE esecute following lines
        # if truthValues[key] == TRUE  => FALSE go to the next element in the dictionary
        if not truthValues[key]:
            for truthValue in list(truthValues.values()):
                print("T" if truthValue else "F", end=" | ")

            # Print weight and result of the line
            weight = 1
            for key, value in truthValues.items():
                if value == True:
                    weight *= positive_weights.get(key)
                else:
                    weight *= negative_weights.get(key)        

            print("\t", weight, end="\t| ")
                
            # Evaluate teh proposition and print the result
            if parseProposition(P, truthValues):
                # keep track of the weight
                total_weight += weight
                print("T")
            else:
                print("F")
            j = len(truthValues.values()) - 1
        else:
            j -= 1

    print("\n\nWeighted Model Counting: ", total_weight)