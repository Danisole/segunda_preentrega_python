from cliente_class import Cliente_black
import random

id=random.randrange(100, 300)

print("--------------------------------------------------")

descuento = input("Elije de que app tendras 20% descuento:\n -Pedidos Ya\n -Uber eats\n -Rappi ").capitalize()


cliente2 = Cliente_black(id, "Morena", "rioja este", 12345, descuento)

print(cliente2)

print("--------------------------------------------------")

print(cliente2.membresia())

print("--------------------------------------------------")

print(cliente2.comprar_articulo())

print("--------------------------------------------------")

monto_compra = float(input("Ingrese el monto de su compra: $ "))

print(cliente2.puntos(monto_compra))
