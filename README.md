# Wanting

A voice activate artifact

- change the brightness based on the length of the conversation
- y
- z

## Setup

 For this project you are going to need

### Equipment

* Raspberry pi
* Philips Hue Bulb and Bridge
* [Seeed Studio Respeaker](https://www.amazon.com/seeed-Studio-ReSpeaker-4-Mic-Raspberry/dp/B076SSR1W1)

### Libraries

```Shell
# Instructions for Philips Hue
pip install phue

# Instructions for Respeaker Libraries
sudo apt-get update
sudo apt-get upgrade
git clone https://github.com/respeaker/seeed-voicecard.git
cd seeed-voicecard
sudo ./install.sh
reboot

sudo raspi-config
# Select 7 Advanced Options
# Select A4 Audio
# Select 1 Force 3.5mm ('headphone') jack
# Select Finish

sudo raspi-config
# "Interfacing Options"
# "SPI"
# Enable SPI
# Select Finish

# Instructions for Voice Activity Detection Libraries
#git clone https://github.com/respeaker/mic_array
apt-get install portaudio19-dev
pip install pyaudio
pip install webrtcvad

```

### Notes

```Shell

pwd
#打印当前工作目录

ifconfig
#当前所有网络接口;View and change the configuration of the network interfaces

sudo apt install python-virtualenv
#Resolve issues between Python and Linux with virtualenv

history
#check previous commands
!数字
#再次使用指令

reboot
#restart system

#run mic_array
cd mic_array/
python vad_doa.py

# send files between pi and macbook
scp send file
```
