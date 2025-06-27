import os, msvcrt
from funciones_compra import *
menu = '''TOTEM AUTOATENCIÓN RESERVA STRIKE
1.- Reservar zapatillas
2.- Buscar zapatillas reservadas.
3.- Cancelar reserva de zapatillas.
4.- Salir
'''
while True:
    os.system('cls')
    print(menu)
    opc= input("Ingrese una opción del menú\n> ")
    os.system('cls')

    if opc == "1":
        reservar_producto("Zapatillas Strike", 1)
        mostrar_stock()
    elif opc == "2":
        mostrar_reservas()
        mostrar_stock
    elif opc == "3":
        cancelar_reserva("Zapatillas Strike", 1)
    elif opc == "4":
        print("Gracias por visitar el sitio web!")
        break
    else:
        print("Debe ingresar una opción válida!!")
    msvcrt.getch
    input("Presione una tecla para continuar...")
