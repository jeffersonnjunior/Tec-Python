import unittest
import pandas as pd
from app.features import train_model, make_predictions

class TestEngineeringFunctions(unittest.TestCase):

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