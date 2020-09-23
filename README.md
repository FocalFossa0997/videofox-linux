# videofox-linux
VideoFox is a simple application that allows you to perform complex actions on video files without having to type in long ffmpeg commands.  
# How to use
VideoFox has no gui, so you will have to launch it from the command line.Everything else is described in the application.  
# Known problems
- The executable has to be named VideoFox in order for the exit funstion to work  
- The application cannot detect which linux distro you are on, so you will have to manually select the package manager that your system uses  
# Forking and modifying
If you want to fork and/or modyfy this, you can! Just make sure to credit me as the creator of the original release.  
# Can't get VideoFox to work?
Feel free to share your problems if they are not listed here. Anyways, here are the most common errors that occur when trying to install / run

`[14153] Error loading Python lib '/tmp/_MEIWKI4Pl/libpython3.8.so.1.0': dlopen: /lib/x86_64-linux-gnu/libm.so.6: version GLIBC_2.29' not found (required by /tmp/_MEIWKI4Pl/libpython3.8.so.1.0)`  
> This occurs when you don't have Python 3.8 installed. Either install it or [recompile it](https://youtu.be/Tp1B9HqqNhE)  

`sh: 1: ffmpeg: not found`
> This occurs when you don't have ffmpeg installed. VideoFox can install it for you, just select it on the main menu.
