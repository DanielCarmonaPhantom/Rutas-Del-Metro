from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt



def obtener_linea(df, linea):
    plt.axis('off')
    x = df[df['Linea'] == linea][1]
    y = df[df['Linea'] == linea][0]
    
    color = df[df['Linea'] == linea]['Color'].iloc[0]
    # return plt.plot(x, y, color=color, marker='*')
    plt.legend(loc = 'upper right')
    plt.title('Metro de la CDMX')
    return plt.plot(x, y,  color=color,marker='*', label=linea)

def imprimir_mapa(datos):
    coordenadas = datos['Coordenadas'].str.split(',', expand=True)
    df_new = pd.concat([datos, coordenadas] , axis=1)
    df_new[0] = df_new[0].astype(float)
    df_new[1] = df_new[1].astype(float)


    obtener_linea(df_new, '1')
    obtener_linea(df_new, '2')
    obtener_linea(df_new, '3')
    obtener_linea(df_new, '4')
    obtener_linea(df_new, '5')
    obtener_linea(df_new, '6')
    obtener_linea(df_new, '7')
    obtener_linea(df_new, '8')
    obtener_linea(df_new, '9')
    obtener_linea(df_new, 'A')
    obtener_linea(df_new, 'B')
    obtener_linea(df_new, '12')

    return plt.show()

def imprimir_menu():
    print("\nEscoge la opción que gustas.")
    print(" A Imprimir mapa del metro")
    print(" B imprimir las estaciones del metro")
    print(" C Calcular una ruta ")
    print(" D Salir")


def imprimir_estaciones(datos):
    estaciones = datos['Linea'].unique()

    for name in estaciones:
        print("+" + "-" *  10)
        print("| Linea " + name + (" " * 7))
        print("+" + "-" *  10)
        for estacion in datos[datos['Linea'] == name]['Estacion'].values:
            print("| " + estacion)

def pintar_info(Origen, Destino, tiempo1, tiempo2, minutos):
    print("\n" + "-"*20)
    print(f'{tiempo1}-{tiempo2}      {minutos} min')
    print(f'\n{Origen.title()} > {Destino.title()}')
    print(f'{tiempo1} {Origen.title()}')
    print(f'{tiempo2} {Destino.title()}')
    print("-"*20 + "\n")

def pintar_trayectoria(lista_estaciones, tiempo_entre_estacion, lineas):
    for i in range(len(lista_estaciones)):
        cantidad_transbordes = len(lineas[lineas['Estacion'] == lista_estaciones[i]][['Estacion','Linea']].values)
        if cantidad_transbordes > 0:
            transbordes = ", ".join(lineas[lineas['Estacion'] == lista_estaciones[i]]['Linea'].values)
            print(f'{tiempo_entre_estacion[i]:4} * {lista_estaciones[i].title()}')
            # print(f'      | Líneas: {transbordes}')
            print(f'      |')
    