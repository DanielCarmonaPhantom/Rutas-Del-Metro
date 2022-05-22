## Información relacionada a la busqueda del algoritmo fue hecha por Victor Sanz de su canal de youtube
## Podemos encontrar una explicación en su video https://www.youtube.com/watch?v=w84P5Coifek

import pandas as pd
import networkx as nx
from datetime import datetime, timedelta

def obtener_datos():
    datos = pd.read_csv('metro - Hoja 1.csv')
    datos['Estacion'] = datos['Estacion'].str.lower()
    return datos

def obtener_datos_distancias():
    df = pd.read_csv('Distancias - Hoja 1.csv')
    df['Origen'] = df['Origen'].str.lower()
    df['Destino'] = df['Destino'].str.lower()
    return df

def sacar_estaciones_destino(Origen, Destino):
    df = obtener_datos_distancias()
    METRO = nx.from_pandas_edgelist(df,source='Origen',target='Destino',edge_attr='Longitud')
    try:
        djk_path= nx.dijkstra_path(METRO, source=Origen, target=Destino, weight='Longitud de interestación')
        return(djk_path)
    except:
        print("No encontramos ese origen-destino")

def obtener_transbordes(lista_recorrido):
    pass

    
    
def obtener_tiempo(lista_recorrido):
    df = obtener_datos_distancias()
    lineas = obtener_datos()
    curr = datetime.now()
    distancia = []
    tiempo_entre_estacion = []
    estacion_pasado = ""
    estacion_actual = ""

    for i in range(len(lista_recorrido)-2):
        try:
            longitud = int(df[(df['Origen'] == lista_recorrido[i]) & (df['Destino'] == lista_recorrido[i+1])]['Longitud'].values[0].replace(',',''))
        except:
            longitud = int(df[(df['Origen'] == lista_recorrido[i+1]) & (df['Destino'] == lista_recorrido[i])]['Longitud'].values[0].replace(',',''))
        
        minutos = (longitud * 60)/25400  


        try:
            estacion_actual = lineas[lineas['Estacion'] == lista_recorrido[i]]['Linea'].values[0] 
            if estacion_actual == estacion_pasado:
                pass
            else:
                estacion_pasado = estacion_actual
                minutos = minutos + 5
        except:
            print(f'En {lista_recorrido[i]} hubo pedo')

        distancia.append(minutos)
        minutos_acumulados = sum(distancia)
        new_datetime = timedelta(minutes=minutos_acumulados)
        lapso = curr + new_datetime
        tiempo_entre_estacion.append(lapso.strftime('%H:%M'))
    try:
        longitud = int(df[(df['Origen'] == lista_recorrido[-1]) & (df['Destino'] == lista_recorrido[-2])]['Longitud'].values[0].replace(',',''))
    except:
        longitud = int(df[(df['Origen'] == lista_recorrido[-2]) & (df['Destino'] == lista_recorrido[-1])]['Longitud'].values[0].replace(',',''))
    
    minutos = (longitud * 60)/25400        
    distancia.append(minutos)
    distancia_total = sum(distancia)
    new_datetime = timedelta(minutes=distancia_total)
    lapso = curr + new_datetime
    tiempo_entre_estacion.append(lapso.strftime('%H:%M'))
    return curr.strftime('%H:%M'), lapso.strftime('%H:%M'), int(distancia_total), [curr.strftime('%H:%M')] + tiempo_entre_estacion


