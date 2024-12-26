
## Projeto de Análise de Churn

### Este projeto é uma aplicação de aprendizado de máquina não supervisionado utilizando Python e bibliotecas como pandas, scikit-learn e pytest. O objetivo do projeto é calcular o tempo de permanência dos clientes, agrupá-los em clusters com base no tempo de permanência e valor consumido, e realizar previsões para novos dados.

## Tecnologias Utilizadas
#### Python: Linguagem utilizada no desenvolvimento do projeto.
#### Pandas: Biblioteca para manipulação e análise de dados tabulares.
#### Scikit-Learn: Utilizada para implementação de algoritmos de clustering e métricas de avaliação.
#### Pytest: Frameworks para testes automatizados
#### Poetry: Ferramenta para gerenciamento de dependências e ambiente virtual.

## Estrutura do Projeto

#### app/: Contém a lógica principal do projeto.

##### data/: Contém os arquivos com os dados de entrada e saída.

#### features/: retention.py: Implementa a função calculate_retention_time para calcular o tempo de permanência dos clientes.  clustering.py: Contém a lógica para treinamento do modelo (train_model) e previsão de clusters (make_predictions).

#### pipeline/:Integra as funcionalidades de engenharia de dados, treinamento do modelo e previsão.

#### scripts/: Scripts auxiliares para leitura e criação de arquivos Excel.

#### tests/: Contém as classes responsáveis por executar os testes unitários.

## Funcionalidades
#### Cálculo do Tempo de Permanência: Cálculo do tempo de permanência (em meses) para cada cliente, baseado nas datas de criação e saída.

#### Agrupamento de Clientes: Agrupamento dos clientes em clusters utilizando o algoritmo K-Means, com base nas características de tempo de permanência e valor consumido.

#### Avaliação do Modelo: Divisão dos dados em conjuntos de treino e teste para avaliar a acurácia do modelo de clustering.

#### Previsão de Clusters: Predição de clusters para novos dados de clientes, utilizando o modelo K-Means treinado.

#### Exportação de Resultados: Geração de um arquivo Excel contendo os clusters previstos e informações relevantes, como tempo de permanência e nome do cliente.

#### Manipulação de Dados: Integração com scripts para leitura e escrita de arquivos Excel para facilitar o processamento de dados.

## Rodar projeto

#### Instale as dependências: poetry install

#### Ative o ambiente virtual : poetry shell

#### Rodar o projeto: python main.py