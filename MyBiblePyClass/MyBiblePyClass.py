import configparser
import locale
import os
from datetime import datetime
from enum import IntEnum, auto
from pathlib import Path

class MyBiblePyClass:
    # Konstruktor
    def __init__(self, _pathTrDir:str):
        # Private
        self.__version:str = "0.1"
        # Public
        self.pathTrDir:str = _pathTrDir
        self.filenames = [] # Tablica

        for myfilenames in os.listdir(self.pathTrDir):
            if myfilenames.endswith(".pltmb"): # filtr
                myfilenames = os.path.join(self.pathTrDir, myfilenames)
                self.filenames.append(myfilenames)

    def readText(self, _iTrans:int, _iBook:int, _iChapt:int, _iVers:int):
        if _iTrans >= len(self.filenames): return # Jeśli przekroczono numer tłumaczenia

        file = open(self.filenames[_iTrans], "rt", encoding="utf-8")
        file.readline().strip("\n") # opis

        for strText in  file: # range(31168):
            strText = strText.rstrip("\n")
            if strText == "":
                break
            rFullAdress = strText[0:9]
            iBook = int(rFullAdress[0:3])
            iChapt = int(rFullAdress[3:6])
            iVers = int(rFullAdress[6:9])
            if iBook == _iBook and iChapt == _iChapt and iVers == _iVers:
                break

        file.close()
        return strText[10:]




