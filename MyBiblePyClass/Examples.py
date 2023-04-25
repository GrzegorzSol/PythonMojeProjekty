from MyBiblePyClass import MyBiblePyClass

mbpc = MyBiblePyClass("F:\\DevelopGS\\Dane dla MojaBiblia\\Data")

print("\t\tWczytano {} tłumaczeń".format(len(mbpc.itemstr)))
ITRANSLATE = 2

it = mbpc.itemstr[ITRANSLATE]
print("\t\t{}".format(it.infotr))

print(mbpc.readtext(ITRANSLATE, 6, 15, 59))
print(mbpc.readtext(ITRANSLATE, 1, 1, 2))
