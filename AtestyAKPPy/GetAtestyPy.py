import configparser
import locale
import os
import binascii
from datetime import datetime
from enum import IntEnum, auto
from pathlib import Path

__pathadata: str = "F:\\DevelopGS\\AKPSerwis\\AtestyAKPSerwis_Testing\\Win32\\Release\\BazaŚwiadectwSprawdzania.akbap"

MIN_TEXT = 12
MIN_TEXT_EXT = 20
SMALL_TEXT = 48
MEDIUM_TEX = 96
LONG_TEXT = 118
OTHER_TEXT = 32
NUMBER_TEXT = 16
COMMENT_TEXT = 720

file = open(__pathadata, "rb")

def read_text(_file, _size: int):
  vret: str = ""
  for i in range(_size):
    mystr: bytes = _file.read(1)
    mystrChar: chr = chr(int.from_bytes(mystr))
    if ((i % 2) == 0) and (mystr != b'\x00'):
        vret += mystrChar

  return vret


id_atest = int.from_bytes(file.read(2))  # unsigned short int
numer_atestu: str = read_text(file, SMALL_TEXT)  # SMALL_TEXT
name_ap: str = read_text(file, LONG_TEXT)
# size_rec: int = int.from_bytes(file.read(2))
size_rec: int = file.read(2)  # unsigned int
name_ap_ext: str = read_text(file, LONG_TEXT)
producent: str = read_text(file, MEDIUM_TEX)
typ: str = read_text(file, MEDIUM_TEX)
numer_fabryczny: str = read_text(file, MEDIUM_TEX)
numer_ew: str = read_text(file, NUMBER_TEXT)
zakres_we: str = read_text(file, MEDIUM_TEX)
zakres_wy: str = read_text(file, MEDIUM_TEX)
aparat_kontrolny: str = read_text(file, SMALL_TEXT)
aparat_kontrolny1: str = read_text(file, SMALL_TEXT)
aparat_kontrolny2: str = read_text(file, SMALL_TEXT)
empty = read_text(file, 28)
data_str: str = read_text(file, SMALL_TEXT)
sprawdzil: str = read_text(file, LONG_TEXT)
instr: int = int.from_bytes(file.read(2))  # unsigned short int
notatka: str = read_text(file, COMMENT_TEXT)
nastepne_wzor: str = read_text(file, SMALL_TEXT)
autor: str = read_text(file, MEDIUM_TEX)
jednostki_we: str = read_text(file, MIN_TEXT)
jednostki_wy: str = read_text(file, MIN_TEXT)

print("ID: {}".format(id_atest))
print("numer atestu: {}".format(numer_atestu))
print("nazwa aparatu: {}".format(name_ap))
print("Wielkość rekordu: {}".format(size_rec))
print("nazwa aparatu rozszerzona: {}".format(name_ap_ext))
print("producent: {}".format(producent))
print("typ: {}".format(typ))
print("numer fabryczny: {}".format(numer_fabryczny))
print("numer ewidencyjny: {}".format(numer_ew))
print("zakres wejściowy: {}".format(zakres_we))
print("zakres wyjściowy: {}".format(zakres_wy))
print("aparat kontrolny: {}".format(aparat_kontrolny))
print("aparat kontrolny1: {}".format(aparat_kontrolny1))
print("aparat kontrolny2: {}".format(aparat_kontrolny2))
print("data atestu: {}".format(data_str))
print("sprawdził: {}".format(sprawdzil))
print("instrukcja: {}".format(instr))
print("notatka: {}".format(notatka))
print("następne wzorcowanie: {}".format(nastepne_wzor))
print("pomiary dokonał: {}".format(autor))
print("jednostka wejściowa: {}".format(jednostki_we))
print("jednostka wyjściowa: {}".format(jednostki_wy))

file.close()

# test: int = int.from_bytes(b'\x88\x09')
# print("test: {}".format(test))
