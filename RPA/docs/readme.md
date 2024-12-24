## Projeto de RPA para Busca do Melhor Trajeto de Ônibus

### Este projeto é uma aplicação de automação desenvolvida utilizando Selenium, Python, pandas e manipulação de arquivos Excel. O objetivo do projeto é encontrar o melhor trajeto de ônibus com base em dados fornecidos em arquivos Excel, integrando web scraping para coletar informações relevantes e gerar relatórios detalhados.

## Tecnologias Utilizadas

#### Python: Linguagem utilizada no desenvolvimento do projeto.

#### Selenium: Biblioteca para automação de interações com a web.

#### Pandas: Biblioteca para análise e manipulação de dados tabulares.

#### Pytest e unittest.mock: Frameworks para testes automatizados e criação de mocks.

#### Poetry: Ferramenta para gerenciamento de dependências e ambiente virtual.


## Estrutura do Projeto

#### app/: Contém a lógica principal do projeto.

#### data/: Contém os arquivos Excel de entrada e saída.

#### scraper/: Contém os scrapers desenvolvidos com Selenium para coletar os dados necessários.

#### scripts/: Scripts auxiliares para manipulação de dados e geração de arquivos Excel.

#### tests/: Contém os testes unitários e de integração usando pytest e unittest.mock.


## Funcionalidades

#### Leitura de Dados: Leitura de um arquivo Excel que contém informações sobre rotas de ônibus.

#### Busca de Trajetos: Uso de Selenium para acessar sites e buscar informações detalhadas sobre as rotas.

#### Geração de Resultados: Geração de um arquivo Excel com o melhor trajeto encontrado e outros detalhes relevantes.


## Rodar projeto

#### Instale as dependências: poetry install

#### Ative o ambiente virtual : poetry shell

#### Rodar o projeto: python main.py