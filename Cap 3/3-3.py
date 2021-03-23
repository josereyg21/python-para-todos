#Ejercicio 3: Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la
#puntuación está fuera de ese rango, muestra un mensaje de error. Si la puntuación
#está entre 0.0 y 1.0, muestra la calificación usando la tabla siguiente:

#Puntuación Calificación
#  >= 0.9 Sobresaliente
#  >= 0.8 Notable
#  >= 0.7 Bien
#  >= 0.6 Suficiente
#  < 0.6 Insuficiente

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



c = input( 'Porfavor ingresa la calificacion en un rango de 0.0 a 1.0:   ')
cl = float(c)
if cl > 1.0 or cl < 0.0:
    print('Porfavor escribe un puntaje entre el rango descrito')
else:
    if cl >= 0.9:
        print('Sobresaliente')
    elif cl >= 0.8:
        print('Notable')
    elif cl >= 0.7:
        print('Bien')
    elif cl >= 0.6:
        print('Suficiente')
    elif cl < 0.6:
        print('insuficiente')
    