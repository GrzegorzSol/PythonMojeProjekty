import configparser
import locale
import os
from datetime import datetime
from enum import IntEnum, auto
from pathlib import Path

class MyBiblePyClass:
    # Konstruktor
    def __init__(self, _pathTrDir):
        # Private
        self.__version:str = "0.1"
        # Public
        self.pathTrDir:str = _pathTrDir
        self.filenames = [] # Tablica
        for myfilenames in os.listdir(self.pathTrDir):
            if myfilenames.endswith(".mbin"): # filtr
                myfilenames = os.path.join(self.pathTrDir, myfilenames)
                self.filenames.append(myfilenames)





