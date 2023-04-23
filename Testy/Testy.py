# import configparser
# import locale
# import os
# from datetime import datetime
# from enum import IntEnum, auto
# from pathlib import Path

books = []
licz = 0

for y in range(8):
    books.append([])  # [] - Księgi, [][] - linie tekstu ksiąg

    for x in range(8):
        licz = licz + 1
        books[y].append("{}".format(licz))

for y in range(8):
    for x in range(8):
        print("[{}][{}] - {}".format(y, x, books[y][x]))

print("{}".format(len(books) * len(books[0])))
