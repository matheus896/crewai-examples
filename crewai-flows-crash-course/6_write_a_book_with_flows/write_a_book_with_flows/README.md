**Fluxo de Escrita de Livros**

Bem-vindo ao Fluxo de Escrita de Livros, desenvolvido pela [crewAI](https://crewai.com). Este modelo foi projetado para ajudá-lo a configurar um sistema de IA multiagente com facilidade, aproveitando a estrutura poderosa e flexível fornecida pela crewAI. Nosso objetivo é permitir que seus agentes colaborem efetivamente em tarefas complexas, maximizando sua inteligência e capacidades coletivas.

**Visão Geral**

Este fluxo irá guiá-lo através do processo de escrita de um livro, alavancando vários agentes de IA, cada um com funções específicas. Aqui está uma breve visão geral do que acontecerá neste fluxo:

1. **Gerar Esboço do Livro**: O fluxo começa usando o `OutlineCrew` para criar um esboço abrangente para o seu livro. Esta equipe irá pesquisar na internet, definir a estrutura e os principais tópicos do livro com base na meta e no tópico fornecidos.

2. **Escrever Capítulos do Livro**: Assim que o esboço estiver pronto, o fluxo iniciará uma nova equipe, `WriteBookChapterCrew`, para cada capítulo descrito na etapa anterior. Cada equipe será responsável por escrever um capítulo específico, garantindo que o conteúdo seja detalhado e coerente.

3. **Juntar e Salvar Capítulos**: Na etapa final, o fluxo combinará todos os capítulos em um único arquivo markdown, criando um livro completo. Este arquivo será salvo na pasta raiz do seu projeto.

Seguindo este fluxo, você pode produzir com eficiência um livro bem estruturado e abrangente, aproveitando o poder de vários agentes de IA para lidar com diferentes aspectos do processo de escrita.

**Instalação**

Certifique-se de ter o Python >=3.10 <=3.13 instalado em seu sistema. Este projeto usa [Poetry](https://python-poetry.org/) para gerenciamento de dependências e manipulação de pacotes, oferecendo uma experiência perfeita de configuração e execução.

Primeiro, se você ainda não o fez, instale o Poetry:

```bash
pip install poetry
```

Em seguida, navegue até o diretório do seu projeto e instale as dependências:

1. Primeiro, bloqueie as dependências e depois instale-as:

```bash
crewai install
```

**Personalização e Dependências**

**Adicione sua `OPENAI_API_KEY` ao arquivo `.env`**
**Adicione sua `SERPER_API_KEY` ao arquivo `.env`**

Para personalizar o comportamento do fluxo de escrita do livro, você pode atualizar os agentes e tarefas definidos no `OutlineCrew` e `WriteBookChapterCrew`. Se você quiser ajustar o fluxo em si, precisará modificar o fluxo em `main.py`.

- **Agentes e Tarefas**: Modifique `src/write_a_book_with_flows/config/agents.yaml` para definir seus agentes e `src/write_a_book_with_flows/config/tasks.yaml` para definir suas tarefas. É aqui que você pode personalizar como o esboço do livro é gerado e como os capítulos são escritos.

- **Ajustes de Fluxo**: Modifique `src/write_a_book_with_flows/main.py` para ajustar o fluxo. É aqui que você pode alterar como o fluxo orquestra as diferentes equipes e tarefas.

**Executando o Projeto**

Para iniciar sua equipe de agentes de IA e começar a execução da tarefa, execute isto a partir da pasta raiz do seu projeto:

```bash
crewai run
```

Este comando inicializa o Fluxo write_a_book_with_flows, reunindo os agentes e atribuindo-lhes tarefas conforme definido em sua configuração.

Quando você inicia o fluxo, ele orquestra várias equipes para executar as tarefas. O fluxo primeiro gerará um esboço do livro, depois criará e executará uma equipe para cada capítulo e, finalmente, juntará todos os capítulos em um único arquivo markdown.

**Entendendo Seu Fluxo**

O Fluxo write_a_book_with_flows é composto por vários agentes de IA, cada um com funções, metas e ferramentas exclusivas. Esses agentes colaboram em uma série de tarefas, definidas em `config/tasks.yaml`, alavancando suas habilidades coletivas para atingir objetivos complexos. O arquivo `config/agents.yaml` descreve os recursos e configurações de cada agente em seu fluxo.

**Estrutura do Fluxo**

1. **OutlineCrew**: Esta equipe é responsável por gerar o esboço do livro. Ele define a estrutura e os principais tópicos do livro com base na meta e no tópico fornecidos.

2. **WriteBookChapterCrew**: Para cada capítulo descrito pelo `OutlineCrew`, um novo `WriteBookChapterCrew` é criado. Cada uma dessas equipes é responsável por escrever um capítulo específico, garantindo conteúdo detalhado e coerente.

3. **Juntar e Salvar**: Depois que todos os capítulos são escritos, o fluxo os combina em um único arquivo markdown, criando um livro completo.

Ao entender a estrutura do fluxo, você pode ver como várias equipes são orquestradas para trabalhar juntas, cada uma lidando com uma parte específica do processo de escrita do livro. Essa abordagem modular permite uma produção de livros eficiente e escalável.

**Suporte**

Para suporte, dúvidas ou feedback sobre o Fluxo {{crew_name}} ou crewAI.

- Visite nossa [documentação](https://docs.crewai.com)
- Entre em contato conosco através do nosso [repositório GitHub](https://github.com/joaomdmoura/crewai)
- [Junte-se ao nosso Discord](https://discord.com/invite/X4JWnZnxPb)
- [Converse com nossos documentos](https://chatg.pt/DWjSBZn)

Vamos criar maravilhas juntos com o poder e a simplicidade do crewAI.
