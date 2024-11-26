from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel


class ExampleState(BaseModel):
    counter: int = 0
    message: str = ""


class StructuredExampleFlow(Flow[ExampleState]):

    @start()
    def first_method(self):
        print("Iniciando o fluxo")
        print(f"Estado antes de first_method:\n{self.state}\n")
        self.state.message = "Hello from structured flow"
        self.state.counter += 1

    @listen(first_method)
    def second_method(self):
        print(f"Estado antes de second_method:\n{self.state}\n")
        self.state.counter += 1
        self.state.message += " - updated"

    @listen(second_method)
    def third_method(self):
        print(f"Estado antes de third_method:\n{self.state}\n")
        self.state.counter += 1
        self.state.message += " - updated again"

        print(f"State depois de third_method: {self.state}")


flow = StructuredExampleFlow()
flow.kickoff()

print(f"Estado Final:\n{flow.state}")
