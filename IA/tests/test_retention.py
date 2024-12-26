import unittest
import pandas as pd
from app.features import calculate_retention_time

class TestEngineeringFunctions(unittest.TestCase):

    def setUp(self):
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