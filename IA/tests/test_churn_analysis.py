import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from app.pipelines.churn_analysis import run_churn_analysis

class TestChurnAnalysis(unittest.TestCase):

    @patch('app.pipelines.churn_analysis.read_training_data')
    @patch('app.pipelines.churn_analysis.read_testing_data')
    @patch('app.pipelines.churn_analysis.create_file')
    @patch('app.pipelines.churn_analysis.train_model')
    @patch('app.pipelines.churn_analysis.make_predictions')
    def test_run_churn_analysis(self, mock_make_predictions, mock_train_model, mock_create_file, mock_read_testing_data, mock_read_training_data):
        df_train = pd.DataFrame({
            'Nome': ['Cliente1', 'Cliente2', 'Cliente3'],
            'Data_de_Criacao': ['2022-01-01', '2022-06-01', '2022-03-01'],
            'Data_de_Saida': ['2023-01-01', '2023-06-01', '2023-03-01'],
            'Valor_Consumido': [100, 200, 150]
        })
        df_train['Data_de_Criacao'] = pd.to_datetime(df_train['Data_de_Criacao'])
        df_train['Data_de_Saida'] = pd.to_datetime(df_train['Data_de_Saida'])

        df_test = pd.DataFrame({
            'Nome': ['Cliente4'],
            'Data_de_Criacao': ['2022-01-01'],
            'Valor_Consumido': [150]
        })
        df_test['Data_de_Criacao'] = pd.to_datetime(df_test['Data_de_Criacao'])

        mock_read_training_data.return_value = df_train
        mock_read_testing_data.return_value = df_test
        mock_train_model.return_value = (MagicMock(), df_train)
        mock_make_predictions.return_value = df_test

        run_churn_analysis()

        mock_read_training_data.assert_called_once()
        mock_read_testing_data.assert_called_once()
        mock_train_model.assert_called_once_with(df_train)
        mock_make_predictions.assert_called_once()
        mock_create_file.assert_called_once_with(df_test)
