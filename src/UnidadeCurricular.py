# Imports locais
from src.UnidadeCurricularException import UCException


class UnidadeCurricular:
    '''
    Este arquivo contém a classe responsável por representar as unidades curriculares de um curso.

    Essa classe tem os seguintes atributos: nome, carga_horaria, pre_requisitos e obrigatoria. Estes são os elementos
    mínimos necessários para a aplicação, pois assim é possível representar a relação de dependência entre
    certas unidades e outras.
    '''


    def __init__(self, nome: str, carga_horaria: int, pre_requisitos: list["UnidadeCurricular"], obrigatoria: bool) -> None:
        '''
        Construtor da classe UnidadeCurricular.

        Parâmetros:
        - nome (str): Nome da unidade.
        - carga_horaria (int): Carga horária da unidade.
        - pre_requisitos (list[UnidadeCurricular]): Unidades curriculares necessárias para cursar esta.

        Retorno:
        - None.
        '''
        self.nome           = nome
        self.carga_horaria  = carga_horaria
        self.pre_requisitos = pre_requisitos
        self.obrigatoria    = obrigatoria


    def __str__(self) -> str:
        '''
        Método chamado quando uma objeto da classe é chamado através do print().
        
        Parâmetros:
        - None.

        Retorno:
        - (str): Nome e carga horária da unidade curricular.
        '''
        return f"({'OBR' if self.obrigatoria else 'OPT'}) {self.nome} ({self.carga_horaria}h)"


    @property
    def nome(self) -> str:
        '''
        Getter para o nome da unidade curricular.

        Parâmetros:
        - None.

        Retorno:
        - nome (str): Nome da uc.
        '''
        return self._nome

    
    @nome.setter
    def nome(self, nome: str) -> None:
        '''
        Setter para o nome da unidade curricular.

        Parâmetros:
        - nome (str): Nome da uc.

        Retorno:
        - None
        '''
        if not isinstance(nome, str):
            raise UCException("NomeNotStr", "O nome da unidade curricular informada não é válido.")

        if nome == "":
            raise UCException("NomeIsEmpty", "O nome da unidade curricular está vazio.")
        
        self._nome = nome

    
    @property
    def carga_horaria(self) -> int:
        '''
        Getter para a carga horária da unidade curricular.

        Parâmetros:
        - None.

        Retorno:
        - carga_horaria (int): Carga horária da uc.
        '''
        return self._carga_horaria


    @carga_horaria.setter
    def carga_horaria(self, carga_horaria: int) -> None:
        '''
        Setter para a carga horária da unidade curricular.

        Parâmetros:
        - carga_horaria (int): Carga horária da UC.

        Retorno:
        - None.
        '''
        if not isinstance(carga_horaria, int):
            raise UCException("CargaHorariaIsNotInt", "A carga horária informada para o unidade não é válida.")
        
        if carga_horaria <= 0:
            raise UCException("CargaHorariaInvalida", "A carga horária informada para a unidade é inválida.")

        self._carga_horaria = carga_horaria


    @property
    def pre_requisitos(self) -> list["UnidadeCurricular"]:
        '''
        Getter para os pré-requisitos da unidade curricular.

        Parâmetros:
        - None.

        Retorno:
        - pre_requisitos (list[UnidadeCurricular]): Lista de pré-requisitos da UC.
        '''
        return self._pre_requisitos


    @pre_requisitos.setter
    def pre_requisitos(self, pre_requisitos: list["UnidadeCurricular"]) -> None:
        '''
        Setter dos pré-requisitos da unidade curricular.

        Parâmetros:
        - pre_requisitos (list[UnidadeCurricular]): Lista de pré-requisitos da UC.

        Retorno:
        - None.
        '''

        if not isinstance(pre_requisitos, list):
            raise UCException("PreRequisitosInvalidos", "Os pré-requisitos da unidade são inválidos.")

        if not all(isinstance(pre_requisito, UnidadeCurricular) for pre_requisito in pre_requisitos):
            raise UCException("PreRequisitosInvalidos", "Nem todos os pré-requisitos para a unidade são válidos.")

        self._pre_requisitos = pre_requisitos


    @property
    def obrigatoria(self) -> bool:
        '''
        Getter para o status de obrigatoriedade da unidade curricular.

        Parâmetros:
        - None.

        Retorno:
        - obrigatoria (bool): Booleano que representa se a UC é obrigatória ou não.
        '''
        return self._obrigatoria


    @obrigatoria.setter
    def obrigatoria(self, obrigatoria: bool) -> None:
        '''
        Setter para o status de obrigatoriedade da unidade curricular.

        Parâmetros:
        - obrigatoria (bool): Booleano que representa se a UC é obrigatória ou não.

        Retorno:
        - None.
        '''
        if not isinstance(obrigatoria, bool):
            raise UCException("ObrigatoriedadeNotBool", "A obrigatoriedade da unidade é inválida.")

        self._obrigatoria = obrigatoria


    def add_pre_requisito(self, pre_requisito: "UnidadeCurricular") -> None:
        '''
        Método que adiciona uma unidade curricular para a lista de pré-requisitos da UC.

        Parâmetros:
        - unidade_curricular (UnidadeCurricular): Unidade a ser adicionada.

        Retorno:
        - None.
        '''
        if not isinstance(pre_requisito, UnidadeCurricular):
            raise UCException("PreRequisitoInvalido", "O pré-requisito é inválido.")

        if pre_requisito in self.pre_requisitos:
            raise UCException("PreRequisitoJaAdicionado", "O pré-requisito já está presente na lista de pré-requisitos da unidade.")

        self.pre_requisitos.append(pre_requisito)


    def del_pre_requisito(self, pre_requisito: "UnidadeCurricular") -> None:
        '''
        Método que remove uma unidade curricular da lista de pré-requisitos da UC.

        Parâmetros:
        - unidade_curricular (UnidadeCurricular): Unidade a ser removida.

        Retorno:
        - None.
        '''
        if not isinstance(pre_requisito, UnidadeCurricular):
            raise UCException("PreRequisitoInvalido", "O pré-requisito é inválido.")

        if pre_requisito in self.pre_requisitos:
            self.pre_requisitos.append(pre_requisito)
