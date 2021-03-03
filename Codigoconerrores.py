import tkinter #Se importa la libreria tkinter

#inicialización de variables para el programa
lista = [2, 6, 9, 5] 
total=0
for i in range(len(lista)):#ciclo for que recorre cada elemento en la lista
    total += lista[i]#se le suma el valor actual de la lista que se está tomando
    print (total)#impresión en pantalla del valor actual de la suma de los elementos recorridos
