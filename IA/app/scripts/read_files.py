import sys
import os
import pandas as pd
import openpyxl

def read_training_data(file_path: str) -> pd.DataFrame:
    df = pd.read_excel(file_path, usecols=['Nome', 'Data_de_Criacao', 'Data_de_Saida', 'Valor_Consumido'])
    return df

def read_testing_data(file_path: str) -> pd.DataFrame:
    df = pd.read_excel(file_path, usecols=['Nome', 'Data_de_Criacao', 'Valor_Consumido'])
    return df