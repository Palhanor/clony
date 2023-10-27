import os
# import sys
from clony import Clony

if __name__ == '__main__':
    # print(sys.getrecursionlimit())
    run = True
    while run:
        path = input("Insira a pasta a ser verificada: ")
        if not os.path.isdir(path):
            print("Input inválido! Insira o caminho para um diretório.")
            continue
        if path != "exit":
            clony = Clony(path)
            clony.list_dirs()
            clony.list_files()
            clony.find_duplicate()
        run = True if input("\nDeseja verificar outro diretório (s/n)? ").lower() != "n" else False
