from MyBiblePyClass import MyBiblePyClass

mbpc = MyBiblePyClass("F:\\DevelopGS\\Dane dla MojaBiblia\\Data")

#  print("Katalog z danymi: \"{}\"".format(mbpc._pathtrdir))
# for x in mbpc.filenames:
#     print(x)

print("Wczytano {} tłumaczeń".format(len(mbpc.itemstr)))
ITRANSLATE = 1

it = mbpc.itemstr[ITRANSLATE]
print("{} - {}".format(it.infotr, it.namepathtr))

file = open(mbpc.filenames[ITRANSLATE], "r", encoding="utf-8")
file.seek(it.books[1])
line = file.readline()
print(line)
file.close()

# print(mbpc.readtext(ITRANSLATE, 45, 1, 1))
