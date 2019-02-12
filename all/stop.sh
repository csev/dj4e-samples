
unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac

djangos=`ps -efwww | grep ' ./manage.py runserver 0.0.0.0:80[0-9][0-9]' | wc -l`

echo Killing $djangos Djangos on this server...
sleep 5

if [ "$machine" == "Linux" ] ; then
    ps -efwww | grep ' ./manage.py runserver 0.0.0.0:80[0-9][0-9]' | awk '{print "kill " $2}' | sh
else
    ps -ewww | grep ' ./manage.py runserver 0.0.0.0:80[0-9][0-9]' | awk '{print "kill " $1}' | sh
fi
