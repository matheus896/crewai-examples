import os
import streamlit as st
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configuração da página do Streamlit
st.set_page_config(page_title="AI News Generator", page_icon="📰", layout="wide")

# Título e descrição
st.title("🤖 AI News Generator, alimentado por CrewAI")
st.markdown("Gere posts de blog abrangentes sobre qualquer tópico usando agentes de IA.")

# Barra lateral
with st.sidebar:
    st.header("Configurações de Conteúdo")

    # Fazer a entrada de texto ocupar mais espaço
    topic = st.text_area(
        "Digite seu tópico",
        height=100,
        placeholder="Digite o tópico sobre o qual deseja gerar conteúdo..."
    )

    # Adicionar mais controles na barra lateral, se necessário
    st.markdown("### Configurações Avançadas")
    temperature = st.slider("Temperatura", 0.0, 1.0, 0.7)

    # Adicionar espaçamento
    st.markdown("---")

    # Tornar o botão de gerar mais proeminente na barra lateral
    generate_button = st.button("Gerar Conteúdo", type="primary", use_container_width=True)

    # Adicionar algumas informações úteis
    with st.expander("ℹ️ Como usar"):
        st.markdown("""
        1. Digite o tópico desejado na área de texto acima
        2. Ajuste a temperatura, se necessário (maior = mais criativo)
        3. Clique em 'Gerar Conteúdo' para começar
        4. Aguarde a IA gerar seu artigo
        5. Baixe o resultado como um arquivo markdown
        """)

def generate_content(topic):
    llm = LLM(
        model="gemini/gemini-1.5-flash",
        temperature=0.7
    )

    search_tool = SerperDevTool(n_results=10)

    # Primeiro Agente: Analista de Pesquisa Sênior
    senior_research_analyst = Agent(
        role="Senior Research Analyst",
        goal=f"Pesquisar, analisar e sintetizar informações abrangentes sobre {topic} de fontes confiáveis da web",
        backstory="Você é um analista de pesquisa experiente com habilidades avançadas em pesquisa na web. "
                "Você se destaca em encontrar, analisar e sintetizar informações de "
                "toda a internet usando ferramentas de busca. Você é habilidoso em "
                "diferenciar fontes confiáveis das não confiáveis, "
                "verificar fatos, cruzar referências de informações e "
                "identificar padrões e insights-chave. Você fornece "
                "relatórios de pesquisa bem organizados com citações "
                "e verificação de fontes adequadas. Sua análise inclui tanto "
                "dados brutos quanto insights interpretados, tornando informações "
                "complexas acessíveis e acionáveis.",
        allow_delegation=False,
        verbose=True,
        tools=[search_tool],
        llm=llm
    )

    # Segundo Agente: Escritor de Conteúdo
    content_writer = Agent(
        role="Content Writer",
        goal="Transformar descobertas de pesquisa em posts de blog envolventes, mantendo a precisão",
        backstory="Você é um escritor de conteúdo habilidoso especializado em criar "
                "conteúdo envolvente e acessível a partir de pesquisa técnica. "
                "Você trabalha em estreita colaboração com o Analista de Pesquisa Sênior e se destaca em manter o equilíbrio perfeito entre escrita informativa e envolvente, "
                "garantindo que todos os fatos e citações da pesquisa "
                "sejam devidamente incorporados. Você tem talento para tornar "
                "tópicos complexos acessíveis sem simplificá-los demais.",
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    # Tarefa de Pesquisa
    research_task = Task(
        description=("""
            1. Realizar uma pesquisa abrangente sobre {topic} incluindo:
                - Desenvolvimentos e notícias recentes
                - Principais tendências e inovações do setor
                - Opiniões e análises de especialistas
                - Dados estatísticos e insights de mercado
                - utilizar fontes de pesquisa do mundo inteiro
            2. Avaliar a credibilidade da fonte e verificar todos os fatos
            3. Organizar as descobertas em um relatório de pesquisa estruturado
            4. Incluir todas as citações e fontes relevantes
        """),
        expected_output="""Um relatório de pesquisa detalhado contendo:
            - Resumo executivo das principais descobertas
            - Análise abrangente das tendências e desenvolvimentos atuais
            - Lista de fatos e estatísticas verificados
            - Todas as citações e links para as fontes originais
            - Categorização clara dos principais temas e padrões
            Por favor, formate com seções e pontos claros para fácil referência.""",
        agent=senior_research_analyst
    )

    # Tarefa de Escrita
    writing_task = Task(
        description=("""
            Usando o relatório de pesquisa fornecido, crie um post de blog envolvente que:
            1. Transforme informações técnicas em conteúdo acessível
            2. Mantenha toda a precisão dos fatos e citações da pesquisa
            3. Inclua:
                - Introdução cativante
                - Seções de corpo bem estruturadas com cabeçalhos claros
                - Conclusão convincente
            4. Preserve todas as citações de fontes no formato [Source: URL]
            5. Inclua uma seção de Referências no final
        """),
        expected_output="""Um post de blog polido em formato markdown que:
            - Envolve os leitores enquanto mantém a precisão
            - Contém seções bem estruturadas
            - Inclui citações online hiperlinkadas para a URL da fonte original
            - Apresenta as informações de maneira acessível, mas informativa
            - Segue o formato markdown adequado, use H1 para o título e H3 para as subseções
            - Esteja em português Brasileiro.""",
        agent=content_writer
    )

    # Criar Crew
    crew = Crew(
        agents=[senior_research_analyst, content_writer],
        tasks=[research_task, writing_task],
        verbose=True
    )

    return crew.kickoff(inputs={"topic": topic})

# Área principal de conteúdo
if generate_button:
    with st.spinner('Gerando conteúdo... Isso pode levar um momento.'):
        try:
            result = generate_content(topic)
            st.markdown("### Conteúdo Gerado")
            st.markdown(result)

            # Adicionar botão de download
            st.download_button(
                label="Baixar Conteúdo",
                data=result.raw,
                file_name=f"{topic.lower().replace(' ', '_')}_article.md",
                mime="text/markdown"
            )
        except Exception as e:
            st.error(f"Ocorreu um erro: {str(e)}")

# Rodapé
st.markdown("---")
st.markdown("Construído com CrewAI e Streamlit")