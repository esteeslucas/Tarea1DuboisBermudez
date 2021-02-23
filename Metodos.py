def check_char(x):
    v = str(x)
    if (not(v.isalpha()) or len(v)!=1):
        if (not isinstance(x,str)):
            return ("Error, se introdujo un caracter que no es de tipo string")
        elif(len(v)!=1):
            return ("Error, se introdujo más de un caracter")
        elif (not(v.isalpha())):
              return ("Error, se introdujo un caracter que no pertenece al alfabeto")
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

