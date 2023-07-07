def EstudanteException(Exception):
    def __init__(self, valor:str, mensagem:str):
        self.valor    = valor
        self.mensagem = mensagem
        super().__init__(self.mensagem)