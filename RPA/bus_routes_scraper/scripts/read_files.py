import sys
import os
import pandas as pd
import openpyxl
from ..scraper import run_scraper
from .create_files import create_file

def run_read_files() -> None:
    file_path = 'C:/Users/jefferson.aleluia/Onibus_Rota.xlsx'
    df = pd.read_excel(file_path, usecols=['Partida', 'Destino'])

    start_text = df.iloc[0]['Partida']
    destination_text = df.iloc[0]['Destino']

    lines = run_scraper(start_text, destination_text)
    create_file(lines)