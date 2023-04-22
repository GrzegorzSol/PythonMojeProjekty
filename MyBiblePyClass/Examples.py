from MyBiblePyClass import MyBiblePyClass

mbpc = MyBiblePyClass("F:\\DevelopGS\\Dane dla MojaBiblia\\Data")

print("Katalog z danymi: \"{}\"".format(mbpc.pathTrDir))
for x in mbpc.filenames:
    print(x)

print("{} elementów".format(len(mbpc.filenames)))
print(mbpc.readText(0, 45, 1, 1))
print("Plik")
