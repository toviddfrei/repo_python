#!/usr/bin/env python3

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