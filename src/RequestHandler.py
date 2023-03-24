import requests
from bs4 import BeautifulSoup
from src.RequestException import RequestException
from src.UnidadeCurricular import UnidadeCurricular
from src.UnidadeCurricularException import UnidadeCurricularException

"""
Este arquivo contém as funções que conectam no sistema da UFMS e verificam se o curso existe, bem como pegam as suas unidades curriculares.
A classe RequestException serve para levantar exceções caso de erro durante algum processo listado acima.
"""

def find_curso_by_id(codigo:int) -> bool:
	"""
	Função que verifica se um curso existe.
	Retorno: (bool) Verdadeiro, caso exista. Falso, caso não exista.
	"""
	link = f"https://ensino.ufms.br/cursos/view/{codigo}"
	response = requests.get(link)

	if response.status_code == 200:
		return True

	return False


def filter_nome(nome:str) -> str:
	"""
	Função que tira os "lixos" do nome da unidade curricular resgatado do sistema.
	Retorno: (str) Nome filtrado.
	"""
	filtered_nome = ''.join(letter + " " for letter in nome.split())
	filtered_nome = filtered_nome.replace("(OPT)", "").replace("(OBR)", "").replace(".", "").strip()
	return filtered_nome


def filter_carga_horaria(carga_horaria:str) -> int:
	"""
	Função que filtra a carga horária e a converte para inteiro.
	Retorno: (int) Carga horária.
	"""
	return int(carga_horaria[0:-1])


def is_optativa(nome:str) -> bool:
	"""
	Função que verifica se a matéria é optativa ou não.
	Retorno: (bool) Verdadeiro, caso seja. Falso, caso não seja.
	"""
	return '(OPT)' in nome


def get_pre_requisito(pre_requisito:str) -> "UnidadeCurricular":
	"""
	Função que busca um pré-requisito dentre as unidades curriculares registradas durante execução.
	Retorno: ("UnidadeCurricular") A própria unidade curricular ou 'None', caso não exista.
	"""
	return UnidadeCurricular.find_unidade_curricular_by_nome(pre_requisito)


def get_unidades_curriculares_from_curso(codigo:int) -> list["UnidadeCurricular"]:
	"""
	Função que busca as unidades curriculares dentro do sistema da UFMS.
	Retorno: (list["UnidadeCurricular"]) lista das unidades curriculares.
	"""

	# Essa parte verifica se o curso existe.
	if not find_curso_by_id(codigo):
		raise RequestException("CursoNotFound", f"O curso com código {codigo} não existe")

	# Caso o curso exista, ele busca o HTML relacionado aos pré-requisitos.
	all_subjects = requests.get(f'https://ensino.ufms.br/cursos/prerequisito/{codigo}')
	table = BeautifulSoup(all_subjects.content, 'html.parser').find('tbody') # Essa parte pega a tabela das unidades curriculares.

	# Essa parte verifica se existe uma tabela com as unidades.
	if isinstance(table, type(None)):
		raise RequestException("UnidadesCurricularesNotFound", f"Não foi possível achar as undiades curriculares do curso com código {codigo}")

	# Lista de unidades e pré-requisitos registrados
	unidades_curriculares = []
	pre_requisitos = []

	for tr in table.find_all('tr'):
		td = tr.find_all('td')

		# Caso a linha da tabela tenha mais de dois valores, é uma unidade curricular.
		if len(td) > 2:
			nome = filter_nome(td[0].get_text())
			carga_horaria = filter_carga_horaria(td[1].get_text())
			optativa = is_optativa(td[0].get_text())
			pre_requisito = filter_nome(td[2].get_text())

			# Criando unidade curricular.
			try:
				unidade_curricular = UnidadeCurricular(nome, carga_horaria, None, optativa)
				
				unidades_curriculares.append(unidade_curricular)
				pre_requisitos.append(pre_requisito)

			# Essa parte verifica se deu um erro durante a criação.
			# Alguns cursos tem unidades com nomes duplicados? Tipo SI (1907).
			except UnidadeCurricularException as e:
				print(f"Excessão em: {nome}")
				print(f"{e.valor}: {e.message}\n")

			finally:
				continue

	# Adicionando os pré-requisitos as unidades curriculares.
	for i in range(len(unidades_curriculares)):
		pre_requisito = get_pre_requisito(pre_requisitos[i])
		unidades_curriculares[i].pre_requisito = pre_requisito

	return unidades_curriculares
