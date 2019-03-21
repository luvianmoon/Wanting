# Workflow
# write script on macbook
#save it with command+s
# crlck stage
# commit
# push

# ssh into Pi on HANABI
# On the Pi
cd ~/Wanting
git pull


# After finished the coding:
# write code to let raspberry pi run script after lxde(the interface that appear when electricity cable was pug in)

# open up the file using nano: call
nano /home/pi/.config/autostart/clock.desktop
# write
[Desktop Entry]
Type=Application
Name=Clock
Exec=x-terminal-emulator -e python2 /home/pi/Wanting/ConcentrationLight.py
# save & exit
