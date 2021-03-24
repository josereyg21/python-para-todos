# Ejercicio 6: Reescribe el programa de cálculo del salario, con tarifa-ymedia para las horas extras,
# y crea una función llamada calculo_salario que reciba dos parámetros (horas y tarifa).

def calculo_salario(a,b):
    salario = a * b
    return salario

def calculo_salario2(a,b):
    salario2 = ((40 * b) + ((a - 40) * (b* 1.5)))
    return salario2

h = input('Introduzca hora: ')
t = input('Introduzca tarifa: ')
a = float(h)
b = float(t)
if a < 40:
    print(calculo_salario(a,b))
else:
    print(calculo_salario2(a,b))
    

