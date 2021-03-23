# Ejercicio 1: Reescribe el programa del cálculo del salario para darle al empleado
# 1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.

h = input('Introduzca las horas: ')
t = input('Introduzca la tarifa por hora: ')
hr = float(h)
tr = float(t)
if hr > 40 :
    print('Salario',float((40 * tr) + ((hr - 40) * (tr * 1.5))))
else:
    print('Salario',float(hr * tr))