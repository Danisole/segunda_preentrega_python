
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
        break
    
    else:
        print("La opcion que ingresaste es incorrecta")    




