
# CrewAI - Autonomous AI Agent Orchestration Framework

✨ **Empower your AI agents to collaborate and tackle complex tasks.** ✨

CrewAI is designed to enable AI agents to assume roles, share goals, and operate together in a cohesive unit - much like a well-oiled crew. Whether it's automating multi-step processes, complex research analysis, or intricate problem-solving, CrewAI provides the framework for sophisticated multi-agent interactions.

[![Build Status](https://img.shields.io/github/actions/workflow/status/joaomdmoura/crewai/ci.yml?branch=main)](https://github.com/joaomdmoura/crewai/actions/workflows/ci.yml)
[![PyPI Version](https://img.shields.io/pypi/v/crewai.svg)](https://pypi.org/project/crewai/)
[![License](https://img.shields.io/github/license/joaomdmoura/crewai)](https://github.com/joaomdmoura/crewai/blob/main/LICENSE)
[![Discord](https://img.shields.io/discord/1178134545809510470?label=discord)](https://discord.com/invite/X4JWnZnxPb)
[![Twitter](https://img.shields.io/twitter/follow/joaomdmoura?style=social)](https://twitter.com/joaomdmoura)

---

## Table of Contents

- [Introduction](#introduction)
- [Core Concepts](#core-concepts)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Key Components](#key-components)
  - [Agents](#agents)
  - [Tasks](#tasks)
  - [Tools](#tools)
  - [Crews](#crews)
  - [Process](#process)
  - [Memory](#memory)
  - [Knowledge](#knowledge)
  - [Flows](#flows)
  - [LiteAgent](#liteagent)
- [Command Line Interface (CLI)](#command-line-interface-cli)
- [Directory Structure Overview](#directory-structure-overview)
- [Contributing](#contributing)
- [License](#license)
- [Community & Support](#community--support)

---

## Introduction

CrewAI helps you create cutting-edge AI agent crews that excel at complex tasks through collaboration. Built with flexibility and developer experience in mind, it allows you to define roles, goals, and tools for your agents, orchestrate their execution, and manage their interactions effectively.

**Why CrewAI?**

-   **Role-Based Agent Design:** Easily customize agents with specific roles, goals, and backstories for targeted task execution.
-   **Autonomous Inter-Agent Delegation:** Agents can autonomously delegate tasks and inquire amongst themselves, enhancing problem-solving efficiency.
-   **Flexible Task Management:** Define tasks with customizable tools and dynamically assign them to agents.
-   **Process Strategy:** Choose between sequential or hierarchical task execution, with more strategies coming soon.
-   **Tool Integration:** Seamlessly integrate existing tools (e.g., LangChain tools) or define your own custom tools.
-   **State Management & Memory:** Manage agent state, memory (short-term, long-term, entity), and knowledge bases.
-   **Flow Orchestration:** Design complex, multi-crew workflows using the `Flow` feature for advanced coordination.
-   **CLI Support:** Create, manage, train, and deploy your crews using the intuitive Command Line Interface.

## Core Concepts

-   **Agent:** An autonomous unit programmed to perform tasks, make decisions, and communicate. Defined by a role, goal, backstory, tools, and potentially memory and delegation capabilities.
-   **Task:** A specific assignment given to an Agent. Includes a description, expected output, and the assigned agent.
-   **Tool:** A capability an Agent can use (e.g., web search, database query, code execution).
-   **Crew:** A group of Agents and Tasks working together. Orchestrates the overall process.
-   **Process:** The strategy defining how Tasks are executed within a Crew (e.g., `sequential`, `hierarchical`).
-   **LLM:** The language model powering the Agents' reasoning and decision-making.
-   **Memory:** Enables agents to retain information across task executions (short-term, long-term, entity, user, external).
-   **Knowledge:** Provides agents access to external information sources (files, databases, etc.).
-   **Flow:** An advanced mechanism to orchestrate workflows involving multiple crews or complex conditional logic.
-   **LiteAgent:** A simplified agent variant for straightforward interactions without complex delegation needs.

## Features

-   🤖 **Role-Playing:** Agents have customizable roles, goals, and backstories.
-   🤝 **Collaboration:** Agents can delegate tasks and ask questions to each other.
-   🛠️ **Tool Usage:** Equip agents with diverse tools to interact with the world.
-   🧠 **Memory:** Support for short-term, long-term, entity, user, and external memory.
-   📚 **Knowledge Base:** Integrate external knowledge sources for richer context.
-   📈 **Process Management:** Choose sequential or hierarchical execution modes.
-   🌊 **Flow Orchestration:** Build complex workflows connecting multiple crews.
-   📄 **Flexible Output:** Define output formats (raw, JSON, Pydantic models).
-   🔒 **Security:** Basic fingerprinting for component tracking.
-   💬 **CLI:** Easily create, run, train, test, and deploy crews.
-   🧩 **Extensibility:** Designed for easy integration and customization.

## Installation

Make sure you have Python >= 3.10 installed.

```bash
pip install crewai
```

For specific integrations (e.g., tools), you might need extra dependencies:

```bash
pip install 'crewai[tools]'
```

## Quick Start

Here's a simple example of a two-agent crew for researching a topic and writing a brief report:

```python
import os
from crewai import Agent, Task, Crew, Process

# Configure your LLM (e.g., OpenAI API key)
# Make sure to set the OPENAI_API_KEY environment variable
# os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

# Define Agents
researcher = Agent(
  role='Senior Research Analyst',
  goal='Uncover cutting-edge developments in AI and data science',
  backstory="""You work at a leading tech think tank.
  Your expertise lies in identifying emerging trends.
  You have a knack for dissecting complex data and presenting
  actionable insights.""",
  verbose=True,
  allow_delegation=False,
  # You can add tools like this: tools=[my_tool_instance]
  # llm=OpenAI(temperature=0.7, model_name="gpt-4") # Optional LLM configuration
)
writer = Agent(
  role='Tech Content Strategist',
  goal='Craft compelling content on tech advancements',
  backstory="""You are a renowned Content Strategist, known for
  your insightful and engaging articles.
  You transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=True
)

# Define Tasks
task1 = Task(
  description="""Conduct a comprehensive analysis of the latest advancements in AI in 2024.
  Identify key trends, breakthrough technologies, and potential industry impacts.""",
  expected_output="A full analysis report",
  agent=researcher
)

task2 = Task(
  description="""Using the insights provided, develop an engaging blog post that highlights the most significant AI advancements.
  Your post should be informative yet accessible, catering to a tech-savvy audience.
  Make it sound cool, avoid complex words so it doesn't sound like AI.""",
  expected_output="A 4-paragraph blog post",
  agent=writer
)

# Create and Run the Crew
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  process=Process.sequential, # Tasks will be executed sequentially
  verbose=2 # Can be 1 or 2; 0 is silent
)

# Execute the crew to see them collaborate
result = crew.kickoff()

print("######################")
print("Crew Execution Result:")
print(result)
```

**Note:** Ensure you have your LLM provider (like OpenAI) configured, typically by setting the appropriate environment variables (e.g., `OPENAI_API_KEY`).

## Key Components

### Agents

Agents are the core actors in CrewAI. They are defined by:

-   `role`: Their function within the crew (e.g., 'Researcher').
-   `goal`: Their primary objective.
-   `backstory`: Context about their experience and skills.
-   `llm`: The language model they use.
-   `tools`: A list of tools they can utilize.
-   `allow_delegation`: Whether they can delegate tasks to other agents.
-   `verbose`: Enables detailed logging of their actions.
-   `memory`: Enables memory features for the agent.

*(See `src/crewai/agent.py`)*

### Tasks

Tasks define the work to be done. Key attributes include:

-   `description`: What needs to be accomplished.
-   `expected_output`: The desired outcome or format of the result.
-   `agent`: The agent assigned to the task.
-   `tools`: Specific tools available for this task (overrides agent's default tools).
-   `context`: Output from other tasks to use as input.
-   `async_execution`: Whether the task can run concurrently.
-   `output_json`/`output_pydantic`: Define structured output formats.
-   `callback`: A function to call upon task completion.

*(See `src/crewai/task.py`)*

### Tools

Tools grant agents capabilities beyond language generation. CrewAI supports integration with various toolkits (like LangChain) and allows defining custom tools using the `BaseTool` class.

*(See `src/crewai/tools/`)*

### Crews

A Crew brings agents and tasks together. It defines:

-   `agents`: The list of agents in the crew.
-   `tasks`: The list of tasks to be executed.
-   `process`: The execution strategy (`sequential` or `hierarchical`).
-   `memory`: Enables shared memory for the crew.
-   `manager_llm`: The LLM used by the manager agent in hierarchical processes.
-   `verbose`: Controls the logging level for the crew's execution.

*(See `src/crewai/crew.py`)*

### Process

Defines how tasks are orchestrated within a crew:

-   **Sequential:** Tasks are executed one after another in the defined order.
-   **Hierarchical:** A manager agent coordinates task execution, potentially assigning tasks dynamically and reviewing results.

*(See `src/crewai/process.py`)*

### Memory

CrewAI supports different memory types to help agents retain information:

-   **Short-Term:** For immediate context within a task execution chain.
-   **Long-Term:** For persistent storage across different crew runs (useful for learning and improvement).
-   **Entity:** Stores structured information about specific entities.
-   **User:** Stores user-specific preferences or information (requires specific configuration, e.g., Mem0).
-   **External:** Integrates with external memory providers (e.g., Mem0).

*(See `src/crewai/memory/`)*

### Knowledge

Provide agents with access to external data sources like files (PDF, CSV, JSON, Text, Excel), strings, or custom sources through knowledge bases. Requires embedding configuration.

*(See `src/crewai/knowledge/`)*

### Flows

Flows allow for orchestrating complex workflows beyond a single crew. You can define dependencies, conditional execution, and routing between different methods or even different crews using `@start`, `@listen`, and `@router` decorators. Flows can be visualized using the `plot()` method.

*(See `src/crewai/flow/`)*

### LiteAgent

A simplified agent implementation (`src/crewai/lite_agent.py`) designed for less complex scenarios where autonomous delegation or advanced memory features are not required. It focuses on direct execution and tool usage based on provided messages.

## Command Line Interface (CLI)

CrewAI offers a powerful CLI to streamline your workflow:

-   `crewai create crew <name>`: Scaffold a new crew project structure.
-   `crewai create flow <name>`: Scaffold a new flow project structure.
-   `crewai run`: Run your crew or flow (detects type from `pyproject.toml`).
-   `crewai train`: Train your crew based on feedback (experimental).
-   `crewai test`: Evaluate crew performance over multiple iterations.
-   `crewai install`: Install project dependencies using `uv`.
-   `crewai update`: Migrate `pyproject.toml` from poetry to uv format.
-   `crewai deploy`: Manage deployments with CrewAI+.
-   `crewai tool`: Create, install, and publish custom tools.
-   `crewai flow`: Commands specific to managing flows (e.g., `kickoff`, `plot`, `add-crew`).
-   `crewai reset-memories`: Clear specific types of stored memory.
-   `crewai chat`: Start an interactive chat session with your crew.
-   `crewai signup`/`login`: Authenticate with CrewAI+.

*(See `src/crewai/cli/`)*

## Directory Structure Overview

The library is organized as follows:

```
└── crewai/                  # Main package directory
    ├── __init__.py          # Exports core classes (Agent, Task, Crew, Process, LLM, Flow, Knowledge)
    ├── agent.py             # Core Agent class implementation
    ├── crew.py              # Core Crew class implementation
    ├── lite_agent.py        # LiteAgent class implementation
    ├── llm.py               # LLM integration class (uses LiteLLM)
    ├── process.py           # Defines execution processes (sequential, hierarchical)
    ├── task.py              # Core Task class implementation
    ├── agents/              # Agent internals
    │   ├── agent_builder/   # Base classes and utilities for agent building
    │   ├── cache/           # Caching mechanisms for tools
    │   ├── parser.py        # Agent output parsing logic (ReAct style)
    │   ├── tools_handler.py # Handles tool usage within agents
    │   └── ...
    ├── cli/                 # Command Line Interface
    │   ├── templates/       # Project templates (crew, flow, tool)
    │   ├── authentication/  # CLI authentication logic
    │   ├── deploy/          # CLI deployment logic (CrewAI+)
    │   ├── tools/           # CLI tool management logic
    │   └── ...              # Other CLI commands (create, run, test, etc.)
    ├── crews/               # Crew-related utilities (e.g., CrewOutput)
    ├── flow/                # Flow orchestration logic
    │   ├── persistence/     # State persistence for flows
    │   ├── assets/          # Assets for flow visualization
    │   └── ...              # Flow class, visualizer, decorators, etc.
    ├── knowledge/           # Knowledge base functionality
    │   ├── embedder/        # Embedding model wrappers (e.g., FastEmbed)
    │   ├── source/          # Knowledge source types (files, strings, etc.)
    │   ├── storage/         # Storage backends (ChromaDB RAG, SQLite LTM)
    │   └── ...
    ├── llms/                # LLM base classes and specific integrations
    ├── memory/              # Memory systems
    │   ├── contextual/      # Context building from memories
    │   ├── entity/          # Entity memory
    │   ├── external/        # External memory integration
    │   ├── long_term/       # Long-term memory
    │   ├── short_term/      # Short-term memory
    │   ├── storage/         # Storage backends for memory
    │   └── user/            # User-specific memory (deprecated)
    ├── project/             # Utilities for defining crews within projects (CrewBase, annotations)
    ├── security/            # Security features (fingerprinting)
    ├── tasks/               # Task internals (conditional tasks, outputs)
    ├── telemetry/           # Anonymous usage data collection
    ├── tools/               # Tool definitions (BaseTool, agent tools, cache tools)
    ├── translations/        # Internationalization files (prompts, errors)
    ├── types/               # Custom Pydantic type definitions
    └── utilities/           # Common helper functions, constants, logging, etc.
        ├── evaluators/      # Crew/Task evaluation logic
        └── events/          # Event system for monitoring and integration
```

## Contributing

Contributions are welcome! Please read our contributing guidelines (`CONTRIBUTING.md` - *if available*) before submitting pull requests.

Key steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Write tests for your changes.
5.  Ensure all tests pass (`pytest`).
6.  Format your code (`ruff format .` and `ruff check --fix .`).
7.  Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Community & Support

-   **Discord:** [Join our Discord server](https://discord.com/invite/X4JWnZnxPb) for discussions and support.
-   **GitHub:** Report issues or contribute on our [GitHub repository](https://github.com/joaomdmoura/crewai).
-   **Documentation:** Find more detailed information in the [official documentation](https://docs.crewai.com).
-   **Twitter:** Follow [@joaomdmoura](https://twitter.com/joaomdmoura) for updates.
