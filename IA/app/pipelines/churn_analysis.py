import os
from app.scripts import read_training_data, read_testing_data, create_file
from app.features import train_model, make_predictions

def run_churn_analysis() -> None:
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_directory = os.path.join(project_root, 'data')

    file_name_training = 'Base_Clientes_Treinamento.xlsx'
    file_path = os.path.join(data_directory, file_name_training)

    df = read_training_data(file_path)

    kmeans, df = train_model(df)

    print(df.head())

    file_name_testing = 'Base_Clientes_Teste.xlsx'
    file_path = os.path.join(data_directory, file_name_testing)

    df = read_testing_data(file_path)

    df = make_predictions(kmeans, df)

    create_file(df)

    print(df.head())

if __name__ == "__main__":
    run_churn_analysis()