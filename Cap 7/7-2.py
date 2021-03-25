# Ejercicio 2: Escribe un programa que solicite un nombre de archivo
# y después lea ese archivo buscando las líneas que tengan la siguiente
# forma:

# X-DSPAM-Confidence: 0.8475

# **Cuando encuentres una línea que comience con “X-DSPAM-Confidence:” ponla
# aparte para extraer el número decimal de la línea. Cuenta esas líneas y después
# calcula el total acumulado de los valores de “spam-confidence”. Cuando llegues al
# final del archivo, imprime el valor medio de “spam confidence”.

# Ingresa un nombre de archivo: mbox-short.txt
# Promedio spam confidence: 0.750718518519

m = 0
n = 0
x = input('Ingrese el nombre del archivo: ')
y = open(x)
for z in y:
    if z.startswith('X-DSPAM-Confidence:'):
        m = m + float(z[20: ])
        n = n + 1

print('Promedio spam confidence:', m/n)

        