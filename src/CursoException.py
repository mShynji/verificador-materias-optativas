class CursoException(Exception):
	def __init__(self, valor:str, message:str):
		self.valor = valor
		self.message = message
		super().__init__(self.message)