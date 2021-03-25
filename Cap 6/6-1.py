# Ejercicio 1: Escribe un bucle while que comience con el último carácter
# en la cadena y haga un recorrido hacia atrás hasta el primer carácter
# en la cadena, imprimiendo cada letra en una línea independiente.


x = input('Introduce una palabra ')
t = list(x)
for i in reversed(t):
    print(i)