from MyBiblePyClass import MyBiblePyClass

mbpc = MyBiblePyClass("F:\\DevelopGS\\Dane dla MojaBiblia\\Data")

# print("\t\tWczytano {} tłumaczeń".format(len(mbpc.itemstr)))
ITRANSLATE = 2

it = mbpc.itemstr[ITRANSLATE]
# print("\t\t{}".format(it.infotr))

# print("{}{}".format(mbpc.readtext(ITRANSLATE, 6, 15, 59), "\n"))

listaresult = []
listaresult = mbpc.readtextall(12, 2, 23)
for strout in listaresult:
    print(strout)

mbpc.createpdfalltext(listaresult)
