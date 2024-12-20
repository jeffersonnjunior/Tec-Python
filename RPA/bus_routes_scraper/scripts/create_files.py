import pandas as pd

def create_file(list_of_lines: list[str]) -> None:
    if not list_of_lines:
        print("A lista de linhas está vazia.")
        return

    print("Linhas recebidas:", list_of_lines)
    df = pd.DataFrame(list_of_lines, columns=['Linhas'])
    df.to_excel('C:/Users/jefferson.aleluia/Rotas_Onibus_Rota.xlsx', index=False)