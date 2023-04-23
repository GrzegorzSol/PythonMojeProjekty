from MyBiblePyClass import MyBiblePyClass

mbpc = MyBiblePyClass("F:\\DevelopGS\\Dane dla MojaBiblia\\Data")

#  print("Katalog z danymi: \"{}\"".format(mbpc._pathtrdir))
# for x in mbpc.filenames:
#     print(x)

print("Wczytano {} tłumaczeń".format(len(mbpc.itemstr)))
ITRANSLATE = 2

it = mbpc.itemstr[ITRANSLATE]
print("{} - {}".format(it.infotr, it.namepathtr))

#  print(mbpc.readtext(ITRANSLATE, 64, 1, 1))
print(it.books[65][15])
