import unittest
import pandas as pd
from sklearn.cluster import KMeans
from app.features import train_model

class TestEngineeringFunctions(unittest.TestCase):

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
