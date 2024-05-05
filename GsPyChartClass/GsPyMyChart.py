#  Copyright (c) Grzegorz Sołtysik 05.05.2024, 06:08
#  Nazwa projektu: GsPyChartClass
#  Nazwa pliku: GsPyMyChart.py

import fpdf

class GsPointF:
    def __init__(self, _fX: float = 0, _fY: float = 0):
        self.fX: float = _fX
        self.fY: float = _fY
class GsRectF:
    def __init__(self, _fLeft: float = 0, _fTop: float = 0, _fRight: float = 0, _fBottom: float = 0):
        self.fLeft: float = _fLeft
        self.fTop: float = _fTop
        self.fRight: float = _fRight
        self.fBottom: float = _fBottom

    def height(self):
        return self.fBottom - self.fTop

    def width(self):
        return self.fRight - self.fLeft

    def set_width(self, _width: float):
        self.fRight = self.fLeft + _width

    def set_height(self, _height: float):
        self.fBottom = self.fTop + _height

    def inflate(self, _l: float, _t: float, _r: float, _b: float):
        self.fLeft -= _l
        self.fTop -= _t
        self.fRight += _r
        self.fBottom += _b

    def centre(self):
        c = GsPointF((self.fLeft + self.fRight) / 2, (self.fTop + self.fBottom) / 2)
        return c


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
        # kopiowanie niektórych danych wejściowych
        self._iWidth: int = iWidth
        self._iHeight: int = iHeight
        self._iLeft: int = iLeft
        self._iTop: int = iTop
        self._strTitle: str = strTitle
        # Kolory wykresów i opisów pomiarów
        self._colorRef: tuple = (0, 0, 255)
        self._colorMeas: tuple = (255, 0, 0)
        self._colorDiff: tuple = (0, 200, 0)
        # Kopiowanie tablicy wejściowych do tablic składowych klasy
        self._fTableRef: tuple = fInTableRef.copy()
        self._fTableMeas: tuple = fInTableMeas.copy()
        self._cuiCount: int = len(self._fTableRef)

        fDeltaRef: float = self._fTableRef[self._cuiCount - 1] - self._fTableRef[0]
        fDeltaMeas: float = self._fTableMeas[self._cuiCount - 1] - self._fTableMeas[0]
        # Wybranie większej delty
        if fDeltaRef >= fDeltaMeas:
            self._fDelta: float = fDeltaRef
        elif fDeltaRef < fDeltaMeas:
            self._fDelta: float = fDeltaMeas

        # Wynajdywanie najmniejszej wartości z obu tablic
        if self._fTableRef[0] <= self._fTableMeas[0]:
            self._fYMin: float = self._fTableRef[0]
        elif self._fTableRef[0] > self._fTableMeas[0]:
            self._fYMin: float = self._fTableMeas[0]
        # Potrzebne obliczenia
        self.__calculate()
        # Tworzenie dokumentu PDF
        self.__pdf_init()
        # Rysowanie nagłówka
        self.__paint_title()

    def __del__(self):
        """
        @return: Brak.
        """
        del self._pdf  # Likwidacja objektu, klasy fpdf.FPDF

    # Obliczanie niezbędnych danych
    def __calculate(self):
        """
        :return: Brak.
        """
        # self._iCountRef = len(self._fDefTableRef)
        # O jaką wartość od góry i od dołu zostanie zmniejszony wykres dla lepszej czytelności oraz zmieszczenia opisu.
        self.__fDecSize: float = 20
        fDefA4width: float = 8.27 * 72
        fDefA4Height: float = 11.69 * 72
        self._RectDrawBaseF: GsRectF = GsRectF(self._iLeft, self._iTop, self._iLeft + fDefA4width, self._iTop + fDefA4Height)
        # Definiowanie wymiarów wykresu, zależnie od danych wejściowych
        if self._iWidth > 0:
            # Szerokość
            self._RectDrawBaseF.fRight = self._iLeft + self._iWidth

        if self._iHeight > 0:
            # Wysokość
            self._RectDrawBaseF.fBottom = self._iTop + self._iHeight

        # Definiowanie offsetu
        self._fOffset: float = 10.0
        # Definiowanie obszaru przeznaczonego na opis
        self._DrawRectTitleF: GsRectF = GsRectF()
        self._DrawRectTitleF.fLeft = self._RectDrawBaseF.fLeft + (2 * self._fOffset)
        self._DrawRectTitleF.fTop = self._RectDrawBaseF.fTop + self.__fDecSize
        self._DrawRectTitleF.fRight = self._DrawRectTitleF.fLeft + (self._RectDrawBaseF.width() / 3)
        self._DrawRectTitleF.fBottom = self._DrawRectTitleF.fTop + self._fOffset
        # Zmniejszenie wymiaru osi współrzędnych
        self._RectDrawBaseF.inflate(-self._fOffset, -self._fOffset, -self._fOffset, -self._fOffset)
        # Wymiary wykresu
        self._RectDrawF: GsRectF = GsRectF(self._RectDrawBaseF.fLeft, self._RectDrawBaseF.fTop,
                                           self._RectDrawBaseF.fRight, self._RectDrawBaseF.fBottom)
        # Zmniejszenie wielkości obszaru wykresu dla lepszej czytelności
        self._RectDrawF.inflate(0, -self.__fDecSize, 0, -self.__fDecSize)

        self._fYConvRef: float = self._RectDrawF.height() / self._fDelta  # Współczynnik przeliczeń dla osi Y
        self._fX: float = self._RectDrawF.width() / self._cuiCount  # Współczynnik przeliczeń dla osi X
        self._fYReference_0: float = self._RectDrawF.fBottom + (self._fYMin * self._fYConvRef)  # Współrzędne Y, dla osi oznaczającej '0'

        #  Wypełnienie tablicy krotek, współrzędnych dla pomiarów referencyjnych i rzeczywistych
        self._PointFRef: list = []
        self._PointFMeas: list = []
        for i in range(self._cuiCount):
            self._PointFRef.append((self._RectDrawF.fLeft + (i * self._fX),
                                    self._fYReference_0 - (self._fYConvRef * self._fTableRef[i])))
            self._PointFMeas.append((self._RectDrawF.fLeft + (i * self._fX),
                                    self._fYReference_0 - (self._fYConvRef * self._fTableMeas[i])))

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
        # Rysowanie siatki: Y-kolejnych numer pomiarów
        # 	                X-Wartości pomiarów referencyjnych
        self._pdf.set_draw_color(220, 220, 220)
        # Rysowanie pionowych i poziomych linii
        for i in range(1, self._cuiCount):
            self._pdf.polyline([(self._PointFRef[i][0], self._RectDrawBaseF.fBottom),
                                (self._PointFRef[i][0], self._RectDrawBaseF.fTop)])
            self._pdf.polyline([(self._RectDrawBaseF.fLeft, self._PointFRef[i][1]),
                                (self._RectDrawBaseF.fRight, self._PointFRef[i][1])])

        # Rysowanie osi X i Y
        self._pdf.set_draw_color(0, 0, 0)
        self._pdf.set_line_width(1.5)
        self._pdf.polyline([(self._RectDrawBaseF.fLeft, self._RectDrawBaseF.fTop),
                        (self._RectDrawBaseF.fLeft, self._RectDrawBaseF.fBottom)])
        self._pdf.polyline([(self._RectDrawBaseF.fLeft, self._fYReference_0),
                            (self._RectDrawBaseF.fRight, self._fYReference_0)])

    # Rysowanie tytułu
    def __paint_title(self):
        """
        :return: Brak.
        """
        self._pdf.set_font("TimesN", size=10)
        self._pdf.set_xy(self._DrawRectTitleF.fLeft, self._DrawRectTitleF.fTop)
        self._pdf.set_line_width(0.1)
        self._pdf.set_fill_color(255, 255, 0)
        self._pdf.multi_cell(self._DrawRectTitleF.width(), self._DrawRectTitleF.height(),
                       txt=self._strTitle, border=1, align="C", fill=True)


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
        self._strPathFilePDF = strPathPDF  # Ścieżka dostępu do pliku pdf
        super().__init__(fInTableRef, fInTableMeas, strTitle, iLeft, iTop, iHeight,
                         iWidth)  # Wywołanie konstruktora klasy przodka
        # Tworzenie wykresu i zapisywanie go w pliku pdf
        self.__createpdf()

    # Destruktor
    def __del__(self):
        """
        :return: Brak.
        """
        super().__del__()

    def __printDifferent(self):
        """
        :return: Brak.
        """
        # Rysowanie różnicy
        self._pdf.set_line_width(0.5)
        self._pdf.set_draw_color(self._colorDiff)
        for i in range(self._cuiCount):
            self._pdf.polyline([(self._PointFRef[i][0], self._PointFRef[i][1]),
                                (self._PointFMeas[i][0], self._PointFMeas[i][1])])

    def __printMarkMeas(self):
        """
        :return: Brak.
        """
        # Rysowanie zaznaczeń pomiarów
        fOffsetMark: float = 2  # Przesunięcia, szerokość, wysokość zaznaczeń

        self._pdf.set_fill_color(0, 80, 0)
        self._pdf.set_draw_color(0, 0, 0)
        for i in range(self._cuiCount):
            self._pdf.rect(self._PointFRef[i][0] - fOffsetMark, self._PointFRef[i][1] - fOffsetMark,
                           2 * fOffsetMark, 2 * fOffsetMark, style="DF")
            self._pdf.rect(self._PointFMeas[i][0] - fOffsetMark, self._PointFMeas[i][1] - fOffsetMark,
                           2 * fOffsetMark, 2 * fOffsetMark, style="DF")

    def __printLegend(self):
        """
        :return: Brak.
        """
        #
        fHorMeasTextOffset: float = 10.0  # Przesunięcie poziome opisu pomiarów rzeczywistych
        # Opis punktów pomiarowych
        for i in range(self._cuiCount):
            self._pdf.set_text_color(self._colorRef)
            strText: str = str(self._fTableRef[i])
            fHorRefTextOffset: float = self._pdf.get_string_width(strText) * 1.8  # Przesunięcie poziome opisu pomiarów referencyjnego
            self._pdf.text(self._PointFRef[i][0] - fHorRefTextOffset, self._PointFRef[i][1], strText)

            self._pdf.set_text_color(self._colorMeas)
            strText: str = str(self._fTableMeas[i])
            self._pdf.text(self._PointFMeas[i][0] + fHorMeasTextOffset, self._PointFMeas[i][1], strText)

    def __createpdf(self):
        """
        :return: Brak.
        """
        # Rysowanie różnicy
        self.__printDifferent()
        # Rysowanie właściwego wykresu
        self._pdf.set_line_width(0.8)

        self._pdf.set_draw_color(0, 0, 255)
        self._pdf.polyline(self._PointFRef)
        self._pdf.set_draw_color(255, 0, 0)
        self._pdf.polyline(self._PointFMeas)
        # Rysowanie zaznaczeń pomiarów
        self.__printMarkMeas()
        # Rysowanie opisów
        self.__printLegend()

        self._pdf.output(self._strPathFilePDF)


"""
--------------------------- Klasa GsPyMyChartBox ---------------------------
"""
class GsPyMyChartBox(GsPyMyChartBase):
    def __init__(self, fInTableRef: list, fInTableMeas: list, strPathPDF: str, strTitle: str = "", iLeft: int = 0, iTop: int = 0, iHeight: int = 0, iWidth: int = 0):
        """
        :param fInTableRef: Tablica wyników referencyjnych.
        :param fInTableMeas: Tablica pomiarów.
        :return: Brak.
        """
        self._strPathFilePDF = strPathPDF  # Ścieżka dostępu do pliku pdf
        super().__init__(fInTableRef, fInTableMeas, strTitle, iLeft, iTop, iHeight,
                         iWidth)  # Wywołanie konstruktora klasy przodka
        # Tworzenie wykresu i zapisywanie go w pliku pdf
        self.__createpdf()

    def __del__(self):
        """
        :return: Brak.
        """
        super().__del__()
        
    def __PrintLegend(self):
        """
        :return: Brak.
        """
        fVertTextOffsetU: float = 3.0  # Przesunięcie w góre
        fVertTextOffsetD: float = 3 * fVertTextOffsetU  # Przesunięcie w dół
        fOffSetTextMaes: float = (self._fX / 3) + 1  # Przesunięcie w prawo
        # Opis punktów pomiarowych

        for i in range(self._cuiCount):
            self._pdf.set_text_color(self._colorRef)
            strText: str = str(self._fTableRef[i])
            # fTextWidth: float = self._pdf.get_string_width(strText) / 2
            if self._PointFRef[i][1] <= self._fYReference_0:
                self._pdf.text(self._PointFRef[i][0], self._PointFRef[i][1] - fVertTextOffsetU, strText)
            else:
                self._pdf.text(self._PointFRef[i][0], self._PointFRef[i][1] + fVertTextOffsetD, strText)
            self._pdf.set_text_color(self._colorMeas)
            strText: str = str(self._fTableMeas[i])
            if self._PointFMeas[i][1] <= self._fYReference_0:
                self._pdf.text(self._PointFMeas[i][0] + fOffSetTextMaes, self._PointFMeas[i][1] - fVertTextOffsetU, strText)
            else:
                self._pdf.text(self._PointFMeas[i][0] + fOffSetTextMaes, self._PointFMeas[i][1] + fVertTextOffsetD, strText)


    def __createpdf(self):
        """
        :return: Brak.
        """
        fWidthBar: float = self._fX / 3
        for i in range(self._cuiCount):
            fHeightBarRef: float = self._fYReference_0 - self._PointFRef[i][1]
            fAbsHeightBarRef: float = abs(fHeightBarRef)
            self._pdf.set_fill_color(self._colorRef)
            if self._PointFRef[i][1] <= self._fYReference_0:
                self._pdf.rect(self._PointFRef[i][0], self._PointFRef[i][1], fWidthBar, fAbsHeightBarRef, style="DF")
            else:
                self._pdf.rect(self._PointFRef[i][0], self._fYReference_0, fWidthBar, fAbsHeightBarRef, style="DF")

            fHeightBarMeas: float = self._fYReference_0 - self._PointFMeas[i][1]
            fAbsHeightBarMeas: float = abs(fHeightBarMeas)
            self._pdf.set_fill_color(self._colorMeas)
            if self._PointFMeas[i][1] <= self._fYReference_0:
                self._pdf.rect(self._PointFMeas[i][0] + fWidthBar + 1, self._PointFMeas[i][1], fWidthBar, fAbsHeightBarMeas, style="DF")
            else:
                self._pdf.rect(self._PointFMeas[i][0] + fWidthBar + 1, self._fYReference_0, fWidthBar, fAbsHeightBarMeas, style="DF")

        # Rysowanie opisów
        self.__PrintLegend()
        self._pdf.output(self._strPathFilePDF)
