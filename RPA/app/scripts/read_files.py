import sys
import os
import pandas as pd
import openpyxl
from ..scraper import run_scraper
from .create_files import create_file

def run_read_files() -> None:
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_directory = os.path.join(project_root, 'data')
    file_name_training = 'Onibus_Rota.xlsx'
    file_path = os.path.join(data_directory, file_name_training)

    df = pd.read_excel(file_path, usecols=['Partida', 'Destino'])

    for index, row in df.iterrows():
        start_text = row['Partida']
        destination_text = row['Destino']

        lines = run_scraper(start_text, destination_text)
        file_name = f"Linhas_{start_text}_{destination_text}.xlsx"
        create_file(lines, file_name)