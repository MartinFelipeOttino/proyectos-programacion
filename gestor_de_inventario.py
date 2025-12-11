# =======================================================================================================
# FUNCIONES
# =======================================================================================================


def formato_moneda(valor):
    temp = "{:,.2f}".format(valor)
    return temp.replace(",", "X").replace(".", ",").replace("X", ".")

def agregar_producto(inventario):
    while True:
        nombre = input("Ingrese el nombre del nuevo producto (deje en blanco para salir): ").lower()
        if nombre == "":
            print("Volviendo al menú principal...")
            break

        try:
            precio = float(input("Ingrese el precio: "))
            cantidad = int(input("Ingrese la cantidad en stock: "))
            if precio < 0:
                print("Error: El precio NO puede ser negativo.")
                continue
            if cantidad <= 0:
                print("Error: La cantidad mínima es 1.")
                continue

            producto = {"NOMBRE": nombre, "PRECIO": precio, "CANTIDAD": cantidad}
            inventario.append(producto)
            print(f"Producto '{nombre.title()}' agregado correctamente.\n")

        except ValueError:
            print("Error: Ingrese valores numéricos válidos para precio y cantidad.\n")

def mostrar_inventario(inventario):
    if not inventario:
        print("INVENTARIO VACIO")
    else:
        print("-" * 20, "INVENTARIO ACTUAL", "-" * 20)
        for indice, producto in enumerate(inventario, 1):
            print(indice, "=", producto)

def eliminar_producto(inventario):
    while True:
        if not inventario:
            print("No hay productos para eliminar")
            break
        for indice, producto in enumerate(inventario, 1):
            print(indice, "=", producto)
        entrada = input("ELiga el producto a eliminar (deje en blanco para salir): ")
        if entrada == "":
            print("Volviendo al menú principal...")
            break

        try:
            indice = int(entrada) - 1
            if indice < 0 or indice >= len(inventario):
                print("Producto no encontrado")
                continue
            inventario.pop(indice)
            if indice == 0:
                print("No hay productos para eliminar", "Volviendo al menú principal...", sep='\n')
                break
        except ValueError:
            print("Error: Ingrese un valor numérico válido.\n")


def generar_archivo_csv(inventario):
    valor_total = 0

    if len(inventario) == 0:
        print("No hay datos para generar el archivo")
        return

    for producto in inventario:
        valor_producto = producto["PRECIO"] * producto["CANTIDAD"]

        valor_total += valor_producto

    with open("inventario.csv", "w", encoding="utf-8", newline='') as archivo:
        archivo.write("Producto;Precio;Cantidad;Valor_Total\n")
        for producto in inventario:
            valor = producto["PRECIO"] * producto["CANTIDAD"]
            precio_str = formato_moneda(producto["PRECIO"])
            valor_str = formato_moneda(valor)
            archivo.write('"' + producto["NOMBRE"] + '";"' + precio_str + '";"' +
                          str(producto["CANTIDAD"]) + '";"' + valor_str + '"\n')

        total_str = formato_moneda(valor_total)
        archivo.write("\nTOTAL DEL INVENTARIO" + '";"' + '";"' + '";"' + total_str + '"\n')

    print("Archivo 'inventario.csv' creado exitosamente.")


# =======================================================================================================
# PROGRAMA PRINCIPAL
# =======================================================================================================


inventario = []

print("-" * 60, "LISTA DE OPCIONES", "-" * 60, "1. Agregar nuevo producto al inventario",
      "2. Ver listado completo de productos", "3. Eliminar un producto",
      "4. Crear archivo", "5. Salir del sistema.", sep="\n")

while True:
    try:
        print("-" * 60)
        opcion = input("Ingrese su opción: ")

        if opcion < '1' or opcion > '6':
            print("Opción no válida. Por favor ingrese 1, 2, 3, 4 o 5")
            continue
        elif opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            mostrar_inventario(inventario)
        elif opcion == '3':
            eliminar_producto(inventario)
        elif opcion == '4':
            generar_archivo_csv(inventario)
        elif opcion == '5':
            print("ADIOS")
            break

    except ValueError:
        print("Valor NO válido")
        continue
    except:
        print("Error inesperado")
        break