## O Wayne Foundation CRUD é uma aplicação web 

### desenvolvida utilizando FastAPI, SQLAlchemy e PostgreSQL. O objetivo do projeto é gerenciar informações de benefícios e beneficiários oferecidos pela Wayne Foundation, através de um sistema CRUD (Create, Read, Update, Delete). A aplicação também integra-se com a API ViaCEP para obter informações de endereços com base no CEP informado pelos usuários para realizar a criação de um Orphanages .



## Tecnologias Utilizadas

#### Python: Linguagem utilizada no desenvolvimento do projeto.

#### FastAPI: Framework web para criar a API RESTful.

#### SQLAlchemy: ORM (Object-Relational Mapping) para interação com o banco de dados.

#### PostgreSQL: Banco de dados relacional.

#### Poetry: Gerenciamento de dependências e ambiente virtual.

#### ViaCEP API: Serviço externo para consulta de endereços por CEP.



## Estrutura do Projeto

#### app/: Contém os módulos principais da aplicação.

#### routes/: Rotas e controladores da API.

#### services/: Lógica de negócio e integração com APIs externas.

#### crud/: Funções para realizar as operações usando o ORM

#### db/: Configuração e gerenciamento do banco de dados.

#### models/: Definição das entidades e modelos de dados.

#### schemas/: Validação e estrutura de entrada/saída dos dados.

#### exceptions/: Contém as excessões personalizadas

#### clients/: Contém os clientes para integração com APIs externas

#### tests/: Contém as classes responsáveis por executar os testes unitários.


## Entidade

#### Dependent: Representa um beneficiário da Wayne Foundation.

#### Assosiation: Representa um doador que contribui para a Wayne Foundation.

#### Donations: Registra uma doação realizada por um Association.

#### Orphanages: Representa um orfanato que cuida de um ou mais Dependents.



## Rodar projeto

#### Instale as dependências: poetry install

#### Ative o ambiente virtual : poetry shell

#### Rodar a API: uvicorn main:app --reload
