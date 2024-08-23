
#!/usr/bin/env python3

# Ejercicio 1

exe1_str = "Hello"
exe1_number = 123456
exel_list = ["blue", "green", "red", "yellow"]
exe1_bool = True

# Ejercicio 2

exe2_idstr = exe1_str[:3]
print(exe2_idstr)

# Ejercicio 3

exe3_list_new = exel_list[0]
print(exe3_list_new)

# Ejercicio 4

exe4_number_new = exe1_number + 10
print(exe4_number_new)

# Ejercicio 5

print(exel_list.pop())

# Ejercicio 6

nombres = 'harry,alex,susie,jared,gail,conner'

exe6_list = nombres.split(',')
print(exe6_list)

# Ejercicio 7

exe7_str_new = nombres[:5].upper() + nombres[5:]

print(exe7_str_new)

# Ejercicio 8

exe8_var1_name = "World"
exe8_var2_greet = "Hi"
exe8_var3_year = 2024

print("{1} {0} {2}".format(exe8_var1_name, 
                           exe8_var2_greet, exe8_var3_year))

# Ejercicio 9

print(f"{exe8_var2_greet} {exe8_var1_name}")