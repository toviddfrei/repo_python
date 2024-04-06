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

"""
Devolver un valor de una función en python

Devolver el valor de una función en python, es obtener un resultado
de la función y guardarlo en una variable que nos permita pasarlo a otra
parte de la aplicación según se demande el uso de la función. Esto seria
la declaración de devolución, retornar 

Tenemos la declaración impresa que ofrece el resultado solo a la salida
estandar el monitor, imprimir

Ejemplo:

def full_name(first, last):
  return f'{first} {last}'

kristine = full_name('Kristine', 'Hudgens')

def greeting(name):
  print(f'Hi {name}!')

greeting(kristine)
"""

# Esta funcion devuelve un nombre completo formateado
# y lo almacena en la variable que le llama, Kristine
def full_name(first, last):
  return f'{first} {last}'
# Llamamos a la funcion y guardamos el retorno
kristine = full_name('Kristine', 'Hudgens')

# Esta funcion imprime el nombre que le pasa la variable
# Kristine almacena el retorno de la funcion full_name
def greeting(name):
  print(f'Hi {name}!')

# Llamamos a la funcion y le pasamos la variable
greeting(kristine)

# Coding Exercise
# Create a function called sum_two_numbers that accepts two arguments.
# The function should 'return' the total of 
# those two arguments added together.
# Ejercicio de codificación
# Crea una función llamada suma_dos_números que acepta dos argumentos.
# La función debería 'devolver' el total de
# esos dos argumentos sumados.

def sum_two_numbers(num1, num2):
   return num1 + num2


total_sum = sum_two_numbers(15,21)

def result_sum(sum):
   print(sum)


result_sum(total_sum)


"""
Anidar funciones en funciones principales:

Anidar funciones dentro de funciones es una caracteristica bastante particular de python,
no todos los lenguajes de programación lo permiten.

La sintaxis, es tal como la hemos aprendido, hay que tener cuidado
y observar muy bien el flujo, canalizacion de la entrada y la salida. La sangria en las funciones es 
fundamental generar los bloques de codigo para que se nos entienda, y separar las funciones con dos
lineas vacias, haciendolas visibles

Cuando decidir anidar o no funciones, no hay regla estandarizada, la recomendacion
seria cuando una funcion no tenga existencia valida sin la dependencia de una funcion
superior ahi que anidar. Pero si esa funcion es llamada por varias partes de la 
aplicacion seria interesante mantenerla independiente para poder manejarla asi.

Ejemplo:

def full_name(first, last):
  return f'{first} {last}'

kristine = full_name('Kristine', 'Hudgens')

def greeting(name):
  print(f'Hi {name}!')

greeting(kristine)


anidamos la funcion full_name en greeting
- la funcion full_name, tiene poco sentido sin la funcion saludo, por lo tanto 
es conveniente anidarla

# Podemos modificar los parametros que recibe greeting, 
# Modificamos los parametros que recibe full_name, retornamos los parametros que 
# esta canalizando la funcion greeting
# full_name retorna los mismo valores que antes
# greeting imprime los valores tal como antes, que se le pasan al llamarla

def greeting(first, last):
  def full_name():
    return f'{first} {last}'

  print(f'Hi {full_name()}!')


greeting('Kristine', 'Hudgens')
"""

# declaramos la funcion, pasandole dos parametros, first and last
def greeting(first, last):
  # anidamos la funcion full_name, que retorna los parametros pasados formateados
  def full_name():
    # retornamos los valores formateados
    return f'{first} {last}'
  # imprimimos el saludo en consola, tomando el retorno de la funcion full_name
  print(f'Hi {full_name()}!')

# llamamos a la funcion greeting pasandole los parametros necesarios
greeting('Kristine', 'Hudgens')

# Coding Exercise
# Create a function called greeting that accepts a persons name as an argument.
# Your function should return "Hello, {persons name}".
# Example: Passing in 'Jordan' should return 'Hello, Jordan'
# Ejercicio de codificación
# Cree una función llamada saludo que acepte el nombre de una persona como argumento.
# Tu función debería devolver "Hola, {nombre de la persona}".
# Ejemplo: Pasar 'Jordan' debería devolver 'Hola, Jordan'

def greeting(persons_name):
   return f'Hello, {persons_name}'


greeting('Jordan')
# print(greeting('Jordan'))

"""
Argumentos predeterminados en funciones:

Los argumentos predeterminados los podemos utilizar para pasarle a la funcion argumentos,
estandar anticipando que el argumento necesario este vacio y esto nos lleve a un error, si
tenemos un argumento que se incorpora a peticion evitaremos un posible error de falta de 
argumento o argumento no valido.

Se considera muy mala practica utilizar una lista como argumento predeterminado, esa lista
siempre sera la misma acumulando argumentos, no comenzara de cero.
La razon la explica la mutabilidad e inmutabilidad, las listas son mutables, por lo tanto
reside en un espacio de memoria para toda la aplicación.

La sintaxis es ofrecer un valor al argumento, en caso de estar vacio, aparece, en el momento
el argumento esta lleno, el valor predeterminado no aparece.

def greeting(name = 'invitado'):

La declaracion ID, nos devuelve el espacio de memoria que ocupa una variable, una lista, un dato...
Lo utilizamos para comprobar y verificar que la lista collection es la misma no empieza en cada llamadda
si no acumula, el ejemplo mas claro es que esta funcion fuera llamada por dos partes diferentes de la
aplicacion, tendriamos un problema, los datos estarian erroneos, la lista no estaria vacia de elementos


Ejemplo:

Como se debe hacer y como no:

def greeting(name = 'Guest'):
  print(f'Hi {name}!')

greeting()
greeting('Kristine')

# Nope
def some_function(collection = []):
  collection.append(1)
  print(id(collection))
  return collection


print(some_function())
print(some_function())
"""

# Es mala practica utilizar listas para parametros predeterminados
def some_function(collection = []):
  collection.append(1)
  # verifica que la lista ocupa el mismo espacio de memoria
  print(id(collection))
  return collection

# verificamos que la lista es igual, no empieza vacia, acumula elementos
print(some_function())
print(some_function())


# Coding Exercise
# Create a function called counter that accepts an argument called initial_count
# and returns that argument incremented by 1.
# initial_count must have a default value of 0.
# Ejercicio de codificación
# Crea una función llamada contador que acepta un argumento llamado cuenta_inicial
# y devuelve ese argumento incrementado en 1.
# cuenta_inicial debe tener un valor predeterminado de 0.

def counter(initial_count = 0):
   return initial_count + 1

counter()
counter(21)
# print(counter())
# print(counter(21))
   

"""
Utilizar argumentos de funciones con nombre:

Los argumentos posicionales, definen el mapeo entre el valor y como se usa esta completamente
determinado por la posición y el orden en el que pasamos valores.

Con aplicaciones + grandes los argumentos posicionales pueden generar confusión.

Los argumentos con nombres brindan la posibilidad de ser mucho más explicito.

Somos + explicitos pasando argumentos con nombres
(Lo explicito mejor que lo implicito)

Como regla general si ser estipulada es que si hay mas de dos argumentos se utilice, argumentos
con nombre.

Ejemplo:

Utilizar argumentos por nombres, nos proporciona flexibilidad a la hora de canalizar 
nuestros valores y ser muy explicito para evitar errores en el orden.

def full_name(first, last):
  print(f'{first} {last}')


full_name('Kristine', 'Hudgens')
full_name(first = 'Kristine', last = 'Hudgens')
full_name(last = 'Hudgens', first = 'Kristine')
"""

# Coding Exercise
# Behind the scenes of the code test is a function called sequence that 
# accepts 5 arguments: first, second, third, fourth, and fifth. Unfortunately,
# they are not in sequential order. Using named arguments, call the sequence 
# function and pass in the 5 arguments, setting their values to 1, 2, 3, 4, 5 respectively.
# Ejercicio de codificación
# Detrás de escena de la prueba de código hay una función llamada secuencia que
# acepta 5 argumentos: primero, segundo, tercero, cuarto y quinto. Desafortunadamente,
# no están en orden secuencial. Usando argumentos con nombre, llame a la secuencia
# funciona y pasa los 5 argumentos, estableciendo sus valores en 1, 2, 3, 4, 5 respectivamente.

def named_arguments_practice(sequence):
    sequence(first = 1, second = 2, third = 3, fourth = 4, fifth = 5) # Replace this code comment with your code


"""
desempaquetar argumentos de funciones:

Hay ocasiones en que una funcion, necesita canalizar una coleccion de datos, no conociendo de 
antemano la cantidad en cuestión.

La sintaxis es que comenzara los argumentos con un asterisco def function_name(*args), y la palabra
arg convencion comun que es la abreviatura de arguments, denominado unpacking.
*arg esto representa que es una version desempaquetada o una lista de elementos

Descompresión y listas de argumentos nos hace trabajar con Tuplas

Ejemplo:

def greeting(*args):
  print('Hi ' + ' '.join(args))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


def greeting(*names):
  print('Hi ' + ' '.join(names))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


def greeting(time_of_day, *args):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
greeting('Morning', 'Tiffany', 'Hudgens')

"""
# declaramos la funcion pasandole una lista de argumentos
# difinidos por el asterisco *arg
# utilizamos la funcion .join, le pasamos un espacio vacio como valor set ' '.join() 
def greeting(*args):
  print('Hi ' + ' '.join(args))


greeting('Kristine', 'no', 'Hudgens')
greeting('Tiffany', 'Hudgens')

# declaramos la funcion y le pasamos dos argumentos 
# un argumento por nombre y una lista de argumentos
# al pasarlo lo pasmos como una tupla de elmentos
def greeting(time_of_day, *args):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
greeting('Morning', 'Tiffany', 'Hudgens')