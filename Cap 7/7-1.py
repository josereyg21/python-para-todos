# Ejercicio 1: Escribe un programa que lea un archivo e imprima 
# su contenido (línea por línea), todo en mayúsculas. 

x = input('Dame el nombre del archivo porfavor: ')
x1 = open(x)

for x2 in x1:
    x3 = x2.strip()
    print(x3.upper())