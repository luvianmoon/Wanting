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


# Step to do after finished the coding:
# write code to let raspberry pi run script after turn on(the interface that appear when electricity cable was pug in)

# create Shell to put python file in
# https://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/
nano launcher.sh
sh /home/pi/Wanting/launcher.sh

# Set WiFi network priority
https://raspberrypi.stackexchange.com/questions/58304/how-to-set-wifi-network-priority



# open up the file using nano: call
# https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup#method-2-autostart
nano /home/pi/.config/autostart/clock.desktop
# write
[Desktop Entry]
Type=Application
Name=Clock
Exec=x-terminal-emulator -e python2 /home/pi/Wanting/ConcentrationLight.py
# above code ask pi to open terminal and run
# save & exit

PhueRequestTimeout Error
# can due to send command right after changing the internet. just need to wait for a few sec
