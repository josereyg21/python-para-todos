# Ejercicio 3: Encapsula este código en una función llamada cuenta, y
# hazla genérica de tal modo que pueda aceptar una cadena y una letra
# como argumentos.

# El siguiente programa cuenta el número de veces que la letra “a” aparece en una cadena:


#  palabra = 'banana'
#  contador = 0
#  for letra in palabra:
#    if letra == 'a':
#       contador = contador + 1
#  print(contador)


x = input('Tu palabra es: ')
y = input('Letra que quieres buscar: ')
print(x.count(y))