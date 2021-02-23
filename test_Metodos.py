import Metodos

def test_caso1():
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
    for i in range(len(letras)):
        resultado = Metodos.check_char(letras[i])
        assert resultado == 0
    for i in range(len(letras)):
        resultado = Metodos.check_char(letras[i].upper())
        assert resultado == 0
def test_caso2():
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
    for i in range(len(letras)):
        resultado = Metodos.caps_switch(letras[i])
        assert resultado == letras[i].upper()
    for i in range(len(letras)):
        resultado = Metodos.caps_switch(letras[i].upper())
        assert resultado == letras[i].lower()
