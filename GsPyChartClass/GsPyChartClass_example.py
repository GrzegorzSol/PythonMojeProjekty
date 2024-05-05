#  Copyright (c) Grzegorz Sołtysik 05.05.2024, 06:08
#  Nazwa projektu: GsPyChartClass
#  Nazwa pliku: GsPyChartClass_example.py

# from GsPyMyChart import GsPyMyChart, GsPointF, GsRectF
from GsPyMyChart import *


fTable = [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
fTableM = [-0.8, 0.2, 1.0, 2.3, 3.3, 4.2, 5.3, 6.3, 7.4, 8.4, 9.4]
stringTitle: str = "Wykres błędów dla aparatu: Przetwornik ciśnienia, firmy Yokogawa o numerze ewidencyjnym:\n fabrycznym:"


a = GsPyMyChart(fInTableRef=fTable, fInTableMeas=fTableM, strPathPDF="Liniowy_wymiarowany.pdf",
				strTitle=stringTitle,
                iLeft=100, iTop=400, iWidth=300, iHeight=400)

b = GsPyMyChart(fInTableRef=fTable, fInTableMeas=fTableM, strTitle=stringTitle, strPathPDF="Liniowy_maksymalny.pdf")

c = GsPyMyChartBox(fInTableRef=fTable, fInTableMeas=fTableM, strPathPDF="Słupkowy_wymiarowany.pdf",
				strTitle=stringTitle,
                iLeft=100, iTop=400, iWidth=300, iHeight=400)

d = GsPyMyChartBox(fInTableRef=fTable, fInTableMeas=fTableM, strTitle=stringTitle, strPathPDF="Słupkowy_maksymalny.pdf")

# e = GsRectF(12, 12, 32, 48)
# f = c.centre()
# print("c.width: {}, c.height: {}".format(c.width(), c.height()))
# print("X: {}, Y: {}".format(d.fX, d.fY))
