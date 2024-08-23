#!/usr/bin/env python3

"""
Cree bucle for python
"""

# Creamos un interrogador al sensor
status_list = [0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,1]
count_sensor = len(status_list)
count = 0
sensor_status = status_list[0]

#print(count_sensor)
#print(sensor_status)

while count < count_sensor:
    #print("iteration loop")
    #print(status_list)
    sensor_status = status_list[count]
    #print(sensor_status)
    count += 1
else:
    print("end loop")

# La siguiente construcción, sabiendo que el sensor, nos ofrece servicio, nos lanza un estado 0,
# quiere decir en funcionamiento ok, o 1 que sería error de sensor.
# Ahora obtendremos el valor de temperatura que también lanza el sensor.

# Ajustamos una lista de temperaturas
check_temp = [12.6,-500,21.14,-500,23.1,16.5,29.6,-15.2,28.6,-500,23.21,-500,43.2,-500,-500,-500,33.6,11.12,-6.3, -500]
count_temp = len(check_temp)
temp = check_temp[0]

# Creamos nuestras bibliotecas de datos, diccionarios y listas
grades = {
    'Frio' : 'Entre 0 y 21 grados',
    'Agradable' : 'Entre 21 y 25 grados',
    'Calor' : 'Entre 25 y help',
    }
ropa = ['abrigo', 'sudadera', 'camiseta']

# Verificamos los datos pasados, estado sensor y temperatura
if count_temp == count_sensor:
    for t in check_temp:
        if t > -25.00 and t <= 21.00:
            print(f" Temperatura : {t} grados, {grades['Frio']} de temperatura, se recomienda : {ropa[0]}")
        elif t > 21.00 and t <= 25.00:
            print(f" Temperatura : {t} grados, {grades['Agradable']} de temperatura, se recomienda : {ropa[1]}")
        elif t > 25.00 and t <= 55.00:
            print(f" Temperatura : {t} grados, {grades['Calor']} de temperatura, se recomienda : {ropa[2]}")
        else:
            print(f" Error toma muestra : {t}")
else:
    print("error system")


"""
Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
"""
def sum_function(a, b, c):
    return a + b + c

sum_function(1, 2, 3)


"""
Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
"""
x = lambda a, b, c: a + b + c
print(x(1, 2, 3))


"""
Utilizando la siguiente lista y variable, determine si el valor
de la variable coincide o no con un valor de la lista. 
*Sugerencia, si es necesario, utilice un bucle for in y el 
operador in.
"""

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

# Tenemos que recorrer toda la lista y una vez terminada, devolver
# el resultado, esta en la lista o no esta.
# Necesito un contador que acumule las veces que hay coincidencia
# Lo mejor sería crear una función y pasarle los valores, para que
# solo devuelva un resultado y sea mas legible lo que estamos haciendo

def search_element(name, list):
    count = 0
    for n in lista_nombre:
        if n == nombre:
            count += 1
    
    if count > 0:
        print("Si está en la lista")
    else:
        print("No está en la lista")

search_element(nombre,lista_nombre)