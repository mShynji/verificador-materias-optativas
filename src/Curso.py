import RequestHandler as RH
from CursoException import CursoException
from RequestException import RequestException
from UnidadeCurricular import UnidadeCurricular
from UnidadeCurricularException import UnidadeCurricularException

class Curso:
	def __init__(self, codigo:int) -> None:
		if not RH.find_curso_by_id(codigo):
			raise RequestException("CursoNotFound", f"O curso com código {codigo} não existe")

		self.codigo(codigo)
		self.unidades_curriculares(self.codigo)


	@property
	def codigo(self) -> int:
		return self._codigo


	@property
	def unidades_curriculares(self) -> list["UnidadeCurricular"]:
		return self._unidades_curriculares


	@codigo.setter
	def codigo(self, codigo:int) -> None:
		if not isinstance(codigo, int):
			raise CursoException("CodigoNotInt", "O código não é um inteiro")

		self._codigo = codigo

	@unidades_curriculares.setter
	def unidades_curriculares(self, codigo:int) -> None:
		unidades_curriculares = RH.get_unidades_curriculares_from_curso(codigo)

		self._unidades_curriculares = unidades_curriculares
	
