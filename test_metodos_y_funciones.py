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