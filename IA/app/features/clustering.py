import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from app.features.retention import calculate_retention_time


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