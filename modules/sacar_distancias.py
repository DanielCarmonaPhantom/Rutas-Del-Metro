import pandas as pd
import networkx as nx

def sacar_estaciones_destino(Origen, Destino):
    df = pd.read_csv('Distancias - Hoja 1.csv')
    df['Origen'] = df['Origen'].str.lower()
    df['Destino'] = df['Destino'].str.lower()
    METRO = nx.from_pandas_edgelist(df,source='Origen',target='Destino',edge_attr='Longitud')
    djk_path= nx.dijkstra_path(METRO, source=Origen, target=Destino, weight='Longitud de interestación')
    print(djk_path)
    