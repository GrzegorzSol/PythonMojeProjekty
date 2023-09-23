#  Copyright (c) Grzegorz Sołtysik
#  Nazwa projektu: openpyxl
#  Nazwa pliku: DetectorClass.py
#  Data: 09.09.2023, 09:05

import datetime
import calendar
import enum
import openpyxl
import locale

class EnumAdressColumns(enum.IntEnum):
    """
    Klasa numerów poszczególnych kolumn w arkuszu
    """
    enAdrCol_Object = 0
    enAdrCol_LastData = enum.auto()
    enAdrCol_NextData = enum.auto()
    enAdrCol_Status = enum.auto()
    enAdrCol_Ages = enum.auto()


AdresAllColumnsTable = [  # Współrzędna pozioma kolumn
    "B", "C", "D", "E", "I"
]

class CheckScheduleClass:
    def __init__(self, _strpath: str):
        """
        :param _strpath: Ścieżka dostępu do arkusza
        """
        # Private
        self.__xlspathfile__: str = _strpath  # Ścieżka dostępu do arkusza
        self.__startcell__: int = 4  # Adres pionowy rozpoczęcia danych
        self.__stopcell__: int = 60  # Adres pionowy zakończenia danych
        self.__allowablerange__: int = 20  # Dopuszczalna rożnica między aktualna data a następnym sprawdzaniem.
        # Jeśli różnica jest mniejsza niż zdeklarowana, czujnik jest "Do kalibracji lub sprawdzenia"
        # Public
        self.openworkbook = openpyxl.load_workbook(self.__xlspathfile__)
        self.actiweworkbook = self.openworkbook.active
        self.nowdate = datetime.datetime.now()  # Aktualna data

    @staticmethod
    def __add_month__(indate: datetime, add: int) -> int:
        """
        :param indate: Data początkowa. Ten argument jest, potrzebny ze wzgledu na potrzebe znajomości kolejnych miesięcy
        :param add: Ile miesięcy należy dodać do daty początkowej
        :return: Obliczona ilość dni zawartych w kolejnych miesiącach, które będą dodane
        """
        count_day: int = 0  # Ile dni trzeba dodać
        month: int = indate.month
        year: int = indate.year

        for ilicz in range(1, add + 1):
            new_month = month + ilicz

            if new_month > 12:
                month = new_month - 12
                count = calendar.monthrange(year, month)[1]
                count_day += count
            else:
                count = calendar.monthrange(year, new_month)[1]
                count_day += count

        return count_day

    def getpath(self):
        return self.__xlspathfile__

    def execute(self, createfilereport: bool = False):
        file = 0  # Uchwyt do zapisywanego pliku
        filereport: str = "kalendarz_kontroli.txt"

        try:
            if createfilereport:
                # Tworzenie raportu kalendarza kontroli czujników
                file = open(filereport, "w", encoding="utf-8")
                locale.setlocale(locale.LC_ALL, "")
                strhead: str = "{:^88}{}\n\n".format("Raport kalendarza kontroli czujników:", self.nowdate.strftime("%d-%B-%Y"))
                file.write(strhead)
        except IOError:
            print("Błąd otwarcia, lub zapisu do pliku: {}".format(filereport))

        for iLicz in range(self.__startcell__, self.__stopcell__):
            adresstitle: str = "{}{}".format(
                AdresAllColumnsTable[EnumAdressColumns.enAdrCol_Object], iLicz)
            adresslastdata: str = "{}{}".format(
                AdresAllColumnsTable[EnumAdressColumns.enAdrCol_LastData], iLicz)
            adressnext: str = "{}{}".format(
                AdresAllColumnsTable[EnumAdressColumns.enAdrCol_NextData], iLicz)
            adresstatus: str = "{}{}".format(
                AdresAllColumnsTable[EnumAdressColumns.enAdrCol_Status], iLicz)
            adressage: str = "{}{}".format(AdresAllColumnsTable[EnumAdressColumns.enAdrCol_Ages], iLicz)

            title: str = self.actiweworkbook[adresstitle].value

            lastdata: datetime = self.actiweworkbook[adresslastdata].value  # Data ostatniego sprawdzania

            count_day: int = self.__add_month__(lastdata, self.actiweworkbook[adressage].value)  # Ilość dni do następnego sprawdzania
            nextdata: datetime = lastdata + datetime.timedelta(count_day)  # Obliczona data następnego sprawdzania
            self.actiweworkbook[adressnext] = nextdata
            # Obliczanie różnicy między aktualną datą a zaplanowaną data sprawdzania
            deltaages: datetime = nextdata - self.nowdate  # Różnica między zaplanowaną datą kontroli a aktualną datą
            delta: int = abs(deltaages.days)
            # print("delta: {}".format(abs(delta)))

            if createfilereport:
                # Tworzenie raportu kalendarza kontroli czujników
                strtowrite: str = "{:>74}\tTermin wzorcowania: {}\n".format(title, nextdata.strftime("%d-%B-%Y"))
                try:
                    file.write(strtowrite)
                except IOError:
                    print("Błąd zapisu do pliku: {}".format(filereport))

            # print("deltaint: {} nextdataint: {} delta: {}".format(deltaint, nextdataint, delta ))
            if delta > self.__allowablerange__:
                # Nie dopuszczalna różnica. Może to być spowodowane przekroczeniem terminu lub termin nastąpi w odległym czasie
                if self.nowdate < nextdata:
                    self.actiweworkbook[adresstatus] = "Aktualne"
                    self.actiweworkbook[adresstatus].fill = openpyxl.styles.PatternFill(fill_type="solid",
                                                                                        start_color="00FFFFFF",
                                                                                        end_color="00FFFFFF")
                    self.actiweworkbook[adresstatus].font = openpyxl.styles.Font(bold=False, color="00000000")
                else:
                    self.actiweworkbook[adresstatus] = "Nieaktualne"
                    self.actiweworkbook[adresstatus].fill = openpyxl.styles.PatternFill(fill_type="solid",
                                                                                        start_color="00FF0000",
                                                                                        end_color="00FF0000")
                    self.actiweworkbook[adresstatus].font = openpyxl.styles.Font(bold=True, color="00000000")
            else:  # Dopuszczalna różnica. Może termin być przekroczony lub się zbliża. Bez względu na to różnica jest akceptowalna
                # i należy czujnik skontrolować w jak najszybszym czasie
                self.actiweworkbook[adresstatus] = "Do kalibracji lub sprawdzenia"
                self.actiweworkbook[adresstatus].fill = openpyxl.styles.PatternFill(fill_type="solid",
                                                                                    start_color="000000FF",
                                                                                    end_color="000000FF")
                self.actiweworkbook[adresstatus].font = openpyxl.styles.Font(bold=True, color="00FFFF00")

        if createfilereport:
            # Tworzenie raportu kalendarza kontroli czujników
            file.close()
