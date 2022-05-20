import pandas as pd
import matplotlib.pyplot as plt

def obtener_linea(df, linea):
    plt.axis('off')
    x = df[df['Linea'] == linea][1]
    y = df[df['Linea'] == linea][0]
    color = df[df['Linea'] == linea]['Color'].iloc[0]
    return plt.plot(x, y, color=color)

def imprimir_mapa():
    datos = pd.read_csv('metro - Hoja 1.csv')
    coordenadas = datos['Coordenadas'].str.split(',', expand=True)
    df_new = pd.concat([datos, coordenadas] , axis=1)
    df_new[0] = df_new[0].astype(float)
    df_new[1] = df_new[1].astype(float)

    obtener_linea(df_new, 'B')
    obtener_linea(df_new, '1')

    return plt.show()