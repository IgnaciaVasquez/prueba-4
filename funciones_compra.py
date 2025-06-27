
compra = [{
    'nombre': 'nombre',
    'codigo': 'EstoyEnListaDeReserva'
}]
stock = 20
def comprar_entrada():
    nombre = input("Ingrese su nombre y apellido\n> ")
    if nombre not in compra:
        print("Nombre ingresado correctamente!")
        compra.append
    else:
        print("Nombre ya ingresado!")
        return
    
    codigo = input("Ingrese código\n> ")
    if codigo == compra[{'codigo'}]:
        global stock
        stock -= 1
    else:
        print("Código incorrecto!")
        return
    