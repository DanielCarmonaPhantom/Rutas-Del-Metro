## Información relacionada a la busqueda del algoritmo fue hecha por Victor Sanz de su canal de youtube
## Podemos encontrar una explicación en su video https://www.youtube.com/watch?v=w84P5Coifek

import pandas as pd
import networkx as nx
from datetime import datetime, timedelta

def obtener_datos_distancias():
    df = pd.read_csv('Distancias - Hoja 1.csv')
    df['Origen'] = df['Origen'].str.lower()
    df['Destino'] = df['Destino'].str.lower()
    return df

def sacar_estaciones_destino(Origen, Destino):
    df = obtener_datos_distancias()
    METRO = nx.from_pandas_edgelist(df,source='Origen',target='Destino',edge_attr='Longitud')
    djk_path= nx.dijkstra_path(METRO, source=Origen, target=Destino, weight='Longitud de interestación')
    return(djk_path)
    
def obtener_tiempo(lista_recorrido):
    df = obtener_datos_distancias()
    curr = datetime.now()
    distancia = []
    for i in range(len(lista_recorrido)-2):
        distancia.append(int(df[((df['Origen'] == lista_recorrido[i])|(df['Origen'] == lista_recorrido[i+1])) & ((df['Origen'] == lista_recorrido[i])|(df['Origen'] == lista_recorrido[i+1]))]['Longitud'].values[0].replace(',','')))
    distancia_total = sum(distancia)
    minutos = (distancia_total * 60)/25400
    new_datetime = timedelta(minutes=minutos)
    lapso = curr + new_datetime
    return curr.strftime('%H:%M'), lapso.strftime('%H:%M'), int(minutos)

