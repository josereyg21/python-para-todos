# Descargar una copia de un archivo www.py4e.com/code3/romeo.txt.
# Escribir un programa para abrir el archivo romeo.txt y leerlo línea
# por línea. Para cada línea, dividir la línea en una lista de palabras
# utilizando la función split. Para cada palabra, revisar si la palabra ya
# se encuentra previamente en la lista. Si la palabra no está en la lista,
# agregarla a la lista. Cuando el programa termine, ordenar e imprimir
# las palabras resultantes en orden alfabético.



vid = []
o = input('Porfavor dame el nombre del archivo ')
r = open(o)
for x in r:
    c = x.split()
    for i in c:
        if i not in vid:
            vid.append(i)

vid.sort()
print(vid)   
    

