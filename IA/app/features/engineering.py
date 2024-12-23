import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from datetime import datetime

def calculate_retention_time(df: pd.DataFrame) -> pd.DataFrame:
    df['Data_de_Criacao'] = pd.to_datetime(df['Data_de_Criacao'])
    df['Data_de_Saida'] = pd.to_datetime(df['Data_de_Saida'])
    df['Tempo_de_Permanencia'] = ((df['Data_de_Saida'] - df['Data_de_Criacao']).dt.days // 30).fillna(0).astype(int)

    return df


def train_model(df: pd.DataFrame) -> tuple[KMeans, pd.DataFrame]:
    df = calculate_retention_time(df)

    X = df[['Tempo_de_Permanencia', 'Valor_Consumido']]

    kmeans = KMeans(n_clusters=2, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)

    X_train, X_test, y_train, y_test = train_test_split(X, df['Cluster'], test_size=0.2, random_state=42)

    kmeans.fit(X_train)

    y_pred = kmeans.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f'Acurácia de agrupamento: {accuracy}')

    return kmeans, df


def make_predictions(kmeans: KMeans, df: pd.DataFrame) -> pd.DataFrame:
    hoje = pd.Timestamp(datetime.now())
    df['Data_de_Criacao'] = pd.to_datetime(df['Data_de_Criacao'])
    df['Tempo_de_Permanencia'] = ((hoje - df['Data_de_Criacao']).dt.days // 30).fillna(0).astype(int)

    X_new = df[['Tempo_de_Permanencia', 'Valor_Consumido']]
    predictions = kmeans.predict(X_new)

    df['Cluster_Predito'] = predictions
    print(df.head())

    return df[['Nome', 'Tempo_de_Permanencia', 'Cluster_Predito']]