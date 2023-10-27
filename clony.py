import os
import hashlib

class Clony:
    def __init__(self, origin):
        self.results = {}
        self.colisions = set()
        self.position = 0
        self.origin = origin
        self.ignore = ["node_modules", "venv"]
        self.dir_list = self._get_all_dirs(self.origin, [])
        self.file_list = self._get_all_files()

    def _get_all_dirs(self, current_dir, dir_list):
        child_directories = [d for d in os.listdir(current_dir)
                             if os.path.isdir(os.path.join(current_dir, d)) and d not in self.ignore]
        for directory in child_directories:
            dir_list.append(os.path.join(current_dir, directory))
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
        BUF_SIZE = 65536  # bytes
        for file in self.file_list:
            sha256 = hashlib.sha256()
            with open(file, 'rb') as f:
                while True:
                    data = f.read(BUF_SIZE)
                    if not data:
                        break
                    sha256.update(data)
            self._insert_file(sha256.hexdigest(), file)

    def _insert_file(self, checksum, file):
        if checksum in self.results:
            self.results[checksum].append(file)
            self.colisions.add(checksum)
        else:
            self.results[checksum] = [file]

    def find_duplicate(self):
        self._list_files()
        print("\nCÓPIAS ENCONTRADAS:")
        for checksum in self.colisions:
            print(f"{len(self.results[checksum])} arquivos identicos: {checksum}")
            for file in self.results[checksum]:
                print(f"\t{file}")

    def list_dirs(self):
        print("\nDIRETÓRIOS VASCULHADOS:")
        [print(i) for i in self.dir_list]

    def list_files(self):
        print("\nARQUIVOS VERIFICADOS")
        [print(i) for i in self.file_list]
