
if [ -f manage.py ]; then
   echo "In the wrong folder"
   exit
fi

cd all
python3 ./manage.py migrate
python3 ./manage.py runserver 0.0.0.0:8001 &

cd ../hello
python3 ./manage.py migrate
python3 ./manage.py runserver 0.0.0.0:8002 &

cd ../getpost
python3 ./manage.py migrate
python3 ./manage.py runserver 0.0.0.0:8003 &

cd ../users
python3 ./manage.py migrate
python3 ./manage.py runserver 0.0.0.0:8004 &

cd ../tracks
python3 ./manage.py migrate
python3 ./manage.py runserver 0.0.0.0:8005 &

cd ../views
python3 ./manage.py migrate
python3 ./manage.py runserver 0.0.0.0:8006 &

cd ../templates
python3 ./manage.py migrate
python3 ./manage.py runserver 0.0.0.0:8007 &

cd ../generic
python3 ./manage.py migrate
python3 ./manage.py runserver 0.0.0.0:8008 &

cd ../session
python3 ./manage.py migrate
python3 ./manage.py runserver 0.0.0.0:8009 &

cd ../form
python3 ./manage.py migrate
python3 ./manage.py runserver 0.0.0.0:8010 &

cd ../dj4ecrud
python3 ./manage.py migrate
python3 ./manage.py runserver 0.0.0.0:8011 &

sleep 8
echo
echo "Start at http://localhost:8001/"
