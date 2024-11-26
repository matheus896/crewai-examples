from crewai.flow.flow import Flow, listen, start


class UntructuredExampleFlow(Flow):

    @start()
    def first_method(self):
        print("Iniciando o fluxo")
        print(f"Estado antes de first_method:\n{self.state}")
        self.state["message"] = "Olá do fluxo não estruturado"
        self.state["counter"] = 0

    @listen(first_method)
    def second_method(self):
        print(f"Estado antes do second_method:\n{self.state}")
        self.state["message"] += " - updated"
        self.state["counter"] += 1

    @listen(second_method)
    def third_method(self):
        print(f"Estado antes do third_method:\n{self.state}")
        self.state["message"] += " - updated again"
        self.state["counter"] += 1

        print(f"Estado depois do third_method: {self.state}")


flow = UntructuredExampleFlow()
flow.kickoff()

print(f"Estado final:\n{flow.state}")
