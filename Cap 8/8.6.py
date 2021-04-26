# Reescribe el programa que pide al usuario una lista de
# números e imprime el máximo y el mínimo de los números al final cuando
# el usuario ingresa “hecho”. Escribe el programa para almacenar los
# números que el usuario ingrese en una lista, y utiliza las funciones max()
# y min() para calcular el máximo y el mínimo después de que el bucle
# termine.

o = []
while True:
    k = input('Ingresa un numero: ')
    if k == 'hecho':
        break
    else:
        o.append(k)

print('Maximo', float(max(o)))
print('Minimo', float(min(o)))