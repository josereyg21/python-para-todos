#Ejercicio 1: Escribe un programa que lea repetidamente números hasta
#que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
#muestra por pantalla el total, la cantidad de números y la media de
#esos números. Si el usuario introduce cualquier otra cosa que no sea un
#número, detecta su fallo usando try y except, muestra un mensaje de
#error y pasa al número siguiente.

# Introduzca un número: 4
# Introduzca un número: 5
# Introduzca un número: dato erróneo
# Entrada inválida

# Introduzca un número: 7
# Introduzca un número: fin
# 16 3 5.33333333333

try:
    n = 0
    o = 0
    while True:
        x = input('Introduzca número: ')
        if x == 'fin' : break
        y = float(x)
        n = n + y
        o = o + 1
except:
    print(' Dato Erróneo')

print('Total',n)
print('Cantidad de numeros',o)
print('Media', n/o)
