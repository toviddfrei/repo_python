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

La diferencia principal entre un bucle for-in y un bucle while, es que como sabemos el
for-in, tiene un inicio y un final predeterminado, la cantidad de elementos por los que
tiene que iterar comienza en el primero y se detiene en el ultimo. Sin embargo un bucle
while no tiene un final definido, si no le predeterminamos ese final, podemos crear
un bucle infinito, con las consecuencias que eso puede acarrear, bloqueo de computador.

Para definir cuando debe terminar un bucle while, debemos crear un valor centinela, para
decirle cuando alcance ese valor parate.
Vamos a crear un valor centinela contando todos los elementos de la lista con la función
len(), cuando len() nos devuelva el valor total de los elementos añadimos la condicion de
mayor que 0 ese sera el valor centinela cuando la condicion sea menor a 0 y el condicional
no se cumpla, el bucle se detendra.

Ejemplo:

Vamos a iterar un rango de 1 a 100, pero iremos eliminando elementos segun iteremos el
rango, cuando la condicion que estipulemos no se cumpla el bule while se detendra.

iteramos el rango con while, le pasamos la cantidad de elementos con len función, y
mostramos y eliminamos el ultimo elemento con pop()

nums = list(range(1,100))

while len(nums) > 0:
    print(nums.pop())


Ejemplo 1:

Creamos un juego de adivinanza, el usuario debe averiguar un valor, una vez lo acierte el 
bucle while se detendra y saldra este valor que se tiene que averiguar es el valor centinela
el que hace que while se detenga.

Utilizamos el bucle while, y el condicional if, si el retorno es True, seguimos iterando, si 
el retorno el False, terminamos el bucle y nos salimos.
Retornaremos False cuando el usuario acierte, True es devuelto mientras el usuario no acierte.

def guessing_game():
  while True:
    print('What is your guess?')
    guess = input()

    if guess == '42':
      print('You correctly guessed it!')
      return False
    else:
      print(f"No, {guess} isn't the answer, please try again\n")

guessing_game()
"""
# Bucle while, cuenta atras con funcion len() y pop() 
nums = list(range(1,100))

while len(nums) > 0:
    print(nums.pop())

# Juego adivinar el valor
# Si adivinas el valor, bucle while se detiene
def guessing_game():
  # mientras return sea True, seguira iterando
  while True:
    print('What is your guess?')
    # le preguntamos al usuario un valor
    guess = input()

    # Aplicamos la condicion del valor centinela
    if guess == '42':
      print('You correctly guessed it!')
      # Si el usuario acierta retornamos False y se
      # detiene el bucle
      return False
    # Si no continua el blucle hasta que acertemos
    else:
      print(f"No, {guess} isn't the answer, please try again\n")

guessing_game()

# Coding Exercise
# In the below starter code, place 4 dog names (elements) of your
# choice in the dog_house list. Then write a while loop that iterates
# through the dog_house list and prints each dogs name. An iterator
# variable named "counter" must be set, and must have an initial value of 0.

# Hint: An iterator value (also sometimes called a sentinel value) is a
# value that exists outside of your loop, and that you update or otherwise
# keep track of each time you loop, so that your while loop knows when to end.

"""
Example:
iterator_value = 0
while iterator_value < 10:
    print("Keep looping...")
    iterator_value += 1
"""

# Ejercicio de codificación
# En el siguiente código de inicio, coloque 4 nombres de perros (elementos)
# de su elección en la lista dog_house. Luego, escriba un bucle while que 
# recorra la lista dog_house e imprima el nombre de cada perro. 
# Se debe establecer una variable iteradora denominada "contador" 
# y debe tener un valor inicial de 0.

# Sugerencia: un valor de iterador (también llamado a veces valor centinela)
# es un valor que existe fuera de su ciclo y que usted actualiza o realiza
# un seguimiento cada vez que realiza un ciclo, para que su ciclo while sepa
# cuándo finalizar.

"""
Ejemplo:
valor_iterador = 0
mientras valor_iterador < 10:
    print("Seguir bucle...")
    valor_iterador += 1
"""

def loop_using_while():
    dog_house = ['luna','sol','plata', 'oro'] # Put dog names here
    # Write your code here
    counter = 0
    
    while len(dog_house) > counter:
        print(f"{dog_house[counter]}")
        counter += 1 
    return [dog_house, counter]

loop_using_while()

"""
Combinar y aplanar listas con el bucle for-in.

Vamos a utilizar la función append() para agregar elementos nuevos a la lista

Ejemplo:

Tenemos dos listas de elementos, state antiguos, nuevos state, queremos 
tener una sola lista con los estados nuevos actualizados, la forma de hacerlo,
no es sumar una lista a la otra, esto agregara una lista completa a la otra lista
queremos tener una sola lista con todos los elementos.

state_old = ['On', 'Off', 'Pause']
state_new = ['Stop', 'Cancel', 'Slow']

# No es lo que buscamos
state_new += state_old
"""
# Combinar listas con for-in
state_old = ['On', 'Off', 'Pause']
state_new = ['Stop', 'Cancel', 'Slow']

# Averiguar si es util esta forma

## state_new += state_old

# No es lo que buscamos
state_db = [state_old, state_new]
print(state_db)

# Utilizamos bucle for-in
for state in state_old:
    state_new.append(state)
    print(state)

print(state_new)

# Coding Exercise
# Write a for loop that takes each number from the numbers list,
# increments it by 1, and adds it to the result list.
# Ejercicio de codificación
# Escribe un bucle for que tome cada número de la lista de números,
# lo incrementa en 1 y lo agrega a la lista de resultados.

def loop_over_list():
    numbers = [1,2,3,4,5,6]
    result = []
    
    # Write your code here
    for num in numbers:
        result.append(num + 1)
    
    return result

print(loop_over_list())


"""
Compresión de listas.

El tema que vamos a discutir es una lista de comprensión. 
Y lo que eso significa esencialmente es que podemos configurar varios bucles
for-in para que funcionen en una sola línea y, de hecho, podemos generar 
listas a partir de esas líneas de código.

Voy a desmenuzar este codigo, mostrando la compresión de listas.

# De forma tradicional

# Creamos una lista num_list, con rango de valores de 1 a 11, imprimira de 1 a 10
num_list = range(1, 11)
# Creamos una segunda lista vacia cubed_nums
cubed_nums = []
# Creamos un bucle for-in que itera sobre la num_list
for num in num_list:
  # Añadimos en la lista vacia, cubed_nums el resultado de num elevado al cubo
  cubed_nums.append(num ** 3)

print(f"{cubed_nums}, tradicional")

# Por compresión de listas

# Creamos una lista cubed_nums, donde guardaremos los resultados
# Abrimos corchetes como en una lista
# la primera expresión antes del bucle, debe ser la operacion o el valor que queremos
# Justo despues expresamos el bucle for, tal como antes for num in num_list
# El resto la hace python, itera sobre num_list, extrae un num lo eleva al cubo y lo
# guarda en la lista cubed_nums
cubed_nums = [num ** 3 for num in num_list]

print(f"{cubed_nums}, compresion")

Podemos crear otro ejemplo, de compresion de listas incluyendo un condicional al bucle
for-in con el condicional if, buscando solo lo valores pares en la salida de la
compresión

# De forma tradicional

# Creamos una lista vacia even_numbers
even_numbers = []
# Creamos el bucle for-in para iterar sobre nuestra lista base de 1 a 11
for num in num_list:
  # Creamos el condicional para obtener los pares con el operador de modulo, el cual
  # retorna 0 cuando no tiene resto, por lo tanto son pares.
  if num % 2 == 0:
    # Añadimos el num a la lista vacia
    even_numbers.append(num)

print(even_numbers)

# Utilizando compresion de lista

# Creamos la lista even_numbers
# Aperturamos la lista con los corchetes
# Dato que guardara, antes del inicio del bucle for
# Creamos el bucle for, iterando el data num con nuestra lista base
# Justo despues expresamos el condicional if buscando los valores deteminados
# La operativa es la misma cada iteracion de bucle for por num_list
# Es pasada al condicional para obtener el valor y si cumple la condicion
# Es guardado en num detro de la lista even_numbers
even_numbers = [num for num in num_list if num % 2 == 0]

print(even_numbers)
"""

# De forma tradicional

# Creamos una lista num_list, con rango de valores de 1 a 11, imprimira de 1 a 10
num_list = range(1, 11)
# Creamos una segunda lista vacia cubed_nums
cubed_nums = []
# Creamos un bucle for-in que itera sobre la num_list
for num in num_list:
  # Añadimos en la lista vacia, cubed_nums el resultado de num elevado al cubo
  cubed_nums.append(num ** 3)

print(f"{cubed_nums}, tradicional")

# Por compresión de listas

# Creamos una lista cubed_nums, donde guardaremos los resultados
# Abrimos corchetes como en una lista
# la primera expresión antes del bucle, debe ser la operacion o el valor que queremos
# Justo despues expresamos el bucle for, tal como antes for num in num_list
# El resto la hace python, itera sobre num_list, extrae un num lo eleva al cubo y lo
# guarda en la lista cubed_nums
cubed_nums = [num ** 3 for num in num_list]

print(f"{cubed_nums}, compresion")

# De forma tradicional

# Creamos una lista vacia even_numbers
even_numbers = []
# Creamos el bucle for-in para iterar sobre nuestra lista base de 1 a 11
for num in num_list:
  # Creamos el condicional para obtener los pares con el operador de modulo, el cual
  # retorna 0 cuando no tiene resto, por lo tanto son pares.
  if num % 2 == 0:
    # Añadimos el num a la lista vacia
    even_numbers.append(num)

print(f"{even_numbers}, tradicional")

# Utilizando compresion de lista

# Creamos la lista even_numbers
# Aperturamos la lista con los corchetes
# Dato que guardara, antes del inicio del bucle for
# Creamos el bucle for, iterando el data num con nuestra lista base
# Justo despues expresamos el condicional if buscando los valores deteminados
# La operativa es la misma cada iteracion de bucle for por num_list
# Es pasada al condicional para obtener el valor y si cumple la condicion
# Es guardado en num detro de la lista even_numbers
even_numbers = [num for num in num_list if num % 2 == 0]

print(f"{even_numbers}, compresion")


# Coding Exercise
# Create a variable called result and use list comprehension 
# to increment each number from the numbers list by 1
# Ejercicio de codificación
# Crea una variable llamada resultado y usa lista de comprensión
# para incrementar cada número de la lista de números en 1.

def list_comprehension():
    numbers = [1,2,3,4,5,6]
    # Write your code here
    result = [num + 1 for num in numbers]
    
    return result

print(list_comprehension())