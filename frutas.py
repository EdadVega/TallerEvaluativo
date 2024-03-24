def ingresar_frutas():
    n = int(input("Ingrese la cantidad de frutas para el salpicón: "))
    frutas = []
    for i in range(n):
        id_fruta = i + 1
        nombre_fruta = input(f"Ingrese el nombre de la fruta {id_fruta}: ")
        precio_unitario = float(input(f"Ingrese el precio unitario de {nombre_fruta}: "))
        cantidad = int(input(f"Ingrese la cantidad de {nombre_fruta}: "))
        fruta = {"id": id_fruta, "nombre": nombre_fruta, "precio_unitario": precio_unitario, "cantidad": cantidad}
        frutas.append(fruta)
    return frutas

def calcular_costo_total(frutas):
    costo_total = 0
    for fruta in frutas:
        costo_fruta = fruta["precio_unitario"] * fruta["cantidad"]
        costo_total += costo_fruta
    return costo_total

def ordenar_frutas_por_costo(frutas):
    frutas_ordenadas = sorted(frutas, key=obtener_costo_total_fruta, reverse=True)
    return frutas_ordenadas

def obtener_costo_total_fruta(fruta):
    return fruta["precio_unitario"] * fruta["cantidad"]

def encontrar_fruta_mas_barata(frutas):
    fruta_mas_barata = frutas[0]
    for fruta in frutas:
        if fruta["precio_unitario"] < fruta_mas_barata["precio_unitario"]:
            fruta_mas_barata = fruta
    return fruta_mas_barata

def respuesta_general():
    frutas = ingresar_frutas()
    costo_total = calcular_costo_total(frutas)
    print(f"El costo total del salpicón es: ${costo_total}")
    frutas_ordenadas = ordenar_frutas_por_costo(frutas)
    print("Frutas ordenadas de mayor a menor costo:")
    for fruta in frutas_ordenadas:
        print(f"ID: {fruta['id']}, Nombre: {fruta['nombre']}, Precio unitario: ${fruta['precio_unitario']}, Cantidad: {fruta['cantidad']}")
    fruta_mas_barata = encontrar_fruta_mas_barata(frutas)
    print(f"La fruta más barata es: {fruta_mas_barata['nombre']}, con un precio unitario de ${fruta_mas_barata['precio_unitario']}")

respuesta_general()