import Metodos
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
def test_caso1():
    for i in range(len(letras)):
        resultado = Metodos.check_char(letras[i])
        assert resultado == 0
    for i in range(len(letras)):
        resultado = Metodos.check_char(letras[i].upper())
        assert resultado == 0
def test_caso2():
    for i in range(len(letras)):
        resultado = Metodos.caps_switch(letras[i])
        assert resultado == letras[i].upper()
    for i in range(len(letras)):
        resultado = Metodos.caps_switch(letras[i].upper())
        assert resultado == letras[i].lower()
def test_caso3():
    resultado = Metodos.check_char("abcd")
    assert resultado == "Error, se introdujo más de un caracter"
def test_caso4():
    resultado = Metodos.check_char("1")
    assert resultado == ("Error, se introdujo un caracter que no pertenece al alfabeto")
def test_caso5():
    resultado = Metodos.check_char(123)
    assert resultado == ("Error, se introdujo un caracter que no es de tipo string")
    
