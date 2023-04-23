# import configparser
# import locale
# import fileinput
import os
# from datetime import datetime
# from enum import IntEnum, auto
# from pathlib import Path

MAX_BOOKS: int = 73  # Maksymalna ilość ksiąg

# ----- Klasa tłumaczeń ItemTrans -----
class ItemTrans:
    def __init__(self, _pathtr: str):
        self.namepathtr = _pathtr
        self.books: int = []  # Tablica ksiąg
        self.fileh = None
        #  Odczyt nazwy tłumaczenia z pierwszej linijki pliku
        try:
            self.fileh = open(self.namepathtr, "rt", encoding="utf-8")
            self.infotr = self.fileh.readline().strip("\n")  # opis
            self.__readallbooks__()
        finally:
            self.fileh.close()

    def __readallbooks__(self):  # Metoda prywatna
        #  Odczyt poszczególnych ksiąg
        # for coutbooks in range(1, MAX_BOOKS):
        #     for strtext in self.fileh:
        #         if int(strtext[0:3]) == coutbooks:
        #             print("{}".format(strtext.strip("\n")))
        #             break
        strtext = self.fileh.readline() # .strip("\n")
        for coutbooks in range(1, MAX_BOOKS):
            while strtext:
                if int(strtext[0:3]) == coutbooks:
                    self.books.append(self.fileh.tell() - len(strtext) - 5)
                    # print("{}-{} - {}".format(len(strtext), self.fileh.tell(), strtext.strip("\n")))
                    break
                strtext = self.fileh.readline() # .strip("\n")

# ----- Klasa główna MyBiblePyClass -----
class MyBiblePyClass:
    # Konstruktor
    def __init__(self, _pathtrdir: str):
        # Private
        self.__version: str = "0.1"
        # Public
        self.pathtrdir: str = _pathtrdir
        self.filenames = []  # Tablica
        self.itemstr: ItemTrans = []

        for myfilenames in os.listdir(self.pathtrdir):
            if myfilenames.endswith(".pltmb"):  # filtr
                myfilenames = os.path.join(self.pathtrdir, myfilenames)
                self.filenames.append(myfilenames)
                self.itemstr.append(ItemTrans(myfilenames))  # Dodawanie do tablicy objektów tłumaczenia

    def readtext(self, _itrans: int, _ibook: int, _ichapt: int, _ivers: int):
        if _itrans >= len(self.filenames):
            return  # Jeśli przekroczono numer tłumaczenia

        mytranslate: str = self.itemstr[_itrans].namepathtr
        file = None
        strtext = None
        try:
            file = open(mytranslate, "rt", encoding="utf-8")
            file.readline().strip("\n")  # opis

            for strtext in file:  # range(31168):
                strtext = strtext.rstrip("\n")
                if strtext == "":
                    break
                rfulladress = strtext[0:9]
                ibook = int(rfulladress[0:3])
                ichapt = int(rfulladress[3:6])
                ivers = int(rfulladress[6:9])
                if ibook == _ibook and ichapt == _ichapt and ivers == _ivers:
                    break
        finally:
            file.close()

        return strtext[10:]
