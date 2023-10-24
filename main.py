# TODO: Ver como tratar arquivos triplicados...

import os
import hashlib

class Clony:
    def __init__(self, origin):
        self.results = []
        self.position = 0
        self.origin = origin
        self.dir_list = self._get_all_dirs(self.origin, [])
        self.file_list = self._get_all_files()

    def _get_all_dirs(self, origin, dir_list):
        child_directories = [d for d in os.listdir(origin)
                             if os.path.isdir(os.path.join(origin, d))]
        for directory in child_directories:
            dir_list.append(os.path.join(origin, directory))
        while self.position < len(dir_list):
            self.position += 1
            self._get_all_dirs(dir_list[self.position-1], dir_list)
        return dir_list

    def _get_all_files(self):
        all_files = [os.path.join(self.origin, f)
                     for f in os.listdir(self.origin)
                     if os.path.isfile(os.path.join(self.origin, f))]
        for directory in self.dir_list:
            for file in os.listdir(directory):
                if os.path.isfile(os.path.join(directory, file)):
                    all_files.append(os.path.join(directory, file))
        return all_files

    def _list_files(self):
        BUF_SIZE = 65536
        for file in self.file_list:
            sha1 = hashlib.sha256()
            with open(file, 'rb') as f:
                while True:
                    data = f.read(BUF_SIZE)
                    if not data:
                        break
                    sha1.update(data)
            self.results.append({"path": file, "hash": sha1.hexdigest()})

    def find_duplicate(self):
        self._list_files()
        for i, file1 in enumerate(self.results):
            for file2 in self.results[i + 1:]:
                if file1["hash"] == file2["hash"]:
                    print(f"Hash: {file1['hash']}\n\t{file1['path']}\n\t{file2['path']}\n")

if __name__ == '__main__':
    path = input("Insira a pasta a ser verificada: ")
    clony = Clony(path)
    print("DIRETÓRIOS VASCULHADOS")
    [print(i) for i in clony.dir_list]
    print("\nARQUIVOS AVALIADOS")
    [print(i) for i in clony.file_list]
    print("\nCÓPIAS ENCONTRADAS")
    clony.find_duplicate()