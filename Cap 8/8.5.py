# Escribir un programa para leer a través de datos de una bandeja de entrada de correo y cuando encuentres una línea que comience
# con “From”, dividir la línea en palabras utilizando la función split.
# Estamos interesados en quién envió el mensaje, lo cual es la segunda
# palabra en las líneas que comienzan con From.

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# Tendrás que analizar la línea From e imprimir la segunda palabra de
# cada línea From, después tendrás que contar el número de líneas From:
#  e imprimir el total al final. 

dv = []
oi = 0
k = input('Dame el nombre del archivo ')
j = open(k)
for i in j:
    o = i.split()
    for u in o:
        if u.startswith('From:'):
            oi = oi + 1
            print(o[1:2])

print(' Hay', oi, 'lineas en el archivo con la palabra From al inicio')
