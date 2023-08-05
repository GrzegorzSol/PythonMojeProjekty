from MyBiblePyClass import MyBiblePyClass  # , EnumDecodeListText

mbpc = MyBiblePyClass("F:\\DevelopGS\\Dane dla MojaBiblia\\Data")

# print("\t\tWczytano {} tłumaczeń".format(len(mbpc.itemstr)))
ITRANSLATE = 2

# it = mbpc.itemstr[ITRANSLATE]
# print("\t\t{}".format(it.infotr))
# listvers = []
# listvers = mbpc.readtext(ITRANSLATE, 60, 2, 4)
# print("{} {}:{} {}".format(listvers[EnumDecodeListText.endec_smalnamebook],
#                      listvers[EnumDecodeListText.endec_chapt],
#                      listvers[EnumDecodeListText.endec_vers],
#                      listvers[EnumDecodeListText.endec_text], "\n"))

listaresult = mbpc.readtextall(41, 2, 4)
for strout in listaresult:
    print(strout)
