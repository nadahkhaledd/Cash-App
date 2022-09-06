echo "Waiting for SQL..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done
echo "SQL started"
python http://manage.py makemigrations
python http://manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.filter(username='nadah').exists() or User.objects.create_superuser('nadah', 'nadahkhaledd@gmail.com, 'nadah1234')" | python http://manage.py shell
python http://manage.py runserver 0.0.0.0:8000