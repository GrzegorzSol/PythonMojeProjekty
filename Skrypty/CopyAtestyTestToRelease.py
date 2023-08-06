from os import chdir, path, popen
from shutil import copy2

# Ścieżka dostępu do katalogu źródłowego
SourceDir: str = "F:\\DevelopGS\\AKPSerwis\\AtestyAKPSerwis_Testing"
# Ścieżka dostępu do katalogu przeznaczenia
# DestDir: str = "F:\\DevelopGS\\AKPSerwis\\AtestyAKPSerwis"
DestDir: str = "F:\\DevelopGS\\Python\\PythonMojeProjekty\\Skrypty\\Testy"
# Lista plików do pominienia
ListNames = ["GsDebugClass.h", "GsLibrary.cpp",
             "GsLibrary.h",
             "GsRegisterSystemClass.cpp", "GsRegisterSystemClass.h",
             "GsWinControls.cpp", "GsWinControls.h","GsWinControlsData.h",
             "BaseAtestsLibrary.h",
             "uAllBasesClass.cpp", "uAllBasesClass.h",
             "uAtestsManometersWindow.cpp", "uAtestsManometersWindow.dfm", "uAtestsManometersWindow.h",
             "uAttLibrary.cpp", "uAttLibrary.h",
             "uBaseAtClass.cpp", "uBaseAtClass.h",
             "uBaseAtManometersClass.cpp", "uBaseAtManometersClass.h",
             "uGlobalDefsBaseAtests.cpp", "uGlobalDefsBaseAtests.h",
             "uMainAtests.cpp", "uMainAtests.dfm", "uMainAtests.h", "uMainAtests.vlb",
             "uMyReqMessageWindow.cpp", "uMyReqMessageWindow.dfm", "uMyReqMessageWindow.h",
             "uProgressWindow.cpp", "uProgressWindow.dfm", "uProgressWindow.h",
             "uSensorsWindow.cpp", "uSensorsWindow.dfm", "uSensorsWindow.h",
             "uSetupsAtestsWindow.cpp", "uSetupsAtestsWindow.dfm", "uSetupsAtestsWindow.h", "uSetupsAtestsWindow.vlb",
             "uViews.cpp", "uViews.dfm", "uViews.h",
             "uWindowTableView.cpp", "uWindowTableView.dfm", "uWindowTableView.h"]

chdir(SourceDir)
resultstring: str
# Kopiowanie plików do katalogu głównego
for mypath in ListNames:
    resultstring = copy2(mypath, DestDir)
    print("Sopiowano {}".format(resultstring))

popen(path.join(DestDir, "uGlobalDefsBaseAtests.h"))

