from langchain_ollama import ChatOllama

# Logo Mais Será Settado Configurações Globais

class Model:
    def __init__ (self, local_model, prod_model):
        self.local_model = local_model
        self.prod_model = prod_model

    def get_local_model(self):
        llm = ChatOllama(
            model = self.local_model,
            temperature = 0.4,
            num_predict = 200,
            # Outros Parâmetros ...
        )

        return llm
