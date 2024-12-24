import pandas as pd
import os

def create_file(list_of_lines: list[str], file_name: str) -> None:
    if not list_of_lines:
        print("A lista de linhas está vazia.")
        return

    df = pd.DataFrame(list_of_lines, columns=['Rota'])

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_directory = os.path.join(project_root, 'data')
    file_name_training = f'{file_name}'
    file_path = os.path.join(data_directory, file_name_training)

    df.to_excel(file_path, index=False)