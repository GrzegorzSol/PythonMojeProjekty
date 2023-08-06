from os import chdir, path, popen
from pathlib import Path
from shutil import copy2, copytree, ignore_patterns

# Ścieżka dostępu do katalogu źródłowego
SourceDir: str = "F:\\DevelopGS\\MojaBibliaNG_Testing"
# Ścieżka dostępu do katalogu przeznaczenia
DestDir: str = "F:\\DevelopGS\\MojaBibliaNG_Git"
# DestDir: str = "F:\\DevelopGS\\Python\\PythonMojeProjekty\\Skrypty\\Testy"
# Lista plików do pominienia
ListNames = ["GsDebugClass.h", "Headers.h",
             # Lista plików z katalogu źródłowego do skopiowania do katalogu przeznaczenia
             "uChapterEditWindow.cpp", "uChapterEditWindow.dfm", "uChapterEditWindow.h",
             "uDictGrecPolWindow.cpp", "uDictGrecPolWindow.dfm", "uDictGrecPolWindow.h",
             "uFastTipsWindow.cpp", "uFastTipsWindow.dfm", "uFastTipsWindow.h",
             "uGlobalVar.cpp", "uGlobalVar.h",
             "uHelpMyBibleWindow.cpp", "uHelpMyBibleWindow.dfm", "uHelpMyBibleWindow.h",
             "uHistoryChaptersOpen.cpp", "uHistoryChaptersOpen.dfm", "uHistoryChaptersOpen.h",
             "uImageAndTextWindow.cpp", "uImageAndTextWindow.dfm", "uImageAndTextWindow.h",
             "uInformationsAppWindow.cpp", "uInformationsAppWindow.dfm", "uInformationsAppWindow.h",
             "uLibrary.cpp", "uLibrary.h",
             "uMainWindow.cpp", "uMainWindow.dfm", "uMainWindow.h",
             "uMyBibleNGLibrary.cpp", "uMyBibleNGLibrary.h",
             "uReadingPlanWindow.cpp", "uReadingPlanWindow.dfm", "uReadingPlanWindow.h",
             "uReadUpdateWindow.cpp", "uReadUpdateWindow.dfm", "uReadUpdateWindow.h",
             "uSchemeVersWindow.cpp", "uSchemeVersWindow.dfm", "uSchemeVersWindow.h",
             "uSearchTextWindow.cpp", "uSearchTextWindow.dfm", "uSearchTextWindow.h",
             "uSelectVersWindow.cpp", "uSelectVersWindow.dfm", "uSelectVersWindow.h",
             "uSendingMailWindow.cpp", "uSendingMailWindow.dfm", "uSendingMailWindow.h",
             "uSetupsWindow.cpp", "uSetupsWindow.dfm", "uSetupsWindow.h",
             "uViewAllResourcesWindow.cpp", "uViewAllResourcesWindow.dfm", "uViewAllResourcesWindow.h"]
# Nazwy katalogów dodatkowych modułów
ListModules = ["GsComponents", "GsReadBibleTextClass"]

chdir(SourceDir)
resultstring: str
strpatterns: str = "__*"
# Kopiowanie plików do katalogu głównego
for mypath in ListNames:
    resultstring = copy2(mypath, DestDir)
    print("Sopiowano {}".format(resultstring))

# Kopiowanie plików z modułów dodatkowych
for mymodulepath in ListModules:
    Path(path.join(DestDir, mymodulepath)).mkdir(parents=True,
                                                 exist_ok=True)  # Sprawdzanie, czy istnieje katalog na archiwum, jeśli nie to zostanie stworzony (Python ≥ 3.5)
    resultstring = copytree(mymodulepath, path.join(DestDir, mymodulepath), dirs_exist_ok=True,
                            ignore=ignore_patterns(strpatterns))
    print("Sopiowano {}".format(resultstring))

popen(path.join(DestDir, "uGlobalVar.h"))
