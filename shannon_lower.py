def shannon_lower(key, lit):
    par = 1
    formula = ""
    if key in lit:
        # Chiave minuscola e compare nella formula
        lit.remove(key.lower())
        formula += "(" + key.upper() + "&"
        if len(lit) == 1:
            # Formula lunghezza 1
            formula += lit[0] + ")|"
        else:
            # Formula lunghezza > 1
            for i in range(len(lit) - 1):
                if lit[i].isupper():
                    formula += "(" + lit[i] + "|(" + lit[i].lower() + "&"
                else:
                    formula += "(" + lit[i] + "|(" + lit[i].upper() + "&"
                par += 2
            # Insert last literal and close parentesis
            formula += lit[-1]
            formula += ")" * par
            formula += "|"
    else:
        # Chiave minuscola e non compare nella formula
        # Devo eliminare la negazione
        lit.remove(key.upper())
        formula += "(" + key.lower() + "&" 
        if len(lit) == 1:
            # Formula lunghezza 1
            formula += lit[0] + ")"
        else:
            # Formula lunghezza > 1
            for i in range(len(lit) - 1):
                if lit[i].isupper():
                    formula += "(" + lit[i] + "|(" + lit[i].lower() + "&"
                else:
                    formula += "(" + lit[i] + "|(" + lit[i].upper() + "&"
                par += 2
            # Insert last literal and close parentesis
            formula += lit[-1]
            formula += ")" * par
            formula += "|"
    return formula