import src.RequestHandler as RH
from src.CursoException import CursoException
from src.RequestException import RequestException
from src.UnidadeCurricular import UnidadeCurricular

"""
Este arquivo contém uma classe que representa um único curso .
A classe curso tem um código e uma lista contendo as unidades curriculares relacionadas ao curso.
A classe CursoException é utilizada para levantar exeções no código.

O módulo RequestHandler lida com a conexão ao sistema da UFMS.
"""

class Curso:
	def __init__(self, codigo:int) -> None:
		"""
		Construtor da classe.
		Retorno: (None).
		"""

		# Essa parte do código verifica se o curso existe.
		if not RH.find_curso_by_id(codigo):
			raise RequestException("CursoNotFound", f"O curso com código {codigo} não existe")

		# Essa parte do código busca todas as matérias do curso listadas no sistema. (ensino.ufms.br)
		unidades_curriculares = RH.get_unidades_curriculares_from_curso(codigo)

		self.codigo = codigo
		self.unidades_curriculares = unidades_curriculares


	@property
	def codigo(self) -> int:
		"""
		Getter do código do curso.
		Retorno: (int) código do curso.
		"""
		return self._codigo


	@property
	def unidades_curriculares(self) -> list["UnidadeCurricular"]:
		"""
		Getter das unidades curriculares do curso.
		Retorno: (list["UnidadeCurricular"]) lista das unidades curriculares do curso.
		"""
		return self._unidades_curriculares


	@codigo.setter
	def codigo(self, codigo:int) -> None:
		"""
		Setter do código do curso.
		Retorno: (None);
		"""

		# Essa parte do código verifica se o código informado é um inteiro.
		if not isinstance(codigo, int):
			raise CursoException("CodigoNotInt", "O código não é um inteiro")

		self._codigo = codigo


	@unidades_curriculares.setter
	def unidades_curriculares(self, unidades_curriculares:list["UnidadeCurricular"]) -> None:
		"""
		Setter das unidades curriculares do curso.
		Retorno: (None).
		"""

		# Essa parte do código verifica se as unidades são uma lista.
		if not isinstance(unidades_curriculares, list):
			raise CursoException("UnidadesCurricularesNotList", "As unidades curriculares não são uma lista")

		# Essa parte do código verifica se todos os itens da lista são instâncias da classe UnidadeCurricular.
		if not all(isinstance(unidade_curricular, UnidadeCurricular) for unidade_curricular in unidades_curriculares):
			raise CursoException("NotAllUnidadesCurricularesAreInstanceOfUnidadeCurricular",
								 "Nem todos os itens das unidades curriculares são instâncias da classe UnidadeCurricular")

		self._unidades_curriculares = unidades_curriculares
	
