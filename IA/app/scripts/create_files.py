import pandas as pd
import os

def create_file(df: pd.DataFrame) -> None:
    if df.empty:
        print("O DataFrame está vazio.")
        return

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_directory = os.path.join(project_root, 'data')
    file_name_training = 'Resultado_Churn.xlsx'
    file_path = os.path.join(data_directory, file_name_training)
    df.to_excel(file_path, index=False)