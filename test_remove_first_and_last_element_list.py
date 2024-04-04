#!/usr/bin/env python3

"""
Ejercicio, eliminar el primer y ultimo elemento de una lista.

Tengo dos ejercicios similares un borrador mio, que voy arreglar y 
explicar

Utilizamos la desestructuracion de python es una gran opción entre 
todos los lenguajes, por su sencillez

Desestructuraremos las listas en variables, contando que la primera
y ultima variable la desechamos, ni siquiera la nombramos se declara
con _ guion bajo por eso la expresion _, variable, _ la primera y 
ultima out.
Luego añadimos a la variable un *variable, por lo tanto recogera todos
los elementos entre el primero y el ultimo y creara una lista con todos
ellos.
Detalle importante implementar un condicional para contar como minimo
con 3 elementos en la lista, si no puede darse a error dejando la lista vacia

"""
# Borrador io
# Creo tres listas diferentes
html = ['<h1>','some content','</h1>']
html_2 = ['<h1>','some content','</h1>', 'more']
num_list = [1,2,3,4,5,6]

# Creo una funcion remover primero y ultimo
def remove_first_and_last(list_to_clean):
    # Desfragmetamos la lista en tres variables
    # Desechamos la primera y ultima _
    # Creamos una nueva lista con los elementos en medio
    _, *two, _ = list_to_clean

    # Muy importante retornar valor de la funcion.
    return two

print(remove_first_and_last(html))
print(remove_first_and_last(html_2))
print(remove_first_and_last(num_list))

"""
list.append('Hola')
print(list)

list.remove(html[0])
print(list)

list.pop()
print(list)
"""

def remove_first_and_last(list_to_clean):
  _, *content, _ = list_to_clean
  return content


html = ['<h1>', 'My content', '</h1>']

print(remove_first_and_last(html))

other_content_to_clean = ['', 'My content', 'Something else', '/']

print(remove_first_and_last(other_content_to_clean))

num_list = [1,2,3,4,5,6]

print(remove_first_and_last(num_list))