# Ejercicio 7: Reescribe el programa de calificaciones del capítulo anterior usando una función llamada calcula_calificacion, que reciba una
#puntuación como parámetro y devuelva una calificación como cadena.

# Puntuación Calificación
#  > 0.9 Sobresaliente
#  > 0.8 Notable
#  > 0.7 Bien
#  > 0.6 Suficiente
#  <= 0.6 Insuficiente

# Introduzca puntuación: 0.95
# Sobresaliente

# Introduzca puntuación: perfecto
# Puntuación incorrecta

# Introduzca puntuación: 10.0
# Puntuación incorrecta

# Introduzca puntuación: 0.75
# Bien

# Introduzca puntuación: 0.5
# Insuficiente


def calcula_calificacion(b):
    if b >= 0.9:
        print('Sobresaliente')
    elif b >= 0.8:
        print('Notable')
    elif b >= 0.7:
        print('Bien')
    elif b >= 0.6:
        print('Suficiente')
    elif b < 0.6:
        print('insuficiente')
    return b

x = input('Ingresa Calificacion: ')
b = float(x)
calcula_calificacion(b)