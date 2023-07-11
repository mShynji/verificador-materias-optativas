# Imports de bibliotecas externas
import requests
from bs4 import BeautifulSoup

# Imports locais
from src.Curso import Curso
from src.CursoException import CursoException
from src.UnidadeCurricular import UnidadeCurricular


def exists(codigo: int) -> bool:
    '''
    Função que procura o código de um curso no site da UFMS e retorna se ele existe ou não.

    Parâmetros:
    - codigo (int): Código do curso.

    Retorno:
    - (bool): True se existe, False se não existe.
    '''
    link = f"https://ensino.ufms.br/cursos/view/{codigo}"
    response = requests.get(link)

    return (True if response.status_code == 200 else False)


def filtrarNome(nome: str) -> str:
    '''
    Função que filtra o nome da UC dentro da tabela da matriz curricular do curso.

    Parâmetro:
    - nome (str): Nome da unidade curricular "sujo".

    Retorno:
    - nome_filtrado (str): Nome sem os "lixos".
    '''
    nome_filtrado = ''.join(letter + " " for letter in nome.split())
    nome_filtrado = nome_filtrado.replace("(OPT)", "").replace("(OBR)", "").replace(".", "").strip()
    return nome_filtrado


def filtrarCargaHoraria(carga_horaria: str) -> int:
    '''
    Função que filtra a carga horária da UC.

    Parâmetro:
    - carga_horaria (str): Carga horária da maneira que está na tabela da matriz curricular.

    Retorno:
    - carga_horaria (int): Remove a letra 'h' do final e converte a variável para inteiro.
    '''
    return int(carga_horaria[0:-1])


def isObrigatoria(nome: str) -> str:
    '''
    Função que verifica o status de obrigatoriedade da unidade curricular.

    Parâmetros:
    - nome (str): Nome da UC na tabela de matriz curricular.

    Retorno:
    - (bool): True se for obrigatório, False se for optativa.
    '''
    return "(OBR)" in nome


def scrapeMatrizCurricular(codigo: int) -> list["UnidadeCurricular"]:
    '''
    Função responsável por organizar as informações da matriz curricular de um curso.

    Parâmetros:
    - codigo (int): Código do curso.

    Retorno:
    - matriz_curricular (list[UnidadeCurricular]): matriz curricular do curso.
    '''
    html = requests.get(f"https://ensino.ufms.br/cursos/prerequisito/{codigo}")
    table = BeautifulSoup(html.content, "html.parser").find("tbody")

    if isinstance(table, type(None)):
        return None

    pre_requisitos = []
    matriz_curricular = []

    '''
    Essa parte filtra cada coluna da tabela

    Um eve rant que eu tenho é que o jeito que a tabela foi construída no site da UFMS não é muito
    bom. É muito confuso e mal estruturado. Tem um monte de linha vazia e coluna vazia também. Foi um pouco
    complicado de fazer o web scraping nas tabelas dos cursos da Facom, que foi os que eu testei. Então tem
    a grande possibilidade de não funcionar para cursos de fora da Facom ou para cursos com PPC antigo.
    '''
    for tr in table.find_all('tr'):
        td = tr.find_all('td')

        if len(td) > 2:
            nome = filtrarNome(td[0].get_text())
            carga_horaria = filtrarCargaHoraria(td[1].get_text())
            pre_requisito = filtrarNome(td[2].get_text())
            obrigatoria = isObrigatoria(td[0].get_text())

            unidade_curricular = UnidadeCurricular(nome, carga_horaria, [], obrigatoria)

            matriz_curricular.append(unidade_curricular)
            pre_requisitos.append(pre_requisito)

    # Essa parte é responsável por adicionar os pré-requisitos de cada matéria do curso
    for i in range(len(matriz_curricular)):
        pre_requisito = ""
        
        for j in range(len(matriz_curricular)):
            if matriz_curricular[j].nome == pre_requisitos[i]:
                pre_requisito = matriz_curricular[i]
                break

        if isinstance(pre_requisito, UnidadeCurricular):
            matriz_curricular[i].add_pre_requisito(pre_requisito)

    return matriz_curricular


def scrapeNomeCurso(codigo: int) -> str:
    '''
    Função que busca o nome do curso com base no seu código.

    Parâmetros:
    - codigo (int): Código do curso.

    Retorno:
    - nome (str): Nome do curso.
    '''
    link = f"https://ensino.ufms.br/cursos/view/{codigo}"
    html = requests.get(link)
    
    nome = BeautifulSoup(html.content, "html.parser").find("small").get_text()
    return " ".join(nome.split()[2:len(nome.split())])


def findCurso(codigo: int) -> "Curso":
    '''
    Função que busca as informações de um curso no site da UFMS.

    Parâmetros:
    - codigo (int): Código do curso.

    Retorno:
    - (Curso): curso.
    '''
    if not exists(codigo):
        raise CursoException("CursoDoesNotExist", f"O curso com código {codigo} não existe.")

    nome = scrapeNomeCurso(codigo)
    matriz_curricular = scrapeMatrizCurricular(codigo)

    if isinstance(matriz_curricular, type(None)):
        raise CursoException("MatrizCurricularNotFound", f"Não foi possível achar a matriz curricular do curso com código.")

    return Curso(codigo, nome, matriz_curricular)