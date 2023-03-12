class Cliente:
    
    def __init__(self, ID, nombre, direccion, membresia):
        self.ID = ID
        self.nombre = nombre
        self.direccion = direccion
        self.membresia = membresia
        

    def __str__(self):
        return(f"Cliente: {self.ID}, {self.nombre}, {self.direccion}, {self.membresia}")


    def comprar_articulo(self):

        print("estoy comprando")
        # carrito=[]
        
        # articulos = input("ingrese los articulos, solo podra cargar 5 articulos por compra: ")

        # for articulos in range(5):

        #     return carrito.apped(articulos)


