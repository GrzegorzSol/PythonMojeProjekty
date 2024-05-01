#  Copyright (c) Grzegorz Sołtysik 01.05.2024, 06:03
#  Nazwa projektu: GsPyChartClass
#  Nazwa pliku: GsPyMyChart.py

import fpdf

"""
-------------------------- Klasa GsPyMyChartBase ----------------------------
"""
class GsPyMyChartBase:
    # Konstruktor klasy bazowej
    def __init__(self, fInTableRef: list, fInTableMeas: list, strTitle: str):
        """
        @param: fInTableRef: Tablica wyników referencyjnych.
        @param: fInTableMeas: Tablica pomiarów.
        @return: Brak.
        """
        # print("Konstruktor klasy GsPyMyChartBase")
        # Zmienne protected
        self._iMaxMeas: int = 11
        self._fTableRef: list = fInTableRef.copy()
        self._fTableMeas: list = fInTableMeas.copy()
        self._strTitle: str = strTitle
        # Potrzebne obliczenia
        self.__calculate()
        # Tworzenie dokumentu PDF
        self.__pdf_init()
        # Rysowanie nagłówka
        self.__paint_title()

    # Obliczanie niezbędnych danych
    def __calculate(self):
        """
        @return: Brak.
        """
        # Zmienne publiczne
        self._iCountRef: int = len(self._fTableRef)
        # Wymiary w pikselach kartki A4
        self._fMaxWidth: float = 8.27 * 72
        self._fMaxHeight: float = 11.69 * 72
        self._fOffset: float = 20  # Offset x, y wykresu
        # Wymiary wykresu
        self._fWidth: float = self._fMaxWidth - (2 * self._fOffset)
        self._fHeight: float = self._fMaxHeight - (2 * self._fOffset)
        __fReductionNet: float = 20  # O ile zostanie zmniejszony wykres w pionie i poziomie względem współrzędnych.
        __fWidthOffset: float = self._fWidth - __fReductionNet  # Zmniejszenie siatki w poziomie
        __fheightOffset: float = self._fHeight - __fReductionNet  # Zmniejszenie siatki w pionie

        # Obliczanie współczynników konwersji
        self._fYConvRef: float = __fheightOffset / self._fTableRef[self._iCountRef - 1]  # Ilość pikseli na jednostkę, tablica wyników odniesienia, oś Y
        self._fX: float = __fWidthOffset / (self._iCountRef - 1)  # Ilość pikseli na kolejny pomiar, os X

        # Listy krotek dla pomiarów referencyjnych i rzeczywistych
        self._myListRef: list = []
        self._myListMeas: list = []
        # Wypełnienie listy krotek dla pomiarów referencyjnych i rzeczywistych
        for i in range(self._iCountRef):
            self._myListRef.append((self._fOffset + (self._fX * i),
                                    self._fHeight + self._fOffset - (self._fYConvRef * self._fTableRef[i])))
            self._myListMeas.append((self._fOffset + (self._fX * i),
                                     self._fHeight + self._fOffset - (self._fYConvRef * self._fTableMeas[i])))

    # Inicjalizacja podstawowych zmiennych dla klasy FPDF
    def __pdf_init(self):
        """
        @return: Brak.
        """
        self._pdf = fpdf.FPDF(orientation="P", unit="pt", format="A4")
        self._pdf.add_page()
        # Definiowanie czcionek
        self._pdf.add_font("TimesI", fname="C:\\Windows\\Fonts\\Timesi.ttf")
        self._pdf.add_font("TimesN", fname="C:\\Windows\\Fonts\\Times.ttf")
        self._pdf.add_font("TimesB", fname="C:\\Windows\\Fonts\\Timesbd.ttf")
        self._pdf.add_font("TimesBI", fname="C:\\Windows\\Fonts\\Timesbi.ttf")
        # Rysowanie osi X i Y
        self._pdf.polyline([(self._fOffset, self._fOffset), (self._fOffset, self._fOffset + self._fHeight),
                            (self._fOffset + self._fWidth, self._fOffset + self._fHeight)])
        # --- Rysowanie siatki ---
        # Rysowanie pionowych linii
        self._pdf.set_draw_color(220, 220, 220)
        for i in range(1, self._iCountRef):
            self._pdf.polyline([(self._fOffset + (self._fX * i), self._fOffset),
                                (self._fOffset + (self._fX * i), self._fHeight + self._fOffset)])
        # Rysowanie poziomych linii
        for i in range(self._iCountRef):
            self._pdf.polyline([(self._fOffset, self._fHeight + self._fOffset - (self._fYConvRef * self._fTableRef[i])),
                                (self._fOffset + self._fWidth,
                                 self._fHeight + self._fOffset - (self._fYConvRef * self._fTableRef[i]))])

    # Rysowanie tytułu
    def __paint_title(self):
        """
        @return: Brak.
        """
        self._fSetFontSize: float = 12  # Wymiar czcionki
        self._pdf.set_text_color(0, 0, 0)
        self._pdf.set_fill_color(r=255, g=255, b=0)
        self._pdf.set_font("TimesN", size=self._fSetFontSize)
        self._pdf.set_xy(self._fOffset, self._fOffset)
        self._pdf.cell(w=self._fWidth, h=self._fOffset, txt=self._strTitle, border=1, align="C", fill=True)

    # Destruktor klasy bazowej
    def __del__(self):
        """
        @return: Brak.
        """
        del self._pdf  # Likwidacja objektu, klasy fpdf.FPDF
        # print("Destruktor klasy GsPyMyChartBase")


"""
---------------------------- Klasa GsPyMyChart ------------------------------
"""
class GsPyMyChart(GsPyMyChartBase):
    # Konstruktor
    def __init__(self, fInTableRef: list, fInTableMeas: list, strPathPDF: str, strTitle: str = ""):
        """
        @param: fInTableRef: Tablica wyników referencyjnych.
        @param: fInTableMeas: Tablica pomiarów.
        @return: Brak.
        """
        # print("Konstruktor klasy GsPyMyChart")
        super().__init__(fInTableRef, fInTableMeas, strTitle)  # Wywołanie konstruktora klasy przodka
        if self._iCountRef > self._iMaxMeas or self._iCountRef != len(self._fTableMeas):
            # Listy wejściowe, a co następuje składowe,  mają różną ilość elementów.
            return

        self.pathPDF: str = strPathPDF
        # Tworzenie wykresu i zapisywanie go w pliku pdf
        self.__createpdf()

    # Destruktor
    def __del__(self):
        """
        @return: Brak.
        """
        super().__del__()
        # print("Destruktor klasy GsPyMyChart")

    def __createpdf(self):
        """
        @return: Brak.
        """
        # Rysowanie linii, różnicy
        self._pdf.set_line_width(2)
        self._pdf.set_draw_color(40, 255, 40)
        for i in range(1, self._iCountRef):
            self._pdf.polyline([(self._fOffset + (self._fX * i),
                                 self._fHeight + self._fOffset - (self._fYConvRef * self._fTableRef[i])),
                                (self._fOffset + (self._fX * i),
                                 self._fHeight + self._fOffset - (self._fYConvRef * self._fTableMeas[i]))])
        # Rysowanie właściwego wykresu
        self._pdf.set_line_width(2)

        self._pdf.set_draw_color(0, 0, 255)
        self._pdf.polyline(self._myListRef)
        self._pdf.set_draw_color(255, 0, 0)
        self._pdf.polyline(self._myListMeas)

        # print("myListRef: {}".format(myListRef))

        self._pdf.output(self.pathPDF)


"""
-------------------------- Klasa GsPyMyChartBox -----------------------------
"""

class GsPyMyChartBox(GsPyMyChartBase):
    # Konstruktor
    def __init__(self, fInTableRef: list, fInTableMeas: list, strPathPDF: str, strTitle: str = ""):
        """
        @param: fInTableRef: Tablica wyników referencyjnych.
        @param: fInTableMeas: Tablica pomiarów.
        @return: Brak.
        """
        # print("Konstruktor klasy GsPyMyChart")
        super().__init__(fInTableRef, fInTableMeas, strTitle)  # Wywołanie konstruktora klasy przodka
        if self._iCountRef > self._iMaxMeas or self._iCountRef != len(self._fTableMeas):
            # Listy wejściowe, a co następuje składowe,  mają różną ilość elementów.
            return

        self.pathPDF: str = strPathPDF
        # Tworzenie wykresu i zapisywanie go w pliku pdf
        self.__createpdf()

    # Destruktor
    def __del__(self):
        """
        @return: Brak.
        """
        super().__del__()

    def __createpdf(self):
        """
        @return: Brak.
        """
        # Rysowanie właściwego wykresu
        for i in range(self._iCountRef):
            self._pdf.set_draw_color(0, 0, 0)
            self._pdf.set_fill_color(0, 0, 255)
            self._pdf.rect(self._myListRef[i][0], self._myListRef[i][1],
                           10, self._fHeight - self._myListRef[i][1] + self._fOffset, "FD")
            self._pdf.set_draw_color(0, 0, 0)
            self._pdf.set_fill_color(255, 0, 0)
            self._pdf.rect(self._myListMeas[i][0] + 10, self._myListMeas[i][1],
                           10, self._fHeight - self._myListMeas[i][1] + self._fOffset, "FD")

        self._pdf.output(self.pathPDF)
