from MyBiblePyClass import MyBiblePyClass

mbpc = MyBiblePyClass("F:\\DevelopGS\\Dane dla MojaBiblia\\Data")

#  print("Katalog z danymi: \"{}\"".format(mbpc._pathtrdir))
# for x in mbpc.filenames:
#     print(x)

print("\t\tWczytano {} tłumaczeń".format(len(mbpc.itemstr)))
ITRANSLATE = 1

it = mbpc.itemstr[ITRANSLATE]
print("\t\t{}".format(it.infotr))

print(mbpc.readtext(ITRANSLATE, 1, 1, 1))
print(mbpc.readtext(ITRANSLATE, 1, 1, 2))
