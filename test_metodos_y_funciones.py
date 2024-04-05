#!/usr/bin/env python3

"""
Introducció a métodos y funciones:

Las funciones o métodos pueden almacenar procedimientos y procesos, los puedes llamar
desde cualquier otra parte de la aplicación.

Hay tres componentes cuando pensamos utilizar una función o método:

- La entrada, que es lo que vamos a canalizar
- Los procesos o procedimientos en si dentro de la función o método
- La salida, lo que deseamos obtener

Crear funciones nos permite la reutilización del código es distintas partes del programa
es mucho más profesional.

Las funciones nos permiten implementar cambios globales a la aplicación, si modificamos una
función todas las llamadas que se realicen a esa función desde cualquier parte del programa
será modificado automáticamente, sin tener que buscar donde debemos realizar el cambio en 
los diferentes trozos de código.

"""
# Declaramos la funcion con def
# Le damos un nombre descriptivo
# Cerramos con parentesis y si queremos pasar parametros, 
# los nombramos dentro
# Cerramos la linea con dos puntos creamos bloque de codigo
# Sangria y expresión que queramos crear.
def greeting(text_greeting):
    print(text_greeting)

# Llamaos a la funcion por su nombre, y le pasamos parametros si los necesita
greeting('Hola compañero,')

"""
Sintaxis básica de funciones:

La sintaxis báscisa empieza por la palabra def,
luego nombras la funcion como en la variables de forma caja de serpiente entre guiones bajos
y minusculas. Luego parentesis y terminas la linea con dos puntos.

Despues de la declaración de la funcion la siguiente linea debe ser sangrada con dos o cuatro 
espacios, segun queramos.

Entre la definición de la funcion y la siguiente linea que vas ha utilizar crear dos lineas de
espacio.

Podemos pasarle argumentos a la función, los argumentos pueden ser cualquier tipo de valor o elementos
cadenas, numeros, listas, diccionarios, estos argumentos se escriben entre los parentesis en la 
declaracion de la funcion, entonces la funcion espera recibir los valores detallados en sus argumentos
para poder continuar, si no recibe lo que necesita suelta un TypeError.

Ejemplos:

def full_name(first, last):
  print(f'{first} {last}')


full_name('Kristine', 'Hudgens')

def auth(email, password):
  if email == 'kristine@hudgens.com' and password == 'secret':
    print('You are authorized')
  else:
    print('You are not authorized')


auth('kristine@hudgens.com', 'asdf')

def hundred():
  for num in range(1, 101):
    print(num)


hundred()

def counter(max_value):
  for num in range(1, max_value):
    print(num)


counter(501)
"""

# Coding Exercise
# Create a function called greeting that prints
# "hello" when the function is called.
# Ejercicio de codificación
# Crea una función llamada saludo que imprime
# "hola" cuando se llama a la función.

def greeting():
    print("hello")


greeting()
