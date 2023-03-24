from src.UnidadeCurricularException import UnidadeCurricularException

"""
Este arquivo contém uma classe que representa uma única unidade curricular.
A classe UnidadeCurricular possuí um nome, carga horária (em horas) e uma lista de pré-requisitos.
A classe UnidadeCurricularException é utilizada para levantar uma exceção no código.
"""

class UnidadeCurricular:
	unidades_curriculares = [] # lista estática para guardar todas as unidades curriculares instanciadas durante a execução.

	def __init__(self, nome:str, carga_horaria:int, pre_requisito:"UnidadeCurricular", optativa:bool="False") -> None:
		"""
		Construtor da classe.
		Retorno: (None).
		"""

		# Essa parte levanta uma exceção caso exista outra unidade curricular com o mesmo nome.
		if UnidadeCurricular.find_unidade_curricular_by_nome(nome):
			raise UnidadeCurricularException("UnidadeCurricularExists", "A unidade curricular já existe")

		self.nome = nome
		self.carga_horaria = carga_horaria
		self.pre_requisito = pre_requisito
		self.optativa = optativa # Assume que não é optativa por default

		UnidadeCurricular.unidades_curriculares.append(self)
			

	def __str__(self) -> str:
		"""
		Método que retorna uma string quando chamam print(UnidadeCurricular).
		Retorno: (str) String com informações da unidade curriular.
		"""
		return f"{'(OPT)' if self.optativa else '(OBG)'} Nome={self.nome[:30]:<32} CargaHoraria={(str(self.carga_horaria)+'h'):<6} Pre-Requisito={(self.pre_requisito.nome[0:30] if self.pre_requisito else 'Nenhum'):<32}"


	@staticmethod
	def get_all_unidades_curriculares() -> list["UnidadeCurricular"]:
		"""
		Método estático que retorna todas as unidades curriculares gravadas durante a execução.
		Retorno: (list["UnidadeCurricular"]) lista de todas as unidades curiculares.
		"""
		return UnidadeCurricular.unidades_curriculares


	@staticmethod
	def find_unidade_curricular_by_nome(nome:str) -> "UnidadeCurricular":
		"""
		Método estático para achar a primeira unidade curricular com um certo nome.
		Retorno: ("UnidadeCurricular") Unidade curricular com o nome informado como parâmetro.
				 (None) Caso a unidade curricular não exista.
		"""
		unidades_curriculares = UnidadeCurricular.get_all_unidades_curriculares()

		# Essa parte do código assume que cada unidade curricular vai ter um nome único.
		# Caso, de algum jeito, tenham duas unidades com o mesmo nome, este método só retorna a primeira.
		for unidade_curricular in unidades_curriculares:
			if unidade_curricular.nome == nome:
				return unidade_curricular

		# Caso a unidade não exista, retorna nulo.
		return None


	@property
	def nome(self) -> str:
		"""
		Getter para o nome da unidade.
		Retorno: (str) nome do curso.
		"""
		return self._nome


	@property
	def carga_horaria(self) -> int:
		"""
		Getter para a carga horária da unidade.
		Retorno: (int) carga horária do curso.
		"""
		return self._carga_horaria


	@property
	def pre_requisito(self) -> "UnidadeCurricular":
		"""
		Getter para a lista de pré-requisitos.
		Retorno: ("UnidadeCurricular") pré-requisito do curso.
		"""
		return self._pre_requisito


	@property
	def optativa(self) -> bool:
		"""
		Getter para verificar se a matéria é optativa ou não.
		Retorno: (bool) True se matéria for optativa. False se não for.
		"""
		return self._optativa
	
	
	@nome.setter
	def nome(self, nome:str) -> None:
		"""
		Setter para o nome da unidade.
		Retorno: (None).
		"""

		# Essa parte do código levanta uma exceção caso o valor não seja uma string.
		if not isinstance(nome, str):
			raise UnidadeCurricularException("NomeNotStr", "O nome não é uma string")

		self._nome = nome


	@carga_horaria.setter
	def carga_horaria(self, carga_horaria:int) -> None:
		"""
		Setter para a carga horária da unidade.
		Retorno: (None).
		"""

		# Essa parte do código levanta uma exceção caso o valor não seja um inteiro.
		if not isinstance(carga_horaria, int):
			raise UnidadeCurricularException("CargaHorariaNotInt", "A carga horária não é um inteiro")

		self._carga_horaria = carga_horaria


	@pre_requisito.setter
	def pre_requisito(self, pre_requisito:"UnidadeCurricular") -> None:
		"""
		Setter para os pré-requisitos da unidade.
		Retorno: (None).
		"""

		# Essa parte do código verifica se o pré-requisito é uma unidade curricular ou None.
		if not isinstance(pre_requisito, (UnidadeCurricular, type(None))):
			print(f"{pre_requisito} + {type(pre_requisito)}")
			raise UnidadeCurricularException("PreRequisitoNotUnidadeCurricular", "O pré-requisito não é uma instância de UnidadeCurricular")

		self._pre_requisito = pre_requisito


	@optativa.setter
	def optativa(self, optativa:bool) -> None:
		"""
		Setter para saber se a matéria é optativa ou não.
		Retorno: (None)
		"""

		# Essa parte do código levanta uma exceção caso o valor não seja booleano.
		if not isinstance(optativa, bool):
			raise UnidadeCurricularException("OptativaNotBool", "Matéria precisa ser optativa ou não.")

		self._optativa = optativa


	def is_pre_requisito(self, pre_requisito:"UnidadeCurricular") -> bool:
		"""
		Método para verificar se um pré-requisito já faz parte dos pré-requisitos da matéria.
		Retorno: (bool) Verdadeiro, caso seja. False, caso não seja.
		"""
		return pre_requisito == self.pre_requisito