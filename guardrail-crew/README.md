# Projeto Guardrail Crew

Este projeto é uma implementação de um sistema de validação de resumos utilizando a biblioteca Guardrails e a CrewAI. O objetivo é realizar pesquisas na web, gerar resumos e validar esses resumos com base em critérios de qualidade.

## Estrutura do Projeto

O projeto é composto por vários arquivos, sendo os principais:

- `custom_tool.py`: Contém a lógica para validação de resumos utilizando a biblioteca Guardrails.
- `crew.py`: Define os agentes e tarefas que compõem o fluxo de trabalho do sistema.
- `.env`: Armazena as variáveis de ambiente necessárias para a execução do projeto.

## Bibliotecas Utilizadas

### 1. Guardrails
A biblioteca Guardrails é utilizada para validar a qualidade dos resumos gerados. Ela permite definir métricas como informatividade, coerência, concisão e engajamento, que são utilizadas para avaliar os resumos.

### 2. CrewAI
A CrewAI é uma biblioteca que facilita a criação de agentes que podem realizar tarefas específicas. Neste projeto, utilizamos agentes para pesquisar na web, escrever resumos e validar esses resumos.

### 3. Pydantic
Pydantic é uma biblioteca para validação de dados e criação de modelos de dados. No projeto, ela é utilizada para definir a estrutura da saída esperada da validação dos resumos.

### 4. dotenv
A biblioteca dotenv é utilizada para carregar variáveis de ambiente a partir de um arquivo `.env`. Isso é útil para manter as chaves de API e outras configurações sensíveis fora do código-fonte.

## Dependências Necessárias

As dependências do projeto estão listadas no arquivo `pyproject.toml`. Para instalar as dependências, você pode usar o seguinte comando:

```
pip install -r requirements.txt
```

As principais dependências são:

- `crewai>=0.86.0`: Biblioteca para criação de agentes e tarefas.
- `guardrails-ai>=0.1.8`: Biblioteca para validação de resumos.
- `tools>=0.1.9`: Biblioteca para ferramentas auxiliares.

## Variáveis de Ambiente

O arquivo `.env` contém as seguintes variáveis de ambiente necessárias para a execução do projeto:

- `SERPER_API_KEY`: Chave da API para o Serper.
- `CEREBRAS_API_KEY`: Chave da API para o Cerebras.

Certifique-se de preencher essas chaves com os valores corretos antes de executar o projeto.

## Execução do Projeto

Para executar o projeto, você pode rodar o arquivo `crew.py`. O código irá iniciar o fluxo de trabalho, realizando uma pesquisa na web sobre o impacto da inteligência artificial nas mudanças climáticas, gerando um resumo e validando-o.


