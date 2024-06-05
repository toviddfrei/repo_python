"""
Script para crear usuario y contraseña, solicitando
el nombre completo.

He utilizado la importacion del modulo random ya que 
queria darle algo de aleatorio a la contraseña.
"""
import random

class User:
    def __init__(self, name):
        self.name = name

    def iduser(self):
        iduser = self.name[0:9].replace(' ','')
        return iduser
        
    def idpass(self):
        idpass = str(len(self.name))+str(random.randrange(3,33,3))
        return idpass
        
    def formatter(self):
        user = self.iduser()
        password = self.idpass()
        return f'The user name is: {user}, and the password is: {user}{password}'

# Introduzca su nombre completo
user_reg = User('Daniel Miñana Montero')

print(user_reg)
print(user_reg.formatter())