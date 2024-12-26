import pandas as pd

def calculate_retention_time(df: pd.DataFrame) -> pd.DataFrame:
    df['Data_de_Criacao'] = pd.to_datetime(df['Data_de_Criacao'])
    df['Data_de_Saida'] = pd.to_datetime(df['Data_de_Saida'])
    df['Tempo_de_Permanencia'] = ((df['Data_de_Saida'] - df['Data_de_Criacao']).dt.days // 30).fillna(0).astype(int)

    return df