import os
import shutil

# Ścieżka dostępu do katalogu źródłowego
SourceDir: str = "F:\\DevelopGS\\MojaBibliaNG_Testing"
# Ścieżka dostępu do katalogu przeznaczenia
DestDir: str = "F:\\DevelopGS\\Python\\PythonMojeProjekty\\Skrypty\\Testy"  # "F:\\DevelopGS\\MojaBibliaNG_Git"
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

os.chdir(SourceDir)
# Kopiowanie plików do katalogu głównego
for mypath in ListNames:
    shutil.copy(mypath, DestDir)
# Kopiowanie plików z modułów dodatkowych
for mymodulepath in ListModules:
    shutil.copytree(mymodulepath, os.path.join(DestDir, mymodulepath), dirs_exist_ok=True)

# os.system("dir")
