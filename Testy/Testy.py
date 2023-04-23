import configparser
import locale
import os
from datetime import datetime
from enum import IntEnum, auto
from pathlib import Path

PATHFILE = "F:\\DevelopGS\\Dane dla MojaBiblia\\Data\\ReadingPlan\\Chronologiczny_Test.rpf"

file = open(PATHFILE,  "rt", encoding="utf-8")
line = file.readline()
while line:
    line = file.readline().strip("\n")
    print("{} - {}".format(file.tell(), line))