# AI News Generator

Este projeto é um gerador de notícias de IA que utiliza o framework CrewAI para criar posts de blog abrangentes sobre qualquer tópico. Ele usa agentes de IA para pesquisar, analisar e escrever conteúdo.

## Bibliotecas Necessárias

- **streamlit**: Para criar a interface web interativa.
- **crewai**: Para orquestrar os agentes de IA e suas tarefas.
- **crewai_tools**: Para fornecer ferramentas aos agentes, como a SerperDevTool para pesquisa na web.
- **python-dotenv**: Para carregar variáveis de ambiente de um arquivo .env.

## Configuração do Ambiente

1.  **Instale as bibliotecas necessárias:**

    ```bash
    pip install streamlit crewai crewai-tools python-dotenv
    ```
2.  **Crie um arquivo .env** na raiz do diretório `ai-news/` e adicione as seguintes variáveis de ambiente:

    ```env
    SERPER_API_KEY=sua_chave_serper_api
    COHERE_API_KEY=sua_chave_cohere_api
    CEREBRAS_API_KEY=sua_chave_cerebras_api
    GEMINI_API_KEY=sua_chave_gemini_api
    ```
    Substitua `sua_chave_...`, pela suas chaves de API. Você pode obter uma chave da API Serper em [https://serper.dev/](https://serper.dev/), uma chave da API Cohere em [https://cohere.com/](https://cohere.com/), uma chave da API Cerebras em [https://cerebras.com/](https://cerebras.com/) e uma chave da API Gemini em [https://ai.google.dev/](https://ai.google.dev/).

## Como Usar

1.  Execute o aplicativo Streamlit:

    ```bash
    streamlit run app.py
    ```
2.  Abra o aplicativo no seu navegador (geralmente em `http://localhost:8501`).
3.  Digite o tópico sobre o qual deseja gerar conteúdo na área de texto.
4.  Ajuste a temperatura, se necessário (maior = mais criativo).
5.  Clique em "Gerar Conteúdo" para iniciar o processo.
6.  Aguarde a IA gerar o artigo.
7.  Baixe o resultado como um arquivo markdown.

## Arquitetura do Código

O arquivo `app.py` contém o código principal do aplicativo. Ele define dois agentes:

-   **Senior Research Analyst**: Responsável por pesquisar, analisar e sintetizar informações sobre o tópico fornecido.
-   **Content Writer**: Responsável por transformar as descobertas da pesquisa em um post de blog envolvente.

O aplicativo usa o Streamlit para criar uma interface web onde o usuário pode inserir o tópico, ajustar a temperatura e gerar o conteúdo. O CrewAI é usado para orquestrar os agentes e suas tarefas.

## Fluxo do Programa

1.  O usuário insere um tópico na interface do Streamlit.
2.  O aplicativo cria dois agentes: um analista de pesquisa e um escritor de conteúdo.
3.  O analista de pesquisa usa a ferramenta SerperDevTool para pesquisar informações sobre o tópico.
4.  O analista de pesquisa organiza as descobertas em um relatório de pesquisa estruturado.
5.  O escritor de conteúdo usa o relatório de pesquisa para criar um post de blog envolvente.
6.  O aplicativo exibe o post de blog gerado na interface do Streamlit.
7.  O usuário pode baixar o post de blog como um arquivo markdown.

## Observações

-   O modelo de linguagem utilizado é o `gemini/gemini-1.5-flash`.
-   A temperatura pode ser ajustada para controlar a criatividade do modelo.
-   O aplicativo usa a ferramenta SerperDevTool para pesquisa na web.
-   O aplicativo agora suporta múltiplos modelos de linguagem, incluindo `gemini/gemini-1.5-flash`, `command-r` e `cerebras/llama-3.3-70b`.
