"""
Este arquivo contém uma classe que herda os atributos e métodos da classe Exception do Python.
A classe UnidadeCurricularException é uma classe para gerenciamento de excessões customizada,
possuindo um valor, que funciona como uma espécie de ID para a excessão, e uma mensagem, que
detalha a excessão.
"""

class UnidadeCurricularException(Exception):
	def __init__(self, valor:str, message:str):
		self.valor = valor
		self.message = message
		super.__init__(self.message)