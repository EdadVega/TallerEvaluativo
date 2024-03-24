import string
import random


inventario = []

ubicaciones = {"A": 0, "B": 0, "C": 0, "D": 0}
def generar_id():
    ids_existentes = [producto["id"] for producto in inventario]
    while True:
        id_nuevo = random.randint(1, 100)
        if id_nuevo not in ids_existentes:
            return id_nuevo

def registrar_producto():
    
    try:
        id_existente = None
        referenciaprod = None
        
        nombre = input("Ingrese el nombre del producto: ")
        for producto in inventario:
            if producto["nombre"] == nombre:
                id_existente = producto["id"]
                referenciaprod = producto["referencia"]
                print(f"El producto '{nombre}' ya existe en el inventario con ID {id_existente}.")
                break
            
        precio = float(input("Ingrese el precio unitario del producto: "))

        descripcion = input("Ingrese la descripción del producto: ")
        casa = input("Ingrese la casa a la que pertenece el producto: ")
        
        if referenciaprod is not None:
            referencia = referenciaprod
        else: 
            referencia = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        
        
        pais_origen = input("Ingrese el país de origen del producto: ")
        unidades = int(input("Ingrese el número de unidades compradas: "))
        garantia = input("¿El producto tiene garantía extendida?  si/no: ").lower() == "si"

        if id_existente is not None:
            id_nuevo = id_existente
        else:
            id_nuevo = generar_id()
        
        ubicacion = "A"
        for ubicacion_actual in ["A", "B", "C", "D"]:
            if ubicaciones[ubicacion_actual] + unidades <= 50:
                ubicacion = ubicacion_actual
                ubicaciones[ubicacion_actual] += unidades
                break
        else:
            print(f"Superaste el máximo de almacenamiento de la ubicación (50 productos). \nEspacio ocupado: A: {ubicaciones['A']}, B: {ubicaciones['B']}, C: {ubicaciones['C']}, D: {ubicaciones['D']}")
            return
        nuevo_producto = {
            
            "id": id_nuevo,
            "nombre": nombre,
            "precio": precio,
            "ubicacion": ubicacion,
            "descripcion": descripcion,
            "casa": casa,
            "referencia": referencia,
            "pais_origen": pais_origen,
            "unidades": unidades,
            "garantia": garantia
        }
        inventario.append(nuevo_producto)
        print(f"Producto registrado con ID: {id_nuevo}")
        print(f"Guardado en ubicación: {ubicacion} (Espacio ocupado en: A: {ubicaciones['A']}, B: {ubicaciones['B']}, C: {ubicaciones['C']}, D: {ubicaciones['D']})")
    except ValueError:
        print("Se experaba un  valor numero para precio y unidades.")
    except Exception as e:
        print(print(f"Guardado en ubicación: {ubicacion} (Espacio ocupado en: A: {ubicaciones['A']}, B: {ubicaciones['B']}, C: {ubicaciones['C']}, D: {ubicaciones['D']})"),e)


def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario:")
        for producto in inventario:
            print(f" \n ID: {producto['id']}, \nNombre: {producto['nombre']}, \nPrecio: {producto['precio']}, \nUbicación: {producto['ubicacion']}, \nDescripción: {producto['descripcion']}, \nCasa: {producto['casa']}, \nReferencia: {producto['referencia']}, \nPaís de origen: {producto['pais_origen']}, \nUnidades: {producto['unidades']}, \nGarantía: {producto['garantia']} \n ----------- \n")

def buscar_producto():
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    productos_encontrados = [producto for producto in inventario if producto["nombre"].lower() == nombre_buscar.lower()]
    if not productos_encontrados:
        print(f"No se encontró ningún producto con el nombre '{nombre_buscar}'.")
    else:
        for producto in productos_encontrados:
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Descripción: {producto['descripcion']}, Ubicación: {producto['ubicacion']}")


def modificar_unidades():
    nombre_modificar = input("Ingrese el nombre del producto a modificar: ")
    productos_encontrados = [producto for producto in inventario if producto["nombre"].lower() == nombre_modificar.lower()]
    if not productos_encontrados:
        print(f"No se encontró ningún producto con el nombre '{nombre_modificar}'.")
    else:
        for producto in productos_encontrados:
            nuevas_unidades = int(input(f"Ingrese el nuevo número de unidades para '{producto['nombre']}' (actual: {producto['unidades']}): "))
            if nuevas_unidades <= producto["unidades"]:
                producto["unidades"] = nuevas_unidades
                print(f"Las unidades de '{producto['nombre']}' se han actualizado a {nuevas_unidades}.")
            else:
                print("El número de unidades no puede ser mayor al número inicial.")
                
def eliminar_producto():
    nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ")
    productos_encontrados = [producto for producto in inventario if producto["nombre"].lower() == nombre_eliminar.lower()]
    if not productos_encontrados:
        print(f"No se encontró ningún producto con el nombre '{nombre_eliminar}'.")
    else:
        for producto in productos_encontrados:
            confirmacion = input(f"¿Está seguro de eliminar '{producto['nombre']}'? (s/n): ").lower()
            if confirmacion == "s":
                inventario.remove(producto)
                print(f"El producto '{producto['nombre']}' ha sido eliminado del inventario.")
            else:
                print(f"No se eliminó el producto '{producto['nombre']}'.")

while True:
    print("\nMenú de opciones:")
    print("1. Registrar un producto")
    print("2. Buscar y mostrar todos los productos")
    print("3. Buscar un producto por nombre")
    print("4. Modificar el número de unidades de un producto")
    print("5. Eliminar un producto del inventario")
    print("6. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        registrar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        modificar_unidades()
    elif opcion == "5":
        eliminar_producto()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")