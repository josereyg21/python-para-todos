# Algunas veces cuando los programadores se aburren o
# quieren divertirse un poco, agregan un inofensivo Huevo de Pascua
# a su programa. Modifica el programa que pregunta al usuario por el
# nombre de archivo para que imprima un mensaje divertido cuando el
# usuario escriba “na na boo boo” como nombre de archivo. El programa
# debería funcionar normalmente para cualquier archivo que exista o no
# exista. Aquí está un ejemplo de la ejecución del programa



try:
    z = 0
    x = input('Porfavor ingresa el nombre de tu archivo: ')
    if x == 'na na boo boo':
        print('NA NA BOO BOO PARA TU - Te he atrapado!')
    else:
        y = open(x)
        for d in y:
            if d.startswith('Subject: '):
                z = z + 1
        print('Hay',z,'lineas subject en',x)

except:
    print('El archivo no puede ser abierto',x)

