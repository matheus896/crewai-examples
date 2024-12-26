from guardrails import Guard
from guardrails.hub import LLMCritic
from dotenv import load_dotenv
from crewai_tools import tool

# Carregando variáveis de ambiente
load_dotenv()

# Guardrails Validator
guard = Guard().use(
    LLMCritic,
    metrics={
        "informative": {
            "description": "An informative summary captures the main points of the input and is free of irrelevant details.",
            "threshold": 75,
        },
        "coherent": {
            "description": "A coherent summary is logically organized and easy to follow.",
            "threshold": 50,
        },
        "concise": {
            "description": "A concise summary is free of unnecessary repetition and wordiness.",
            "threshold": 50,
        },
        "engaging": {
            "description": "An engaging summary is interesting and holds the reader's attention.",
            "threshold": 50,
        },
    },
    max_score=100,
    llm_callable="cerebras/llama-3.3-70b",
    on_fail="exception",
)

@tool
def validate_summary(summary: str) -> str:
    """
    Valida um resumo usando Guardrails e retorna uma mensagem de aprovação ou falha.
    """
    try:
        guard.validate(summary)
        return "Resumo validado com sucesso! O resumo atende aos critérios de qualidade."
    except Exception as e:
        return f"Erro na validação: {str(e)}. O resumo não passou nos critérios."


