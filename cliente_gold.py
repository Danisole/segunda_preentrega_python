from cliente_class import Cliente_gold
import random

id=random.randrange(100, 500)

tu_app = input("Elije una app y la suscripcion sera bonificada: ").lower()

cliente3 = Cliente_gold(id, "Morena", "rioja este", 12345, tu_app)

print(cliente3)

print(cliente3.comprar_articulo())

print(cliente3.membresia())

monto_compra = float(input("Ingrese el monto de su compra: $ "))

print(cliente3.puntos(monto_compra))
