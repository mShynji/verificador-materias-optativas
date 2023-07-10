# Imports de sistema
from os import name, system, listdir as os_name

# Imports locais
from src.Curso import Curso
from src.Estudante import Estudante
from src.UnidadeCurricular import UnidadeCurricular


def clear():
    '''
    Função responsável por limpar o terminal/cmd independente do sistema operacional do usuário.
    '''
    if os_name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def main():
    '''
    A main é responsável por operar como o menu do usuário para cadastrar e carregar perfis. 
    '''
    while True:
        clear()

        print(f"{f' Verificador de matérias optativas UFMS ':*^50}")
        print("")
        print("1. Criar perfil")
        print("2. Carregar perfil de arquivo")
        print("3. Mais informações")
        print("")
        print("0. Sair")

        try:
            ans = int(input(":. "))

            match(ans):
                case 1:
                    print("a")
                    input()
                case 2:
                    print("b")
                    input()
                case 3:
                    print("c")
                    input()
                case 0:
                    print("")
                    break
                case _:
                    print("d")
                    input()
        except ValueError:
            clear()
            print("[!] Favor informar apenas valores numéricos.")
            input()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n[!] Programa terminado de maneira inesperada!")
    finally:
        print("Programa terminado, até a próxima :)")