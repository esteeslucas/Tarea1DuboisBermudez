def check_char(x):  # método checkchar, entra un dato y se
    # verifica que sea un caracter
    v = str(x)  # Convierte lo que sea que entre a un string para que
    # sea más facil manipularlo independientemente de lo que
    # realmente sea la entrada
    if (not(v.isalpha()) or len(v) != 1 or not isinstance(x, str)):
        # Si hay algún error, ya que para que haya un error,
        #  no pertenece al abecedario,
        #  el largo es diferente de 1 o no es un string.
        if (not isinstance(x, str)):  # Si no es un string,
            # se retorna el siguiente error
            return ("Error, se introdujo un caracter que no es de tipo string")
        elif(len(v) != 1):  # Error si no es un solo caracter
            return ("Error, se introdujo más de un caracter")
        elif (not(v.isalpha())):  # Error si no pertenece al abecedario
            return ("""Error, se introdujo
                    un caracter que no pertenece al alfabeto""")
    else:
        return (0)


def caps_switch(x):  # Entra el dato a invertir caps
    if(check_char(x) == 0):  # Si es un solo caracter
        # y se cumplen las condiciones de check_char(x)
        if(str(x).isupper()):  # Si es mayuscula
            return (str(x).lower())  # Pasese a minuscula
        else:  # Sino
            return (str(x).upper())  # Pasese a mayuscula
    else:
        return (check_char(x))  # De lo contrario,
    # retorne lo mismo que retorne check_char(x) con esa entrada.
