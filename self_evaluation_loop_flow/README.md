 # {{loop_flow}} Crew

Bem-vindo ao projeto {{loop_flow}} Crew, impulsionado por [crewAI](https://crewai.com). Este modelo é projetado para ajudá-lo a configurar um sistema de IA multiagente com facilidade, aproveitando o poderoso e flexível framework fornecido pela crewAI. Nosso objetivo é permitir que seus agentes colaborem efetivamente em tarefas complexas, maximizando sua inteligência e capacidades coletivas.

## Instalação

Certifique-se de ter o Python >=3.10 <=3.13 instalado no seu sistema. Este projeto usa [UV](https://docs.astral.sh/uv/) para gerenciamento de dependências e manipulação de pacotes, oferecendo uma experiência de configuração e execução sem complicações.

Primeiro, se ainda não o fez, instale o uv:

```bash
pip install uv
Em seguida, navegue até o diretório do seu projeto e instale as dependências:

(Opcional) Bloqueie as dependências e instale-as usando o comando CLI:


crewai install
Personalização
Adicione sua OPENAI_API_KEY ao arquivo .env

Modifique src/self_evaluation_loop_flow/config/agents.yaml para definir seus agentes
Modifique src/self_evaluation_loop_flow/config/tasks.yaml para definir suas tarefas
Modifique src/self_evaluation_loop_flow/crew.py para adicionar sua própria lógica, ferramentas e argumentos específicos
Modifique src/self_evaluation_loop_flow/main.py para adicionar entradas personalizadas para seus agentes e tarefas
Executando o Projeto
Para iniciar sua equipe de agentes de IA e começar a execução de tarefas, execute isso a partir da pasta raiz do seu projeto:


crewai run
Este comando inicializa a Crew self_evaluation_loop_flow, montando os agentes e atribuindo-lhes tarefas conforme definido em sua configuração.

Este exemplo, sem modificações, criará um arquivo report.md com a saída de uma pesquisa sobre LLMs na pasta raiz.

Entendendo Sua Crew
A Crew self_evaluation_loop_flow é composta por múltiplos agentes de IA, cada um com funções, objetivos e ferramentas únicos. Esses agentes colaboram em uma série de tarefas definidas em config/tasks.yaml, utilizando suas habilidades coletivas para alcançar objetivos complexos. O arquivo config/agents.yaml descreve as capacidades e configurações de cada agente em sua equipe.

Suporte
Para suporte, perguntas ou feedback sobre a {{loop_flow}} Crew ou crewAI.

Visite nossa documentação
Entre em contato conosco através do nosso repositório GitHub
Junte-se ao nosso Discord
Converse com nossos docs
Vamos criar maravilhas juntos com o poder e a simplicidade da crewAI.
