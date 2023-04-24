# import configparser
# import locale
# import os
# from datetime import datetime
from enum import IntEnum, auto

# from pathlib import Path

class EnumInfoAllBooks(IntEnum):
    eninfo_Number = 0
    eninfo_Fullname = auto()  # Pełna nazwa księgi
    eninfo_Smalname = auto()  # Skrócona nazwa księgi
    eninfo_Coutchapt = auto()  # Ilość rozdziałów w księdze


InfoAllBooks = [  # --- Stary Testament
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

for info in range(len(InfoAllBooks)):
    print("{} - {} - {} - {} rozdziałów".format(InfoAllBooks[info][EnumInfoAllBooks.eninfo_Number],
                                                InfoAllBooks[info][EnumInfoAllBooks.eninfo_Fullname],
                                                InfoAllBooks[info][EnumInfoAllBooks.eninfo_Smalname],
                                                InfoAllBooks[info][EnumInfoAllBooks.eninfo_Coutchapt]))
print("{} - {}".format(len(InfoAllBooks), len(InfoAllBooks[0])))