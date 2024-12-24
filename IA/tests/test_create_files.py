import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import os
from app.scripts.create_files import create_file

class TestCreateFile(unittest.TestCase):

    @patch('app.scripts.create_files.pd.DataFrame.to_excel')
    @patch('app.scripts.create_files.os.path.join')
    @patch('app.scripts.create_files.os.path.dirname')
    @patch('app.scripts.create_files.os.path.abspath')
    def test_create_file_with_data(self, mock_abspath, mock_dirname, mock_join, mock_to_excel):
        mock_abspath.return_value = '/fake/path'
        mock_dirname.side_effect = ['/fake', '/fake']
        mock_join.side_effect = [
            '/fake/data',
            '/fake/data/Resultado_Churn.xlsx'
        ]

        df = pd.DataFrame({
            'Nome': ['Cliente1', 'Cliente2'],
            'Valor_Consumido': [100, 200]
        })

        create_file(df)

        mock_abspath.assert_called_once()
        self.assertEqual(mock_dirname.call_count, 2)
        mock_dirname.assert_any_call('/fake/path')
        self.assertEqual(mock_join.call_count, 2)
        mock_join.assert_any_call('/fake', 'data')
        mock_join.assert_any_call('/fake/data', 'Resultado_Churn.xlsx')
        mock_to_excel.assert_called_once_with('/fake/data/Resultado_Churn.xlsx', index=False)

    @patch('builtins.print')
    def test_create_file_empty_dataframe(self, mock_print):
        df = pd.DataFrame()

        create_file(df)

        mock_print.assert_called_once_with("O DataFrame está vazio.")