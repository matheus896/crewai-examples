# Edu Crew

Bem-vindo ao projeto Edu Crew, desenvolvido pela [crewAI](https://crewai.com). Este template foi projetado para ajudá-lo a configurar um sistema de IA multiagente com facilidade, aproveitando o poderoso e flexível framework fornecido pela crewAI. Nosso objetivo é permitir que seus agentes colaborem de forma eficaz em tarefas complexas, maximizando sua inteligência coletiva e capacidades.

## Instalação

Certifique-se de ter Python >=3.10 <=3.13 instalado em seu sistema. Este projeto utiliza [UV](https://docs.astral.sh/uv/) para gerenciamento de dependências e manipulação de pacotes, oferecendo uma experiência de configuração e execução sem complicações.

Primeiro, se ainda não tiver feito isso, instale o UV:

```bash
pip install uv
```

Em seguida, navegue até o diretório do seu projeto e instale as dependências:

(Opcional) Trave as dependências e instale-as utilizando o comando da CLI:

```bash
crewai install
```

### Personalizando

**Adicione sua `OPENAI_API_KEY` no arquivo `.env`**

- Modifique `src/edu_flow/config/agents.yaml` para definir seus agentes
- Modifique `src/edu_flow/config/tasks.yaml` para definir suas tarefas
- Modifique `src/edu_flow/crew.py` para adicionar sua própria lógica, ferramentas e argumentos específicos
- Modifique `src/edu_flow/main.py` para adicionar entradas personalizadas para seus agentes e tarefas

## Executando o Projeto

Para iniciar sua equipe de agentes de IA e começar a execução das tarefas, execute este comando a partir da pasta raiz do seu projeto:

```bash
crewai run
```

Este comando inicializa a Crew edu-flow, montando os agentes e atribuindo a eles as tarefas definidas em sua configuração.

Este exemplo, sem modificações, criará um arquivo `report.md` com o resultado de uma pesquisa sobre LLMs na pasta raiz.

## Entendendo Sua Equipe

A equipe edu-flow é composta por vários agentes de IA, cada um com funções, objetivos e ferramentas únicas. Esses agentes colaboram em uma série de tarefas, definidas em `config/tasks.yaml`, aproveitando suas habilidades coletivas para atingir objetivos complexos. O arquivo `config/agents.yaml` descreve as capacidades e configurações de cada agente em sua equipe.

## Suporte

Para suporte, perguntas ou feedback sobre o Edu Crew ou crewAI:

- Visite nossa [documentação](https://docs.crewai.com)
- Entre em contato conosco através do nosso [repositório no GitHub](https://github.com/joaomdmoura/crewai)
- [Junte-se ao nosso Discord](https://discord.com/invite/X4JWnZnxPb)
- [Converse com nossa documentação](https://chatg.pt/DWjSBZn)

Vamos criar maravilhas juntos com o poder e a simplicidade da crewAI.

