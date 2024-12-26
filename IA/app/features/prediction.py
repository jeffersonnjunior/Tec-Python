import pandas as pd
from sklearn.cluster import KMeans
from datetime import datetime

def make_predictions(kmeans: KMeans, df: pd.DataFrame) -> pd.DataFrame:
    hoje = pd.Timestamp(datetime.now())
    df['Data_de_Criacao'] = pd.to_datetime(df['Data_de_Criacao'])
    df['Tempo_de_Permanencia'] = ((hoje - df['Data_de_Criacao']).dt.days // 30).fillna(0).astype(int)

    X_new = df[['Tempo_de_Permanencia', 'Valor_Consumido']]
    predictions = kmeans.predict(X_new)

    df['Cluster_Predito'] = predictions
    print(df.head())

    return df[['Nome', 'Tempo_de_Permanencia', 'Cluster_Predito']]