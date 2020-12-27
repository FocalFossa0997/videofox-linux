import os
from os import path
def sys(command):
    os.system(command)
def c():
    os.system("clear")
def message(message=""):
    print(message)
    print("Press [enter] to dismiss")
    dummy = input()
    c()
def box(title, messsage):
    c()
    print(f"== {title} ============")
    print("Press [enter] to dismiss")
    dummy = input()
    c()
def errorSound():
    sys('/usr/bin/canberra-gtk-play --id="dialog-error" --description="" &')
def  completeSound():
    sys('/usr/bin/canberra-gtk-play --id="complete" --description="" &')
def installffmpeg():
    c()
    choice = ""
    print("In order to install correctly, you will need to select which package manager you use. Type < to go back\n1. apt (Debian/Ubuntu)\n2. apt-get (Debian/Ubuntu)\n3. dnf (Fedora)\n4. yum (Fedora)\n5. pacman (Arch)\n6. Portage (Gentoo)")
    choice = input(">")
    if choice == "<":
        return
    elif choice == "1":
        sys("sudo apt install -y ffmpeg")
        completeSound()
        message()
        return
    elif choice == "2":
        sys("sudo apt-get install -y ffmpeg")
        completeSound()
        message()
        return
    elif choice == "3":
        sys("sudo dnf install ffmpeg")
        completeSound()
        message()
        return
    elif choice == "4":
        sys("sudo yum install ffmpeg")
        completeSound()
        message()
        return
    elif choice == "5":
        sys("sudo pacman -S ffmpeg")
        completeSound()
        message()
        return
    elif choice == "6":
        sys("sudo emerge -a ffmpeg")
        completeSound()
        message()
        return
    else:
        errorSound()
        message("Please choose a packagae manager from the list!")
def convertFPS():
    c()
    inf = ""
    outf = ""
    fps = 0
    print("Enter an input file path or type < to go back")
    inf = input(">")
    if inf == "<":
        return
    elif path.exists(inf):
        pass
    else:
        errorSound()
        message("That file or file path does not extst! Please try again")
        return
    c()
    print("Enter an output file path or type < to go back")
    outf = input(">")
    if outf == "<":
        return
    c()
    print("Enter a framerate for the output or type < to go back")
    fps = input(">")
    if fps == "<":
        return
    sys(f"ffmpeg -i {inf} -c:v libx264 -preset veryslow -crf 24  -framerate {fps}  -profile:v high -level 4.1 -tune film  -acodec copy   {outf}")
    completeSound()
    message()
def interlaceVideo():
    c()
    inf = ""
    outf = ""
    print("Enter an input file path or type < to go back")
    inf = input(">")
    if inf == "<":
        return
    elif path.exists(inf):
        pass
    else:
        errorSound()
        message("That file or file path does not extst! Please try again")
        return
    c()
    print("Enter an output file path or type < to go back")
    outf = input(">")
    if outf == "<":
        return
    c()
    sys(f"ffmpeg -i {inf} -c:v libx264 -pix_fmt yuv420p -flags +ilme+ildct {outf}")
    completeSound()
    message()
def deleteVideo():
    c()
    inf = ""
    dc = ""
    print("Enter an input file path or type < to go back")
    inf = input(">")
    if inf == "<":
        return
    elif path.exists(inf):
        pass
    else:
        errorSound()
        message("That file or file path does not extst! Please try again")
        return
    c()
    print("Are you sure you want to delete that video file? [y/N]")
    dc = input(">")
    if dc == "y" or dc == "Y" or dc == "yes" or dc == "Yes" or dc =="YES":

        sys(f"rm -v {inf}")
        completeSound()
        message()
    else:
        errorSound()
        message("Abort.")
def copyVideo():
    inf = ""
    outf = ""
    c()
    print("Enter an input file path or type < to go back")
    inf = input(">")
    if inf == "<":
        return
    elif path.exists(inf):
        pass
    else:
        errorSound()
        message("That file or file path does not extst! Please try again")
        return
    c()
    print("Enter an output file path or type < to go back")
    outf = input(">")
    if outf == "<":
        return
    elif outf == inf or path.exists(outf):
        errorSound()
        c()
        print("That output file or file path already exists. Overwrite? [y/N]")
        dc = input(">")
        if dc == "y" or dc == "Y" or dc == "yes" or dc == "Yes" or dc =="YES":

            sys(f"rm {outf}")
            sys(f"dd if='{inf}' of='{outf}'")
            completeSound()
            message()
        else:
            errorSound()
            message("Abort.")
    else:
        sys(f"dd if='{inf}' of='{outf}'")
        completeSound()
        message()
def renameVideo():
    c()
    print("Enter an input file path or type < to go back")
    inf = input(">")
    if inf == "<":
        return
    elif path.exists(inf):
        pass
    else:
        errorSound()
        message("That file or file path does not extst! Please try again")
        return
    c()
    print("Enter a new name for the file or type < to go back")
    outf = input(">")
    if outf == "<":
        return
    elif inf == outf or path.exists(outf):
        c()
        errorSound()
        print("That new file name is identical to the old file name!")
        message()
        return
    else:
        c()
        sys(f"mv -v {inf} {outf}")
        completeSound()
        message()
    c()
def listDir():
    c()
    choice = ""
    cwd = os.getcwd()
    print("Enter a subdirectory to list the contents of,\nleave blank to list the contents of the current working directory,\nor type < to go back")
    choice = input(">")
    if choice == "<":
        return
    elif choice == "":
        c()
        sys(f"dir")
        completeSound()
        message()
    else:
        c()
        sys(f"dir {cwd}/{choice}")
        completeSound()
        message()
def about():
    c()
    completeSound()
    print("VideoFox is a simple application that allows you to perform complex actions on video files without having to type in long ffmpeg commands.\nVideoFox is created by: Focal Fossa")
    message()
def mainMenu():
    c()
    print("VideoFox version 9.12.2020\n©Focal Fossa 2020\n0. Install ffmpeg\n1. Change a video's framerate\n2. Interlace a video\n3. Delete a video\n4. Copy a video\n5. Rename a video\n6. List contents of current working directory or subdirectory\n7. About\n8. Exit")
    selection = input(">")
    if selection == "0":
        installffmpeg()
    elif selection == "1":
        convertFPS()
    elif selection == "2":
        interlaceVideo()
    elif selection == "3":
        deleteVideo()
    elif selection == "4":
        copyVideo()
    elif selection == "5":
        renameVideo()
    elif selection == "6":
        listDir()
    elif selection == "7":
        about()
    elif selection == "8":
        c()
        sys("killall VideoFox")
    else:
        errorSound()
        message("Enter a valid command!")
while True:
    mainMenu()
