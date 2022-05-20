from modules.pintar import imprimir_mapa, imprimir_menu, imprimir_estaciones
from modules.sacar_distancias import sacar_estaciones_destino

def main():
    

    opcion = 'Z'

    while opcion != 'D':
        imprimir_menu()

        opcion = input("\nIngresa tu opción: ")
        if opcion == 'A':
            imprimir_mapa()
        elif opcion == 'B':
            imprimir_estaciones()
        elif opcion == 'C':
            origen = input('Escribe la estación Origen: ').lower()
            destino = input('Escribe la estación Destino: ').lower()
            sacar_estaciones_destino(origen,destino)

    


if __name__ == '__main__':
    main()