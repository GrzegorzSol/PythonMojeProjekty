#  Copyright (c) Grzegorz Sołtysik 01.05.2024, 06:03
#  Nazwa projektu: GsPyChartClass
#  Nazwa pliku: GsPyChartClass_example.py

from GsPyMyChart import GsPyMyChart, GsPyMyChartBox


fTable = [0.78, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
fTableM = [0.50, 1.1, 2.9, 3.3, 4.9, 5.5, 6.6, 7.7, 8.8, 9.1, 10.0]

a = GsPyMyChart(fTable, fTableM, "test.pdf", "Wykres liniowy błędów dla aparatu:")
b = GsPyMyChartBox(fTable, fTableM, "test1.pdf", "Wykres słupkowy błędów dla aparatu:")
