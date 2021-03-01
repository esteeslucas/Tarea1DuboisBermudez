import Metodos #Archivo en el que se encuentran 
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]#Todas las letras del abecedario
def test_caso1():#Un caso de éxito para check_char evaluando todos los caracteres entre A-Z y a-z. Esto quiere decir que se llama a check_char y se espera que su resultado siempre sea 0.
    for i in range(len(letras)):#Para todas las letras del abecedario
        resultado = Metodos.check_char(letras[i]) #Guardar resultado como el valor retornado por el método check_char en minúscula
        assert resultado == 0 #Verificar que dé 0
    for i in range(len(letras)): #Para todas las letras del abecedario
        resultado = Metodos.check_char(letras[i].upper()) #Guardar el resultado como el valor retornado por el método check_char pero esta vez para las mayúsculas
        assert resultado == 0 #Verificar que dé 0
def test_caso2(): #Un caso de éxito para caps_switch evaluando todos los caracteres entre A-Z y a-z. Esto quiere decir que; por ejemplo, si se llama el método con parámetro de “a” la respuesta debe de ser “A”.
    for i in range(len(letras)):#Para todas las letras del abecedario
        resultado = Metodos.caps_switch(letras[i]) #Guardar como resultado el valor retornado por el método caps_switch en minúscula
        assert resultado == letras[i].upper() #Verifica que el valor retornado sea la misma letra pero en mayúscula
    for i in range(len(letras)):
        resultado = Metodos.caps_switch(letras[i].upper())#Guardar como resultado el valor retornado por el método caps_switch en mayúscula
        assert resultado == letras[i].lower()#Verifica que el valor retornado sea la misma letra pero en minúscula
def test_caso3():#Un caso negativo donde se verifica el punto b del método check_char
    resultado = Metodos.check_char("abcd") #guardar resultado como el valor retornado por check_char al introducir más de un caracter como entrada.
    assert resultado == "Error, se introdujo más de un caracter" # Verificar que se retorne el error adecuado.
def test_caso4():#Un caso negativo donde se verifica el punto c del método check_char
    resultado = Metodos.check_char("1")#Se guarda como resultado el valor retornado por el método check_char al introducir un valor de entrada que no pertenece al abecedario
    assert resultado == ("Error, se introdujo un caracter que no pertenece al alfabeto")#Se verifica que se retorne el error adecuado.
def test_caso5():#Un caso negativo donde se verifica el punto del método check_char.
    resultado = Metodos.check_char(123)#Se guarda como resultado el método check_char al introducir como entrada un número.
    assert resultado == ("Error, se introdujo un caracter que no es de tipo string") #Verifica que arroje el error adecuado.
    
