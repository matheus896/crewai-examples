from typing import Type

from crewai_tools import BaseTool
from pydantic import BaseModel, Field


class CharacterCounterInput(BaseModel):
    """Esquema de entrada para CharacterCounterTool."""

    text: str = Field(..., description="A string para contar os caracteres.")

class CharacterCounterTool(BaseTool):
    name: str = "Character Counter Tool"
    description: str = "Conta o número de caracteres em uma string fornecida."
    args_schema: Type[BaseModel] = CharacterCounterInput

    def _run(self, text: str) -> str:
        character_count = len(text)
        return f"A string de entrada tem {character_count} caracteres."

