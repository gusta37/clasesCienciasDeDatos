""" 
Condicional parcial (solo el if) con expresión lógica compuesta (and).

Desarrollo un programa que verifica si un número es mayor que 10 y también par, usando "and".
"""

numero = int(input("Ingrese un número: "))

if numero > 10 and numero % 2 == 0:
    print("El número es mayor que 10 y par")