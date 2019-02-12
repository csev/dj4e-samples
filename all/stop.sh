
echo "This kills most all the DJangos running on this server..."

ps -a | grep ' ./manage.py runserver 80[0-9][0-9]' | awk '{print "kill " $1}' | bash

