from clony import Clony

if __name__ == '__main__':
    path = input("Insira a pasta a ser verificada: ")
    clony = Clony(path)
    clony.list_dirs()
    clony.list_files()
    clony.find_duplicate()
    input("\nPressione qualquer tecla para finalizar o programa...")
