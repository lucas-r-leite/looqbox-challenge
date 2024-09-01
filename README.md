# Scripts Python para o Desafio Looqbox

Este repositório contém scripts em Python para resolver três desafios de análise de dados utilizando consultas SQL e visualização de dados. Os scripts foram projetados para interagir com um banco de dados MySQL e realizar diversas tarefas de manipulação e visualização de dados usando bibliotecas Python como `pandas`, `SQLAlchemy` e `seaborn`.

## Pré-requisitos e Configurações

Antes de executar os scripts, certifique-se de ter o seguinte instalado:

- Python 3.x
- Criação de um ambiente virtual
- Banco de dados MySQL
- Bibliotecas Python necessárias

1. Criação do ambiente virtual:

```bash
python -m venv venv
```

2. Instalação das bibliotecas:

```bash
pip install -r requirements.txt
```

3. Configuração do Banco de Dados:

Crie um arquivo `.env` e adicione as seguintes linhas:

```bash
IP=<seu-ip-do-banco-de-dados>
DB_NAME=<seu-nome-do-banco-de-dados>
DB_USER=<seu-usuario-do-banco-de-dados>
DB_PASS=<sua-senha-do-banco-de-dados>
```

## Scripts

Cada script pode ser executado de forma independente.

1. `first.py`

Este script gera uma consulta SQL com base em filtros fornecidos pelo usuário e recupera dados da tabela data_product_sales. A função retrieve_data aceita os parâmetros product_code, store_code e date e retorna um DataFrame do Pandas com os resultados filtrados.

#### Parâmetros

- `product_code`(int): Código do produto.
- `store_code`(int): Código da loja.
- `date`(lista): Lista contendo as duas strings de data no formato ISO 8601 (AAAA-MM-DD).

2. `second.py`

Este script recupera dados das tabelas data_store_cad e data_store_sales usando consultas SQL pré-definidas. Ele filtra os dados de vendas para um período especificado, mescla com as informações da loja, calcula o valor médio de vendas por transação (TM) e exibe uma tabela resumo ordenada pelo nome da loja.

3. `third.py`

Este script realiza análise de dados e visualização usando a tabela IMDB_Movies. Ele gera vários gráficos para analisar os dados dos filmes, como os 10 filmes principais por receita, a relação entre classificações de filmes e receita, e a distribuição de filmes por gênero.

### Visualização

- Gráfico de Barras: Top 10 filmes por receita;
- Gráfico de Dispersão: Receita vs Classificação IMDB;
- Gráfico de Barras: Número de filmes dos 10 gêneros principais.
