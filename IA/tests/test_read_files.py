import unittest
from unittest.mock import patch
import pandas as pd
from app.scripts.read_files import read_training_data, read_testing_data

class TestReadFiles(unittest.TestCase):

    @patch('app.scripts.read_files.pd.read_excel')
    def test_read_training_data(self, mock_read_excel):
        mock_df = pd.DataFrame({
            'Nome': ['Cliente1', 'Cliente2'],
            'Data_de_Criacao': ['2023-01-01', '2023-01-02'],
            'Data_de_Saida': ['2023-02-01', '2023-02-02'],
            'Valor_Consumido': [100, 200]
        })
        mock_read_excel.return_value = mock_df

        file_path = '/fake/path/treinamento.xlsx'

        df = read_training_data(file_path)

        mock_read_excel.assert_called_once_with(file_path, usecols=['Nome', 'Data_de_Criacao', 'Data_de_Saida', 'Valor_Consumido'])
        pd.testing.assert_frame_equal(df, mock_df)

    @patch('app.scripts.read_files.pd.read_excel')
    def test_read_testing_data(self, mock_read_excel):
        mock_df = pd.DataFrame({
            'Nome': ['Cliente1', 'Cliente2'],
            'Data_de_Criacao': ['2023-01-01', '2023-01-02'],
            'Valor_Consumido': [100, 200]
        })
        mock_read_excel.return_value = mock_df

        file_path = '/fake/path/teste.xlsx'

        df = read_testing_data(file_path)

        mock_read_excel.assert_called_once_with(file_path, usecols=['Nome', 'Data_de_Criacao', 'Valor_Consumido'])
        pd.testing.assert_frame_equal(df, mock_df)