from os import system
from sys import platform,argv

import termcolor

windows = "windows"
macos = "macos"
linux = "linux"

windows_comp = " pixelrailfight-mod --platform=win32 --asar --overwrite"
linux_comp = " pixel-railfight-mod --overwrite --asar --platform=linux --prune=true"
macos_comp = " --overwrite --platform=darwin --prune=true --asar"

def main(os):
    system("clear")

    if len(argv) == 2:
        if argv[1] == "--spec":
            gprint("Platform to compile for (darwin for MacOS, win32 for windows, linux for linux):")
            spec = input()

            if spec == "win32" or spec == "darwin" or spec == "linux":
                base(spec)
            else:
                termcolor.cprint("Error: Misinputted platform", 'red')
                exit()
        else:
            termcolor.cprint("Error: Unknown command line argument", 'red')
            exit()

    base(os)

def base(os):
    gprint("Icon support? (y/n): ")
    icon = input()

    if(icon == "y"):
        gprint("Path to .icns file:")
        icon_path = input()
    else:
        gprint("Not adding icon")

        gprint("Path to folder containing main.js:")
        path = input()
        electron = "electron-packager " + path + compcommands(os)
        system(electron)
        exit()

    gprint("Path to folder containing main.js:")
    path = input()
    electron = "electron-packager " + path + compcommands(os) + " --icon=" + icon_path
    system(electron)




def gprint(text):
    termcolor.cprint(text, 'green')

def compcommands(os):
    if os == windows:
        return windows_comp
    elif os == linux:
        return linux_comp
    elif os == macos:
        return macos_comp

def getOS():
    windows = "windows"
    macos = "macos"
    linux = "linux"
    if platform == "linux" or platform == "linux2":
        return linux
    elif platform == "darwin":
        return macos
    elif platform == "win32":
        return windows


if __name__ == '__main__':
    main(getOS())
