from assets.coeficientes import coeficiente_gold, coeficiente_black
import random
from datetime import datetime


ticket = random.randrange(100000, 500000)
fecha_ticket = datetime.now()
class Cliente:
    
    def __init__(self, ID, nombre, direccion, telefono):
        self._ID = ID
        self._nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        

    def __str__(self):
        return(f"Cliente: el ID del cliente es: {self._ID}, nombre: {self._nombre}, con domicilio: {self.direccion}, numero de telefono: {self.telefono}")


    def comprar_articulo(self):

        carrito = []

        while True:
            print("1. Añadir producto al carrito")
            print("2. Remover producto del carrito")
            print("3. Ver lista de compras")
            print("4. Salir del programa")

            try:

                opciones_carrito = int(input("Ingrese la opcion deseada: "))

            except:
                print("La opcion indicada no es correcta")
                opciones_carrito = int(input("Ingrese nuevamente una opcion: "))

            
            if opciones_carrito == 1:

                producto = input("Ingrese un producto:  ").lower()

                if producto in carrito:
                    print(f"El producto {producto} ya esta en la lista")
                else:
                    carrito.append(producto)
                    print(f"Ud. agrego {producto} a su carrito")

            elif opciones_carrito == 2:

                producto = input("Ingrese un producto:  ").lower()

                if producto not in carrito:
                    print(f"El producto {producto} no esta en el carrito")
                else:
                    carrito.remove(producto) 
                    print(f"Ud. removio {producto} satisfactoriamente")

                    if carrito == []:
                        print("El carrito esta vacio")

            elif opciones_carrito == 3:

                print("Lista de compras: ")

                if carrito == []:
                        print("El carrito esta vacio")

                else:
                    for art in carrito:
                        print("-", art) 
            
            elif opciones_carrito == 4:

                if carrito == []:
                    print("El carrito esta vacio, lo esperamos nuevamente para su proxima compra")
                    break

                else:    
                    print(f"Felicitaciones! su compra finalizo correctamente,su numero de Ticket es: {ticket}, Fecha {fecha_ticket} ")
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
            print("Disculpe, la opcion ingresada no corresponde")

            tipo_membresia = input("Ingrese nuevamente el tipo de membresia deseada:\n -Standar\n -Gold\n -Black:  ").capitalize()



class Cliente_gold(Cliente):

    def __init__(self, ID, nombre, direccion, telefono, app_bonificada):

        super().__init__(ID, nombre, direccion, telefono)
        self.app_bonificada = app_bonificada

    def __str__(self):
        return f"Tu app bonificada es: {self.app_bonificada}" 

    def comprar_articulo(self):
        return super().comprar_articulo()

    def membresia(self):
        return super().membresia()

    def puntos(self, pesos_compra):

        return(f"Los puntos de esta compra son: {coeficiente_gold(pesos_compra):.2f} puntos")    



class Cliente_black(Cliente):

    def __init__(self, ID, nombre, direccion, telefono, descuento):
        
        super().__init__(ID, nombre, direccion, telefono)
        self.descuento = descuento

    def __str__(self):
        return f"Tendras todos los dias 20% de descuento en: {self.descuento}"   

    def comprar_articulo(self):
        return super().comprar_articulo()

    def membresia(self):
        return super().membresia()  

    def puntos(self, pesos_compra):

        return(f"Los puntos de esta compra son: {coeficiente_black(pesos_compra):.2f} puntos")  

