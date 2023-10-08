def shannon_equal(key, tuple, case):
    par = 1
    formula = "(" + key + ")|("

    #remove key from sub1 and sub2
    if case == "l":
        # key is lower
        # check length of sub1
        for i in range(len(tuple)):
            #keep literals
            if "|" in tuple[i]:
                lit = tuple[i].split("|")
                lit.remove(key)

            # Create the formula
            if len(lit) == 1:
                formula += "(" + key.upper() + "&" + lit[0] + ")&("
            else:
                for j in range(len(lit) - 1):
                    if lit[j].isupper():
                        formula += lit[j] + "|(" + lit[j].lower() + "&"
                    else:
                        formula += lit[j] + "|(" + lit[j].upper() + "&"
                    par += 2
                # Insert last literal and close parentesis
                formula += lit[-1]
                formula += ")" * par
                formula += "|"
    else:
        # key is upper
        # check length of sub1
        for i in range(len(tuple)):
            #keep literals
            if "|" in tuple[i]:
                lit = tuple[i].split("|")
                lit.remove(key)

            # Create the formula
            if len(lit) == 1:
                formula += "(" + key.lower() + "&" + lit[0] + ")&("
            else:
                for j in range(len(lit) - 1):
                    if lit[j].isupper():
                        formula += lit[j] + "|(" + lit[j].lower() + "&"
                    else:
                        formula += lit[j] + "|(" + lit[j].upper() + "&"
                    par += 2
                # Insert last literal and close parentesis
                formula += lit[-1]
                formula += ")" * par
                formula += "|"
    return formula