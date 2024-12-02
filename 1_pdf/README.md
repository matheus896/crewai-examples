# Rag PDF com CrewAI
Este script Python utiliza a biblioteca crewai para criar uma estrutura de assistente automático (Crew) que busca e responde perguntas em um PDF. O sistema inclui dois agentes distintos: um agente de pesquisa para extrair dados do PDF e um agente de escrita profissional para escrever emails com base nas informações extraídas.

# Pré-requisitos
Python: Certifique-se de ter o Python instalado em sua máquina. A versão recomendada é a 3.12

- Bibliotecas necessárias:

crewai
crewai_tools
pydotenv

- Para instalar as bibliotecas necessárias, execute:

pip install crewai crewai_tools  
pip install python-dotenv

# Como Usar

- Configurar o Ambiente:

Certifique-se de que o arquivo .env esteja configurado com as variáveis necessárias, se houver algum.

- Execute:

venv\Scripts\activate # Para Windows
source venv/bin/activate # Para Linux/Mac

- Executar o Script:

python 1_crew.py

- Interagir com o Sistema:

Você será solicitado a informar qual seção do relatório de inspeção deseja gerar uma ordem de trabalho.
O sistema então buscará e responderá às perguntas fornecidas.

# Estrutura do Sistema

- Agentes:

Research Agent: Responsável por pesquisar e extrair informações do PDF, garantindo precisão e rapididade nas buscas.
Professional Writer Agent: Conhecido por suas habilidades de escrita profissional para criar emails a partir dos dados extraídos pelo Research Agent.
- Tarefas:

Answer Customer Question Task:

Busca e responde perguntas do relatório de inspeção com base no conteúdo do PDF.

Write Email Task:

Escreve um email para um contratante, detalhando os problemas encontrados na seção especificada pelo usuário e solicitando uma ordem de trabalho ou plano para corrigi-los.
O email é assinado com informações pessoais como nome e empresa.

- Cronograma

O sistema utiliza um cronograma sequencial (Process.sequential), onde as tarefas são executadas em ordem. Isso garante que todas as etapas necessárias estejam concluídas antes de avançar para a próxima.

# Considerações
O PDF precisa estar localizado no mesmo diretório que o script.
Se você estiver usando um ambiente diferente (por exemplo, um servidor ou Docker), certifique-se de adaptar as configurações de ambiente corretamente.
Este sistema foi projetado para uso em cenários específicos e pode necessitar adaptação para outros tipos de aplicativos.

# Licença
Este software é distribuído sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.

