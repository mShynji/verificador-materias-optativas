# Imports locais
from src.CursoException import CursoException
from src.UnidadeCurricular import UnidadeCurricular


class Curso:
    '''
    Este arquivo contém a classe do curso, responsável por armazenar suas respectivas
    unidades curriculares para consulta.

    Essa classe dispõe dos seguintes atributos: id, nome e matriz_curricular. O id é necessário
    para obter as unidades curriculares no site da UFMS. O nome é utilizado para melhor identificação
    por parte do usuário. A matriz_curricular guarda a relação das unidades curriculares do curso,
    tanto cada unidade individualmente, bem como suas dependências, carga horária e afins.
    '''


    def __init__(self, id: int, nome: str, matriz_curricular: list["UnidadeCurricular"]) -> None:
        '''
        Construtor da classe Curso.

        Parâmetros:
        - id (int): Id do curso.
        - nome (str): Nome do curso.
        - matriz_curricular (list[UnidadeCurricular]): Matriz curricular do curso.

        Retorno:
        - None.
        '''
        self.id                = id
        self.nome              = nome
        self.matriz_curricular = matriz_curricular


    def __str__(self) -> str:
        '''
        Método chamado quando uma objeto da classe é chamado através do print().
        
        Parâmetros:
        - None.

        Retorno:
        - (str): Id e nome do curso.
        '''
        return f"({self.id}) {self.nome}"

    
    def printInfo(self) -> None:
        '''
        Método para printar as informações do curso:

        Parâmetros:
        - None.

        Retorno:
        - None.
        '''
        print(f"Curso: {f'{self}':<50}")
        print(f"Número de unidades curriculares: {len(self.matriz_curricular)}")
        for index, unidade_curricular in enumerate(self.matriz_curricular):
            print(f"{f'{unidade_curricular}':<50}")


    @property
    def id(self) -> int:
        '''
        Getter para o id do curso.
        
        Parâmetros:
        - None.

        Retorno:
        - id (int): Id do curso.
        '''
        return self._id


    @id.setter
    def id(self, id: int) -> None:
        '''
        Setter para o id do curso.
        
        Parâmetros:
        - id (int): Id do curso.
        
        Retorno:
        - None.
        '''
        if not isinstance(id, int):
            raise CursoException("IdNotInt", "O Id do curso informado não é válido.")
        
        self._id = id


    @property
    def nome(self) -> str:
        '''
        Getter para o nome do curso.

        Parâmetros:
        - None.

        Retorno:
        - nome (str): Nome do curso.
        '''
        return self._nome


    @nome.setter
    def nome(self, nome: str) -> None:
        '''
        Setter para o nome do curso.

        Parâmetros:
        - nome (str): Nome do curso.
        
        Retorno:
        - None.
        '''
        if not isinstance(nome, str):
            raise CursoException("NomeNotStr", "O nome do curso informado não é válido.")

        if nome == "":
            raise CursoException("NomeIsEmpty", "O nome do curso está vazio.")

        self._nome = nome

    
    @property
    def matriz_curricular(self) -> list["UnidadeCurricular"]:
        '''
        Getter para a matriz curricular do curso.

        Parâmetros:
        - None.

        Retorno:
        - matriz_curricular (list[UnidadeCurricular]): Matriz curricular do curso.
        '''
        return self._matriz_curricular

    
    @matriz_curricular.setter
    def matriz_curricular(self, matriz_curricular: list["UnidadeCurricular"]) -> None:
        '''
        Setter para matriz curricular do curso.

        Parâmetros:
        - matriz_curricular (list[UnidadeCurricular]): Matriz curricular do curso.

        Retorno:
        - None.
        '''
        if not isinstance(matriz_curricular, list):
            raise CursoException("UnidadesCurricularesInvalidas", "As unidades curriculares informadas são inválidas.")

        if not all(isinstance(unidade_curricular, UnidadeCurricular) for unidade_curricular in matriz_curricular):
            raise CursoException("UnidadesCurricularesInvalidas", "Nem todas as unidades curriculares são válidas.")

        self._matriz_curricular = matriz_curricular

    
    def add_unidade_curricular(self, unidade_curricular: "UnidadeCurricular") -> None:
        '''
        Método que adiciona uma unidade curricular para a matriz do curso.

        Parâmetros:
        - unidade_curricular (UnidadeCurricular): Unidade a ser adicionada.

        Retorno:
        - None.
        '''
        if not isinstance(unidade_curricular, UnidadeCurricular):
            raise CursoException("UnidadeCurricularInvalida", "A unidade curricular informada é inválida.")
        
        if unidade_curricular in self.matriz_curricular:
            raise CursoException("UnidadeCurricularJaAdicionada", "A unidade curricular já está presente na matriz.")

        self.matriz_curricular.append(unidade_curricular)

    
    def del_unidade_curricular(self, unidade_curricular: "UnidadeCurricular") -> None:
        '''
        Método para remover uma unidade curricular da matriz do curso.
        
        Parâmetros:
        - unidade_curricular (UnidadeCurricular): Unidade a ser removida.

        Retorno:
        - None.
        '''
        if not isinstance(unidade_curricular, UnidadeCurricular):
            raise CursoException("UnidadeCurricularInvalida", "A unidade curricular informada é inválida.")

        if unidade_curricular in self.matriz_curricular:
            self.matriz_curricular.remove(unidade_curricular)