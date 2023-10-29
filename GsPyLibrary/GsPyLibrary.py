
#  Copyright (c) Grzegorz Sołtysik
#  Nazwa projektu: GsPyLibrary
#  Nazwa pliku: GsPyLibrary.py
#  Data: 09.09.2023, 09:00

import configparser
import locale
import os
from datetime import datetime
from enum import IntEnum, auto
from pathlib import Path

# Klasa enumeracji dla typu archiwizatora
class TypeArch(IntEnum):
    en7Zip = 1000
    enRar = auto()

def nowdatetime():
    """
    OPIS: Funkcja odczytuje i formatuje datę i czas
    :return: strdatetime: str - odczytana i zformatowana data i czas
    """
    loc = locale.getlocale()  # Odczyt bierzących ustawień
    locale.setlocale(locale.LC_ALL, "Polish_Poland.utf8")
    nowdate = datetime.now()
    strdatetime: str = "_" + nowdate.strftime("%d-%B-%Y_%H-%M-%S")
    locale.setlocale(locale.LC_ALL, loc)  # Powrót do pierwotnych ustawień lokalizacji
    return strdatetime

def getvalueini(pathini: str, sectionini: str, valueini: str, defaultvalue: str):
    """
    OPIS: Funkcja odczytuje wartość w pliku "pathini", sekcji "sectionini", dla klucza "valueini"
          lub odczytuje wartość domyślną "defaultvalue" w wypadku braku jakiegoś elementu

    :param pathini:str - Ścieżka dostępu do pliku konfiguracyjnego .ini
    :param sectionini:str - Nazwa sekcji w pliku ini
    :param valueini:str - Wartość dla sekcji "sectionini" w pliku ini
    :param defaultvalue:str - Domyślna wartość dla valueini
    :return: strret
    """
    if os.path.exists(pathini) is False:
        strret: str = ""
    else:
        config = configparser.ConfigParser()
        config.read(pathini)

        strret = config.get(sectionini, valueini, fallback=defaultvalue)
    return strret

def archiweproject(pathsourcedir: str, typearch: TypeArch = TypeArch.en7Zip):
    """
    OPIS: Funkcja archiwizuje projekt z ścieżki dostępu "pathsourcedir"
    :param pathsourcedir: str-Ścieżka dostępu do głównego katalogu projektu
    :param typearch:TypeArch-Domyślny typ archiwizacji
    :return: pass
    """
    # Stworzenie prostej tekstowej winiety
    nowdate = datetime.now()
    strdatetime: str = nowdate.strftime("%d-%m-%Y")
    about: str = "archiweproject v0.8.5423 © Grzegorz Sołtysik Oświęcim {}".format(strdatetime)

    arch7zip: str = "7z.exe"  # Nazwa archiwizatora 7zip
    arch7zipdll: str = "7z.dll"  # Nazwa biblioteki potrzebnej dla archiwizatora 7z
    mypythonfileconfig: str = "myconfigpython.ini"  # Nazwa pliku konfiguracyjnego ze ścieżką dostępu do domyślnego katalogu na archiwa
    defaultpatharch: str = "F:\\DevelopGS\\Archiwa"  # Domyślna ścieżka dostępu do głównego katalogu archiwum
    archivedir: str = getvalueini(mypythonfileconfig, "main", "defprojectarchive", defaultpatharch)

    syntax7zip: str = "{} a -t7z {} {}"  # Składnia wywoływania archiwizatora 7zip
    syntaxrar: str = "{} a -s -r -m5 -ma5 {} {}"  # Składnia wywoływania archiwizatora rar

    # Określenie ściezki dostępu do archiwizatora 7zip
    archiveexe7zip: str = getvalueini(mypythonfileconfig, "main", "patharch7zip", "7z.exe")
    # Zmiana rozszerzenia z .exe na .dll dla archiwizatora 7zip
    archivedll7zip: str = archiveexe7zip.replace(arch7zip, arch7zipdll)

    # Określenie ściezki dostępu do archiwizatora rar
    archiveexerar: str = getvalueini(mypythonfileconfig, "main", "patharchRar", "rar.exe")

    # Sprawdzanie czy istnieje archiwizer w bierzącym katalogu
    if os.path.exists(archiveexe7zip) and os.path.exists(archivedll7zip):
        pass
    else:
        print("Archiwizator 7z.exe nie istnieje w bierzącym katalogu!")
        exit()
    # Stworzenie dodatku do nazwy archiwum z bierzącą data i czasem
    fulldatetime: str = nowdatetime()

    print("{}".format(about))
    # Wyciągnięcie ze ścieżki dostępu do projektu, samej nazwy projektu
    nameproject: str = os.path.basename(pathsourcedir)
    # Przejście powyżej "pathsourcedir" do katalogu z projektami
    directoryprojects: str = os.path.dirname(pathsourcedir)
    # Aktualnym katalogiem katalog z projektami. Aktalnym katalogiem MUSI być katalog z projektami, gdyż podczas
    # uruchamiania właściwej archiwizacji ścieżka do katalogu żródłowego, jest ścieżką względną (os.getcwd() + projectname)
    os.chdir(directoryprojects)
    nameprojectarchiwe: str = os.path.join(archivedir, nameproject)  # Ścieżka do nowego archiwum projektu
    Path(nameprojectarchiwe).mkdir(parents=True, exist_ok=True)  # Sprawdzanie czy istnieje katalog na archiwum, jeśli nie to zostanie stworzony (Python ≥ 3.5)

    # tworzenie pełnej ściezki dostępu do archiwum (wraz z modyfikacją nazwy archiwum przez dodanie daty i czasu)
    nameprojectarchiwefull7zip: str = os.path.join(nameprojectarchiwe, nameproject)  # Archiwum 7zip
    nameprojectarchiwefullrar: str = nameprojectarchiwefull7zip  # Archiwum rar
    nameprojectarchiwefullrar += fulldatetime  # Archiwum rar
    nameprojectarchiwefull7zip += fulldatetime + ".7z"  # Archiwum 7zip

    createarchive7z: str = syntax7zip.format(archiveexe7zip, nameprojectarchiwefull7zip, nameproject)
    createarchiverar: str = syntaxrar.format(archiveexerar, nameprojectarchiwefullrar, nameproject)

    # ---- Wykonywanie poleceń dosa ----
    # Właściwa archiwizacja
    if typearch == TypeArch.en7Zip:
        os.system(createarchive7z)
    elif typearch == TypeArch.enRar:
        os.system(createarchiverar)
    else:
        exit(1)

    os.chdir(nameprojectarchiwe)  # Aktualnym katalogiem jest katalog anarchism
    os.system("cls")  # Wyczyszczenie konsoli
    os.system("dir")
    # os.system("pause") # Czekanie na naciśnięcie dowolnego klawisza, by zamknąć konsole
