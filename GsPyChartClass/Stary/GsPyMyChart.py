#  Copyright (c) Grzegorz Sołtysik 05.05.2024, 18:44
#  Nazwa projektu: GsPyChartClass
#  Nazwa pliku: GsPyMyChart.py

import fpdf

"""
-------------------------- Klasa GsPyMyChartBase ----------------------------
Prywatne zasady nazewnictwa zmiennych dla kodów źródłowych w Pythonie:
    - przedrostek "-" zmienna lub metoda, funkcja, protected
    - przedrostek "__" zmienna lub metoda, funkcja, prywatna
    - pierwsza litera "i", zmienna typu integer
    - pierwsza litera "f", zmienna typu float
    - pierwsza litera "str", zmienna typy napis
    - po literze oznaczającej typ nazwa "Def", zmienna została zdefiniowana w metodzie konstruktora __init__()
"""
class GsPyMyChartBase:
    # Konstruktor klasy bazowej
    def __init__(self, fInTableRef: list, fInTableMeas: list, strTitle: str,
                 iLeft: int, iTop: int, iHeight: int, iWidth: int):
        """
        :param fInTableRef: Tablica wyników referencyjnych.
        :param fInTableMeas: Tablica pomiarów.
        :param strTitle: Napis, będący tytułem, domyślnie pusty.
        :param iHeight: Wysokość wykresu, zdefiniowany przez użytkownika, domyślnie zero, wtedy wysokość będzie całej kartki A4.
        :param iWidth: Szerokość wykresu, zdefiniowany przez użytkownika, domyślnie zero, wtedy szerokość będzie całej kartki A4.
        :return: Brak.
        """
        # print("Konstruktor klasy GsPyMyChartBase")
        # Zmienne protected
        self._fDefOffset: float = 20  # Offset x, y wykresu
        self._fMaxWidth: float  # Maksymalna szerokość, która albo jest domyślna, albo jest zdefiniowana przez użytkownika.
        self._fMaxHeight: float  # Maksymalna wysokość, która albo jest domyślna, albo jest zdefiniowana przez użytkownika.
        self._fDefLeft: float = iLeft  # Współrzędna X wykresu użytkownika
        self._fDefTop: float = iTop  # Współrzędna Y wykresu użytkownika
        self._fWidth: float  # Szerokość wykresu self._fMaxWidth - self._fOffset
        self._fHeight: float  # Wysokość wykresu self._fMaxHeight - self._fOffset
        self._fYConvRef: float  # Współczynnik przeliczeniowy dla osi Y z dla pomiaru
        self._fX: float  # Współczynnik przeliczeniowy dla osi X z dla pomiaru
        # Listy krotek dla pomiarów referencyjnych i rzeczywistych
        self._myListRef: list = []  # Lista współrzędnych dla narysowania wykresy pomiarów referencyjnych.
        self._myListMeas: list = []  # Lista współrzędnych dla narysowania wykresy pomiarów rzeczywistych.
        self._iDefMaxMeas: int = 11  # Maksymalna ilość pomiarów dla wszystkich wykresów
        self._fDefTableRef: tuple = fInTableRef.copy()  # Krotka pomiarów referencyjnych, będąca kopią argumentu fInTableRef.
        self._fDefTableMeas: tuple = fInTableMeas.copy()  # Krotka pomiarów rzeczywistych, będąca kopią argumentu fInTableMeas.
        self._iCountRef: int = len(self._fDefTableRef)  # Ilość pomiarów, która jest identyczna w wynikach referencyjnych, jak i rzeczywistych.
        self._fDefDown: float = self._fDefTableRef[0]  # najmniejsza wartość
        self._fDefMinHeight: float = 400  # Minimalna, dopuszczalna wysokość
        self._fDefMinWidth: float = 300  # Minimalna, dopuszczalna szerokość
        self._iDefHeight: int = iHeight  # Wysokość wprowadzona przez użytkownika, domyślnie 0
        self._iDefWidth: int = iWidth  # Szerokość wprowadzona przez użytkownika, domyślnie 0
        # Zmienne i metody prywatne
        self.__strDefTitle: str = strTitle  # Tytuł wykresu, domyślnie pusty napis

        # Największa delta
        fDeltaRef: float = self._fDefTableRef[self._iCountRef - 1] - self._fDefTableRef[0]
        fDeltaMeas: float = self._fDefTableMeas[self._iCountRef - 1] - self._fDefTableMeas[0]
        # Wybranie większej delty

        # Potrzebne obliczenia
        self.__calculate()
        # Tworzenie dokumentu PDF
        self.__pdf_init()
        # Rysowanie nagłówka
        self.__paint_title()

    # Obliczanie niezbędnych danych
    def __calculate(self):
        """
        :return: Brak.
        """
        # self._iCountRef = len(self._fDefTableRef)
        # Wymiary w pikselach kartki A4
        fDefaultWidth: float = 8.27 * 72  # Domyślna szerokość kartki
        fDefaultHeight: float = 11.69 * 72  # Domyślna wysokość kartki
        # Warunek wysokości i szerokości
        if self._iDefHeight == 0:
            # Wykres na całą kartkę
            self._fMaxHeight = fDefaultHeight
        else:
            # Wysokość użytkownika
            self._fMaxHeight = self._iDefHeight

        if self._iDefWidth == 0:
            self._fMaxWidth = fDefaultWidth
        else:
            # Szerokość użytkownika
            self._fMaxWidth = self._iDefWidth

        # Pilnowanie by wymiary wprowadzone przez użytkownika nie były za małe.
        if self._fMaxWidth < self._fDefMinWidth:
            self._fMaxWidth = self._fDefMinWidth
        if self._fMaxHeight < self._fDefMinHeight:
            self._fMaxHeight = self._fDefMinHeight

        # Wymiary wykresu
        self._fWidth = self._fMaxWidth - (2 * self._fDefOffset)
        self._fHeight = self._fMaxHeight - (2 * self._fDefOffset)
        __fReductionNet: float = self._fDefOffset  # O ile zostanie zmniejszony wykres w pionie i poziomie względem współrzędnych.
        __fWidthOffset: float = self._fWidth - __fReductionNet  # Zmniejszenie siatki w poziomie
        __fheightOffset: float = self._fHeight - __fReductionNet  # Zmniejszenie siatki w pionie

        # Obliczanie współczynników konwersji
        self._fYConvRef = __fheightOffset / self._fDefTableRef[self._iCountRef - 1]  # Ilość pikseli na jednostkę, tablica wyników odniesienia, oś Y
        self._fX = __fWidthOffset / (self._iCountRef - 1)  # Ilość pikseli na kolejny pomiar, os X

        # Wypełnienie listy krotek dla pomiarów referencyjnych i rzeczywistych
        for i in range(self._iCountRef):
            self._myListRef.append((self._fDefOffset + (self._fX * i) + self._fDefLeft,
                                    self._fHeight + self._fDefOffset - (self._fYConvRef * self._fDefTableRef[i]) + self._fDefTop))
            self._myListMeas.append((self._fDefOffset + (self._fX * i) + self._fDefLeft,
                                     self._fHeight + self._fDefOffset - (self._fYConvRef * self._fDefTableMeas[i]) + self._fDefTop))

    # Inicjalizacja podstawowych zmiennych dla klasy FPDF
    def __pdf_init(self):
        """
        :return: Brak.
        """
        self._pdf = fpdf.FPDF(orientation="P", unit="pt", format="A4")
        self._pdf.add_page()
        # Definiowanie czcionek
        self._pdf.add_font("TimesI", fname="C:\\Windows\\Fonts\\Timesi.ttf")
        self._pdf.add_font("TimesN", fname="C:\\Windows\\Fonts\\Times.ttf")
        self._pdf.add_font("TimesB", fname="C:\\Windows\\Fonts\\Timesbd.ttf")
        self._pdf.add_font("TimesBI", fname="C:\\Windows\\Fonts\\Timesbi.ttf")
        # Rysowanie osi X i Y
        self._pdf.polyline([(self._fDefOffset + self._fDefLeft, self._fDefOffset + self._fDefTop),
                            (self._fDefOffset + self._fDefLeft, self._fDefOffset + self._fHeight + self._fDefTop),
                            (self._fDefOffset + self._fWidth + self._fDefLeft, self._fDefOffset + self._fHeight + self._fDefTop)])
        # --- Rysowanie siatki ---
        # Rysowanie pionowych linii
        self._pdf.set_draw_color(220, 220, 220)
        for i in range(1, self._iCountRef):
            self._pdf.polyline([(self._fDefOffset + (self._fX * i) + self._fDefLeft, self._fDefOffset + self._fDefTop),
                                (self._fDefOffset + (self._fX * i) + self._fDefLeft, self._fHeight + self._fDefOffset + self._fDefTop)])
        # Rysowanie poziomych linii
        for i in range(self._iCountRef):
            self._pdf.polyline([(self._fDefOffset + self._fDefLeft, self._fHeight + self._fDefOffset - (self._fYConvRef * self._fDefTableRef[i]) + self._fDefTop),
                                (self._fDefOffset + self._fWidth + self._fDefLeft,
                                 self._fHeight + self._fDefOffset - (self._fYConvRef * self._fDefTableRef[i]) + self._fDefTop)])

    # Rysowanie tytułu
    def __paint_title(self):
        """
        :return: Brak.
        """
        # print("len: {}".format(len(self.__strTitle)))
        if len(self.__strDefTitle) > 0:
            # Gdy argument nie jest pustym napisem
            # self._pdf.set_line_width(2)
            self._pdf.set_draw_color(0, 0, 0)
            self._fSetFontSize: float = 12  # Wymiar czcionki
            self._pdf.set_text_color(0, 0, 0)
            self._pdf.set_fill_color(r=255, g=255, b=0)
            self._pdf.set_font("TimesN", size=self._fSetFontSize)
            self._pdf.set_xy(self._fDefOffset + self._fDefLeft, self._fDefOffset + self._fDefTop)
            self._pdf.cell(w=self._fWidth, h=self._fDefOffset, txt=self.__strDefTitle, border=1, align="C", fill=True)

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
    def __init__(self, fInTableRef: list, fInTableMeas: list, strPathPDF: str, strTitle: str = "", iLeft: int = 0, iTop: int = 0,
                 iHeight: int = 0, iWidth: int = 0):
        """
        :param fInTableRef: Tablica wyników referencyjnych.
        :param fInTableMeas: Tablica pomiarów.
        :return: Brak.
        """
        # print("Konstruktor klasy GsPyMyChart")
        super().__init__(fInTableRef, fInTableMeas, strTitle, iLeft, iTop, iHeight, iWidth)  # Wywołanie konstruktora klasy przodka
        if self._iCountRef > self._iDefMaxMeas or self._iCountRef != len(self._fDefTableMeas):
            # Listy wejściowe, a co następuje składowe,  mają różną ilość elementów.
            return

        self.pathPDF: str = strPathPDF
        # Tworzenie wykresu i zapisywanie go w pliku pdf
        self.__createpdf()

    # Destruktor
    def __del__(self):
        """
        :return: Brak.
        """
        super().__del__()
        # print("Destruktor klasy GsPyMyChart")

    def __createpdf(self):
        """
        :return: Brak.
        """
        # Rysowanie linii, różnicy
        self._pdf.set_line_width(2)
        self._pdf.set_draw_color(40, 255, 40)
        for i in range(1, self._iCountRef):
            self._pdf.polyline([(self._fDefOffset + (self._fX * i) + self._fDefLeft,
                                 self._fHeight + self._fDefOffset - (self._fYConvRef * self._fDefTableRef[i]) + self._fDefTop),
                                (self._fDefOffset + (self._fX * i) + self._fDefLeft,
                                 self._fHeight + self._fDefOffset - (self._fYConvRef * self._fDefTableMeas[i]) + self._fDefTop)])

        # Rysowanie właściwego wykresu
        self._pdf.set_line_width(2)

        self._pdf.set_draw_color(0, 0, 255)
        self._pdf.polyline(self._myListRef)
        self._pdf.set_draw_color(255, 0, 0)
        self._pdf.polyline(self._myListMeas)

        # print("myListRef: {}".format(myListRef))

        # self._pdf.output(self.pathPDF)

