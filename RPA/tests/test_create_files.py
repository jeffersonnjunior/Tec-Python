import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
import os
from app.scripts.create_files import create_file

@patch('app.scripts.create_files.pd.DataFrame.to_excel')
@patch('app.scripts.create_files.os.path.dirname')
@patch('app.scripts.create_files.os.path.abspath')
@patch('app.scripts.create_files.os.path.join', side_effect=os.path.join)
def test_create_file(mock_join, mock_abspath, mock_dirname, mock_to_excel):
    mock_abspath.return_value = '/fake/path'
    mock_dirname.return_value = '/fake'

    list_of_lines = ['Linha 1', 'Linha 2']
    file_name = 'test_file.xlsx'

    create_file(list_of_lines, file_name)

    mock_to_excel.assert_called_once()
    args, kwargs = mock_to_excel.call_args
    assert args[0] == os.path.join('/fake', 'data', file_name)
    assert kwargs['index'] == False

    with patch('builtins.print') as mock_print:
        create_file([], file_name)
        mock_print.assert_called_once_with("A lista de linhas está vazia.")