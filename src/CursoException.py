class CursoException(Exception):
    def __init__(self, valor: str, mensagem: str) -> None:
        self.valor    = valor
        self.mensagem = mensagem
        super().__init__(self.mensagem)