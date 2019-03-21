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

# open up the file using nano:
sudo nano /etc/xdg/lxsession/LXDE/autostart
# add the following line to the bottom of the file (just as last line)
@sh /home/pi/myproject/myscript.sh"别人的文件，可以用py文件代替”
# save and reboot!
