
#  Copyright (c) Grzegorz Sołtysik
#  Nazwa projektu: MegaScripts
#  Nazwa pliku: GsMegaCloudMaster.py
#  Data: 09.09.2023, 09:01

import os, locale
from datetime import datetime

def nowdatetime():
    """
    Funkcja odczytuje i odpowiednio formatuje datę i czas. Funkcja jest nie wywoływana z zewnątrz
    :return: strdatetime - zformatowana data i czas
    """
    loc = locale.getlocale()  # Odczyt bierzących ustawień
    locale.setlocale(locale.LC_ALL, "Polish_Poland.utf8")
    nowdate = datetime.now()
    strdatetime = "_" + nowdate.strftime("%d-%B-%Y_%H-%M-%S")
    locale.setlocale(locale.LC_ALL, loc)  # Powrót do pierwotnych ustawień lokalizacji
    return strdatetime
#----------------------------------------------------------------------------
def megadownloads(source:str, destiny:str):
    """
    Funkcja pobiera dane z chmury MEGA do ustalonej lokalizacji
    :param source: ścieżka dostępu do katalogu(pliku) do pobrania
    :param destiny: ścieżka dostępu do katalogu gdzie zostaną pobrane dane
    :return: brak
    """
    megalog = "MEGAclient login grzegorzsol@gmail.com Tuturistan1968M"  # Dane do logowania
    fulldatetime = nowdatetime() # Odczyt daty i czasu dla dodania do ścieżki przeznaczenia
    namemegasource = os.path.split(source) # Katalog i ostatnim elementem ścieżki
    filedirnamedown = namemegasource[1] # Ostatni człon ścieżki dostępu do pobrania
    fullpathdestiny = os.path.join(destiny, filedirnamedown) # Pełna scieżka dostępu do katalogu docelowego
    getmega = "MEGAclient get \"{}\" \"{}\"".format(source, destiny)
    #
    os.system(megalog)  # zalogowanie
    os.system(getmega)  # Pobranie danych
    os.system("MEGAclient logout")  # Wylogowanie
    #
    fullpathdestiny_newname = "{}{}".format(fullpathdestiny, fulldatetime)
    os.rename(fullpathdestiny, fullpathdestiny_newname)  # Zmiana nazwy na nazwę z datę
    #
    currentdir = os.getcwd()  # Katalog aktualny
    path7z = os.path.join(currentdir, "7z.exe")
    path7zdll = os.path.join(currentdir, "7z.dll")
    archivedestiny = "{} a -t7z \"{}\" \"{}\"".format(path7z, fullpathdestiny_newname, fullpathdestiny_newname)

    if os.path.exists(path7z) and os.path.exists(path7zdll):
        print("Pakuje pobrany katalog(plik)")
        os.system(archivedestiny)
    else:
        print("path7z: {} nie istnieje".format(path7z))

    os.chdir(destiny)  # Katalog aktualny to katalog przeznaczenia
    os.system("dir")
    os.system("pause") # Czekanie na naciśnięcie dowolnego klawisza by zamknąć konsole
#----------------------------------------------------------------------------
