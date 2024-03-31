#!/usr/bin/env python3

"""
Como utilizar tuplas como claves de diccionarios
He creado un diccionario, con la clave una tupla y como valor
una lista, las tres estructuras

"""

exemple_dict_key_tuple = {
    (1, 'first_key') : [ 10, 20, 30],
    (3, 'second_key') : [ 40, 50, 60],
    (1, 'three_key') : [ 70, 80, 90],
}

print(list(exemple_dict_key_tuple.keys()))

"""
Con la función zip, que la encontramos el la biblioteca central
nos permite fusionar listas generando tuplas por cada posición de ambas
listas, recordemos que las listas comienzan en 0 entonces seria posición 0
de la lista A con la posición 0 de la lista B.
Nos obliga a tener orden riguroso en las listas que vallamos a fusionar,
si no existe un orden en alguna de las dos el fusionado puede ser que arroje
datos erroneos.
Es una excelente herramientas para el aprendizaje automatico, ya que puede 
generar matrices automaticamente de listas consultadas.

La sintaxis es:

listA = [x,x,x]
listB = [x,x,x]

variable_marcador = zip(listaA, listaB)

Creamos una variable de marcador que contendra las tuplas, y realizamos una
llamada a la función zip, al estar en la biblioteca central no es necesario
importar ningun modulo o función externa.

Hay que convertir en lista el objeto zip que crea al fusionar ambas listas,

print(list(variable_marcador))
"""

# Función Zip

positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

scoreboard = zip(positions, players)

print(list(scoreboard))

# Función zip con ejemplo proyecto personal

goals = ['Control plan general', 'Activar formación continua', 'Alcanzar libertad económica']
time_to_goals = [360, 180, 360]

timeboard = zip(goals, time_to_goals)

print(list(timeboard))

"""
Estructura set, o conjunto, hemos tratado listas, diccionarios, tuplas, esta es la cuarta
estructura set.

Su sintaxis en una especie de combinacion entre ambas estructuras listas y diccionarios.

En lugar de utilizar corchetes como cuando expresamos una lista, utilizamos llaves, en lugar
de utilizar pares clave:valor como cuando escribimos un diccionario, utilizamos elementos 
como en las listas.

La caracteristicas basica que diferencia un conjunto de una lista es que en el conjunto esta 
garantizado que los elementos son unicos, no se repiten.

El uso que le podemos otorgar es que tengamos la necesidad de tener una lista de elementos
pero tambien la garantia de que ninguno de los elementos que estan dentro de la lista esta 
duplicado, es unico.

No tiene un uso muy habitual, pero tiene sus cualidades en diversos momentos, cuando no 
queremos tener toda la funcionalidad de listas, pero queremos una lista de elementos que no se
puedan duplicar seria bueno utilizar un conjunto, aunque si queremos buscar como en una lista
se producira un error, el objeto set que nos retorna no es iterable como las listas, por lo
tanto las busquedas o consultas que podemos realizar serian:

- debemos llamar a todas los elemntos del conjunto, 
- o preguntar por uno en concreto. 

Nos devolvera un valor booleano, Verdadero o Falso.

Ejemplo:

goals = {
    'Control plan general',
    'Activar formación continua',
    'Alcanzar libertad económica',
    }

# Llamamos a todos los elementos
print(goals)

# Consultamos por uno en concreto
# Esperamos un valor de True or False
variable_set1 = 'Activar formación continua' in goals
variabñe_set2 = 'Control plan general' in goals
"""

goals = {
    'Control plan general',
    'Activar formación continua',
    'Alcanzar libertad económica',
    }

print(goals)

variable_set1 = 'Activar formación continua' in goals
print(variable_set1)
variabñe_set2 = 'otros' in goals
print(variabñe_set2)

"""
Trabajar con conjuntos nos ofrece una caracteristica como fusionado de varios conjuntos
este desarrollo lo que realiza es fusionar los conjuntos propuestos y darnos la oportu
nidad de trabajar con los elementos de ambos conjuntos, seleccionando lo que nos requie
ra la ocasión, podemos seleccionar solo los conjuntos no duplicados en ambos conjuntos, 
dandonos la oportunidad de comprobar la no duplicidad de elementos dentro de un conjunto
Podemos seleccionar los elementos que estan duplicados entre los dos conjuntos.
Tal como seria un diagrama de Venn representan los circulos que convergen y crean una
intersección entre ellos, tenemos elementos en el circulo A, tambien en el circulo B, y
se crea la intersección entre ambos donde tambien tenemos elementos que comparten ambos
circulos, en este caso conjuntos.

Ejemplo:

rules_proyect = {
    'Realizar tarea diaria xxx-xx',
    'Realizar tarea semanal xxx-xA',
    'Actualizar rules cada xx dias',
    'Actualizar proyect cada xx dias'
    }

rules_plan = {
    'Realizar tarea diaria xxx-xx',
    'Realizar tarea semanal xxx-xA',
    'Actualizar rules cada xx dias',
    'Comprobar metrica por actualización'
    }
# Creamos una variable marcador, que nos recoje el nuevo objeto conjunto
# Utilizamos el caracter tuberia
merge_set = rules_proyect | rules_plan
print(merge_set)
"""

rules_proyect = {
    'Realizar tarea diaria xxx-xx',
    'Realizar tarea semanal xxx-xA',
    'Actualizar rules cada xx dias',
    'Actualizar proyect cada xx dias'
    }

rules_plan = {
    'Realizar tarea diaria xxx-xx',
    'Realizar tarea semanal xxx-xA',
    'Actualizar rules cada xx dias',
    'Comprobar metrica por actualización'
    }

# Ofrece una lista con los elementos unicos de ambos conjuntos
merge_set = rules_proyect | rules_plan
print(merge_set)

# Ofrece el elemento unico de rules_proyect
exclusive_rules_proyect = rules_proyect - rules_plan
print(exclusive_rules_proyect)

# Ofrece el elemento unico de rules_proyect
exclusive_rules_plan = rules_plan - rules_proyect
print(exclusive_rules_plan)

# Ofrece los elementos que se repiten entre ambos conjuntos
universal_rules = rules_plan & rules_proyect
print(universal_rules)

"""
Desarrollar una función generadora de html, utilizando la
interpolación de cadenas.

Creo la función con la palabra clave def, la nombro con
heading_generator y le paso los parametros que tiene que
obtener, en este caso el titulo y el nivel de la etiqueta
h de HTML (heading_type)
Despues, retorno con formato abriendo la etiqueta y dejando
que automaticamente la interpolacion de cadenas genere el 
nivel obtenido.
"""
def heading_generator(title, heading_type):
    return f'<h{heading_type}>{title}</h{heading_type}>'

print(heading_generator('fhtml', 2))

"""
Bucles en python: Hay dos tipos de bucles en python, bucle for-in y
bucle while.

Ambos se pueden usar para iterar sobre colecciones, rangos, listas,...

Bucle for-in: Queda determinado por el número de elementos con los que
va a iterar.

Bucle while: Su terminación la debe implementar el desarrollador, dandole
las veces que debe iterar y pararse, si no es asi, podemos crear un bucle
infinito, la maquina terminara fallando.

Se utiliza mas el bucle for-in, pero existen algunos casos que es mejor 
utilizar el bucle while que el bucle for-in

Bucle for-in:

El mecanimos del bucle, es igual para todas las colecciones de datos que
deseemos iterar.

Ejemplo: Iterar una lista con las areas

pgeneral_areas = ['social', 'económica', 'educación', 'justicia']

Creamos una variable de bloque o varible iteradora para iterar sobre 
cada uno de los elementos
Por cada nueva iteración del bucle sobre el objeto a iterar la varialbe 
iteradora cambia su valor
La convención comun es que si la coleccion de elementos, tiene una nombre
en plural, se utilice el singular para el nombre de la variable iteradora

for variable_iteradora in pgeneral_areas:
    print(variable_iteradora)

La linea siguiente a los dos puntos inicia un bloque de codigo que en python esta determi
nado por la sangria de 2 o 4 espacios, ojo con esto no hemos extendido información
sin embargo nos puede arrojar error de sangria. El detalle es que todo bloque de codigo
debe estar a continuación de sangria.

De la misma forma podemos trabajar con tuplas, al ser muy similares, aprovechamos
todos los conocimientos

Ejemplo: Iterar una tupla con las areas

pgeneral_areas = ('social', 'económica', 'educación', 'justicia')

La forma de trabajar con diccionarios es algo diferente, recordemos que los diccionarios
lo forman pares de clave=valor, por lo tanto trabajamos con dos elementos.

Esto nos lleva a que tenemos que trabajar con dos elementos por cada iteración del bucle
for-in pasandole dos variables iteradoras y solicitandole al diccionario que actue sobre
cada elemento pasandole la función items(), que nos permite ver dentro del objeto 
diccionario todos sus elementos la sintaxis es dictionary.items()

Ejemplo: Iterar un diccinario con las areas y su nombre nemotecnico

pgeneral_areas = {
    'social' : 'soci',
    'económica' : 'econ',
    'educación' : 'educ',
    'justicia' : 'just'
    }

for first_var_ite, second_var_ite in pgeneral_areas.items():
    print(first_var_ite, second_var_ite)    
"""

# Bucle for and lists
pgeneral_areas = ['social', 'económica', 'educación', 'justicia']

for pgeneral_area in pgeneral_areas:
    print(pgeneral_area)

# Bucle for and tuples
pgeneral_areas = ('social', 'económica', 'educación', 'justicia')

for pgeneral_area in pgeneral_areas:
    print(pgeneral_area)

# Bucle for and dictionary
# Use fuction items()
pgeneral_areas = {
    'social' : 'soci',
    'económica' : 'econ',
    'educación' : 'educ',
    'justicia' : 'just'
    }

for first_var_ite, second_var_ite in pgeneral_areas.items():
    print(first_var_ite, second_var_ite)


"""
Ejercicio prueba de la guias iniciales de bucles
Crear una lista que creo dentro de la función, creo un bucle for-in para manejar la lista e
imprimo el elemento segun itera por la lista, me ha mareado ver un return my_list, solo tengo 
que llamar a la funcion fuera para que imprima la iteracion, pero si quiero llamar a la salida
de la funcion total, tengo la lista en my_list, que lanza return.
"""

# Coding Exercise
# Create a list named my_list with 5 elements. Then loop over the list to print out each element.
# Crear una lista denominada my_list con 5 elementos, imprimir cada elemento de la lista con un loop.
    
def loop_over_list():
    # Write your code here
    my_list = ['On', 'Off', 'Stop', 'Pause', 'Cancel']
    for state in my_list:
        print(state)
    
    return my_list

loop_over_list()


"""
Ejercicio rapido para trabajar con cadenas y loop for-in, las cadenas son caracteres y podemos extraer
cada caracter de la cadena iterando sobre cada caracter.
Ejemplo

alfabeto = ['abcdefghijklmn']

for caracter in alfabeto:
    print(caracter)

"""

# Bucle for-in iteration with string
alfabeto = 'abcdefghijklmn'

for caracter in alfabeto:
    print(caracter)

"""
Ejercicio de la guia bucle for-in iteracion con cadenas

Crea una variable llamada "nombre" y asígnale tu nombre como una cadena. 
Escriba un bucle for in que repita la cadena e imprima cada carácter.
"""
# Coding Exercise
# Create a variable called "name" and assign it your name as a string.
# Write a for in loop that iterates through the string and prints each character.

my_name = 'Daniel'

for caracter in my_name:
    print(caracter)

"""
Pasarle rangos al bucle for-in, lo primero recordar las caracteristicas de los rangos,
su sintaxis, nos solicita el primero y el ultimo y solo llega hasta el anterior al
seleccionado, por lo tanto de 1:5 imprimira 0,1,2,3,4 uno antes del ultimo seleccionado
Hay que recordarlo si no queremos errores.

Pasarle rango al bucle es iterar por esos elementos seleccionados y delimitados, tenemos
que crear pasarle un rango a la varible iteradora.

Tambien podemos darle el intervalo de iteraciones que queremos en el bucle, nos permite
seleccionar los saltos entre elementos que van a ser iterados.

Ejemplo:

for v_iter in range[1,10]:
    print(v_iter)

for v_iter in range[1,10,3]
    print(v_iter)
"""
# Bucle for-in iteration over range
for v_iter in range(1,10):
    print(v_iter)

for v_iter in range(1,10,3):
    print(v_iter)

# Coding Exercise
# Using a range, write a loop that prints out all the numbers from one through 10 (10 is included).
# Usando un rango, escriba un bucle que imprima todos los números del uno al 10 (el 10 está incluido).
    
for num in range(1,11):
    print(num)

"""
Utilizar continue and break en los loop de python.

Tenemos dos operadores de flujo, son continue y break con los que trabajaremos cuando queramos interrumpir
un flujo devido a una condición.

continue --- le da continuidad al flujo, sigue ejecutando el loop en la siguiente iteración o expresión
break --- detiene el bucle y sale de el, terminando la ejecucion 

Ejemplo guia:

usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

for username in usernames:
  if username == 'cersei':
    print(f'Sorry, {username}, you are not allowed')
    continue
  else:
    print(f'{username} is allowed')

for username in usernames:
  if username == 'cersei':
    print(f'{username} was found at index {usernames.index(username)}')
    break
  print(username)

Ejercicio personal:

- Tengo que buscar un estado dentro de la lista de estados generada anteriormente.
- Lo voy a buscar con los dos operadores de flujo, continue y break, continue, me
dejara proseguir con el loop y terminar con todos los elementos, no se parara, pero
break, terminara con el flujo completamente y se saldra del loop.
"""

# Break and Continue with loop for-in
my_list_state = ['On', 'Off', 'Stop', 'Pause', 'Cancel']

for state in my_list_state:
    if state == 'Pause':
        print(f'{state} : Este estado no tiene autorización')
        # utilizo continue para que el flujo continue, en este caso sigue el loop
        continue
    else:
        print(f'{state} : Esta autorizado')    

for state in my_list_state:
    if state == 'Pause':
        # formatear la salida de print con f y buscando el indice del estado iterado por el loop
        # y seleccionado por el condicional if
        print(f'{state} : Este estado no tiene autorización, indice = {my_list_state.index(state)}')
        # utilizo break para salir del condicional y a su vez terminar el loop
        break
    print(f'{state} : Autorizado con indice = {my_list_state.index(state)}')


# Coding Exercise
# Write a loop that loops over the list of vegetables and prints each one out.
# When it reaches 'apple' it should print 'apple is not a vegetable' and then break.
# Escribe un bucle que recorra la lista de verduras e imprima cada una.
# Cuando llegue a 'manzana' debería imprimir 'la manzana no es un vegetal' y luego romperse.

def loop_and_break():
    vegetables = ["onion", "broccoli", "apple", "spinach"]
    
    # Write your code here
    for vegetable in vegetables:
        if vegetable == "apple":
            print(f"{vegetable} is not vegetable")
            break
        print(vegetable)

loop_and_break()

"""
Bucle while, la opción a for-in, pero de uso mucho menor.

"""