# RCT3_audiofix
Script that fixes the crackling audio from Roller Coaster Tycoon 3 on Linux. The music is distorted due to the poor support for ".wma" files within proton/wine. This script will convert these ".wma" files to regular ".mp3" files, but leaves the extension as ".wma" to prevent the game from malfunctioning.


# Requirements
- ffmpeg
- [pydub](https://github.com/jiaaro/pydub)
- For steam users: I recommend to run with proton>7.0.3

# Instructions
First install ffmpeg using your distro's package manager:

Debian based (Ubuntu, Linux mint etc.)
```
sudo apt-get install ffmpeg
```
Arch based (Manjaro, Arch Linux, EndeavourOS etc.)
```
sudo pacman -S ffmpeg
```
Fedora based (Fedora, Red Hat etc.)
```
sudo dnf install ffmpeg
```

Second install the pydub module
```
pip install pydub
```

Third clone the repository, open a terminal and type the following:
```
cd ~ && git clone https://github.com/Tiget1998/RCT3_audiofix.git
```
Find your steamapps/EpicGames folder where RCT3 is located. Usually this is located in(Steam is taken as example here):
```
/home/user/.steam/steam/steamapps/common/
```
Then find your RCT3 folder, and in it find the "Music" folder. Copy this folder to some place safe!!!!!!!!

Copy the path to the "Music" folder, this path should look something like this:
```
/home/user/.steam/steam/steamapps/common/RCT3foldername/Music
```
Finally open a terminal and do the following:
```
cd ~ && cd RCT3_audiofix
python audiofix.py /home/user/.steam/steam/steamapps/common/RCT3foldername/Music

```
A new "Music" folder is located in the same directory as the "audiofix.py"
Copy this folder to your RCT3 install location to replace the original music, MAKE SURE YOU HAVE BACKED UP THE ORIGINAL AUDIO FILES!

Enjoy the music instead of the crackling noises


