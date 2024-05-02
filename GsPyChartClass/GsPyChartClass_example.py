#  Copyright (c) Grzegorz Sołtysik 01.05.2024, 09:44
#  Nazwa projektu: GsPyChartClass
#  Nazwa pliku: GsPyChartClass_example.py

from GsPyMyChart import GsPyMyChart, GsPyMyChartBox

fTable = [0.78, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
fTableM = [0.50, 1.1, 2.9, 3.3, 4.9, 5.5, 6.6, 7.7, 8.8, 9.1, 10.0]

a = GsPyMyChart(fInTableRef=fTable, fInTableMeas=fTableM, strPathPDF="Liniowy_wymiarowany.pdf",
					strTitle="Wykres liniowy błędów dla aparatu:", iHeight=400, iWidth=300, iTop=100, iLeft=100)

b = GsPyMyChartBox(fInTableRef=fTable, fInTableMeas=fTableM, strPathPDF="Słupkowy_wymiarowany.pdf",
						strTitle="Wykres słupkowy błędów dla aparatu:", iHeight=400, iWidth=300, iTop=100, iLeft=100)

c = GsPyMyChartBox(fInTableRef=fTable, fInTableMeas=fTableM, strTitle="Test", strPathPDF="Słupkowy_maksymalny.pdf", iHeight=400)

d = GsPyMyChart(fInTableRef=fTable, fInTableMeas=fTableM, strTitle="Wykres słupkowy błędów dla aparatu:", strPathPDF="Liniowy_maksymalny.pdf")