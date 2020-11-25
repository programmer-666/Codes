import os
import hashlib
class checker:
    def readfile(self, fname):
        self.filename = fname
        with open(self.filename, "rb") as fop:
            self.filecont = fop.read()
    def gethash(self):
        return hashlib.md5(str(self.filecont).encode()).hexdigest()

class directory_processor:
    def __init__(self):
        self.__folders = set()
        self.__files = set()
        self.__other_folders = set()
        self.__folder_path = os.getcwd()
        self._files = self.__files
    def __List_FaF(self):
        for i in os.listdir():
            if os.path.isdir(os.path.abspath(i)):
                self.__folders.add(os.path.abspath(i))
            else:
                self.__files.add(os.path.abspath(i))
    def Process(self):
        os.chdir(str(self.__folder_path))
        self.__List_FaF()
        while len(self.__folders) != 0:
            self.__List_FaF()
            for f in self.__folders:
                os.chdir(f)
                self.__other_folders.add(f)
                self.__List_FaF()
                break
            self.__folders.remove(f)
os.chdir("/media/root/REPO/CodeStorage/")
x = directory_processor()
x.Process()
y = checker()
for i in x._files:
    y.readfile(i)
    print(i,y.gethash())