import unittest
import pandas as pd
from sklearn.cluster import KMeans
from datetime import datetime
from app.features.engineering import calculate_retention_time, train_model, make_predictions

class TestEngineeringFunctions(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.df = pd.DataFrame({
            'Nome': ['Cliente1', 'Cliente2'],
            'Data_de_Criacao': ['2022-01-01', '2022-06-01'],
            'Data_de_Saida': ['2023-01-01', '2023-06-01'],
            'Valor_Consumido': [100, 200]
        })
        self.df['Data_de_Criacao'] = pd.to_datetime(self.df['Data_de_Criacao'])
        self.df['Data_de_Saida'] = pd.to_datetime(self.df['Data_de_Saida'])

    def test_calculate_retention_time(self):
        df_result = calculate_retention_time(self.df.copy())
        self.assertIn('Tempo_de_Permanencia', df_result.columns)
        self.assertEqual(df_result['Tempo_de_Permanencia'].iloc[0], 12)
        self.assertEqual(df_result['Tempo_de_Permanencia'].iloc[1], 12)

    def test_train_model(self):
        self.df = pd.DataFrame({
            'Nome': ['Cliente1', 'Cliente2', 'Cliente3'],
            'Data_de_Criacao': ['2022-01-01', '2022-06-01', '2022-03-01'],
            'Data_de_Saida': ['2023-01-01', '2023-06-01', '2023-03-01'],
            'Valor_Consumido': [100, 200, 150]
        })
        self.df['Data_de_Criacao'] = pd.to_datetime(self.df['Data_de_Criacao'])
        self.df['Data_de_Saida'] = pd.to_datetime(self.df['Data_de_Saida'])

        kmeans, df_result = train_model(self.df.copy())
        self.assertIsInstance(kmeans, KMeans)
        self.assertIn('Cluster', df_result.columns)
        self.assertEqual(len(df_result['Cluster'].unique()), 2)

    def test_make_predictions(self):
        self.df = pd.DataFrame({
            'Nome': ['Cliente1', 'Cliente2', 'Cliente3'],
            'Data_de_Criacao': ['2022-01-01', '2022-06-01', '2022-03-01'],
            'Data_de_Saida': ['2023-01-01', '2023-06-01', '2023-03-01'],
            'Valor_Consumido': [100, 200, 150]
        })
        self.df['Data_de_Criacao'] = pd.to_datetime(self.df['Data_de_Criacao'])
        self.df['Data_de_Saida'] = pd.to_datetime(self.df['Data_de_Saida'])

        kmeans, _ = train_model(self.df.copy())
        df_new = pd.DataFrame({
            'Nome': ['Cliente4'],
            'Data_de_Criacao': ['2022-01-01'],
            'Valor_Consumido': [150]
        })
        df_new['Data_de_Criacao'] = pd.to_datetime(df_new['Data_de_Criacao'])
        df_result = make_predictions(kmeans, df_new)
        self.assertIn('Cluster_Predito', df_result.columns)
        self.assertEqual(df_result['Nome'].iloc[0], 'Cliente4')