# Wanting

A project to do...

- x
- y
- z

## Setup

 For this project you are going to need

### Equipment

* Raspberry pi
* Philips Hue Bulb and Bridge
* [Seeed Studio Respeaker](https://www.amazon.com/seeed-Studio-ReSpeaker-4-Mic-Raspberry/dp/B076SSR1W1)

### Libraries

```bash
pip install phue
apt-get install portaudio19-dev
pip install pyaudio

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
```
