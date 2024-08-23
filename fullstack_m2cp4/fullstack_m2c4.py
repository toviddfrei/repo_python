#!/usr/bin/env python3

from decimal import Decimal
import math

print('\n')
print('Check point 4 - Module 2 \n')

"""
Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
Ejercicio 1: cree una lista, tupla, flotante, entero, decimal y diccionario.
"""

# ex1
print('Exercise 1 \n')
new_list = ['black', 'white', 'red', 'yellow']
print('List: {}'.format(new_list))
new_tuple = ('orange', 'banana', 'apple', 'strawberry')
print('Tuple: {}'.format(new_tuple))
new_float = 80.33
print('Float: {}'.format(new_float))
new_int = 1
print('Integer: {}'.format(new_int))
# importar la funcion Decimal del modulo decimal
new_decimal = Decimal(1.1)
print('Decimal: {}'.format(new_decimal))
new_dict = {
    'four' : 4,
    'three': 3,
    'two'  : 2,
    'one'  : 1
}
print('Dictionary: {}'.format(new_dict))
print('\n')

"""
Exercise 2: Round your float up.
Ejercicio 2: Redondea tu float hacia arriba.

Voy a utilizar el modulo math para poder utilizar la funcion ceil
que ofrece el entero más proximo siempre hacia arriba, tambien 
tenemos la funcion floor que ofrece el entero mas proximo hacia abajo

A parte voy a utilizar el aprendizaje de la guía función exponente manual
para mostrar varios ejemplos, controlando el decremento del contador.
"""

# ex2
# importar módulo math
print('Exercise 2 \n')
print('Float: {}'.format(new_float))

def int_up_always(num):
    """Round up count 3 example"""
    num_example = num
    count = 3

    while count > 0:
        count -= 1
        num_example += 3.1416
        # Redondear siempre hacia arriba:
        print('Always round up: {}'.format(num_example))
        # Redondeado
        num_example = math.ceil(num_example)
        print('Rounded: {}'.format(num_example))

int_up_always(new_float)
print('\n')

"""
Exercise 3: Get the square root of your float.
Ejercicio 3: Obtén la raíz cuadrada de tu float.

Voy a importar el modulo math, para poder operar con la función
sqrt que obtiene la raiz cuadrada del número pasado.
"""

# ex3
# importar modulo math
print('Exercise 3 \n')
print('Float: {}'.format(new_float))
new_float_sqrt = math.sqrt(new_float)
# Raiz cuadrada de mi float:
print('Square root of my float: {}'.format(new_float_sqrt))
print('\n')

"""
Exercise 4: Select the first element from your dictionary.
Ejercicio 4: Selecciona el primer elemento de tu diccionario.

Primero obtengo el primer elemento del diccionario, llamando a la
primera clave.
Utilizo lo aprendido en listas para trabajar con el diccionario
extrayendo el primer elemento del diccionario, tanto de clave como
valor, utilizando las funciones keys y values, y transformo en lista
que me ofrece el objeto de visualización del diccionario.
"""
# ex4
print('Exercise 4 \n')
# Primer elemento del diccionario
first_element_dict = new_dict['four']
print('First element dictionary: {}'.format(first_element_dict))

# Segundo utilizo el objeto de visualización
print('Complete dictionary: {}'.format(new_dict))
first_key = list(new_dict.keys())[0]
first_value = list(new_dict.values())[0]
print('First element key: {}'.format(first_key))
print('First element value: {}'.format(first_value))

# Exemple for exercise teoric number 4
# Obtener la clave 2 y el 2 valor
new_dictionary = {
    'name_1' : 'valor1',
    'name_2' : ['valor1', 'valor2', 'valor3'],
    'name_3' : ('valor1', 'valor2')
}
new_exemple_key_second = list(new_dictionary.keys())[1]
new_exemple_value_second = list(new_dictionary.values())[1][1]
print(new_exemple_key_second)
print(new_exemple_value_second)
print('\n')

"""
Exercise 5: Select the second element from your tuple.
Ejercicio 5: selecciona el segundo elemento de tu tupla.

Utilizare el desempaquetado de la tupla como primera opción y luego seleccionare el sugundo
elemento utilizando el indice, teniendo en cuenta que el indice siempre comienza en 0
"""

# ex5
print('Exercise 5 \n')
# Utilizo el desempaquetado de la tupla
first_element, second_element, third_element, fourth_element = new_tuple
new_tuple_second_element = second_element
# El segundo elemento de la tupla desempaquetado:
print('The second element of the tuple unpacked: {}'.format(new_tuple_second_element))
# Utilizo el indice de la tupla
new_tuple_second_element_index = new_tuple[1]
# El segundo elemento de la tupla indice:
print('The second element of the tuple indexes: {}'.format(new_tuple_second_element_index))
print('\n')

"""
Exercise 6: Add an element to the end of your list.
Ejercicio 6: agregue un elemento al final de su lista.

Utilizo la función extend para agregar elementos nuevos a mi lista
"""
# ex6
print('Exercise 6 \n')
print('List: {}'.format(new_list))
new_list.extend(['blue'])
print('Add new element in my list: {}'.format(new_list[4]))
print('Completed new list: {}'.format(new_list))
print('\n')

"""
Exercise 7: Replace the first element in your list.
Ejercicio 7: Reemplace el primer elemento de su lista.
"""

# ex7
print('Exercise 7 \n')
print('First element my list: {}'.format(new_list[0]))
print('Completed list: {}'.format(new_list))

new_list[0] = 'green'
print('Element to replace: {}'.format(new_list[0]))
print('Completed new list: {}'.format(new_list))
print('\n')

"""
Exercise 8: Sort your list alphabetically.
Ejercicio 8: Ordena tu lista alfabéticamente.

Utilizo la función sorted, que ordena la lista alfabéticamente
Puedo cambiar el orden al reves, añadiendo el parametro reverse = True
"""

# ex8
print('Exercise 8 \n')
print('List: {}'.format(new_list))
new_list_sorted = sorted(new_list)
print('New list ordered:{}'.format(new_list_sorted))
new_list_sorted_reverse = sorted(new_list, reverse=True)
print('New list ordered reverse: {}'.format(new_list_sorted_reverse))
print('\n')

"""
Exercise 9: Use reassignment to add an element to your tuple.
Ejercicio 9: utilice la reasignación para agregar un elemento a su tupla.

Voy a utiliar la reasignación para agregar un nuevo elemento a la tupla, 
como las tuplas son inmutables, debo crear otra nueva tupla y asignale el elemento
nuevo, pero a su vez como para asignar una nuevo elemento a una tupla tiene que
tener como mínimo dos elementos para tratarlo como tupla, debo de insertar una coma
despues del elemento, asi es como lo tratara como una nuevo elemento, a su vez utilizo
el operador de asignación += que me ahorra new_tuple = new_tuple + ('pear',)
"""
# ex9
print('Exercise 9 \n')
print('Tupla: {}'.format(new_tuple))
new_tuple += ('pear',)
print('New tupla: {}'.format(new_tuple))
print('\n')
