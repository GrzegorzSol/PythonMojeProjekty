import datetime
import DetectorClass  # Przestrzeń nazw
# import openpyxl

excellfilepath: str = "TerminarzSprawdzaniaCzujników.xlsx"

openschedule = DetectorClass.CheckScheduleClass(excellfilepath)
openschedule.execute(True)
openschedule.openworkbook.save(openschedule.getpath())
