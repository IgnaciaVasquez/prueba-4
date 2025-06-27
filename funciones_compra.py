
compra = []
stock = 20

def reservar_producto(producto, cantidad):
    global stock
    nombre = input("Introduce tu nombre: ")
    if cantidad <= stock:
        stock -= cantidad
        compra.append((producto, cantidad, nombre))
        print(f"Producto reservado: {producto}, Cantidad: {cantidad}, Nombre: {nombre}")
    else:
        print(f"No hay suficiente stock para reservar {cantidad} unidades de {producto}. Stock actual: {stock}")

def mostrar_reservas():
    nombre = input("Introduce el nombre para buscar reservas: ")
    reservas_encontradas = [reserva for reserva in compra if reserva[2] == nombre]
    if reservas_encontradas:
        print(f"Reservas encontradas para {nombre}:")
        for reserva in reservas_encontradas:
            print(f"Producto: {reserva[0]}, Cantidad: {reserva[1]}")
    else:
        print(f"No se encontraron reservas para {nombre}.")

def cancelar_reserva(producto, cantidad):
    global stock
    nombre = input("Introduce tu nombre para cancelar la reserva: ")
    reservas_a_cancelar = [reserva for reserva in compra if reserva[0] == producto and reserva[1] == cantidad and reserva[2] == nombre]
    if reservas_a_cancelar:
        for reserva in reservas_a_cancelar:
            compra.remove(reserva)
            stock += cantidad
            print(f"Reserva cancelada: Producto: {reserva[0]}, Cantidad: {reserva[1]}, Nombre: {reserva[2]}")
    else:
        print(f"No se encontraron reservas para cancelar: Producto: {producto}, Cantidad: {cantidad}, Nombre: {nombre}")
        print("Asegúrate de que el nombre y los detalles de la reserva sean correctos.")

def mostrar_stock():
    print(f"Stock actual: {stock} unidades disponibles.")
