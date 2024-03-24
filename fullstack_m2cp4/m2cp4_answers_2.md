# Answers check point 4

Exercises

```python
#!/usr/bin/env python3

"""
Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
Ejercicio 1: cree una lista, tupla, flotante, entero, decimal y diccionario.
"""

# ex1
new_list = ['black', 'white', 'red', 'yellow']
new_tuple = ('orange', 'banana', 'apple', 'strawberry')
new_float = 80.51
new_int = 1
new_decimal = 1.1
new_dict = {
    'four' : 4,
    'three': 3,
    'two'  : 2,
    'one'  : 1
}

"""
Exercise 2: Round your float up.
Ejercicio 2: Redondea tu flotador hacia arriba.

Voy a utilizar la función round(), que redondea al entero más 
próximo
"""

new_float_round = round(new_float)
print(new_float_round)

"""
Exercise 3: Get the square root of your float.
Ejercicio 3: Obtén la raíz cuadrada de tu flotador.

Voy a importar el modulo math, para poder operar con la función
sqrt que obtiene la raiz cuadrada del número pasado.
"""
import math

new_float_rooat_round_sqrt)

"""
Exercise 4: Select the first element from your dictionary.
Ejercicio 4: Selecciona el primer elemento de tu diccionario.

Utilizo la primera clave de los elementos del diccionario
"""

first_element_dict = new_dict['four']
print(first_element_dict)

"""
Exercise 5: Select the second element from your tuple.
Ejercicio 5: selecciona el segundo elemento de tu tupla.
"""

new_tuple_second_element = new_tuple[1]
print(new_tuple_second_element)

"""
Exercise 6: Add an element to the end of your list.
Ejercicio 6: agregue un elemento al final de su lista.

Utilizo la función extend para agregar elementos nuevos a mi lista
"""

new_list.extend(['blue'])
print(new_list)

"""
Exercise 7: Replace the first element in your list.
Ejercicio 7: Reemplace el primer elemento de su lista.
"""

new_list[0] = 'green'
print(new_list)

"""
Exercise 8: Sort your list alphabetically.
Ejercicio 8: Ordena tu lista alfabéticamente.

Utilizo la función sorted, que ordena la lista alfabéticamente
Puedo cambiar el orden al reves, añadiendo el parametro reverse = True
"""

new_list_sorted = sorted(new_list)
print(new_list_sorted)
new_list_sorted_reverse = sorted(new_list, reverse=True)
print(new_list_sorted_reverse)

"""
Exercise 9: Use reassignment to add an element to your tuple.
Ejercicio 9: utilice la reasignación para agregar un elemento a su tupla.
"""

new_tuple += ('pear',)
print(new_tuple)
```

## Preguntas teoricas

¿Cuál es la diferencia entre una lista y una tupla en Python?

La diferencia entre lista y tupla es que la lista es mutable, podemos realizar modificaciones sobre la lista original, como
agregar, eliminar, cambiar, etc. Sin embargo las tuplas son inmutables, no podemos modificar la tupla original, si queremos
añadir elementos, eliminar elementos, debemos crear nuevas tuplas manteniendo la original intacta.

¿Cuál es el orden de las operaciones?

Utilizamos un metodo abreviado como PEMDAS para recordarlo, Parentesis, Exponente, Multiplicación, Division, Addición, Sustracción.

¿Qué es un diccionario Python?

Es una estructura de datos muy util que guardamos en una variable, y que nos permite guardar elementos como clave = valor, dandonos la oportunidad de mantener y modificar elementos de cualquier tipo, string, int, float, incluso listas o tuplas dentro de él.

¿Cuál es la diferencia entre el método ordenado y la función de ordenación?

La diferencia es que sort ordena la lista in situ, osea la misma lista original, y la función sorted crea una nueva lista.

¿Qué es un operador de asignación?

El operador de asignación básico es '=', que nos permite asignar un valor a una variable a = 1, a parte luego tenemos otros operadores de
asignación pero son meramente atajos de otros operadores, como '+=' que seria el atajo de 'a = a + 1' que sería igual  'a += 1'

## Preguntas teóricas 2

¿Cuál es el orden de las operaciones?

-- Utilizamos un metodo abreviado como PEMDAS para recordarlo, Parentesis, Exponente, Multiplicación, Division, Addición, Sustracción.
