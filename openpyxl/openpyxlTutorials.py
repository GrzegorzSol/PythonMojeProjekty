# import configparser
# import locale
# import os
# from datetime import datetime
# from enum import IntEnum, auto
# from pathlib import Path
from openpyxl import Workbook, load_workbook

excellfilepath: str = "F:\\GrzegorzS\\Dokumenty\\PracaAKPSerwisAprochem\\AKP SERWIS\\Dokumentacje i schematy\\MojeDokumentyExcella\\Terminarz sprawdzania czujników.xlsm"

wb = load_workbook(excellfilepath)
ws = wb.active
c = ws["D5"].value

print(wb.sheetnames)
print(c)
