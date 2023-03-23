import requests
from BS4 import BeautifulSoup
from RequestException import RequestException
from UnidadeCurricular import UnidadeCurricular

def find_curso_by_id(codigo:int) -> bool:
	link = f"https://ensino.ufms.br/cursos/view/{codigo}"
	response = requests.get(link)

	if requests.status_code == 200:
		return True

	return False

def filter_nome(nome:str) -> str:
	filtered_nome = ''.join(letter + " " for letter in nome.split())
	filtered_nome = filtered_nome.replace("(OPT)", "").replace("(OBR)", "").replace(".", "").strip()
	return filtered_nome

def filter_carga_horaria(carga_horaria:str) -> int:
	return int(carga_horaria[0:-1])

def is_optativa(nome:str) -> bool:
	return '(OPT)' in nome:

def get_pre_requisitos(pre_requisito:str) -> "UnidadeCurricular":
	unidades_curriculares = UnidadeCurricular.get_all_unidades_curriculares()

	for unidade_curricular in unidades_curriculares:
		if unidade_curricular.nome() == pre_requisito:
			return unidade_curricular

	return None

def get_unidades_curriculares_from_curso(codigo:int) -> list["UnidadeCurricular"]:
	if not find_curso_by_id(codigo):
		raise RequestException("CursoNotFound", f"O curso com código {codigo} não existe")

	all_subjects = requests.get(f'https://ensino.ufms.br/cursos/prerequisito/{codigo}')
	table = BeautifulSoup(all_subjects.content, 'html.parser').find('tbody')

	for tr in table.find_all('tr'):
		td = tr.find_all('td')

		if len(td) > 2:

			nome = filter_nome(td[0].get_text())
			carga_horaria = filter_carga_horaria(td[1].get_text())
			optativa = is_optativa(td[0].get_text())

			pre_requisitos = filter_nome(td[2].get_text())

			unidade_curricular = UnidadeCurricular(nome, carga_horaria, [], optativa)
			
			if pre_requisitos != 'Nenhum':
				unidade_curricular.add_pre_requisito(get_pre_requisitos(pre_requisitos))