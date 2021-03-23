# Ejercicio 2: Reescribe el programa del salario usando try y except, de modo que elp
# programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
# un mensaje y saliendo del programa. A continuación se muestran dos ejecuciones
# del programa:

#Introduzca las Horas: 20
#Introduzca la Tarifa por hora: nueve
#Error, por favor introduzca un número

#Introduzca las Horas: cuarenta
#Error, por favor introduzca un número

try:
    h = input('Introduzca las horas: ') 
    hr = float(h)
    t = input('Introduzca la tarifa por hora: ')
    tr = float(t)
    if hr > 40 :
        print('Salario',float((40 * tr) + ((hr - 40) * (tr * 1.5))))
    else:
        print('Salario',float(hr * tr))
except:
    print('Porfavor introduce un número')
