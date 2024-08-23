#!/usr/bin/env python3

"""
Condicionales: 

Es un concepto fundamental que se necesita para volver
dinamica un programa python, y por dinamico queremos decir que tome decisiones
segun la condicion estipulada, y para estipular condiciones utilizamos la
siguiente sintaxis.

Ejemplo basico de condicionales if, if/else, if/elif/else:

# Single condition
age = 25

if age < 25:
  print(f"I'm sorry, you need to be at least 25 years old")

# if/else
age = 55

if age < 25:
  print(f"I'm sorry, {age} is under 25 years old")
else:
  print(f"You're good to go, {age} fits in the range to rent a car")

# if/elif/else
age = 55

if age < 25:
  print(f"I'm sorry, {age} is under 25 years old")
elif age > 100:
  print(f"I'm sorry, {age} is over 100 years old")
else:
  print(f"You're good to go, {age} fits in the range to rent a car")

"""
# Ejemplo personal de uso de condicionales proyecto plive.
# Defino las opciones de valores en una lista de nivel superior
operation_work = ['tasks','budget']
# Pasamos a la variable contenedora el elemento de la lista predefinida
op_work = operation_work[1]
# Creamos el condicional, seleccionando la opcion base de la lista por igual
# Si no es la opcion 0 de la lista, no cumplira la primera condicion salta a
# la segunda
if op_work == 'tasks':
  print(f'Selection: {op_work}')
else:
  print(f'Selection: {op_work}')


# Coding Exercise
# Create a conditional that returns true, using the starting code below.
# Ejercicio de codificación
# Cree un condicional que devuelva verdadero, utilizando el código
# inicial a continuación.

answer = False

if answer == False: #WriteYourConditionsHere:
  answer = True
  print(answer)

print(answer)

"""
Uso del operador ternario con condicionales:

el operador ternario nos permite otorgar una condicion preferente, la 
sintaxis es:
Hay que tener cuidado, ya que añade complejidad al codigo y una de las 
bases de python, es que lo sencillo a lo complejo pep-20. Por lo tanto
si la expresion del operador ternario se extiende mejor utilizar el 
codigo tradicional de las condicionales.

role = 'guest'

auth = 'can access' if role == 'admin' else 'cannot access'

if role == 'admin':
  auth = 'can access'
else:
  auth = 'cannot access'

print(auth)
"""

# Coding Exercise
# Write a ternary operator that sets "language_check" to True 
# if "language" is set as "python", and sets it to False if it's not.
# Ejercicio de codificación
# Escribe un operador ternario que establezca "language_check" en Verdadero
# si "idioma" está configurado como "python", y lo establece en Falso si no lo es.

language = "python"

language_check = True if language == 'python' else False # Write your code here

#Ejemplo personal, traslado este operador ternario a codigo tradicional

if language == 'python':
  language_check = True
else:
  language_check = False


"""
Lista completa de operadores condicionales:

List of comparison operators

# == Equality
# != Inequality
# <> Inequality (deprecated)
# >  Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to
"""


"""
Trabajar cadenas y colecciones con condicionales, usar lo que se llama in operator,
o operador de menbresia in.

Vamos a realizar la busqueda de un valor estipulado, tanto en una cadena como en una
coleccion de elementos con el operador in.

Ejemplo:

Buscamos una palabra dentro de una oración.

word = 'plaza'
oration = 'El coche rodo por la plaza, y luego se fue'

if word in ortation:
  print('{word}, encontrada')
else:
  print('{word}, no encontrada'}
"""
# Busqueda de una palabra en una oración
word = 'plaza'
oration = 'El coche rodo por la plaza, y luego se fue'

if word in oration:
  print(f'{word}, encontrada')
else:
  print(f'{word}, no encontrada')

# Cambiamos la palabra plaza por Plaza
# Esta busqueda no distingue entre mayusculas o minusculas
# Deberiamos pasar todo a minusculas o todo a mayusculas
# para asegurar la busqueda correcta.

word = 'Plaza'
word_lower = word.lower()
oration = 'El coche rodo por la plaza, y luego se fue'
oration_lower = oration.lower()

if word_lower in oration_lower:
  print(f'{word_lower}, encontrada')
else:
  print(f'{word_lower}, no encontrada')

# Busqueda de un elemento en una coleccion

nums = [1, 2, 3, 4]

if 2 in nums:
  print(f'2, encontrado')
else:
  print(f'{2}, no encontrado')

# Coding Exercise
# In the below code, fix the condition so that the program prints out
# "The word is in the sentence".
# Ejercicio de codificación
# En el siguiente código, corrija la condición para que el programa imprima
# "La palabra está en la oración".

"""
Condicionales compuestos:

Los operadores and y or, el operador and es mucho mas restictivo en sus
condicionales, el operador or, es mas flexible.

El operador and, exige que ambas expresiones sean verdaderas, mientras que el 
operador or permite que una de las dos sea falsa 

Ejemplo

username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

if username == 'jonsnow' and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


if username == 'jonsnow' or password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


logged_in = True
standard_user = False

if logged_in and not standard_user:
  print('You can access the admin dashboard')
else:
  print('You can only access the standard dashboard')
"""

# Coding Exercise
# Fill in the below conditional with a compound condition that will 
# print "Success!" if "number" is anything between 1 and 100 (inclusive).
# Ejercicio de codificación
# Complete el siguiente condicional con una condición compuesta que
# imprimir "¡Éxito!" si "número" está entre 1 y 100 (inclusive).


def compound_conditional(number):
    if number >= 1 and number <= 100:#YourCompoundConditionalHere:
        print("Success!")
    else:
        print("Failure...")