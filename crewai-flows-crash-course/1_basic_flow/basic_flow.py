from crewai.flow.flow import Flow, listen, start
from dotenv import load_dotenv
from litellm import completion

load_dotenv()


class ExampleFlow(Flow):
    model = "gemini/gemini-1.5-flash-002"

    @start()
    def generate_city(self):
        print("Iniciando o fluxo")

        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": "Retorne o nome de uma cidade aleatória no mundo.",
                },
            ],
        )

        random_city = response["choices"][0]["message"]["content"]
        print(f"Random City: {random_city}")

        return random_city

    @listen(generate_city)
    def generate_fun_fact(self, random_city):
        print("Cidade aleatória recebida:", random_city)
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Conte-me um fato interessante sobre {random_city}",
                },
            ],
        )

        fun_fact = response["choices"][0]["message"]["content"]
        return fun_fact


flow = ExampleFlow()
result = flow.kickoff()

print(f"Fato engraçado gerado: {result}")
