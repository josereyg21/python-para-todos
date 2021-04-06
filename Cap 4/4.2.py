# Desplaza la última línea del programa anterior hacia arriba,
# de modo que la llamada a la función aparezca antes que las definiciones.
# Ejecuta el programa y observa qué mensaje de error obtienes.

repite_estribillo()

def muestra_estribillo():
    print('Soy un leñador, que alegria.')
    print('Duermo toda la noche y trabajo todo el dia.')

def repite_estribillo():
    muestra_estribillo()
    muestra_estribillo()
