
djangos=`ps -ewww | grep ' ./manage.py runserver 0.0.0.0:80[0-9][0-9]' | wc -l`

echo Killing $djangos Djangos on this server...
sleep 5

ps -ewww | grep ' ./manage.py runserver 0.0.0.0:80[0-9][0-9]' | awk '{print "kill " $1}' | sh

