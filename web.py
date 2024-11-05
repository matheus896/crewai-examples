import os
import streamlit as st
from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
from litellm import completion

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()  # Isso carrega todas as variáveis definidas no arquivo .env, útil para configurar chaves de API e outras variáveis de ambiente.

# Inicializar o modelo OpenAI
llm = LLM(
    model='gemini/gemini-1.5-flash',  # Define o modelo de linguagem a ser utilizado.
    temperature=0.2  # Controla a aleatoriedade das respostas, 0.2 indica uma resposta mais previsível.
)

# Ferramenta de pesquisa na internet
search_tool = SerperDevTool()  # Ferramenta para realizar pesquisas na web.

# Configuração do Streamlit - Interface do usuário
st.title("Pipeline de Criação de Conteúdo para Vídeos no YouTube")  # Título principal da interface do Streamlit.
tema_user = st.text_input("Digite o tema do vídeo:")  # Campo de entrada de texto para o usuário inserir o tema do vídeo.

# Verifica se o botão foi pressionado e se há um tema fornecido pelo usuário
if st.button("Iniciar Processo") and tema_user:
    with st.spinner('Configurando os agentes e iniciando o processo...'):  # Exibe uma animação de carregamento enquanto o processo está sendo executado.
        # 1. Agente Pesquisador
        pesquisador = Agent(
            role='Pesquisador de Tema',  # Define o papel do agente.
            goal='Pesquisar informações detalhadas sobre {tema} na internet',  # Objetivo do agente.
            backstory=(
                "Você é um especialista em pesquisa, com habilidades aguçadas para "
                "encontrar informações valiosas e detalhadas na internet."
            ),  # História do agente, utilizada para dar contexto ao agente.
            verbose=True,  # Permite que o agente forneça informações detalhadas durante o processo.
            memory=True,  # Habilita a memória para que o agente se lembre de informações durante a execução.
            tools=[search_tool],  # Ferramentas disponíveis para o agente, neste caso, a ferramenta de pesquisa.
            llm=llm  # Modelo de linguagem utilizado pelo agente.
        )
        tarefa_pesquisa = Task(
            description=(
                "Pesquisar informações detalhadas e relevantes sobre o tema: {tema}. "
                "Concentre-se em aspectos únicos e dados importantes que podem enriquecer o vídeo. "
                "Todo o texto deve estar em Português Brasil."
            ),  # Descrição da tarefa a ser realizada pelo agente.
            expected_output='Um documento com as principais informações e dados sobre {tema}.',  # Resultado esperado da tarefa.
            tools=[search_tool],  # Ferramentas que podem ser usadas nesta tarefa.
            agent=pesquisador  # Agente responsável por esta tarefa.
        )

        # 2. Agente Escritor de Títulos
        escritor_titulos = Agent(
            role='Escritor de Títulos de Vídeo',  # Define o papel do agente.
            goal='Criar títulos atraentes e otimizados para vídeos sobre {tema}',  # Objetivo do agente.
            verbose=True,  # Permite que o agente forneça informações detalhadas durante o processo.
            memory=True,  # Habilita a memória para este agente.
            backstory=(
                "Você tem uma habilidade especial para criar títulos que capturam a "
                "essência de um vídeo e atraem a atenção do público."
            ),  # História do agente, usada para dar contexto ao seu papel.
            llm=llm  # Modelo de linguagem utilizado pelo agente.
        )
        tarefa_titulos = Task(
            description=(
                "Criar títulos atraentes e otimizados para o vídeo sobre o tema: {tema}. "
                "Certifique-se de que o título seja cativante e esteja otimizado para SEO. "
                "Todo o texto deve estar em Português Brasil."
            ),  # Descrição da tarefa do agente.
            expected_output='Um título otimizado para o vídeo sobre {tema}.',  # Resultado esperado da tarefa.
            agent=escritor_titulos,  # Agente responsável por esta tarefa.
            context=[tarefa_pesquisa]  # Contexto adicional, incluindo informações coletadas na etapa de pesquisa.
        )

        # 3. Agente Escritor de Roteiro
        escritor_roteiro = Agent(
            role='Escritor de Roteiro',  # Define o papel do agente.
            goal='Escrever um roteiro detalhado e envolvente para um vídeo sobre {tema}',  # Objetivo do agente.
            verbose=True,  # Permite que o agente forneça informações detalhadas durante o processo.
            memory=True,  # Habilita a memória para este agente.
            backstory=(
                "Você é um contador de histórias talentoso, capaz de transformar "
                "informações em narrativas cativantes para vídeos."
            ),  # História do agente, para fornecer contexto.
            llm=llm  # Modelo de linguagem utilizado pelo agente.
        )
        tarefa_roteiro = Task(
            description=(
                "Escrever um roteiro detalhado para o vídeo sobre o tema: {tema}. "
                "O roteiro deve ser envolvente e fornecer um fluxo lógico de informações. "
                "Se necessário, especifique imagens que podem enriquecer o conteúdo. "
                "Todo o texto deve estar em Português Brasil."
            ),  # Descrição da tarefa do agente.
            expected_output='Um roteiro completo e bem estruturado para o vídeo sobre {tema}.',  # Resultado esperado.
            agent=escritor_roteiro,  # Agente responsável pela tarefa.
            context=[tarefa_titulos, tarefa_pesquisa]  # Contexto adicional, incluindo título e pesquisa anteriores.
        )

        # 4. Agente Especialista em SEO para YouTube
        especialista_seo = Agent(
            role='Especialista em SEO para YouTube',  # Define o papel do agente.
            goal='Otimizar o roteiro e o título para que o vídeo tenha uma alta performance no YouTube',  # Objetivo do agente.
            verbose=True,  # Permite que o agente forneça informações detalhadas durante o processo.
            memory=True,  # Habilita a memória para o agente.
            backstory=(
                "Você é um expert em SEO, com um profundo entendimento das melhores "
                "práticas para otimizar conteúdo para o YouTube."
            ),  # História do agente para fornecer contexto.
            llm=llm  # Modelo de linguagem utilizado pelo agente.
        )
        tarefa_seo = Task(
            description=(
                "Otimizar o título e o roteiro do vídeo para que tenha uma alta performance no YouTube. "
                "Incorporar as melhores práticas de SEO para garantir uma boa classificação e visibilidade. "
                "Crie hashtags, palavras-chaves e tags de vídeo para YouTube. "
                "Todo o texto deve estar em Português Brasil."
            ),  # Descrição da tarefa de SEO.
            expected_output='Roteiro e título otimizados para o vídeo sobre {tema}, prontos para publicação no YouTube.',  # Resultado esperado.
            agent=especialista_seo,  # Agente responsável pela tarefa.
            context=[tarefa_roteiro, tarefa_titulos, tarefa_pesquisa]  # Contexto adicional com base no trabalho já realizado.
        )

        # 5. Agente Revisor
        revisor = Agent(
            role='Revisor de Conteúdo',  # Define o papel do agente.
            goal='Revisar todo o conteúdo produzido e entregar a versão final ao usuário',  # Objetivo do agente.
            verbose=True,  # Permite que o agente forneça informações detalhadas durante o processo.
            memory=True,  # Habilita a memória para o agente.
            backstory=(
                "Você tem um olho afiado para detalhes, garantindo que todo o conteúdo "
                "esteja perfeito antes de ser entregue ao usuário."
            ),  # História do agente para dar contexto.
            llm=llm  # Modelo de linguagem utilizado pelo agente.
        )
        tarefa_revisao = Task(
            description=(
                "Revisar todo o conteúdo produzido (título, roteiro, e otimização de SEO), "
                "preparar a versão final para entrega ao usuário. "
                "Todo o texto deve estar em Português Brasil."
            ),  # Descrição da tarefa de revisão.
            expected_output='Conteúdo revisado, pronto para entrega ao usuário.',  # Resultado esperado.
            agent=revisor,  # Agente responsável pela revisão.
            context=[tarefa_seo, tarefa_roteiro, tarefa_titulos, tarefa_pesquisa]  # Contexto com todas as etapas anteriores.
        )

        # Formando a crew - Grupo de agentes que trabalham em conjunto
        crew = Crew(
            agents=[pesquisador, escritor_titulos, escritor_roteiro, especialista_seo, revisor],  # Lista de agentes.
            tasks=[tarefa_pesquisa, tarefa_titulos, tarefa_roteiro, tarefa_seo, tarefa_revisao],  # Lista de tarefas em sequência.
            process=Process.sequential,  # Define que o processo deve ser executado de forma sequencial.
            verbose=True  # Detalhamento dos passos durante a execução.
        )

        # Executando o processo com o tema escolhido
        result = crew.kickoff(inputs={'tema': tema_user})  # Inicia o processo com o tema fornecido pelo usuário.

    # Exibindo os resultados
    st.success("Processo concluído!")  # Mensagem de sucesso quando o processo é finalizado.
    st.subheader("Resultado Final")
    st.markdown(result)  # Mostra o resultado final do processo na interface do Streamlit.
