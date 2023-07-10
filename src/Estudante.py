# Imports locais
from src.Curso import Curso
from src.UnidadeCurricular import UnidadeCurricular
from src.EstudanteException import EstudanteException


class Estudante:
    '''
    Este arquivo contém a classe do estudante. Essa classe tem alguns atributos, como nome do estudante, o curso
    que está matriculado e uma lista das unidades curriculares que está cursando. O nome do estudante é apenas
    um diferencial, para facilitar a diferenciação entre os arquivos salvos localmente na máquina, enquanto o
    curso e as unidades cursadas servem para cumprir o principal objetivo do código: verificar quais matérias
    optativas um estudante pode cursar.
    '''


    def __init__(self, nome: str, curso: "Curso", unidades_cursadas: list["UnidadeCurricular"]) -> None:
        '''
        Construtor da classe Estudante.

        Parâmetros:
        - nome (str): Nome do estudante.
        - curso (Curso): Curso que o estudante está matriculado.
        - unidades_cursadas (list[UnidadeCurricular]): Lista de unidades curriculares cursadas.

        Retorno:
        - None.
        '''
        self.nome              = nome
        self.curso             = curso
        self.unidades_cursadas = unidades_cursadas


    def printInfo(self) -> None:
        '''
        Método para printar as informações do estudante.
        
        Parâmetros:
        - None.

        Retorno:
        - None.
        '''
        print(f"Estudante: {self.nome:<50}")
        print(f"Curso: {f'{self.curso}':<50}")
        for index, unidade_curricular in enumerate(self.unidades_cursadas):
            print(f"{f'{unidade_curricular}':<50}")


    @property
    def nome(self) -> str:
        '''
        Getter para o nome do estudante.

        Parâmetros:
        - None.

        Retorno:
        - nome (str): Nome do estudante.
        '''
        return self._nome


    @nome.setter
    def nome(self, nome: str) -> None:
        '''
        Setter para o nome do estudante.

        Parâmetros:
        - nome (str): Nome do estudante.

        Retorno:
        - None.
        '''
        if not isinstance(nome, str):
            raise EstudanteException("NomeNotStr", "O nome informado não é uma string")

        if nome == "":
            raise EstudanteException("NomeIsEmpty", "O nome informado está vazio.")

        self._nome = nome


    @property
    def curso(self) -> "Curso":
        '''
        Getter para o curso que o estudante está cursando.

        Parâmetros:
        - None.

        Retorno:
        - curso (Curso): Curso que o estudante está cursando.
        '''
        return self._curso


    @curso.setter
    def curso(self, curso: "Curso") -> None:
        '''
        Setter para o curso que o estudante está cursando.

        Parâmetros:
        - curso (Curso): Curso que o estudante está cursando

        Retorno:
        - None.
        '''
        if not isinstance(curso, Curso):
            raise EstudanteException("CursoInvalido", "O curso informado é inválido.")

        self._curso  = curso
    

    @property
    def unidades_cursadas(self) -> list["UnidadeCurricular"]:
        '''
        Getter para a lista de unidades curriculares já cursadas pelo estudante.

        Parâmetros:
        - None.

        Retorno:
        - unidades_cursadas (list[UnidadeCurricular]): Lista das unidades curriculares cursadas pelo estudante.
        '''
        return self._unidades_cursadas
    

    @unidades_cursadas.setter
    def unidades_cursadas(self, unidades_cursadas: list["UnidadeCurricular"]) -> None:
        '''
        Setter para a lista de unidades curriculares já cursadas pelo estudante.

        Parâmetros:
        - unidades_cursadas (list[UnidadeCurricular]): Lista de unidades curriculares já cursadas pelo estudante.

        Retorno:
        - None.
        '''
        if not isinstance(unidades_cursadas, list):
            raise EstudanteException("UnidadesCursadasInvalidas", "As unidades curriculares informadas são inválidas.")

        if not all(isinstance(unidade_curricular, UnidadeCurricular) for unidade_curricular in unidades_cursadas):
            raise EstudanteException("UnidadesCursadasInvalidas", "Nem todas as unidades curriculares são válidas.")

        self._unidades_cursadas = unidades_cursadas


    def add_unidade_curricular(self, unidade_curricular: "UnidadeCurricular") -> None:
        '''
        Método para adicionar uma unidade curricular para a lista de unidades curriculares cursadas.

        Parâmetros:
        - unidade_curricular (UnidadeCurricular): Unidade curricular que se deseja marcar como cursada.

        Retorno:
        - None.
        '''
        if not isinstance(unidade_curricular, UnidadeCurricular):
            raise EstudanteException("UnidadeCurricularInvalida", "A unidade curricular informada é inválida.")

        if unidade_curricular in self.unidades_cursadas:
            raise EstudanteException("UnidadeCurricularJaCursada", "A unidade curricular informada já foi cursada.")

        self.unidades_cursadas.append(unidade_curricular)

    
    def del_unidade_curricular(self, unidade_curricular: "UnidadeCurricular") -> None:
        '''
        Método para remover unidade curricular da lista de unidades cursadas.

        Parâmetros:
        - unidade_curricular (UnidadeCurricular): Unidade curricular que se deseja remover da lista.

        Retorno:
        - None.
        '''
        if not isinstance(unidade_curricular, UnidadeCurricular):
            raise EstudanteException("UnidadeCurricularInvalida", "A unidade curricular informada é inválida.")

        if unidade_curricular in self.unidades_cursadas:
            self.unidades_cursadas.remove(unidade_curricular)