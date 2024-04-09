#!/usr/bin/env python3

"""
Funciones lambda, todos los lenguajes modernos de proposito general tienen algun
tipo de estructura de este tipo.

Lambda básicamente es una herramienta que permite resumir una funcion y luego
pasarla a otras funciones.

Las funciones dentro de python se les llama ciudadanos de primera clase lo que 
significa que puedes tratar una funcion como cualquier tipo de objeto.

Lo que nos permite lambda es resumir cualquier comportamiento y luego pasarlo a
una funcion, son muy moviles y faciles de usar, podemos pensar como si fuera una
variable que puedes pasar a una funcion con valores basicos como numeros, cadenas,
diccionario.

Entonces, en resumen, Lambda le brinda la capacidad de ajustar rápida y
fácilmente la funcionalidad, almacenarla en una variable y luego pasar todo el 
proceso a otras funciones y otras partes de su programa.

Ejemplo:

full_name = lambda first, last: f'{first} {last}'


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kristine', 'Hudgens'))
"""

# Ejemplo personal:

# creo la lambda solo para dar formato a los elementos
car_type = lambda marca, modelo: f'{marca} {modelo}'

# creo la funcion que imprimira el mensaje
def selector_car(name):
    print(f'Good car {name}')

# llamo a la funcion, que llama a la variable de lambda
selector_car(car_type('Ford', 'Fiesta'))


# Coding Exercise
# In the code below, create a variable called "greeting" and assign
# it a lambda function that accepts a name as an argument,
# and return the string "Hi, name".
# Example: If you pass in the name "Jordan", 
# it should return "Hi, Jordan".
# Ejercicio de codificación
# En el código siguiente, crea una variable llamada "saludo" y asigna
# es una función lambda que acepta un nombre como argumento,
# y devuelve la cadena "Hola, nombre".
# Ejemplo: Si pasas el nombre "Jordan",
# debería devolver "Hola, Jordan".


def lambda_practice():
    # Write your code here
    greeting = lambda name: f'Hi, {name}'
    greeting('Jordan')
    return greeting


lambda_practice()

