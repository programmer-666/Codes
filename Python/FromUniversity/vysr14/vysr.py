#/usr/bin/python3
#-*- coding: utf-8 -*-
#vysr.py
import os, random
class vysr:
    # Details #
    __name__ = "vysr"
    __version__ = 1.4
    __author__ = "[Programmer-666]"
    __info__ = __name__+" V"+str(__version__)+" "+__author__+"\n"+"""Vysr a XOR based encryption program."""
    # Details #
    def __init__(self, key, sID):
        self.__key = key
        self.__sID = sID
        # Lists #
        self.__listed_file_content = list()
        self.__semi_encrypted_listed_file = list()
        self.__encrypted_file = list()
        # Lists #
    def EncDec(self, filename):
        # defs
        self.fileName = filename
        # file reading
        with open(self.fileName) as ofile:
            self.__readed_file = ofile.read()
        print(self.fileName)
        for i in self.__readed_file:
            self.__listed_file_content.append(i)
        # enc or dec
        for i in self.__listed_file_content:
            self.__semi_encrypted_listed_file.append(chr(self.__key^ord(i)))
        self.__semi_encrypted_listed_file.reverse()
        self.__enc_sID = (ord(self.__sID[0])^ord(self.__sID[1]))^(ord(self.__sID[2])^ord(self.__sID[3]))
        for a in self.__semi_encrypted_listed_file:
            self.__encrypted_file.append(chr(self.__enc_sID^ord(a)))
        # file writing
        if self.fileName[len(self.fileName)-1] == "v":
            with open(self.fileName[:len(self.fileName)-2],"w") as ofile:
                for i in self.__encrypted_file:
                    ofile.write(i)
        else:
            with open(self.fileName+".v","w") as ofile:
                for i in self.__encrypted_file:
                    ofile.write(i)
        # file delete
        os.remove(self.fileName) 
class directory_processor:
    def __init__(self, key, sID, FolderPath):
        self.__key = key
        self.__sID = sID
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
                if i.endswith("png") or i.endswith("docks") or i.endswith("docx") or i.endswith("pdf") or i.endswith("ppt") or i.endswith("mime") or i.endswith("mp4") or i.endswith("mp3") or i.endswith("wbm") or i.endswith("gif") or i.endswith("png") or i.endswith("jpg") or i.endswith("jpeg"):
                    pass
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
        for x in self.__files:
            p = vysr(self.__key, self.__sID)
            if x[-7:] != "vysr.py":
                p.EncDec(x)
# INTRO #
banner = f"""                         
`7M'   `MF'`7M'   `MF',pP"Ybd `7Mb,od8 
  VA   ,V    VA   ,V  8I   `"   MM' "' 
   VA ,V      VA ,V   `YMMMa.   MM     
    VVV        VVV    L.   I8   MM     
     W         ,V     M9mmmP' .JMML.   
              ,V                       
           OOb"                         {vysr.__version__}"""
menu = """  
1: Info
2: Encdec (Encrypt-Decrypt)
0: Exit
 """
# INTRO #
def ccl():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
# MENU #
while True:
    ccl()
    print(f"{banner}\n{menu}")
    sn = input()
    if sn == "1":
        ccl()
        print(f"{banner}\n")
        print(vysr.__info__)
        input()
    elif sn == "2":
        ccl()
        print(f"{banner}\n")
        fdir = input(f"Specify a file directory ({os.getcwd()}): ")
        ky = int(input(f"Key ({fdir}): "))
        sid = input(f"Secret ID [4 char]({fdir, ky}): ")
        p = directory_processor(ky, sid, fdir)
        f = input(f"Start process? (Y/n): ")
        if f == "Y":
            p.Process()
            ccl()
            print("Done")
            break
    elif sn == "0":
        ccl()
        quit()
# MENU #