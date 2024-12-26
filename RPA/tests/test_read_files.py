import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from app.scripts.read_files import run_read_files


class TestRunReadFiles(unittest.TestCase):

    @patch('app.scripts.read_files.create_file')
    @patch('app.scripts.read_files.run_scraper')
    @patch('app.scripts.read_files.pd.read_excel')
    @patch('app.scripts.read_files.os.path.join')
    @patch('app.scripts.read_files.os.path.dirname')
    @patch('app.scripts.read_files.os.path.abspath')
    def test_run_read_files(self, mock_abspath, mock_dirname, mock_join, mock_read_excel, mock_run_scraper,
                            mock_create_file):

        mock_abspath.return_value = '/fake/path'
        mock_dirname.return_value = '/fake'
        mock_join.side_effect = lambda *args: '/'.join(args)

        mock_df = pd.DataFrame({
            'Partida': ['Local1', 'Local2'],
            'Destino': ['Destino1', 'Destino2']
        })
        mock_read_excel.return_value = mock_df
        mock_run_scraper.side_effect = [['Linha1', 'Linha2'], ['Linha3', 'Linha4']]

        run_read_files()

        mock_abspath.assert_called_once()
        self.assertEqual(mock_dirname.call_count, 2)
        mock_join.assert_any_call('/fake', 'data')
        mock_join.assert_any_call('/fake/data', 'Onibus_Rota.xlsx')
        mock_read_excel.assert_called_once_with('/fake/data/Onibus_Rota.xlsx', usecols=['Partida', 'Destino'])
        self.assertEqual(mock_run_scraper.call_count, 2)
        mock_run_scraper.assert_any_call('Local1', 'Destino1')
        mock_run_scraper.assert_any_call('Local2', 'Destino2')
        self.assertEqual(mock_create_file.call_count, 2)
        mock_create_file.assert_any_call(['Linha1', 'Linha2'], 'Linhas_Local1_Destino1.xlsx')
        mock_create_file.assert_any_call(['Linha3', 'Linha4'], 'Linhas_Local2_Destino2.xlsx')