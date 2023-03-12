import random
from datetime import datetime

class Cliente:
    
    def __init__(self, ID, nombre, direccion, telefono):
        self.__ID = ID
        self.__nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        

    def __str__(self):
        return(f"Cliente: el ID del cliente es: {self.__ID}, nombre: {self.__nombre}, con domicilio: {self.direccion}, numero de telefono: {self.telefono}")


    def comprar_articulo(self):

        carrito = []

        while True:
            print("1. Añadir producto al carrito")
            print("2. Remover producto del carrito")
            print("3. Ver lista de compras")
            print("4. Salir del programa")

            opciones_carrito = int(input("Ingrese la ocion deseada: "))

            if opciones_carrito == 1:

                producto = input("Ingrese un producto:  ").lower()

                if producto in carrito:
                    print("El producto ya esta en la lista")
                else:
                    carrito.append(producto)

            elif opciones_carrito == 2:

                producto = input("Ingrese un producto:  ").lower()

                if producto not in carrito:
                    print("Este producto no esta en el carrito")
                else:
                    carrito.remove(producto)   

            elif opciones_carrito == 3:

                print("Lista de compras: ")
                for art in carrito:
                    print("-", art)  
            
            elif opciones_carrito == 4:
                print(f"Compra finalizada, Ticket: {random.randrange(1000, 5000)}, Fecha {datetime.now()} ")
                break
            
            else:
                print("La opcion que ingresaste es incorrecta")    


    def membresia(self):
        
        tipo_membresia = input("Ingrese el tipó de membresia deseada:\n -Standar\n -Gold\n -Black:  ").capitalize()

        if tipo_membresia == "Standar":
            
            print(f"Felicitaciones! Ud eligio ser miembro {tipo_membresia}!")   

        elif tipo_membresia == "Gold":

            print(f"Felicitaciones! Ud eligio ser miembro {tipo_membresia}!")       

        elif tipo_membresia == "Black":

            print(f"Felicitaciones! Ud eligio ser miembro {tipo_membresia}!")

        else:
            print("Disculpe la opcion ingresada no corresponde")
            tipo_membresia = input("Ingrese nuevamente el tipó de membresia deseada:\n -Standar\n -Gold\n -Black:  ").capitalize()