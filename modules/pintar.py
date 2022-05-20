import pandas as pd
import matplotlib.pyplot as plt

def obtener_datos():
    datos = pd.read_csv('metro - Hoja 1.csv')
    return datos

def obtener_linea(df, linea):
    plt.axis('off')
    x = df[df['Linea'] == linea][1]
    y = df[df['Linea'] == linea][0]
    color = df[df['Linea'] == linea]['Color'].iloc[0]
    return plt.plot(x, y, color=color, marker='*')

def imprimir_mapa():
    datos = obtener_datos()
    coordenadas = datos['Coordenadas'].str.split(',', expand=True)
    df_new = pd.concat([datos, coordenadas] , axis=1)
    df_new[0] = df_new[0].astype(float)
    df_new[1] = df_new[1].astype(float)

    obtener_linea(df_new, 'B')
    obtener_linea(df_new, '1')
    obtener_linea(df_new, '2')

    return plt.show()

def imprimir_menu():
    print("\nEscoge la opción que gustas.")
    print(" A Imprimir mapa del metro")
    print(" B imprimir las estaciones del metro")
    print(" C Calcular una ruta ")
    print(" D Salir")


def imprimir_estaciones():
    datos = obtener_datos()

    estaciones = datos['Linea'].unique()

    for name in estaciones:
        print("+" + "-" *  10)
        print("| Linea " + name + (" " * 7))
        print("+" + "-" *  10)
        for estacion in datos[datos['Linea'] == name]['Estacion'].values:
            print("| " + estacion)

    