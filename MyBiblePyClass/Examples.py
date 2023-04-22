from MyBiblePyClass import MyBiblePyClass

mbpc = MyBiblePyClass("F:\\DevelopGS\\Dane dla MojaBiblia\\Data")

#  print("Katalog z danymi: \"{}\"".format(mbpc._pathtrdir))
# for x in mbpc.filenames:
#     print(x)

print("Wczytano {} tłumaczeń".format(len(mbpc.itemstr)))
ITRANSLATE = 3

it = mbpc.itemstr[ITRANSLATE]
print("{} - {}".format(mbpc.itemstr[ITRANSLATE].infotr, it.namepathtr))

print(mbpc.readtext(ITRANSLATE, 45, 1, 1))
