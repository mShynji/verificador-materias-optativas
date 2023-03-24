from os import name, system
from src.Curso import Curso
from src.CursoException import CursoException
from src.RequestException import RequestException
from src.UnidadeCurricular import UnidadeCurricular
from src.UnidadeCurricularException import UnidadeCurricularException

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')


def get_codigo_curso() -> int:
	codigo_curso = None

	while isinstance(codigo_curso, type(None)):
		try:
			codigo_curso = int(input('Informe o código do seu curso:. '))

		except ValueError:
			codigo_curso = None
			print('O código precisa ser um inteiro com 4 digitos!\n')

			continue

	return codigo_curso


def get_curso(codigo_curso) -> "Curso":
	curso = None

	try:
		curso = Curso(codigo_curso)
	except (RequestException, UnidadeCurricularException) as e:
		print(f"\n({e.__class__.__name__})")
		print(f"{e.valor}: {e.message}\n")
	except CursoException as e:
		print(f"\n({e.__class__.__name__})")
		print(f"{e.valor}: {e.message}\n")
		return

	return curso


def main():
	clear()

	curso = None

	while isinstance(curso, type(None)):
		codigo_curso = get_codigo_curso()
		curso = get_curso(codigo_curso)

	clear()

	print("Lista de unidades curriculares do curso:\n")
	for unidade_curricular in curso.unidades_curriculares:
		if unidade_curricular.optativa:
			print(unidade_curricular)


if __name__ == '__main__':
	try:
		main()
	
	except (EOFError, KeyboardInterrupt):
		print('\n\nPrograma finalizado de maneira inesperada!')
	
	finally:
		print('\nObrigado por usar o programa.')