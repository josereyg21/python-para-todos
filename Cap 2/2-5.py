#Ejercicio 5: Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima
# por pantalla la temperatura convertida.

c = input('Ingrese la temperatura en grados Celsius: ')
cs = float(c)
f = ((cs * (9/5)) + 32)
print('La temperatura convertida a grados Fahrenheit es ', f)