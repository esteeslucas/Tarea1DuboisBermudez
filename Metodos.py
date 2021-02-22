def check_char(x):
    v = str(x)
    if (not(v.isalpha()) or len(v)!=1):
        return ("Error 69420, el valor no es un único caracter entre A-Z")
    else:
        return (0)

    
def caps_switch(x):
    if(check_char(x)==0):
        if(str(x).isupper()):
            return (str(x).lower())
        else:
            return (str(x).upper())
    else:
        return (check_char(x))

