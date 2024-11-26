#!/usr/bin/env python
import asyncio
from typing import List

from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel
from write_a_book_with_flows.crews.write_book_chapter_crew.write_book_chapter_crew import (WriteBookChapterCrew,)
from write_a_book_with_flows.types import Chapter, ChapterOutline
from .crews.outline_book_crew.outline_crew import OutlineCrew
import os


class BookState(BaseModel):
    title: str = (
        "Prepare-se para 2025: O Ano dos Agentes Que Transformam Tudo"
    )
    book: List[Chapter] = []
    book_outline: List[ChapterOutline] = []
    topic: str = (
        "O Impacto dos Agentes em 2025"
    )
    goal: str = """
        O objetivo deste livro é fornecer uma visão detalhada de como os agentes impactarão diversas indústrias em 2025.
        Ele explorará as tendências emergentes, analisará avanços significativos e discutirá possíveis desenvolvimentos futuros.
        O livro visa preparar os leitores para as inovações que estão por vir, destacando as tecnologias de agentes de ponta.
    """


class BookFlow(Flow[BookState]):

    @start()
    def generate_book_outline(self):
        print("Kickoff the Book Outline Crew")
        output = (
            OutlineCrew()
            .crew()
            .kickoff(inputs={"topic": self.state.topic, "goal": self.state.goal})
        )

        chapters = output["chapters"]
        print("Chapters:", chapters)

        self.state.book_outline = chapters

    @listen(generate_book_outline)
    async def write_chapters(self):
        print("Writing Book Chapters")
        tasks = []

        async def write_single_chapter(chapter_outline):
            output = (
                WriteBookChapterCrew()
                .crew()
                .kickoff(
                    inputs={
                        "goal": self.state.goal,
                        "topic": self.state.topic,
                        "chapter_title": chapter_outline.title,
                        "chapter_description": chapter_outline.description,
                        "book_outline": [
                            chapter_outline.model_dump_json()
                            for chapter_outline in self.state.book_outline
                        ],
                    }
                )
            )
            title = output["title"]
            content = output["content"]
            chapter = Chapter(title=title, content=content)
            return chapter

        for chapter_outline in self.state.book_outline:
            print(f"Writing Chapter: {chapter_outline.title}")
            print(f"Description: {chapter_outline.description}")
            # Schedule each chapter writing task
            task = asyncio.create_task(write_single_chapter(chapter_outline))
            tasks.append(task)

        # Await all chapter writing tasks concurrently
        chapters = await asyncio.gather(*tasks)
        print("Newly generated chapters:", chapters)
        self.state.book.extend(chapters)

        print("Book Chapters", self.state.book)

    @listen(write_chapters)
    async def join_and_save_chapter(self):
        print("Joining and Saving Book Chapters")
        # Combine all chapters into a single markdown string
        book_content = []

        for chapter in self.state.book:
            # Add the chapter title as an H1 heading and content
            book_content.append(f"# {chapter.title}\n\n{chapter.content}")

        # Criar diretório de saída
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        # Criar nome do arquivo usando o título do livro
        file_name = f"{self.state.title}.md".replace(" ", "_")
        output_path = os.path.join(output_dir, file_name)

        # Salvar o conteúdo no arquivo
        with open(output_path, "w", encoding="utf-8") as file:
            for section in book_content:
                file.write(section)
                file.write("\n\n")

        print(f"Book saved as {output_path}")


def kickoff():
    poem_flow = BookFlow()
    poem_flow.kickoff()


def plot():
    poem_flow = BookFlow()
    poem_flow.plot()


if __name__ == "__main__":
    kickoff()

# cd C:\flow-crewai\crewai-flows-crash-course\6_write_a_book_with_flows\write_a_book_with_flows\src
# uv run kickoff
