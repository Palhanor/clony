from clony import Clony

if __name__ == '__main__':
    path = input("Insira a pasta a ser verificada: ")
    clony = Clony(path)
    print("DIRETÓRIOS VASCULHADOS")
    [print(i) for i in clony.dir_list]
    print("\nARQUIVOS AVALIADOS")
    [print(i) for i in clony.file_list]
    print("\nCÓPIAS ENCONTRADAS")
    clony.find_duplicate()

    input("\nPressione qualquer tecla para finalizar o programa...")
