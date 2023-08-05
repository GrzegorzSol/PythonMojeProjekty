# import configparser
# import locale
# import fileinput
import os
# from datetime import datetime
from enum import IntEnum, auto
# from pathlib import Path
import fpdf

# from fpdf import FPDF

MAX_BOOKS: int = 73  # Maksymalna ilość ksiąg + 1

class EnumInfoAllBooks(IntEnum):
    # Znaczenie poszczególnych pól listy infoallbooks []
    eninfo_Number = 0
    eninfo_Fullname = auto()  # Pełna nazwa księgi
    eninfo_Smalname = auto()  # Skrócona nazwa księgi
    eninfo_Coutchapt = auto()  # Ilość rozdziałów w księdze

class EnumDecodeListText(IntEnum):
    # Znaczenie poszczególnych pól listy zwracanej przez metodę MyBiblePyClass.readtext
    endec_text = 0
    endec_trans = auto()
    endec_smalnamebook = auto()
    endec_book = auto()
    endec_chapt = auto()
    endec_vers = auto()


infoallbooks = [  # --- Stary Testament
    [1, "1 Mojżeszowa", "1Moj", 50],  # 0
    [2, "2 Mojżeszowa", "2Moj", 40],  # 1
    [3, "3 Mojżeszowa", "3Moj", 27],  # 2
    [4, "4 Księga Mojżeszowa", "4Moj", 36],  # 3
    [5, "5 Księga Mojżeszowa", "5Moj", 34],  # 4
    [6, "Księga Jozuego", "Joz", 24],  # 5
    [7, "Księga Sędziów", "Sędź", 21],  # 6
    [8, "Księga Rut", "Rut", 4],  # 7
    [9, "1 Księga Samuela", "1Sam", 31],  # 8
    [10, "2 Księga Samuela", "2Sam", 24],  # 9
    [11, "1 Księga Królewska", "1Król", 22],  # 10
    [12, "2 Księga Królewska", "2Król", 25],  # 11
    [13, "1 Księga Kronik", "1Kron", 29],  # 12
    [14, "2 Księga Kronik", "2Kron", 36],  # 13
    [15, "Księga Ezdrasza", "Ezdr", 10],  # 14
    [16, "Księga Nechemiasza", "Nech", 13],  # 15
    [17, "Księga Estery", "Est", 10],  # 16
    [18, "Księga Joba", "Job", 42],  # 17
    [19, "Księga Psalmów", "Ps", 150],  # 18
    [20, "Przypowieści Salomona", "Przyp", 31],  # 19
    [21, "Księga Kaznodziei Salomona", "Kazn", 12],  # 20
    [22, "Pieśni nad Pieśniami", "PnP", 8],  # 21
    [23, "Księga Izajasza", "Iz", 66],  # 22
    [24, "Księga Jeremiasza", "Jer", 52],  # 23
    [25, "Treny", "Tren", 5],  # 24
    [26, "Księga Ezechiela", "Ez", 48],  # 25
    [27, "Księga Daniela", "Dan", 14],  # 26
    [28, "Księga Ozeasza", "Oz", 14],  # 27
    [29, "Księga Joela", "Jo", 3],  # 28
    [30, "Księga Amosa", "Am", 9],  # 29
    [31, "Księga Abdiasza", "Abd", 1],  # 30
    [32, "Księga Jonasza", "Jon", 4],  # 31
    [33, "Księga Micheasza", "Mich", 7],  # 32
    [34, "Księga Nahuma", "Nah", 3],  # 33
    [35, "Księga Habakuka", "Hab", 3],  # 34
    [36, "Księga Sofoniasza", "Sof", 3],  # 35
    [37, "Księga Aggeusza", "Agg", 2],  # 36
    [38, "Księga Zachariasza", "Zach", 14],  # 37
    [39, "Księga Malachiasza", "Mal", 3],  # 38
    # --- Nowy Testament
    [40, "Ewangelia Mateusza", "Mt", 28],  # 39
    [41, "Ewangelia Marka", "Mk", 16],  # 40
    [42, "Ewangelia Łukasza", "Łk", 24],  # 41
    [43, "Ewangelia Jana", "Jan", 21],  # 42
    [44, "Dzieje Apostolskie", "DzAp", 28],  # 43
    [45, "List Pawła do Rzymian", "Rzym", 16],  # 44
    [46, "1 List Pawła do Koryntian", "1Kor", 16],  # 45
    [47, "2 List Pawła do Koryntian", "2Kor", 13],  # 46
    [48, "List Pawła do Galacjan", "Gal", 6],  # 47
    [49, "List Pawła do Efezjan", "Efez", 6],  # 48
    [50, "List Pawła do Filipian", "Filip", 4],  # 49
    [51, "List Pawła do Kolosan", "Kol", 4],  # 50
    [52, "1 List Pawła do Tesaloniczan", "1Tes", 5],  # 51
    [53, "2 List Pawła do Tesaloniczan", "2Tes", 3],  # 52
    [54, "1 List Pawła do Tymoteusza", "1Tym", 6],  # 53
    [55, "2 List Pawła do Tymoteusza", "2Tym", 4],  # 54
    [56, "List Pawła do Tytusa", "Tyt", 3],  # 55
    [57, "List Pawła do Filemona", "Filem", 1],  # 56
    [58, "List do Hebrajczyków", "Hbr", 13],  # 57
    [59, "List Jakuba", "Jak", 5],  # 58
    [60, "1 List Piotra", "1Pt", 5],  # 59
    [61, "2 List Piotra", "2Pt", 3],  # 60
    [62, "1 List Jana", "1Jan", 5],  # 61
    [63, "2 List Jana", "2Jan", 1],  # 62
    [64, "3 List Jana", "3Jan", 1],  # 63
    [65, "List Judy", "Jud", 1],  # 64
    [66, "Objawienie Jana", "Obj", 22],  # 65
    # --- Apokryfy
    [67, "Księga Tobiasza", "Tob", 14],  # 66
    [68, "Księga Judyty", "Judyt", 16],  # 67
    [69, "Księga I Machabejska", "1Mach", 16],  # 68
    [70, "Księga II Machabejska", "2Mach", 15],  # 69
    [71, "Księga Mądrości", "Mądr", 19],  # 70
    [72, "Księga Syracha", "Syr", 51],  # 71
    [73, "Księga Barucha", "Bar", 6]  # 72
]

# ----- Klasa tłumaczeń ItemTrans -----
class ItemTrans:
    def __init__(self, _pathtr: str):
        self.namepathtr = _pathtr
        self.__fileh__ = None
        self.books = []  # Lista list z wersetami poszczególnych ksiąg
        #  Inicjalizacja listy ksiąg z wersetami
        for licz in range(MAX_BOOKS):
            self.books.append([])
        #  Odczyt nazwy tłumaczenia z pierwszej linijki pliku
        try:
            self.__fileh__ = open(self.namepathtr, "rt", encoding="utf-8")
            self.infotr = self.__fileh__.readline().strip("\n")[1:]  # opis
            self.__readallbooks__()
        finally:
            self.__fileh__.close()

    def __getitem__(self, item: int):
        return self

    def __readallbooks__(self):  # Metoda prywatna
        """
        @return: Brak
        """
        #  Odczyt poszczególnych ksiąg
        strtext = self.__fileh__.readline().strip("\n")
        for coutbooks in range(MAX_BOOKS):
            while strtext:
                if int(strtext[0:3]) == coutbooks + 1:
                    self.books[coutbooks].append(strtext)
                else:
                    break  # Koniec księgi

                strtext = self.__fileh__.readline().strip("\n")

# ----- Klasa główna MyBiblePyClass -----
class MyBiblePyClass:
    # Konstruktor
    def __init__(self, _pathtrdir: str):
        """
        @param _pathtrdir: Ścieżka dostępu do katalogu z tłumaczeniami
        """
        # Private
        self.__version__: str = "v0.3.5678"
        # Public
        self.__pathtrdir__: str = _pathtrdir
        self.__filenames__ = []  # Tablica
        self.__itemstr__ = []  # Tablica objektów typu ItemTrans

        for myfilenames in os.listdir(self.__pathtrdir__):
            if myfilenames.endswith(".pltmb"):  # filtr
                myfilenames = os.path.join(self.__pathtrdir__, myfilenames)
                self.__filenames__.append(myfilenames)
                self.__itemstr__.append(ItemTrans(myfilenames))  # Dodawanie do tablicy objektów tłumaczenia

    def getversion(self):
        """
        @return: Metoda zwraca prywatne pole wersji biblioteki
        """
        return self.__version__

    # def __getitem__(self, item: int):
    #     return self.itemstr[item]

    def readtextall(self, _ibook: int, _ichapt: int = 1, _iver: int = 1) -> []:
        """
        @param _ibook: Numer księgi
        @param _ichapt: Numer rozdziału, domyślnie 1
        @param _iver: Numer wersetu, domyślnie 1
        @return: Metoda zwraca listę tekstów biblijnych wszystkich dostępnych tłumaczeń
        """
        resultlist = []

        for numtr in range(len(self.__itemstr__)):
            resultonetext = self.__readtext__(numtr, _ibook, _ichapt, _iver)
            resultlist.append("{} {}:{} {}".format(resultonetext[EnumDecodeListText.endec_smalnamebook],
                                                   resultonetext[EnumDecodeListText.endec_chapt],
                                                   resultonetext[EnumDecodeListText.endec_vers],
                                                   resultonetext[EnumDecodeListText.endec_text]))

        self.__createpdfalltext__(_ibook, _ichapt, _iver)
        return resultlist

    def __readtext__(self, _itrans: int, _ibook: int, _ichapt: int = 1, _ivers: int = 1) -> []:
        """
        @param _itrans: Numer tłumaczenia
        @param _ibook: Numer księgi
        @param _ichapt: Numer rozdziału, domyślnie 1
        @param _ivers: Numer wersetu, domyślnie 1
        @return: Metoda zwraca tekst biblijny, określony w argumentach metody
        """
        if _itrans >= len(self.__filenames__) or _ibook == 0 or _ichapt == 0 or _ivers == 0:
            return ""  # Jeśli przekroczono zakresy

        it = self.__itemstr__[_itrans]
        listout = []

        for cVers in range(len(it.books[_ibook - 1])):
            strtext = it.books[_ibook - 1][cVers]
            if strtext == "":
                break
            rfulladress = strtext[0:9]
            ibook = int(rfulladress[0:3])
            ichapt = int(rfulladress[3:6])
            try:
                ivers = int(rfulladress[6:9])
            except ValueError:
                ivers = int(rfulladress[6:8])
                # print("except")

            if ibook == _ibook and ichapt == _ichapt and ivers == _ivers:
                textout = "{}".format(strtext[10:])
                listout.append(textout)
                listout.append(_itrans)
                listout.append(infoallbooks[ibook - 1][EnumInfoAllBooks.eninfo_Smalname])
                listout.append(ibook)
                listout.append(ichapt)
                listout.append(ivers)
                break

        return listout  # Będzie zwracaś listę [tekst, tłumaczenie, skrócona nazwa księgi, księga, rozdział, werset] ?

    def __createpdfalltext__(self, _ibook: int, _ichapt: int = 1, _iver: int = 1):
        """
        @param _ibook: Numer księgi
        @param _ichapt: Numer rozdziału
        @param _iver: Numer wersetu
        @return: Brak
        """
        setfontsize = 16
        myimage: str = "Tora.png"
        pdf = fpdf.FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()
        page_width = pdf.w - 2 * pdf.l_margin
        # Definiowanie kolekcji używanych czcionek UTF-8
        pdf.add_font("TimesI", fname="C:\\Windows\\Fonts\\Timesi.ttf")
        pdf.add_font("TimesN", fname="C:\\Windows\\Fonts\\Times.ttf")
        pdf.add_font("TimesB", fname="C:\\Windows\\Fonts\\Timesbd.ttf")
        pdf.add_font("TimesBI", fname="C:\\Windows\\Fonts\\Timesbi.ttf")

        with pdf.local_context(fill_opacity=0.4):
            pdf.image(myimage, x=1, y=1)

        pdf.set_xy(5, setfontsize)

        for numtr in range(len(self.__itemstr__)):
            resultonetext = self.__readtext__(numtr, _ibook, _ichapt, _iver)
            # Adres wersetu
            pdf.set_text_color(0, 0, 255)
            stradres = "{} {}:{}".format(resultonetext[EnumDecodeListText.endec_smalnamebook],
                                         resultonetext[EnumDecodeListText.endec_chapt],
                                         resultonetext[EnumDecodeListText.endec_vers])
            pdf.set_font("TimesB", size=setfontsize)
            pdf.multi_cell(w=page_width, txt=stradres, new_x="LEFT",
                           new_y="NEXT", align="L", max_line_height=pdf.font_size)
            # Właściwy tekst wersetu
            pdf.set_text_color(0)
            pdf.set_x(pdf.font_size)
            pdf.set_font("TimesN", size=setfontsize)
            pdf.multi_cell(w=page_width, txt=resultonetext[EnumDecodeListText.endec_text], new_x="LEFT",
                           new_y="NEXT", align="L", max_line_height=pdf.font_size)
            # Nazwa tłumaczenia
            pdf.set_font("TimesN", size=setfontsize - 4)
            pdf.set_text_color(255, 0, 0)
            pdf.set_x(5)
            strtrans = "[{}]".format(self.__itemstr__[numtr].infotr)
            pdf.multi_cell(w=page_width, txt=strtrans, new_x="LEFT",
                           new_y="NEXT", align="L", max_line_height=pdf.font_size)
            # Oddzielający wiersz z trzema gwiazdkami
            pdf.set_text_color(0)
            pdf.multi_cell(w=page_width, txt="* * *", new_x="LEFT",
                           new_y="NEXT", align="C", max_line_height=pdf.font_size)

        fileresultpdf: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "result.pdf")
        pdf.output(fileresultpdf)
