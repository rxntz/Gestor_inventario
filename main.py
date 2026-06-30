from datos import inventario

while True:
    print("------- MENU ------")
    print("1. Agregar")
    print("2. Ver todo")
    print("3. Calcular total")
    print("4. Salir")

    opcion = input("Elige una opcion: ")

    if opcion== "1":
        nombre= input("Nombre: ")
        precio= float(input("Precio: "))
        cantidad= int(input("Cantidad:"))
        producto= {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        inventario.append(producto)
        print("agregado")

    elif opcion == "2":
        print("----- LISTA ----")
        for item in inventario:
            print("Producto:", item['nombre'], " Precio:", item['precio'], " Stock:", item['cantidad'])

    elif opcion == "3":
        total = 0
        for item in inventario:
            total= total + (item["precio"] * item["cantidad"])
        print("El valor total es:", total)

    elif opcion == "4":
        print("salir")
        break
    else:
        print("ingrese otra opcion!")