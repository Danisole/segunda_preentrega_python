from cliente_class import Cliente
import random

id=random.randrange(100, 500)

cliente1 = Cliente(id, "santiago", "san luis este", 1234)
print(cliente1)

print("--------------------------------------------------")

cliente1.comprar_articulo()

print("--------------------------------------------------")

cliente1.membresia()