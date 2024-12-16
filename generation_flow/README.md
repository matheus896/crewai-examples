# Projeto de Geração de Artigos com Agentes Inteligentes

Bem-vindo ao projeto de geração de artigos utilizando agentes inteligentes, desenvolvido com a framework [crewAI](https://crewai.com). Este projeto tem como objetivo facilitar a criação de artigos informativos através da colaboração de múltiplos agentes, cada um com funções específicas.

## Instalação

Certifique-se de que você possui Python na versão >=3.10 e <=3.13 instalado em seu sistema. Este projeto utiliza [UV](https://docs.astral.sh/uv/) para gerenciamento de dependências e execução, proporcionando uma experiência de configuração e execução simplificada.

Primeiro, se ainda não o fez, instale o UV:

```bash
pip install uv
```

Em seguida, navegue até o diretório do seu projeto e instale as dependências:
(Opcional) Bloqueie as dependências e instale-as usando o comando CLI:
```bash
crewai install
```


### Personalização

**Adicione sua `OPENAI_API_KEY` no arquivo `.env`**

- Modifique `src/teste/config/agents.yaml` para definir seus agentes.
- Modifique `src/teste/config/tasks.yaml` para definir suas tarefas.
- Modifique `src/teste/main.py` para adicionar entradas personalizadas para seus agentes e tarefas.

## Executando o Projeto

Para iniciar sua equipe de agentes de IA e começar a execução das tarefas, execute o seguinte comando a partir da pasta raiz do seu projeto:

```bash
crewai run
```

Este comando inicializa a equipe de teste, reunindo os agentes e atribuindo-lhes tarefas conforme definido em sua configuração.

## Estrutura do Código

O projeto é composto por duas classes principais:

1. **ArtigoState**: Um modelo que armazena o estado do artigo, incluindo o tema e o conteúdo do artigo gerado.
2. **ArtigoFlow**: Uma classe que define o fluxo de trabalho para a geração do artigo, incluindo as etapas de definição do tema, geração do artigo e salvamento do artigo em um arquivo.

### Fluxo de Trabalho

- **Definir Tema**: O agente define um tema para o artigo.
- **Gerar Artigo**: O agente gera o artigo com base no tema definido, utilizando a classe `ArtigoCrew`.
- **Salvar Artigo**: O artigo gerado é salvo em um arquivo chamado `artigo.md`.

## Entendendo Sua Equipe

A equipe de teste é composta por múltiplos agentes de IA, cada um com papéis, objetivos e ferramentas únicas. Esses agentes colaboram em uma série de tarefas, definidas em `config/tasks.yaml`, aproveitando suas habilidades coletivas para alcançar objetivos complexos. O arquivo `config/agents.yaml` descreve as capacidades e configurações de cada agente em sua equipe.

## Suporte

Para suporte, perguntas ou feedback sobre o projeto:

- Visite nossa [documentação](https://docs.crewai.com)
- Entre em contato através do nosso [repositório no GitHub](https://github.com/joaomdmoura/crewai)
- [Participe do nosso Discord](https://discord.com/invite/X4JWnZnxPb)
- [Converse com nossa documentação](https://chat.gpt/DWjSBZn)

Vamos criar maravilhas juntos com o poder e a simplicidade do crewAI!