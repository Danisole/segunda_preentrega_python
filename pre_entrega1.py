def ingresar_datos(nombre, clave, base):

    diccionario_usuario={}

    diccionario_usuario["NOMBRE"]=nombre;
    diccionario_usuario["CLAVE"]=clave;

    print(diccionario_usuario)
    base.append(diccionario_usuario)

    return base

def mostrar_usuario(usuario):
    print("-------------------")
    print(f"Nombre: {usuario['NOMBRE']}")
    print(f"Clave: {usuario['CLAVE']}")
    print("-------------------")

def comprobar_usuario(nombre, clave, base):

    for usuario in base:

        if usuario["NOMBRE"]== nombre and usuario["CLAVE"]==clave:
            return True
        else:
            return False
        
from google.colab import drive 
drive.mount('/drive/')

ruta ="/drive/MyDrive/Colab Notebooks/usuarios.json"

import json

data={}
data['usuarios']=[]

for cada_usuario in base_de_datos:
    data['usuarios'].append(cada_usuario)

print(data)

with open(ruta, "w") as f:

    json.dump(data, f, indent=4)

with open(ruta) as f:
    data_lectura= json.load(f)

    for traer_usuario in data_lectura['usuarios']:
        print("Nombre", traer_usuario["NOMBRE"])
        print("Clave", traer_usuario["CLAVE"])
        print("--------------------------")

base_de_datos= []


nombre = input("ingrese nombre ").lower()

clave =str(input("ingrese clave ")).lower()

base_de_datos= ingresar_datos(nombre, clave, base_de_datos)

nombre = input("ingrese nombre ").lower()

clave =str(input("ingrese clave ")).lower()

base_de_datos= ingresar_datos(nombre, clave, base_de_datos)

nombre = input("ingrese nombre ").lower()
clave =str(input("ingrese clave ")).lower()

base_de_datos= ingresar_datos(nombre, clave, base_de_datos)

if comprobar_usuario("dani", "dani123", data_lectura['usuarios']):
        print("Usuario correcto, bienvenid@")

else:
        print("usuario inexistente")

mostrar_usuario(data_lectura['usuarios'][1])