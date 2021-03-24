# Ejercicio 2: Escribe otro programa que pida una lista de números como
# la anterior y al final muestre por pantalla el máximo y mínimo de los
# números, en vez de la media.

try:
    o = []
    while True:
        x = input('Introduzca número: ')
        if x == 'fin' : break
        y = float(x)
        o.append(y)
except:
    print(' Dato Erróneo')

print('Maximo', max(o))
print('Cantidad de numeros', len(o))
print('Minimo', min(o))