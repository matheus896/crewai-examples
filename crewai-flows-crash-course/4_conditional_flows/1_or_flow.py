from crewai.flow.flow import Flow, listen, or_, start


class OrExampleFlow(Flow):

    @start()
    def start_method(self):
        print("Iniciando o fluxo")
        return "Olá do start method"

    @listen(start_method)
    def second_method(self):
        print("Second method")
        return "Olá do second method"

    @listen(or_(start_method, second_method))
    def logger(self, result):
        print(f"Logger: {result}")


flow = OrExampleFlow()
flow.kickoff()
