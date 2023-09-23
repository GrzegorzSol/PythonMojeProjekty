#  Copyright (c) Grzegorz Sołtysik
#  Nazwa projektu: openpyxl
#  Nazwa pliku: excelscheduledetector.py
#  Data: 09.09.2023, 09:05

import datetime
import DetectorClass  # Przestrzeń nazw

excellfilepath: str = "TerminarzSprawdzaniaCzujników.xlsx"

openschedule = DetectorClass.CheckScheduleClass(excellfilepath)
openschedule.execute(True)
openschedule.openworkbook.save(openschedule.getpath())
