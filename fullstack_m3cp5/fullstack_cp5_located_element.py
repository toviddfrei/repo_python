"""
Utilizando la siguiente lista y variable, determine si el valor
de la variable coincide o no con un valor de la lista. 
*Sugerencia, si es necesario, utilice un bucle for in y el 
operador in.
"""

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

for n in lista_nombre:
    if n == nombre:
        print("Located")
    else:
        print("not located")