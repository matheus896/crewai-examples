#!/usr/bin/env python
from random import randint
from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start
from .crews.artigo_crew.artigo_crew import ArtigoCrew


class ArtigoState(BaseModel):
    tema: str = ""
    artigo: str = ""


class ArtigoFlow(Flow[ArtigoState]):

    @start()
    def definir_tema(self):
        print("Definindo tema")
        self.state.tema = "Agentes Inteligentes em 2025"  # Você pode modificar o tema aqui

    @listen(definir_tema)
    def gerar_artigo(self):
        print("Gerando artigo")
        result = (
            ArtigoCrew()
            .crew()
            .kickoff(inputs={"tema": self.state.tema})
        )

        print("Artigo gerado", result.raw)
        self.state.artigo = result.raw

    @listen(gerar_artigo)
    def salvar_artigo(self):
        print("Salvando artigo")
        with open("artigo.md", "w", encoding= "utf-8") as f:
            f.write(self.state.artigo)


def kickoff():
    artigo_flow = ArtigoFlow()
    artigo_flow.kickoff()


def plot():
    artigo_flow = ArtigoFlow()
    artigo_flow.plot()


if __name__ == "__main__":
    kickoff()

# uv run kikcoff